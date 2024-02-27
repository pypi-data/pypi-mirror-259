# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ApiShieldOperationSchemaValidationSettingsArgs', 'ApiShieldOperationSchemaValidationSettings']

@pulumi.input_type
class ApiShieldOperationSchemaValidationSettingsArgs:
    def __init__(__self__, *,
                 operation_id: pulumi.Input[str],
                 zone_id: pulumi.Input[str],
                 mitigation_action: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiShieldOperationSchemaValidationSettings resource.
        :param pulumi.Input[str] operation_id: Operation ID these settings should apply to. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] mitigation_action: The mitigation action to apply to this operation.
        """
        pulumi.set(__self__, "operation_id", operation_id)
        pulumi.set(__self__, "zone_id", zone_id)
        if mitigation_action is not None:
            pulumi.set(__self__, "mitigation_action", mitigation_action)

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Input[str]:
        """
        Operation ID these settings should apply to. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "operation_id")

    @operation_id.setter
    def operation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "operation_id", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter(name="mitigationAction")
    def mitigation_action(self) -> Optional[pulumi.Input[str]]:
        """
        The mitigation action to apply to this operation.
        """
        return pulumi.get(self, "mitigation_action")

    @mitigation_action.setter
    def mitigation_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mitigation_action", value)


@pulumi.input_type
class _ApiShieldOperationSchemaValidationSettingsState:
    def __init__(__self__, *,
                 mitigation_action: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApiShieldOperationSchemaValidationSettings resources.
        :param pulumi.Input[str] mitigation_action: The mitigation action to apply to this operation.
        :param pulumi.Input[str] operation_id: Operation ID these settings should apply to. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        if mitigation_action is not None:
            pulumi.set(__self__, "mitigation_action", mitigation_action)
        if operation_id is not None:
            pulumi.set(__self__, "operation_id", operation_id)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="mitigationAction")
    def mitigation_action(self) -> Optional[pulumi.Input[str]]:
        """
        The mitigation action to apply to this operation.
        """
        return pulumi.get(self, "mitigation_action")

    @mitigation_action.setter
    def mitigation_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mitigation_action", value)

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[pulumi.Input[str]]:
        """
        Operation ID these settings should apply to. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "operation_id")

    @operation_id.setter
    def operation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_id", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class ApiShieldOperationSchemaValidationSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mitigation_action: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to manage operation-level settings in API Shield Schema Validation 2.0.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example_api_shield_operation = cloudflare.ApiShieldOperation("exampleApiShieldOperation",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            method="GET",
            host="api.example.com",
            endpoint="/path")
        example_api_shield_operation_schema_validation_settings = cloudflare.ApiShieldOperationSchemaValidationSettings("exampleApiShieldOperationSchemaValidationSettings",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            operation_id=example_api_shield_operation.id,
            mitigation_action="block")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mitigation_action: The mitigation action to apply to this operation.
        :param pulumi.Input[str] operation_id: Operation ID these settings should apply to. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiShieldOperationSchemaValidationSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage operation-level settings in API Shield Schema Validation 2.0.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example_api_shield_operation = cloudflare.ApiShieldOperation("exampleApiShieldOperation",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            method="GET",
            host="api.example.com",
            endpoint="/path")
        example_api_shield_operation_schema_validation_settings = cloudflare.ApiShieldOperationSchemaValidationSettings("exampleApiShieldOperationSchemaValidationSettings",
            zone_id="0da42c8d2132a9ddaf714f9e7c920711",
            operation_id=example_api_shield_operation.id,
            mitigation_action="block")
        ```

        :param str resource_name: The name of the resource.
        :param ApiShieldOperationSchemaValidationSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiShieldOperationSchemaValidationSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mitigation_action: Optional[pulumi.Input[str]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiShieldOperationSchemaValidationSettingsArgs.__new__(ApiShieldOperationSchemaValidationSettingsArgs)

            __props__.__dict__["mitigation_action"] = mitigation_action
            if operation_id is None and not opts.urn:
                raise TypeError("Missing required property 'operation_id'")
            __props__.__dict__["operation_id"] = operation_id
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(ApiShieldOperationSchemaValidationSettings, __self__).__init__(
            'cloudflare:index/apiShieldOperationSchemaValidationSettings:ApiShieldOperationSchemaValidationSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            mitigation_action: Optional[pulumi.Input[str]] = None,
            operation_id: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ApiShieldOperationSchemaValidationSettings':
        """
        Get an existing ApiShieldOperationSchemaValidationSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mitigation_action: The mitigation action to apply to this operation.
        :param pulumi.Input[str] operation_id: Operation ID these settings should apply to. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] zone_id: The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiShieldOperationSchemaValidationSettingsState.__new__(_ApiShieldOperationSchemaValidationSettingsState)

        __props__.__dict__["mitigation_action"] = mitigation_action
        __props__.__dict__["operation_id"] = operation_id
        __props__.__dict__["zone_id"] = zone_id
        return ApiShieldOperationSchemaValidationSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="mitigationAction")
    def mitigation_action(self) -> pulumi.Output[Optional[str]]:
        """
        The mitigation action to apply to this operation.
        """
        return pulumi.get(self, "mitigation_action")

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Output[str]:
        """
        Operation ID these settings should apply to. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "operation_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "zone_id")

