# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetCassandraUserResult',
    'AwaitableGetCassandraUserResult',
    'get_cassandra_user',
    'get_cassandra_user_output',
]

@pulumi.output_type
class GetCassandraUserResult:
    """
    A collection of values returned by getCassandraUser.
    """
    def __init__(__self__, access_cert=None, access_key=None, id=None, password=None, project=None, service_name=None, type=None, username=None):
        if access_cert and not isinstance(access_cert, str):
            raise TypeError("Expected argument 'access_cert' to be a str")
        pulumi.set(__self__, "access_cert", access_cert)
        if access_key and not isinstance(access_key, str):
            raise TypeError("Expected argument 'access_key' to be a str")
        pulumi.set(__self__, "access_key", access_key)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="accessCert")
    def access_cert(self) -> str:
        """
        Access certificate for the user if applicable for the service in question
        """
        return pulumi.get(self, "access_cert")

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> str:
        """
        Access certificate key for the user if applicable for the service in question
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        The password of the Cassandra User.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def project(self) -> str:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the user account. Tells whether the user is the primary account or a regular account.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        The actual name of the Cassandra User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")


class AwaitableGetCassandraUserResult(GetCassandraUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCassandraUserResult(
            access_cert=self.access_cert,
            access_key=self.access_key,
            id=self.id,
            password=self.password,
            project=self.project,
            service_name=self.service_name,
            type=self.type,
            username=self.username)


def get_cassandra_user(project: Optional[str] = None,
                       service_name: Optional[str] = None,
                       username: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCassandraUserResult:
    """
    The Cassandra User data source provides information about the existing Aiven Cassandra User.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    user = aiven.get_cassandra_user(project="my-project",
        service_name="my-service",
        username="user1")
    ```


    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str username: The actual name of the Cassandra User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['serviceName'] = service_name
    __args__['username'] = username
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getCassandraUser:getCassandraUser', __args__, opts=opts, typ=GetCassandraUserResult).value

    return AwaitableGetCassandraUserResult(
        access_cert=pulumi.get(__ret__, 'access_cert'),
        access_key=pulumi.get(__ret__, 'access_key'),
        id=pulumi.get(__ret__, 'id'),
        password=pulumi.get(__ret__, 'password'),
        project=pulumi.get(__ret__, 'project'),
        service_name=pulumi.get(__ret__, 'service_name'),
        type=pulumi.get(__ret__, 'type'),
        username=pulumi.get(__ret__, 'username'))


@_utilities.lift_output_func(get_cassandra_user)
def get_cassandra_user_output(project: Optional[pulumi.Input[str]] = None,
                              service_name: Optional[pulumi.Input[str]] = None,
                              username: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCassandraUserResult]:
    """
    The Cassandra User data source provides information about the existing Aiven Cassandra User.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    user = aiven.get_cassandra_user(project="my-project",
        service_name="my-service",
        username="user1")
    ```


    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str username: The actual name of the Cassandra User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    """
    ...
