import logging
from datetime import date, datetime
from typing import Any, Optional, Union

import jwt

from qottoauth import Matching, Namespace
from qottoauth.api import QottoAuthApi
from qottoauth.models import (
    Account, Actor, Application, Authorization,
    CookiePair, Identity, Member, Organization,
    Permission, Role, TokenInfo, User, UserRequest,
)

__all__ = [
    'QottoAuthService',
]

logger = logging.getLogger(__name__)


def _filter_variables(*variables: tuple[str, str, Any]) -> list[tuple[str, str, Any]]:
    return [variable for variable in variables if variable[2] is not None]


class QottoAuthService:

    def __init__(
            self,
            api: QottoAuthApi,
    ):
        self.api = api

    def application(self, id: str) -> Application:
        response = self.api.query(
            name='application',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body=Application.body(),
        )
        return Application.from_dict(response)

    def applications(self, name_contains: Optional[str] = None) -> list[Application]:
        response = self.api.query(
            name='applications',
            variables=_filter_variables(
                ('name_Icontains', 'String', name_contains),
            ),
            body='edges { node {' + Application.body() + '} }'
        )
        return [Application.from_dict(edge['node']) for edge in response['edges']]

    def create_application(
            self,
            code: str, name: Optional[str] = None, description: Optional[str] = None,
            uuid: Optional[str] = None,
    ) -> Application:
        payload = self.api.mutation(
            name='createApplication',
            input_value=dict(uuid=uuid, code=code, name=name, description=description),
            body='application {' + Application.body() + '}',
        )
        return Application.from_dict(payload['application'])

    def register_application(
            self,
            code: str, name: Optional[str] = None, description: Optional[str] = None,
            uuid: Optional[str] = None,
    ) -> Application:
        payload = self.api.mutation(
            name='registerApplication',
            input_value=dict(uuid=uuid, code=code, name=name, description=description),
            body='application { ' + Application.body() + ' }',
        )
        return Application.from_dict(payload['application'])

    def delete_application(self, application: Union[Application, str]) -> bool:
        application_id = application.id if isinstance(application, Application) else application
        response = self.api.mutation(
            name='deleteApplication',
            input_value=dict(applicationId=application_id),
            body='deleted',
        )
        return bool(response['deleted'])

    def permission(self, id: str) -> Permission:
        response = self.api.query(
            name='permission',
            variables=[
                ('id', 'ID!', id),
            ],
            body=Permission.body(),
        )
        return Permission.from_dict(response)

    def permissions(
            self,
            name_contains: Optional[str] = None,
            application: Union[Application, str, None] = None,
            authorization: Union[Authorization, str, None] = None,
    ) -> list[Permission]:
        application_id = application.id if isinstance(application, Application) else application
        authorization_id = authorization.id if isinstance(authorization, Authorization) else authorization
        response = self.api.query(
            name='permissions',
            variables=_filter_variables(
                ('name_Icontains', 'String', name_contains),
                ('application_Id', 'String', application_id),
                ('authorization_Id', 'String', authorization_id),
            ),
            body='edges { node { ' + Permission.body() + ' } }',
        )
        return [Permission.from_dict(edge['node']) for edge in response['edges']]

    def create_permission(
            self,
            application: Union[Application, str],
            code: str, name: Optional[str] = None, description: Optional[str] = None,
            uuid: Optional[str] = None,
    ) -> Permission:
        application_id = application.id if isinstance(application, Application) else application
        payload = self.api.mutation(
            name='createPermission',
            input_value=dict(applicationId=application_id, uuid=uuid, code=code, name=name, description=description),
            body='permission { ' + Permission.body() + ' }',
        )
        return Permission.from_dict(payload['permission'])

    def register_permission(
            self,
            application: Union[Application, str],
            code: str, name: Optional[str] = None, description: Optional[str] = None,
            uuid: Optional[str] = None,
    ) -> Permission:
        application_id = application.id if isinstance(application, Application) else application
        payload = self.api.mutation(
            name='registerPermission',
            input_value=dict(applicationId=application_id, uuid=uuid, code=code, name=name, description=description),
            body='permission { ' + Permission.body() + ' }',
        )
        return Permission.from_dict(payload['permission'])

    def register_permissions(
            self,
            application: Union[Application, str],
            permissions: list[dict[str, Any]],
    ) -> list[Permission]:
        application_id = application.id if isinstance(application, Application) else application
        payload = self.api.mutation(
            name='registerPermissions',
            input_value=dict(applicationId=application_id, permissions=permissions),
            body='permissions { ' + Permission.body() + ' }',
        )
        return [Permission.from_dict(permission) for permission in payload['permissions']]

    def delete_permission(self, permission: Union[Permission, str]) -> bool:
        permission_id = permission.id if isinstance(permission, Permission) else permission
        payload = self.api.mutation(
            name='deletePermission',
            input_value=dict(permissionId=permission_id),
            body='deleted',
        )
        return bool(payload['deleted'])

    def organization(self, id: str) -> Organization:
        response = self.api.query(
            name='organization',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body='id name namespace',
        )
        return Organization.from_dict(response)

    def organizations(
            self,
            name_contains: Optional[str] = None, namespace_contains: Optional[str] = None,
    ) -> list[Organization]:
        response = self.api.query(
            name='organizations',
            variables=_filter_variables(
                ('name_Icontains', 'String', name_contains),
                ('namespace_Icontains', 'String', namespace_contains),
            ),
            body='edges { node { id name namespace } }',
        )
        return [Organization.from_dict(edge['node']) for edge in response['edges']]

    def create_organization(
            self,
            namespace: Union[Namespace, str], name: Optional[str] = None, uuid: Optional[str] = None,
    ) -> Organization:
        payload = self.api.mutation(
            name='createOrganization',
            input_value=dict(
                uuid=uuid,
                name=name,
                namespace=str(namespace),
            ),
            body='organization { ' + Organization.body() + ' }',
        )
        return Organization.from_dict(payload['organization'])

    def register_organization(
            self, namespace: Union[Namespace, str], name: Optional[str] = None, uuid: Optional[str] = None,
    ) -> Organization:
        payload = self.api.mutation(
            name='registerOrganization',
            input_value=dict(
                uuid=uuid,
                name=name,
                namespace=str(namespace),
            ),
            body='organization { ' + Organization.body() + ' }',
        )
        return Organization.from_dict(payload['organization'])

    def delete_organization(self, organization: Union[Organization, str]) -> bool:
        organization_id = organization.id if isinstance(organization, Organization) else organization
        payload = self.api.mutation(
            name='deleteOrganization',
            input_value=dict(organizationId=organization_id),
            body='deleted',
        )
        return bool(payload['deleted'])

    def user(self, id: str) -> User:
        response = self.api.query(
            name='user',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body=User.body(),
        )
        return User.from_dict(response)

    def users(
            self,
            name_contains: Optional[str] = None,
            associated: Optional[bool] = None
    ) -> list[User]:
        response = self.api.query(
            name='users',
            variables=_filter_variables(
                ('associated', 'Boolean', associated),
                ('name_Icontains', 'String', name_contains),
            ),
            body='edges { node { ' + User.body() + ' } }',
        )
        return [User.from_dict(edge['node']) for edge in response['edges']]

    def create_user(
            self,
            name: str,
            email: str,
            given_name: Optional[str] = None,
            middle_name: Optional[str] = None,
            family_name: Optional[str] = None,
            picture: Optional[str] = None,
            birthdate: Union[date, str, None] = None,
            country: Optional[str] = None,
            address: Optional[str] = None,
            phone_number: Optional[str] = None,
            job_title: Optional[str] = None,
            is_superuser: bool = False,
            uuid: Optional[str] = None,
    ) -> User:
        birthdate = date.fromisoformat(birthdate) if isinstance(birthdate, str) else birthdate
        payload = self.api.mutation(
            name='createUser',
            input_value=dict(
                uuid=uuid,
                isSuperuser=is_superuser,
                name=name,
                email=email,
                givenName=given_name,
                middleName=middle_name,
                familyName=family_name,
                picture=picture,
                birthdate=birthdate.isoformat() if birthdate else None,
                country=country,
                address=address,
                phoneNumber=phone_number,
                jobTitle=job_title,
            ),
            body='user { ' + User.body() + ' }',
        )
        return User.from_dict(payload['user'])

    def update_user(
            self, user: Union[User, str],
            add_identity: Union[Identity, str, None] = None, remove_identity: Union[Identity, str, None] = None,
            set_archived: Optional[bool] = None, set_superuser: Optional[bool] = None,
            set_name: Optional[str] = None, set_email: Optional[str] = None,
            set_given_name: Optional[str] = None, set_middle_name: Optional[str] = None,
            set_family_name: Optional[str] = None,
            set_picture: Optional[str] = None, set_birthdate: Union[date, str, None] = None,
            set_country: Optional[str] = None, set_address: Optional[str] = None,
            set_phone_number: Optional[str] = None, set_job_title: Optional[str] = None,
    ) -> User:
        user_id = user.id if isinstance(user, User) else user
        add_identity_id = add_identity.id if isinstance(add_identity, Identity) else add_identity
        remove_identity_id = remove_identity.id if isinstance(remove_identity, Identity) else remove_identity
        payload = self.api.mutation(
            name='updateUser',
            input_value=dict(
                userId=user_id,
                addIdentityId=add_identity_id, removeIdentityId=remove_identity_id,
                setArchived=set_archived, setSuperuser=set_superuser,
                setName=set_name, setEmail=set_email,
                setGivenName=set_given_name, setMiddleName=set_middle_name, setFamilyName=set_family_name,
                setPicture=set_picture, setBirthdate=set_birthdate,
                setCountry=set_country, setAddress=set_address, setPhoneNumber=set_phone_number,
                setJobTitle=set_job_title,
            ),
            body='user { ' + User.body() + ' }',
        )
        return User.from_dict(payload['user'])

    def delete_user(self, user: Union[User, str]) -> bool:
        user_id = user.id if isinstance(user, User) else user
        payload = self.api.mutation(
            name='deleteUser',
            input_value=dict(userId=user_id),
            body='deleted',
        )
        return bool(payload['deleted'])

    def identity(self, id: str) -> Identity:
        response = self.api.query(
            name='identity',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body=Identity.body(),
        )
        return Identity.from_dict(response)

    def identities(
            self,
            provider_id: Optional[str] = None,
            name_contains: Optional[str] = None, email_contains: Optional[str] = None,
            user: Union[User, str, None] = None,
            associated: Optional[bool] = None, pending: Optional[bool] = None, blocked: Optional[bool] = None,
    ) -> list[Identity]:
        response = self.api.query(
            name='identities',
            variables=_filter_variables(
                ('providerId', 'String', provider_id),
                ('name_Icontains', 'String', name_contains),
                ('email_Icontains', 'String', email_contains),
                ('user_Id', 'String', user.id if isinstance(user, User) else user),
                ('associated', 'Boolean', associated),
                ('pending', 'Boolean', pending),
                ('blocked', 'Boolean', blocked),
            ),
            body='edges { node { ' + Identity.body() + ' } }',
        )
        return [Identity.from_dict(edge['node']) for edge in response['edges']]

    def register_identity(self, provider_id: str, id_token: str) -> Identity:
        payload = self.api.mutation(
            name='registerIdentity',
            input_value=dict(providerId=provider_id, idToken=id_token),
            body='identity { ' + Identity.body() + ' }',
        )
        return Identity.from_dict(payload['identity'])

    def update_identity(
            self, identity: Union[Identity, str],
            set_blocked: Optional[bool] = None,
    ) -> Identity:
        identity_id = identity.id if isinstance(identity, Identity) else identity
        payload = self.api.mutation(
            name='updateIdentity',
            input_value=dict(identityId=identity_id, setBlocked=set_blocked),
            body='identity { ' + Identity.body() + ' }',
        )
        return Identity.from_dict(payload['identity'])

    def delete_identity(self, identity: Union[Identity, str]) -> bool:
        identity_id = identity.id if isinstance(identity, Identity) else identity
        payload = self.api.mutation(
            name='deleteIdentity',
            input_value=dict(identityId=identity_id),
            body='deleted',
        )
        return bool(payload['deleted'])

    def authorization(self, id: str) -> Authorization:
        response = self.api.query(
            name='authorization',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body=Authorization.body(),
        )
        return Authorization.from_dict(response)

    def authorizations(
            self,
            name_contains: Optional[str] = None,
            organization: Union[Organization, str, None] = None,
            member: Union[Member, str, None] = None,
            permission: Union[Permission, str, None] = None,
            role: Union[Role, str, None] = None,
    ) -> list[Authorization]:
        organization_id = organization.id if isinstance(organization, Organization) else organization
        member_id = member.id if isinstance(member, Member) else member
        permission_id = permission.id if isinstance(permission, Permission) else permission
        role_id = role.id if isinstance(role, Role) else role
        response = self.api.query(
            name='authorizations',
            variables=_filter_variables(
                ('organization_Id', 'String', organization_id),
                ('name_Icontains', 'String', name_contains),
                ('member_Id', 'String', member_id),
                ('permission_Id', 'String', permission_id),
                ('role_Id', 'String', role_id),
            ),
            body='edges { node { ' + Authorization.body() + ' } }',
        )
        return [Authorization.from_dict(edge['node']) for edge in response['edges']]

    def create_authorization(
            self, name: str, description: str,
            organization: Union[Organization, str],
            matching: Union[Matching, str],
            inheritance: bool,
    ) -> Authorization:
        organization_id = organization.id if isinstance(organization, Organization) else organization
        matching_value = matching.value if isinstance(matching, Matching) else matching
        payload = self.api.mutation(
            name='createAuthorization',
            input_value=dict(
                name=name, description=description,
                organizationId=organization_id,
                matching=matching_value,
                inheritance=inheritance,
            ),
            body='authorization { ' + Authorization.body() + ' }',
        )
        return Authorization.from_dict(payload['authorization'])

    def update_authorization(
            self,
            authorization: Union[Authorization, str],
            add_permission: Union[Permission, str, None] = None, remove_permission: Union[Permission, str, None] = None,
            set_name: Optional[str] = None, set_description: Optional[str] = None,
            set_organization: Union[Organization, str, None] = None,
            set_matching: Union[Matching, str, None] = None,
            set_inheritance: Optional[bool] = None,
    ) -> Authorization:
        authorization_id = authorization.id if isinstance(authorization, Authorization) else authorization
        add_permission_id = add_permission.id if isinstance(add_permission, Permission) else add_permission
        remove_permission_id = remove_permission.id if isinstance(remove_permission, Permission) else remove_permission
        set_organization_id = set_organization.id if isinstance(set_organization, Organization) else set_organization
        set_matching_value = set_matching.value if isinstance(set_matching, Matching) else set_matching
        payload = self.api.mutation(
            name='updateAuthorization',
            input_value=dict(
                authorizationId=authorization_id,
                addPermissionId=add_permission_id,
                removePermissionId=remove_permission_id,
                setName=set_name,
                setDescription=set_description,
                setOrganizationId=set_organization_id,
                setMatching=set_matching_value,
                setInheritance=set_inheritance,
            ),
            body='authorization { ' + Authorization.body() + ' }',
        )
        return Authorization.from_dict(payload['authorization'])

    def delete_authorization(self, authorization: Union[Authorization, str]) -> bool:
        authorization_id = authorization.id if isinstance(authorization, Authorization) else authorization
        payload = self.api.mutation(
            name='deleteAuthorization',
            input_value=dict(authorizationId=authorization_id),
            body='deleted',
        )
        return bool(payload['deleted'])

    def role(self, id: str) -> Role:
        response = self.api.query(
            name='role',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body=Role.body(),
        )
        return Role.from_dict(response)

    def roles(
            self,
            name_contains: Optional[str] = None,
            organization: Union[Organization, str, None] = None,
            member: Union[Member, str, None] = None,
            authorization: Union[Authorization, str, None] = None,
    ) -> list[Role]:
        organization_id = organization.id if isinstance(organization, Organization) else organization
        member_id = member.id if isinstance(member, Member) else member
        authorization_id = authorization.id if isinstance(authorization, Authorization) else authorization
        response = self.api.query(
            name='roles',
            variables=_filter_variables(
                ('name_Icontains', 'String', name_contains),
                ('organization_Id', 'String', organization_id),
                ('member_Id', 'String', member_id),
                ('authorization_Id', 'String', authorization_id),
            ),
            body='edges { node { ' + Role.body() + ' } }',
        )
        return [Role.from_dict(edge['node']) for edge in response['edges']]

    def create_role(
            self, name: str, description: str,
            organization: Union[Organization, str],
            inheritance: bool,
    ) -> Role:
        organization_id = organization.id if isinstance(organization, Organization) else organization
        payload = self.api.mutation(
            name='createRole',
            input_value=dict(
                name=name, description=description,
                organizationId=organization_id,
                inheritance=inheritance,
            ),
            body='role { ' + Role.body() + ' }',
        )
        return Role.from_dict(payload['role'])

    def update_role(
            self,
            role: Union[Role, str],
            add_authorization: Union[Authorization, str, None] = None,
            remove_authorization: Union[Authorization, str, None] = None,
            set_name: Optional[str] = None, set_description: Optional[str] = None,
            set_organization: Union[Organization, str, None] = None,
            set_inheritance: Optional[bool] = None,
    ) -> Role:
        role_id = role.id if isinstance(role, Role) else role
        add_authorization_id = add_authorization.id if isinstance(
            add_authorization, Authorization
        ) else add_authorization
        remove_authorization_id = remove_authorization.id if isinstance(
            remove_authorization, Authorization
        ) else remove_authorization
        set_organization_id = set_organization.id if isinstance(set_organization, Organization) else set_organization
        payload = self.api.mutation(
            name='updateRole',
            input_value=dict(
                roleId=role_id,
                addAuthorizationId=add_authorization_id,
                removeAuthorizationId=remove_authorization_id,
                setName=set_name,
                setDescription=set_description,
                setOrganizationId=set_organization_id,
                setInheritance=set_inheritance,
            ),
            body='role { ' + Role.body() + ' }',
        )
        return Role.from_dict(payload['role'])

    def delete_role(self, role: Union[Role, str]) -> bool:
        role_id = role.id if isinstance(role, Role) else role
        payload = self.api.mutation(
            name='deleteRole',
            input_value=dict(roleId=role_id),
            body='deleted',
        )
        return bool(payload['deleted'])

    def member(self, id: str) -> Member:
        response = self.api.query(
            name='member',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body=Member.body(),
        )
        return Member.from_dict(response)

    def members(
            self,
            user: Union[User, str, None] = None, organization: Union[Organization, str, None] = None,
    ) -> list[Member]:
        user_id = user.id if isinstance(user, User) else user
        organization_id = organization.id if isinstance(organization, Organization) else organization
        response = self.api.query(
            name='members',
            variables=_filter_variables(
                ('user_Id', 'String', user_id),
                ('organization_Id', 'String', organization_id),
            ),
            body='edges { node { ' + Member.body() + ' } }',
        )
        return [Member.from_dict(edge['node']) for edge in response['edges']]

    def create_member(
            self,
            user: Union[User, str],
            organization: Union[Organization, str],
            uuid: Optional[str] = None,
    ) -> Member:
        user_id = user.id if isinstance(user, User) else user
        organization_id = organization.id if isinstance(organization, Organization) else organization
        payload = self.api.mutation(
            name='createMember',
            input_value=dict(
                uuid=uuid,
                userId=user_id,
                organizationId=organization_id,
            ),
            body='member { ' + Member.body() + ' }',
        )
        return Member.from_dict(payload['member'])

    def update_member(
            self,
            member: Union[Member, str],
            add_authorization: Union[Authorization, str, None] = None,
            remove_authorization: Union[Authorization, str, None] = None,
            add_role: Union[Role, str, None] = None, remove_role: Union[Role, str, None] = None,
    ) -> Member:
        member_id = member.id if isinstance(member, Member) else member
        add_authorization_id = add_authorization.id if isinstance(
            add_authorization, Authorization
        ) else add_authorization
        remove_authorization_id = remove_authorization.id if isinstance(
            remove_authorization, Authorization
        ) else remove_authorization
        add_role_id = add_role.id if isinstance(add_role, Role) else add_role
        remove_role_id = remove_role.id if isinstance(remove_role, Role) else remove_role
        payload = self.api.mutation(
            name='updateMember',
            input_value=dict(
                memberId=member_id,
                addAuthorizationId=add_authorization_id,
                removeAuthorizationId=remove_authorization_id,
                addRoleId=add_role_id,
                removeRoleId=remove_role_id,
            ),
            body='member { ' + Member.body() + ' }',
        )
        return Member.from_dict(payload['member'])

    def delete_member(self, member: Union[Member, str]) -> bool:
        member_id = member.id if isinstance(member, Member) else member
        payload = self.api.mutation(
            name='deleteMember',
            input_value=dict(memberId=member_id),
            body='deleted',
        )
        return bool(payload['deleted'])

    def account(self, id: str) -> Account:
        response = self.api.query(
            name='account',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body=Account.body(),
        )
        return Account.from_dict(response)

    def accounts(
            self,
            application: Union[Application, str, None] = None,
            user: Union[User, str, None] = None,
            enabled: Optional[bool] = None,
    ) -> list[Account]:
        application_id = application.id if isinstance(application, Application) else application
        user_id = user.id if isinstance(user, User) else user
        response = self.api.query(
            name='accounts',
            variables=_filter_variables(
                ('application_Id', 'String', application_id),
                ('user_Id', 'String', user_id),
                ('enabled', 'Boolean', enabled),
            ),
            body='edges { node { ' + Account.body() + ' } }',
        )
        return [Account.from_dict(edge['node']) for edge in response['edges']]

    def create_account(self, user: Union[User, str], application: Union[Application, str]) -> Account:
        user_id = user.id if isinstance(user, User) else user
        application_id = application.id if isinstance(application, Application) else application
        payload = self.api.mutation(
            name='createAccount',
            input_value=dict(userId=user_id, applicationId=application_id),
            body='account { ' + Account.body() + ' }',
        )
        return Account.from_dict(payload['account'])

    def update_account(
            self, account: Union[Account, str],
            set_enabled: Optional[bool] = None,
    ) -> Account:
        account_id = account.id if isinstance(account, Account) else account
        payload = self.api.mutation(
            name='updateAccount',
            input_value=dict(
                accountId=account_id,
                setEnabled=set_enabled,
            ),
            body='account { ' + Account.body() + ' }',
        )
        return Account.from_dict(payload['account'])

    def delete_account(self, account: Union[Account, str]) -> bool:
        account_id = account.id if isinstance(account, Account) else account
        payload = self.api.mutation(
            name='deleteAccount',
            input_value=dict(accountId=account_id),
            body='deleted',
        )
        return bool(payload['deleted'])

    def create_user_request(
            self,
            identity: Union[Identity, str],
            name: Optional[str] = None,
            given_name: Optional[str] = None,
            middle_name: Optional[str] = None,
            family_name: Optional[str] = None,
            picture: Optional[str] = None,
            birthdate: Union[date, str, None] = None,
            country: Optional[str] = None,
            address: Optional[str] = None,
            phone_number: Optional[str] = None,
            job_title: Optional[str] = None,
            comment: Optional[str] = None,
    ) -> UserRequest:
        identity_id = identity.id if isinstance(identity, Identity) else identity
        birthdate = date.fromisoformat(birthdate) if isinstance(birthdate, str) else birthdate
        payload = self.api.mutation(
            name='createUserRequest',
            input_value=dict(
                identityId=identity_id, comment=comment,
                name=name,
                givenName=given_name,
                middleName=middle_name,
                familyName=family_name,
                picture=picture,
                birthdate=birthdate.isoformat() if birthdate else None,
                country=country,
                address=address,
                phoneNumber=phone_number,
                jobTitle=job_title,
            ),
            body='userRequest { ' + UserRequest.body() + ' }',
        )
        return UserRequest.from_dict(payload['userRequest'])

    def accept_user_request(self, user_request: Union[UserRequest, str]) -> tuple[User, Identity]:
        user_request_id = user_request.id if isinstance(user_request, UserRequest) else user_request
        payload = self.api.mutation(
            name='acceptUserRequest',
            input_value=dict(userRequestId=user_request_id),
            body='user { ' + User.body() + ' } identity { ' + Identity.body() + ' }',
        )
        return User.from_dict(payload['user']), Identity.from_dict(payload['identity'])

    def reject_user_request(
            self, user_request: Union[UserRequest, str],
            block_identity: bool = False,
            delete_identity: bool = False,
    ) -> Optional[Identity]:
        user_request_id = user_request.id if isinstance(user_request, UserRequest) else user_request
        payload = self.api.mutation(
            name='rejectUserRequest',
            input_value=dict(
                userRequestId=user_request_id,
                blockIdentity=block_identity,
                deleteIdentity=delete_identity,
            ),
            body='identity { ' + Identity.body() + ' }',
        )
        identity = Identity.from_dict(payload['identity']) if payload['identity'] else None
        return identity

    def user_request(self, id: str) -> UserRequest:
        response = self.api.query(
            name='userRequest',
            variables=_filter_variables(
                ('id', 'ID!', id),
            ),
            body=UserRequest.body(),
        )
        return UserRequest.from_dict(response)

    def user_requests(
            self,
            identity: Union[Identity, str] = None,
    ) -> list[UserRequest]:
        identity_id = identity.id if isinstance(identity, Identity) else identity
        response = self.api.query(
            name='userRequests',
            variables=_filter_variables(
                ('identity_Id', 'String', identity_id),
            ),
            body='edges { node { ' + UserRequest.body() + ' } }',
        )
        return [UserRequest.from_dict(edge['node']) for edge in response['edges']]

    def ticket_for_identity(self, identity: Union[Identity, str]) -> str:
        identity_id = identity.id if isinstance(identity, Identity) else identity
        response: str = self.api.query(
            name='identityTicket',
            variables=_filter_variables(
                ('identityId', 'ID!', identity_id),
            ),
        )
        return response

    def identity_for_ticket(self, ticket: str) -> Optional[Identity]:
        try:
            identity_id: str = self.api.query(
                name='checkIdentityTicket',
                variables=_filter_variables(
                    ('identityTicket', 'String!', ticket),
                ),
            )
        except Exception:
            return None
        return self.identity(identity_id)

    def decode_token(self, token: str) -> TokenInfo:
        auth_metadata = self.api.auth_metadata()
        if not token:
            return TokenInfo()
        token_algorithm = auth_metadata['token_algorithm']
        token_public_key = auth_metadata['token_public_key']
        try:
            decoded = jwt.decode(token, token_public_key, algorithms=[token_algorithm])
        except Exception:
            return TokenInfo()
        return TokenInfo(
            user_id=decoded.get('sub'),
            display_name=decoded.get('metadata', {}).get('displayed_name'),
            given_name=decoded.get('metadata', {}).get('given_name'),
            middle_name=decoded.get('metadata', {}).get('middle_name'),
            family_name=decoded.get('metadata', {}).get('family_name'),
            email=decoded.get('metadata', {}).get('email'),
            is_superuser=decoded.get('is_superuser'),
            member_id=decoded.get('metadata', {}).get('member_id'),
            organization_id=decoded.get('metadata', {}).get('organization_id'),
            organization_name=decoded.get('metadata', {}).get('organization_name'),
            organization_namespace=decoded.get('metadata', {}).get('organization_namespace'),
            applications=decoded.get('applications'),
        )

    def actor(self, token: Optional[str] = None, secret: Optional[str] = None) -> Actor:
        if not token or not secret:
            return Actor()
        response = self.api.query(
            name='actor',
            variables=_filter_variables(
                ('tokenCookie', 'String', token),
                ('secretCookie', 'String', secret),
            ),
            body=Actor.body(),
        )
        return Actor.from_dict(response)

    def cookies(self, user: Union[User, str, None] = None,
                organization: Union[Organization, str, None] = None) -> CookiePair:
        user_id = user.id if isinstance(user, User) else user
        organization_id = organization.id if isinstance(organization, Organization) else organization
        response = self.api.query(
            name='cookies',
            variables=_filter_variables(
                ('userId', 'ID', user_id),
                ('organizationId', 'ID', organization_id),
            ),
            body=CookiePair.body(),
        )
        return CookiePair.from_dict(response)

    def is_authorized(
            self,
            actor: Union[User, Member, Actor, str],
            permission: Union[Permission, str],
            organization: Union[Organization, Namespace, str, None] = None,
    ) -> bool:
        actor_id = actor
        if isinstance(actor, User):
            actor_id = actor.id
        elif isinstance(actor, Member):
            actor_id = actor.id
        elif isinstance(actor, Actor):
            if actor.member:
                actor_id = actor.member.id
            elif actor.user:
                actor_id = actor.user.id
            else:
                return False
        permission_id = permission.id if isinstance(permission, Permission) else permission
        organization_id = organization
        if isinstance(organization, Organization):
            organization_id = organization.id
        elif isinstance(organization, Namespace):
            organization_id = str(organization)

        response = self.api.query(
            name='isAuthorized',
            variables=_filter_variables(
                ('actorId', 'ID!', actor_id),
                ('permissionId', 'ID!', permission_id),
                ('organizationId', 'String', organization_id),
            ),
        )
        return bool(response)

    def organizations_where_is_authorized(
            self,
            actor: Union[User, Member, Actor, str],
            permission: Union[Permission, str],
    ) -> list[Organization]:
        actor_id = actor
        if isinstance(actor, User):
            actor_id = actor.id
        elif isinstance(actor, Member):
            actor_id = actor.id
        elif isinstance(actor, Actor):
            if actor.member:
                actor_id = actor.member.id
            elif actor.user:
                actor_id = actor.user.id
            else:
                return []
        permission_id = permission.id if isinstance(permission, Permission) else permission

        response = self.api.query(
            name='organizationsWhereIsAuthorized',
            variables=_filter_variables(
                ('actorId', 'ID!', actor_id),
                ('permissionId', 'ID!', permission_id),
            ),
            body=Organization.body(),
        )
        return [Organization.from_dict(org) for org in response]

    def last_change_date(self) -> datetime:
        response = self.api.query(
            name='lastChangeDate',
        )
        return datetime.fromisoformat(response)
