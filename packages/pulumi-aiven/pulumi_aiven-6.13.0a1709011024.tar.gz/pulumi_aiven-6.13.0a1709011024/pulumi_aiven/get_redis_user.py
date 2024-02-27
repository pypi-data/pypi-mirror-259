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
    'GetRedisUserResult',
    'AwaitableGetRedisUserResult',
    'get_redis_user',
    'get_redis_user_output',
]

@pulumi.output_type
class GetRedisUserResult:
    """
    A collection of values returned by getRedisUser.
    """
    def __init__(__self__, id=None, password=None, project=None, redis_acl_categories=None, redis_acl_channels=None, redis_acl_commands=None, redis_acl_keys=None, service_name=None, type=None, username=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if redis_acl_categories and not isinstance(redis_acl_categories, list):
            raise TypeError("Expected argument 'redis_acl_categories' to be a list")
        pulumi.set(__self__, "redis_acl_categories", redis_acl_categories)
        if redis_acl_channels and not isinstance(redis_acl_channels, list):
            raise TypeError("Expected argument 'redis_acl_channels' to be a list")
        pulumi.set(__self__, "redis_acl_channels", redis_acl_channels)
        if redis_acl_commands and not isinstance(redis_acl_commands, list):
            raise TypeError("Expected argument 'redis_acl_commands' to be a list")
        pulumi.set(__self__, "redis_acl_commands", redis_acl_commands)
        if redis_acl_keys and not isinstance(redis_acl_keys, list):
            raise TypeError("Expected argument 'redis_acl_keys' to be a list")
        pulumi.set(__self__, "redis_acl_keys", redis_acl_keys)
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
        The password of the Redis User.
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
    @pulumi.getter(name="redisAclCategories")
    def redis_acl_categories(self) -> Sequence[str]:
        """
        Defines command category rules. The field is required with`redis_acl_commands` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_categories")

    @property
    @pulumi.getter(name="redisAclChannels")
    def redis_acl_channels(self) -> Sequence[str]:
        """
        Defines the permitted pub/sub channel patterns. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_channels")

    @property
    @pulumi.getter(name="redisAclCommands")
    def redis_acl_commands(self) -> Sequence[str]:
        """
        Defines rules for individual commands. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_commands")

    @property
    @pulumi.getter(name="redisAclKeys")
    def redis_acl_keys(self) -> Sequence[str]:
        """
        Defines key access rules. The field is required with`redis_acl_categories` and `redis_acl_keys`. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "redis_acl_keys")

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
        The actual name of the Redis User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "username")


class AwaitableGetRedisUserResult(GetRedisUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRedisUserResult(
            id=self.id,
            password=self.password,
            project=self.project,
            redis_acl_categories=self.redis_acl_categories,
            redis_acl_channels=self.redis_acl_channels,
            redis_acl_commands=self.redis_acl_commands,
            redis_acl_keys=self.redis_acl_keys,
            service_name=self.service_name,
            type=self.type,
            username=self.username)


def get_redis_user(project: Optional[str] = None,
                   service_name: Optional[str] = None,
                   username: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRedisUserResult:
    """
    The Redis User data source provides information about the existing Aiven Redis User.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    user = aiven.get_redis_user(project="my-project",
        service_name="my-service",
        username="user1")
    ```


    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str username: The actual name of the Redis User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['serviceName'] = service_name
    __args__['username'] = username
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aiven:index/getRedisUser:getRedisUser', __args__, opts=opts, typ=GetRedisUserResult).value

    return AwaitableGetRedisUserResult(
        id=pulumi.get(__ret__, 'id'),
        password=pulumi.get(__ret__, 'password'),
        project=pulumi.get(__ret__, 'project'),
        redis_acl_categories=pulumi.get(__ret__, 'redis_acl_categories'),
        redis_acl_channels=pulumi.get(__ret__, 'redis_acl_channels'),
        redis_acl_commands=pulumi.get(__ret__, 'redis_acl_commands'),
        redis_acl_keys=pulumi.get(__ret__, 'redis_acl_keys'),
        service_name=pulumi.get(__ret__, 'service_name'),
        type=pulumi.get(__ret__, 'type'),
        username=pulumi.get(__ret__, 'username'))


@_utilities.lift_output_func(get_redis_user)
def get_redis_user_output(project: Optional[pulumi.Input[str]] = None,
                          service_name: Optional[pulumi.Input[str]] = None,
                          username: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRedisUserResult]:
    """
    The Redis User data source provides information about the existing Aiven Redis User.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    user = aiven.get_redis_user(project="my-project",
        service_name="my-service",
        username="user1")
    ```


    :param str project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str service_name: Specifies the name of the service that this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    :param str username: The actual name of the Redis User. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
    """
    ...
