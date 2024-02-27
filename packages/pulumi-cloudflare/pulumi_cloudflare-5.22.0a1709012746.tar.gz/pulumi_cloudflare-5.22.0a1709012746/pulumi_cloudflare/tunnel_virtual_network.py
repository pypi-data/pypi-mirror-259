# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TunnelVirtualNetworkArgs', 'TunnelVirtualNetwork']

@pulumi.input_type
class TunnelVirtualNetworkArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 name: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 is_default_network: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a TunnelVirtualNetwork resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] name: A user-friendly name chosen when the virtual network is created.
        :param pulumi.Input[str] comment: Description of the tunnel virtual network.
        :param pulumi.Input[bool] is_default_network: Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "name", name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if is_default_network is not None:
            pulumi.set(__self__, "is_default_network", is_default_network)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        A user-friendly name chosen when the virtual network is created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the tunnel virtual network.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="isDefaultNetwork")
    def is_default_network(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
        """
        return pulumi.get(self, "is_default_network")

    @is_default_network.setter
    def is_default_network(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default_network", value)


@pulumi.input_type
class _TunnelVirtualNetworkState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 is_default_network: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TunnelVirtualNetwork resources.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] comment: Description of the tunnel virtual network.
        :param pulumi.Input[bool] is_default_network: Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
        :param pulumi.Input[str] name: A user-friendly name chosen when the virtual network is created.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if is_default_network is not None:
            pulumi.set(__self__, "is_default_network", is_default_network)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the tunnel virtual network.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="isDefaultNetwork")
    def is_default_network(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
        """
        return pulumi.get(self, "is_default_network")

    @is_default_network.setter
    def is_default_network(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default_network", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-friendly name chosen when the virtual network is created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class TunnelVirtualNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 is_default_network: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource, that manages Cloudflare tunnel virtual networks
        for Zero Trust. Tunnel virtual networks are used for segregation of
        Tunnel IP Routes via Virtualized Networks to handle overlapping
        private IPs in your origins.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.TunnelVirtualNetwork("example",
            account_id="f037e56e89293a057740de681ac9abbe",
            comment="New tunnel virtual network for documentation",
            name="vnet-for-documentation")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/tunnelVirtualNetwork:TunnelVirtualNetwork example <account_id>/<vnet_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] comment: Description of the tunnel virtual network.
        :param pulumi.Input[bool] is_default_network: Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
        :param pulumi.Input[str] name: A user-friendly name chosen when the virtual network is created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TunnelVirtualNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource, that manages Cloudflare tunnel virtual networks
        for Zero Trust. Tunnel virtual networks are used for segregation of
        Tunnel IP Routes via Virtualized Networks to handle overlapping
        private IPs in your origins.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        example = cloudflare.TunnelVirtualNetwork("example",
            account_id="f037e56e89293a057740de681ac9abbe",
            comment="New tunnel virtual network for documentation",
            name="vnet-for-documentation")
        ```

        ## Import

        ```sh
         $ pulumi import cloudflare:index/tunnelVirtualNetwork:TunnelVirtualNetwork example <account_id>/<vnet_id>
        ```

        :param str resource_name: The name of the resource.
        :param TunnelVirtualNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TunnelVirtualNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 is_default_network: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TunnelVirtualNetworkArgs.__new__(TunnelVirtualNetworkArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["comment"] = comment
            __props__.__dict__["is_default_network"] = is_default_network
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
        super(TunnelVirtualNetwork, __self__).__init__(
            'cloudflare:index/tunnelVirtualNetwork:TunnelVirtualNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            is_default_network: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'TunnelVirtualNetwork':
        """
        Get an existing TunnelVirtualNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        :param pulumi.Input[str] comment: Description of the tunnel virtual network.
        :param pulumi.Input[bool] is_default_network: Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
        :param pulumi.Input[str] name: A user-friendly name chosen when the virtual network is created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TunnelVirtualNetworkState.__new__(_TunnelVirtualNetworkState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["comment"] = comment
        __props__.__dict__["is_default_network"] = is_default_network
        __props__.__dict__["name"] = name
        return TunnelVirtualNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account identifier to target for the resource. **Modifying this attribute will force creation of a new resource.**
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the tunnel virtual network.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="isDefaultNetwork")
    def is_default_network(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this virtual network is the default one for the account. This means IP Routes belong to this virtual network and Teams Clients in the account route through this virtual network, unless specified otherwise for each case.
        """
        return pulumi.get(self, "is_default_network")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A user-friendly name chosen when the virtual network is created.
        """
        return pulumi.get(self, "name")

