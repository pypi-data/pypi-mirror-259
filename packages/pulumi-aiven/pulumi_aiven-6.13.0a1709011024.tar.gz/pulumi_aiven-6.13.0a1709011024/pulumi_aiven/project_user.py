# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProjectUserArgs', 'ProjectUser']

@pulumi.input_type
class ProjectUserArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 member_type: pulumi.Input[str],
                 project: pulumi.Input[str]):
        """
        The set of arguments for constructing a ProjectUser resource.
        :param pulumi.Input[str] email: Email address of the user. Should be lowercase. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] member_type: Project membership type. The possible values are `admin`, `developer` and `operator`.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "member_type", member_type)
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        Email address of the user. Should be lowercase. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="memberType")
    def member_type(self) -> pulumi.Input[str]:
        """
        Project membership type. The possible values are `admin`, `developer` and `operator`.
        """
        return pulumi.get(self, "member_type")

    @member_type.setter
    def member_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "member_type", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _ProjectUserState:
    def __init__(__self__, *,
                 accepted: Optional[pulumi.Input[bool]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 member_type: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProjectUser resources.
        :param pulumi.Input[bool] accepted: Whether the user has accepted the request to join the project; adding user to a project sends an invitation to the target user and the actual membership is only created once the user accepts the invitation.
        :param pulumi.Input[str] email: Email address of the user. Should be lowercase. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] member_type: Project membership type. The possible values are `admin`, `developer` and `operator`.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        if accepted is not None:
            pulumi.set(__self__, "accepted", accepted)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if member_type is not None:
            pulumi.set(__self__, "member_type", member_type)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def accepted(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the user has accepted the request to join the project; adding user to a project sends an invitation to the target user and the actual membership is only created once the user accepts the invitation.
        """
        return pulumi.get(self, "accepted")

    @accepted.setter
    def accepted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "accepted", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the user. Should be lowercase. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="memberType")
    def member_type(self) -> Optional[pulumi.Input[str]]:
        """
        Project membership type. The possible values are `admin`, `developer` and `operator`.
        """
        return pulumi.get(self, "member_type")

    @member_type.setter
    def member_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member_type", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class ProjectUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 member_type: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Project User resource allows the creation and management of Aiven Project Users.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        mytestuser = aiven.ProjectUser("mytestuser",
            project=aiven_project["myproject"]["project"],
            email="john.doe@example.com",
            member_type="admin")
        ```

        ## Import

        ```sh
         $ pulumi import aiven:index/projectUser:ProjectUser mytestuser project/email
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email: Email address of the user. Should be lowercase. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] member_type: Project membership type. The possible values are `admin`, `developer` and `operator`.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Project User resource allows the creation and management of Aiven Project Users.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        mytestuser = aiven.ProjectUser("mytestuser",
            project=aiven_project["myproject"]["project"],
            email="john.doe@example.com",
            member_type="admin")
        ```

        ## Import

        ```sh
         $ pulumi import aiven:index/projectUser:ProjectUser mytestuser project/email
        ```

        :param str resource_name: The name of the resource.
        :param ProjectUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 member_type: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectUserArgs.__new__(ProjectUserArgs)

            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            if member_type is None and not opts.urn:
                raise TypeError("Missing required property 'member_type'")
            __props__.__dict__["member_type"] = member_type
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["accepted"] = None
        super(ProjectUser, __self__).__init__(
            'aiven:index/projectUser:ProjectUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accepted: Optional[pulumi.Input[bool]] = None,
            email: Optional[pulumi.Input[str]] = None,
            member_type: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'ProjectUser':
        """
        Get an existing ProjectUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] accepted: Whether the user has accepted the request to join the project; adding user to a project sends an invitation to the target user and the actual membership is only created once the user accepts the invitation.
        :param pulumi.Input[str] email: Email address of the user. Should be lowercase. This property cannot be changed, doing so forces recreation of the resource.
        :param pulumi.Input[str] member_type: Project membership type. The possible values are `admin`, `developer` and `operator`.
        :param pulumi.Input[str] project: Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectUserState.__new__(_ProjectUserState)

        __props__.__dict__["accepted"] = accepted
        __props__.__dict__["email"] = email
        __props__.__dict__["member_type"] = member_type
        __props__.__dict__["project"] = project
        return ProjectUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accepted(self) -> pulumi.Output[bool]:
        """
        Whether the user has accepted the request to join the project; adding user to a project sends an invitation to the target user and the actual membership is only created once the user accepts the invitation.
        """
        return pulumi.get(self, "accepted")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        Email address of the user. Should be lowercase. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="memberType")
    def member_type(self) -> pulumi.Output[str]:
        """
        Project membership type. The possible values are `admin`, `developer` and `operator`.
        """
        return pulumi.get(self, "member_type")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        Identifies the project this resource belongs to. To set up proper dependencies please refer to this variable as a reference. This property cannot be changed, doing so forces recreation of the resource.
        """
        return pulumi.get(self, "project")

