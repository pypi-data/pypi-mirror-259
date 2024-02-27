# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UserFlowAttributeArgs', 'UserFlowAttribute']

@pulumi.input_type
class UserFlowAttributeArgs:
    def __init__(__self__, *,
                 data_type: pulumi.Input[str],
                 description: pulumi.Input[str],
                 display_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a UserFlowAttribute resource.
        :param pulumi.Input[str] data_type: The data type of the user flow attribute. Possible values are `boolean`, `dateTime`, `int64`, `string` or `stringCollection`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of the user flow attribute that is shown to the user at the time of sign-up.
        :param pulumi.Input[str] display_name: The display name of the user flow attribute. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "data_type", data_type)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[str]:
        """
        The data type of the user flow attribute. Possible values are `boolean`, `dateTime`, `int64`, `string` or `stringCollection`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "data_type")

    @data_type.setter
    def data_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_type", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the user flow attribute that is shown to the user at the time of sign-up.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the user flow attribute. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)


@pulumi.input_type
class _UserFlowAttributeState:
    def __init__(__self__, *,
                 attribute_type: Optional[pulumi.Input[str]] = None,
                 data_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserFlowAttribute resources.
        :param pulumi.Input[str] attribute_type: The type of the user flow attribute. Values include `builtIn`, `custom` or `required`.
        :param pulumi.Input[str] data_type: The data type of the user flow attribute. Possible values are `boolean`, `dateTime`, `int64`, `string` or `stringCollection`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of the user flow attribute that is shown to the user at the time of sign-up.
        :param pulumi.Input[str] display_name: The display name of the user flow attribute. Changing this forces a new resource to be created.
        """
        if attribute_type is not None:
            pulumi.set(__self__, "attribute_type", attribute_type)
        if data_type is not None:
            pulumi.set(__self__, "data_type", data_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the user flow attribute. Values include `builtIn`, `custom` or `required`.
        """
        return pulumi.get(self, "attribute_type")

    @attribute_type.setter
    def attribute_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attribute_type", value)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[str]]:
        """
        The data type of the user flow attribute. Possible values are `boolean`, `dateTime`, `int64`, `string` or `stringCollection`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "data_type")

    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the user flow attribute that is shown to the user at the time of sign-up.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the user flow attribute. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


class UserFlowAttribute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages user flow attributes in an Azure Active Directory (Azure AD) tenant.

        ## API Permissions

        The following API permissions are required in order to use this resource.

        When authenticated with a service principal, this resource requires the following application role: `IdentityUserFlow.ReadWrite.All`

        ## Example Usage

        *Basic example*

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example = azuread.UserFlowAttribute("example",
            data_type="string",
            description="Your hobby",
            display_name="Hobby")
        ```

        ## Import

        User flow attributes can be imported using the `id`, e.g.

        ```sh
        $ pulumi import azuread:index/userFlowAttribute:UserFlowAttribute example extension_ecc9f88db2924942b8a96f44873616fe_Hobbyjkorv
        ```

         -> This ID can be queried using the [User Flow Attributes API](https://learn.microsoft.com/en-us/graph/api/identityuserflowattribute-list?view=graph-rest-1.0&tabs=http).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_type: The data type of the user flow attribute. Possible values are `boolean`, `dateTime`, `int64`, `string` or `stringCollection`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of the user flow attribute that is shown to the user at the time of sign-up.
        :param pulumi.Input[str] display_name: The display name of the user flow attribute. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserFlowAttributeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages user flow attributes in an Azure Active Directory (Azure AD) tenant.

        ## API Permissions

        The following API permissions are required in order to use this resource.

        When authenticated with a service principal, this resource requires the following application role: `IdentityUserFlow.ReadWrite.All`

        ## Example Usage

        *Basic example*

        ```python
        import pulumi
        import pulumi_azuread as azuread

        example = azuread.UserFlowAttribute("example",
            data_type="string",
            description="Your hobby",
            display_name="Hobby")
        ```

        ## Import

        User flow attributes can be imported using the `id`, e.g.

        ```sh
        $ pulumi import azuread:index/userFlowAttribute:UserFlowAttribute example extension_ecc9f88db2924942b8a96f44873616fe_Hobbyjkorv
        ```

         -> This ID can be queried using the [User Flow Attributes API](https://learn.microsoft.com/en-us/graph/api/identityuserflowattribute-list?view=graph-rest-1.0&tabs=http).

        :param str resource_name: The name of the resource.
        :param UserFlowAttributeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserFlowAttributeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserFlowAttributeArgs.__new__(UserFlowAttributeArgs)

            if data_type is None and not opts.urn:
                raise TypeError("Missing required property 'data_type'")
            __props__.__dict__["data_type"] = data_type
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["attribute_type"] = None
        super(UserFlowAttribute, __self__).__init__(
            'azuread:index/userFlowAttribute:UserFlowAttribute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attribute_type: Optional[pulumi.Input[str]] = None,
            data_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None) -> 'UserFlowAttribute':
        """
        Get an existing UserFlowAttribute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attribute_type: The type of the user flow attribute. Values include `builtIn`, `custom` or `required`.
        :param pulumi.Input[str] data_type: The data type of the user flow attribute. Possible values are `boolean`, `dateTime`, `int64`, `string` or `stringCollection`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of the user flow attribute that is shown to the user at the time of sign-up.
        :param pulumi.Input[str] display_name: The display name of the user flow attribute. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserFlowAttributeState.__new__(_UserFlowAttributeState)

        __props__.__dict__["attribute_type"] = attribute_type
        __props__.__dict__["data_type"] = data_type
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        return UserFlowAttribute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> pulumi.Output[str]:
        """
        The type of the user flow attribute. Values include `builtIn`, `custom` or `required`.
        """
        return pulumi.get(self, "attribute_type")

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Output[str]:
        """
        The data type of the user flow attribute. Possible values are `boolean`, `dateTime`, `int64`, `string` or `stringCollection`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the user flow attribute that is shown to the user at the time of sign-up.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the user flow attribute. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "display_name")

