# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DirectoryRoleEligibilityScheduleRequestArgs', 'DirectoryRoleEligibilityScheduleRequest']

@pulumi.input_type
class DirectoryRoleEligibilityScheduleRequestArgs:
    def __init__(__self__, *,
                 directory_scope_id: pulumi.Input[str],
                 justification: pulumi.Input[str],
                 principal_id: pulumi.Input[str],
                 role_definition_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a DirectoryRoleEligibilityScheduleRequest resource.
        :param pulumi.Input[str] directory_scope_id: Identifier of the directory object representing the scope of the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] justification: Justification for why the principal is granted the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] principal_id: The object ID of the principal to granted the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] role_definition_id: The template ID (in the case of built-in roles) or object ID (in the case of custom roles) of the directory role you want to assign. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "directory_scope_id", directory_scope_id)
        pulumi.set(__self__, "justification", justification)
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "role_definition_id", role_definition_id)

    @property
    @pulumi.getter(name="directoryScopeId")
    def directory_scope_id(self) -> pulumi.Input[str]:
        """
        Identifier of the directory object representing the scope of the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "directory_scope_id")

    @directory_scope_id.setter
    def directory_scope_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "directory_scope_id", value)

    @property
    @pulumi.getter
    def justification(self) -> pulumi.Input[str]:
        """
        Justification for why the principal is granted the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "justification")

    @justification.setter
    def justification(self, value: pulumi.Input[str]):
        pulumi.set(self, "justification", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[str]:
        """
        The object ID of the principal to granted the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Input[str]:
        """
        The template ID (in the case of built-in roles) or object ID (in the case of custom roles) of the directory role you want to assign. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_definition_id", value)


@pulumi.input_type
class _DirectoryRoleEligibilityScheduleRequestState:
    def __init__(__self__, *,
                 directory_scope_id: Optional[pulumi.Input[str]] = None,
                 justification: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DirectoryRoleEligibilityScheduleRequest resources.
        :param pulumi.Input[str] directory_scope_id: Identifier of the directory object representing the scope of the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] justification: Justification for why the principal is granted the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] principal_id: The object ID of the principal to granted the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] role_definition_id: The template ID (in the case of built-in roles) or object ID (in the case of custom roles) of the directory role you want to assign. Changing this forces a new resource to be created.
        """
        if directory_scope_id is not None:
            pulumi.set(__self__, "directory_scope_id", directory_scope_id)
        if justification is not None:
            pulumi.set(__self__, "justification", justification)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if role_definition_id is not None:
            pulumi.set(__self__, "role_definition_id", role_definition_id)

    @property
    @pulumi.getter(name="directoryScopeId")
    def directory_scope_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the directory object representing the scope of the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "directory_scope_id")

    @directory_scope_id.setter
    def directory_scope_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_scope_id", value)

    @property
    @pulumi.getter
    def justification(self) -> Optional[pulumi.Input[str]]:
        """
        Justification for why the principal is granted the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "justification")

    @justification.setter
    def justification(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "justification", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object ID of the principal to granted the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The template ID (in the case of built-in roles) or object ID (in the case of custom roles) of the directory role you want to assign. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_definition_id", value)


class DirectoryRoleEligibilityScheduleRequest(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_scope_id: Optional[pulumi.Input[str]] = None,
                 justification: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a single directory role eligibility schedule request within Azure Active Directory.

        ## API Permissions

        The following API permissions are required in order to use this resource.

        The calling principal requires one of the following application roles: `RoleEligibilitySchedule.ReadWrite.Directory` or `RoleManagement.ReadWrite.Directory`.

        The calling principal requires one of the following directory roles: `Privileged Role Administrator` or `Global Administrator`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example_user = azuread.get_user(user_principal_name="jdoe@example.com")
        example_directory_role = azuread.DirectoryRole("exampleDirectoryRole", display_name="Application Administrator")
        example_directory_role_eligibility_schedule_request = azuread.DirectoryRoleEligibilityScheduleRequest("exampleDirectoryRoleEligibilityScheduleRequest",
            role_definition_id=example_directory_role.template_id,
            principal_id=azuread_user["example"]["object_id"],
            directory_scope_id="/",
            justification="Example")
        ```

        > Note the use of the `template_id` attribute when referencing built-in roles.

        ## Import

        Directory role eligibility schedule requests can be imported using the ID of the assignment, e.g.

        ```sh
        $ pulumi import azuread:index/directoryRoleEligibilityScheduleRequest:DirectoryRoleEligibilityScheduleRequest example 822ec710-4c9f-4f71-a27a-451759cc7522
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] directory_scope_id: Identifier of the directory object representing the scope of the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] justification: Justification for why the principal is granted the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] principal_id: The object ID of the principal to granted the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] role_definition_id: The template ID (in the case of built-in roles) or object ID (in the case of custom roles) of the directory role you want to assign. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DirectoryRoleEligibilityScheduleRequestArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a single directory role eligibility schedule request within Azure Active Directory.

        ## API Permissions

        The following API permissions are required in order to use this resource.

        The calling principal requires one of the following application roles: `RoleEligibilitySchedule.ReadWrite.Directory` or `RoleManagement.ReadWrite.Directory`.

        The calling principal requires one of the following directory roles: `Privileged Role Administrator` or `Global Administrator`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example_user = azuread.get_user(user_principal_name="jdoe@example.com")
        example_directory_role = azuread.DirectoryRole("exampleDirectoryRole", display_name="Application Administrator")
        example_directory_role_eligibility_schedule_request = azuread.DirectoryRoleEligibilityScheduleRequest("exampleDirectoryRoleEligibilityScheduleRequest",
            role_definition_id=example_directory_role.template_id,
            principal_id=azuread_user["example"]["object_id"],
            directory_scope_id="/",
            justification="Example")
        ```

        > Note the use of the `template_id` attribute when referencing built-in roles.

        ## Import

        Directory role eligibility schedule requests can be imported using the ID of the assignment, e.g.

        ```sh
        $ pulumi import azuread:index/directoryRoleEligibilityScheduleRequest:DirectoryRoleEligibilityScheduleRequest example 822ec710-4c9f-4f71-a27a-451759cc7522
        ```

        :param str resource_name: The name of the resource.
        :param DirectoryRoleEligibilityScheduleRequestArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DirectoryRoleEligibilityScheduleRequestArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_scope_id: Optional[pulumi.Input[str]] = None,
                 justification: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DirectoryRoleEligibilityScheduleRequestArgs.__new__(DirectoryRoleEligibilityScheduleRequestArgs)

            if directory_scope_id is None and not opts.urn:
                raise TypeError("Missing required property 'directory_scope_id'")
            __props__.__dict__["directory_scope_id"] = directory_scope_id
            if justification is None and not opts.urn:
                raise TypeError("Missing required property 'justification'")
            __props__.__dict__["justification"] = justification
            if principal_id is None and not opts.urn:
                raise TypeError("Missing required property 'principal_id'")
            __props__.__dict__["principal_id"] = principal_id
            if role_definition_id is None and not opts.urn:
                raise TypeError("Missing required property 'role_definition_id'")
            __props__.__dict__["role_definition_id"] = role_definition_id
        super(DirectoryRoleEligibilityScheduleRequest, __self__).__init__(
            'azuread:index/directoryRoleEligibilityScheduleRequest:DirectoryRoleEligibilityScheduleRequest',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            directory_scope_id: Optional[pulumi.Input[str]] = None,
            justification: Optional[pulumi.Input[str]] = None,
            principal_id: Optional[pulumi.Input[str]] = None,
            role_definition_id: Optional[pulumi.Input[str]] = None) -> 'DirectoryRoleEligibilityScheduleRequest':
        """
        Get an existing DirectoryRoleEligibilityScheduleRequest resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] directory_scope_id: Identifier of the directory object representing the scope of the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] justification: Justification for why the principal is granted the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] principal_id: The object ID of the principal to granted the role eligibility. Changing this forces a new resource to be created.
        :param pulumi.Input[str] role_definition_id: The template ID (in the case of built-in roles) or object ID (in the case of custom roles) of the directory role you want to assign. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DirectoryRoleEligibilityScheduleRequestState.__new__(_DirectoryRoleEligibilityScheduleRequestState)

        __props__.__dict__["directory_scope_id"] = directory_scope_id
        __props__.__dict__["justification"] = justification
        __props__.__dict__["principal_id"] = principal_id
        __props__.__dict__["role_definition_id"] = role_definition_id
        return DirectoryRoleEligibilityScheduleRequest(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="directoryScopeId")
    def directory_scope_id(self) -> pulumi.Output[str]:
        """
        Identifier of the directory object representing the scope of the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "directory_scope_id")

    @property
    @pulumi.getter
    def justification(self) -> pulumi.Output[str]:
        """
        Justification for why the principal is granted the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "justification")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[str]:
        """
        The object ID of the principal to granted the role eligibility. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Output[str]:
        """
        The template ID (in the case of built-in roles) or object ID (in the case of custom roles) of the directory role you want to assign. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "role_definition_id")

