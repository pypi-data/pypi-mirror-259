# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 account: pulumi.Input[str],
                 token: pulumi.Input[str],
                 prefetch: Optional[pulumi.Input[bool]] = None,
                 sandbox: Optional[pulumi.Input[bool]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] account: The account for API operations.
        :param pulumi.Input[str] token: The API v2 token for API operations.
        :param pulumi.Input[bool] prefetch: Flag to enable the prefetch of zone records.
        :param pulumi.Input[bool] sandbox: Flag to enable the sandbox API.
        :param pulumi.Input[str] user_agent: Custom string to append to the user agent used for sending HTTP requests to the API.
        """
        pulumi.set(__self__, "account", account)
        pulumi.set(__self__, "token", token)
        if prefetch is not None:
            pulumi.set(__self__, "prefetch", prefetch)
        if sandbox is not None:
            pulumi.set(__self__, "sandbox", sandbox)
        if user_agent is not None:
            pulumi.set(__self__, "user_agent", user_agent)

    @property
    @pulumi.getter
    def account(self) -> pulumi.Input[str]:
        """
        The account for API operations.
        """
        return pulumi.get(self, "account")

    @account.setter
    def account(self, value: pulumi.Input[str]):
        pulumi.set(self, "account", value)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        """
        The API v2 token for API operations.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def prefetch(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to enable the prefetch of zone records.
        """
        return pulumi.get(self, "prefetch")

    @prefetch.setter
    def prefetch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "prefetch", value)

    @property
    @pulumi.getter
    def sandbox(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to enable the sandbox API.
        """
        return pulumi.get(self, "sandbox")

    @sandbox.setter
    def sandbox(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sandbox", value)

    @property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> Optional[pulumi.Input[str]]:
        """
        Custom string to append to the user agent used for sending HTTP requests to the API.
        """
        return pulumi.get(self, "user_agent")

    @user_agent.setter
    def user_agent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_agent", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account: Optional[pulumi.Input[str]] = None,
                 prefetch: Optional[pulumi.Input[bool]] = None,
                 sandbox: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the dnsimple package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account: The account for API operations.
        :param pulumi.Input[bool] prefetch: Flag to enable the prefetch of zone records.
        :param pulumi.Input[bool] sandbox: Flag to enable the sandbox API.
        :param pulumi.Input[str] token: The API v2 token for API operations.
        :param pulumi.Input[str] user_agent: Custom string to append to the user agent used for sending HTTP requests to the API.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the dnsimple package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account: Optional[pulumi.Input[str]] = None,
                 prefetch: Optional[pulumi.Input[bool]] = None,
                 sandbox: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if account is None and not opts.urn:
                raise TypeError("Missing required property 'account'")
            __props__.__dict__["account"] = account
            __props__.__dict__["prefetch"] = pulumi.Output.from_input(prefetch).apply(pulumi.runtime.to_json) if prefetch is not None else None
            __props__.__dict__["sandbox"] = pulumi.Output.from_input(sandbox).apply(pulumi.runtime.to_json) if sandbox is not None else None
            if token is None and not opts.urn:
                raise TypeError("Missing required property 'token'")
            __props__.__dict__["token"] = None if token is None else pulumi.Output.secret(token)
            __props__.__dict__["user_agent"] = user_agent
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["token"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'dnsimple',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def account(self) -> pulumi.Output[str]:
        """
        The account for API operations.
        """
        return pulumi.get(self, "account")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        The API v2 token for API operations.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> pulumi.Output[Optional[str]]:
        """
        Custom string to append to the user agent used for sending HTTP requests to the API.
        """
        return pulumi.get(self, "user_agent")

