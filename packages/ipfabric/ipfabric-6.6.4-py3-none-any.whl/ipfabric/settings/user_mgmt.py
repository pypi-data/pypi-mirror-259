import logging
from typing import Any, Optional

import pytz
from pydantic import Field, BaseModel

logger = logging.getLogger("ipfabric")


class Token(BaseModel):
    token_id: str = Field(None, alias="id")
    description: Optional[str] = None
    role_ids: list = Field(None, alias="roleIds")


class User(BaseModel):
    username: str
    user_id: str = Field(None, alias="id")
    local: Optional[bool] = Field(None, alias="isLocal")
    sso_provider: Optional[Any] = Field(None, alias="ssoProvider")
    domains: Optional[Any] = Field(None, alias="domainSuffixes")
    role_names: Optional[list] = Field(alias="roleNames", default_factory=list)
    role_ids: list = Field(None, alias="roleIds")
    ldap_id: Optional[Any] = Field(None, alias="ldapId")
    timezone: Optional[str] = None
    token: Optional[Token] = None
    _get_snapshots_settings: Optional[bool] = None

    @property
    def is_admin(self):
        return (
            True
            if (self.token and "admin" in self.token.role_ids) or (not self.token and "admin" in self.role_ids)
            else False
        )

    @property
    def get_snapshots_settings(self):
        """If the User/Token has access to snapshots/:key/settings Endpoint."""
        if self._get_snapshots_settings is None and self.is_admin:
            self._get_snapshots_settings = True
        return self._get_snapshots_settings

    def set_snapshots_settings(self, v: bool):
        self._get_snapshots_settings = v

    @property
    def error_msg(self):
        msg = f'User "{self.username}" '
        if self.token:
            msg += f'Token "{self.token.description}" '
        return msg


class Role(BaseModel):
    name: str
    role_id: str = Field(None, alias="id")
    description: Optional[str] = None
    role_type: str = Field(None, alias="type")
    admin: bool = Field(None, alias="isAdmin")
    system: bool = Field(None, alias="isSystem")


class UserMgmt:
    def __init__(self, client):
        self.client: Any = client
        self.roles = self.get_roles()
        self.users = self.get_users()

    def get_roles(self, role_name: str = None):
        """
        Gets all users or filters on one of the options.
        :param role_name: str: Role Name to filter
        :return: List of roles
        """
        filters = {"name": ["ieq", role_name]} if role_name else None
        return [Role(**role) for role in self.client.fetch_all("tables/roles", filters=filters, snapshot=False)]

    @property
    def roles_by_id(self):
        return {r.role_id: r for r in self.roles}

    @property
    def roles_by_name(self):
        return {r.name: r for r in self.roles}

    def get_users(self, username: str = None):
        """
        Gets all users or filters on one of the options.
        :param username: str: Username to filter
        :return: List of users
        """
        filters = {"username": ["ieq", username]} if username else None
        users = self.client.fetch_all("tables/users", filters=filters, snapshot=False)
        return [User(**user) for user in users]

    def get_user_by_id(self, user_id: str):
        """
        Gets a user by ID
        :param user_id: Union[str, int]: User ID to filter
        :return: User
        """
        resp = self.client.get("users/" + str(user_id))
        resp.raise_for_status()
        user = resp.json()
        return User(roleNames=[self.roles_by_id[r].name for r in user["roleIds"]], **user)

    def add_user(
        self,
        username: str,
        password: str,
        roles: list,
        timezone: str = "UTC",
    ):
        """
        Adds a user
        :param username: str: Username
        :param password: str: Must be 8 characters
        :param roles: list: Role IDs for Users
        :param timezone: str: v4.2 and above, Defaults UTC.  See pytz.all_timezones for correct syntax
        :return: User
        """
        if len(password) < 8:
            raise SyntaxError("Password must be 8 characters.")
        if not all(x in [r.role_id for r in self.roles] for x in roles):
            raise SyntaxError(f"Only accepted scopes are {[r.role_id for r in self.roles]}")
        payload = {
            "username": username,
            "password": password,
            "roleIds": roles,
        }
        if timezone not in pytz.all_timezones:
            raise ValueError(
                f"Timezone {timezone} is not located. This is case sensitive please see pytz.all_timezones."
            )
        payload["timezone"] = timezone
        resp = self.client.post("users", json=payload)
        resp.raise_for_status()
        user = resp.json()
        return User(roleNames=[self.roles_by_id[r].name for r in user["roleIds"]], **user)

    def delete_user(self, user_id: str):
        """
        Deletes a user and returns list of remaining users
        :param user_id:
        :return:
        """
        resp = self.client.delete("users/" + str(user_id))
        resp.raise_for_status()
        return self.get_users()
