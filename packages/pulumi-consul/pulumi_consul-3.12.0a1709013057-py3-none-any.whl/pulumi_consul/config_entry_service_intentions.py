# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ConfigEntryServiceIntentionsArgs', 'ConfigEntryServiceIntentions']

@pulumi.input_type
class ConfigEntryServiceIntentionsArgs:
    def __init__(__self__, *,
                 jwts: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsJwtArgs']]]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsSourceArgs']]]] = None):
        """
        The set of arguments for constructing a ConfigEntryServiceIntentions resource.
        :param pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsJwtArgs']]] jwts: Specifies a JSON Web Token provider configured in a JWT provider configuration entry, as well as additional configurations for verifying a service's JWT before authorizing communication between services
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] meta: Specifies key-value pairs to add to the KV store.
        :param pulumi.Input[str] name: Specifies the name of a JWT provider defined in the Name field of the jwt-provider configuration entry.
        :param pulumi.Input[str] namespace: Specifies the traffic source namespace that the intention allows or denies traffic from.
        :param pulumi.Input[str] partition: Specifies the name of an admin partition that the intention allows or denies traffic from.
        :param pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsSourceArgs']]] sources: List of configurations that define intention sources and the authorization granted to the sources.
        """
        if jwts is not None:
            pulumi.set(__self__, "jwts", jwts)
        if meta is not None:
            pulumi.set(__self__, "meta", meta)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)

    @property
    @pulumi.getter
    def jwts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsJwtArgs']]]]:
        """
        Specifies a JSON Web Token provider configured in a JWT provider configuration entry, as well as additional configurations for verifying a service's JWT before authorizing communication between services
        """
        return pulumi.get(self, "jwts")

    @jwts.setter
    def jwts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsJwtArgs']]]]):
        pulumi.set(self, "jwts", value)

    @property
    @pulumi.getter
    def meta(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Specifies key-value pairs to add to the KV store.
        """
        return pulumi.get(self, "meta")

    @meta.setter
    def meta(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "meta", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of a JWT provider defined in the Name field of the jwt-provider configuration entry.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the traffic source namespace that the intention allows or denies traffic from.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of an admin partition that the intention allows or denies traffic from.
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsSourceArgs']]]]:
        """
        List of configurations that define intention sources and the authorization granted to the sources.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsSourceArgs']]]]):
        pulumi.set(self, "sources", value)


@pulumi.input_type
class _ConfigEntryServiceIntentionsState:
    def __init__(__self__, *,
                 jwts: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsJwtArgs']]]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsSourceArgs']]]] = None):
        """
        Input properties used for looking up and filtering ConfigEntryServiceIntentions resources.
        :param pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsJwtArgs']]] jwts: Specifies a JSON Web Token provider configured in a JWT provider configuration entry, as well as additional configurations for verifying a service's JWT before authorizing communication between services
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] meta: Specifies key-value pairs to add to the KV store.
        :param pulumi.Input[str] name: Specifies the name of a JWT provider defined in the Name field of the jwt-provider configuration entry.
        :param pulumi.Input[str] namespace: Specifies the traffic source namespace that the intention allows or denies traffic from.
        :param pulumi.Input[str] partition: Specifies the name of an admin partition that the intention allows or denies traffic from.
        :param pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsSourceArgs']]] sources: List of configurations that define intention sources and the authorization granted to the sources.
        """
        if jwts is not None:
            pulumi.set(__self__, "jwts", jwts)
        if meta is not None:
            pulumi.set(__self__, "meta", meta)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)

    @property
    @pulumi.getter
    def jwts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsJwtArgs']]]]:
        """
        Specifies a JSON Web Token provider configured in a JWT provider configuration entry, as well as additional configurations for verifying a service's JWT before authorizing communication between services
        """
        return pulumi.get(self, "jwts")

    @jwts.setter
    def jwts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsJwtArgs']]]]):
        pulumi.set(self, "jwts", value)

    @property
    @pulumi.getter
    def meta(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Specifies key-value pairs to add to the KV store.
        """
        return pulumi.get(self, "meta")

    @meta.setter
    def meta(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "meta", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of a JWT provider defined in the Name field of the jwt-provider configuration entry.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the traffic source namespace that the intention allows or denies traffic from.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of an admin partition that the intention allows or denies traffic from.
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsSourceArgs']]]]:
        """
        List of configurations that define intention sources and the authorization granted to the sources.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigEntryServiceIntentionsSourceArgs']]]]):
        pulumi.set(self, "sources", value)


class ConfigEntryServiceIntentions(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 jwts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsJwtArgs']]]]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsSourceArgs']]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        jwt_provider = consul.ConfigEntry("jwtProvider",
            kind="jwt-provider",
            config_json=json.dumps({
                "ClockSkewSeconds": 30,
                "Issuer": "test-issuer",
                "JSONWebKeySet": {
                    "Remote": {
                        "URI": "https://127.0.0.1:9091",
                        "FetchAsynchronously": True,
                    },
                },
            }))
        web = consul.ConfigEntryServiceIntentions("web",
            jwts=[consul.ConfigEntryServiceIntentionsJwtArgs(
                providers=[consul.ConfigEntryServiceIntentionsJwtProviderArgs(
                    name=jwt_provider.name,
                    verify_claims=[consul.ConfigEntryServiceIntentionsJwtProviderVerifyClaimArgs(
                        paths=[
                            "perms",
                            "role",
                        ],
                        value="admin",
                    )],
                )],
            )],
            sources=[
                consul.ConfigEntryServiceIntentionsSourceArgs(
                    name="frontend-webapp",
                    type="consul",
                    action="allow",
                ),
                consul.ConfigEntryServiceIntentionsSourceArgs(
                    name="nightly-cronjob",
                    type="consul",
                    action="deny",
                ),
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsJwtArgs']]]] jwts: Specifies a JSON Web Token provider configured in a JWT provider configuration entry, as well as additional configurations for verifying a service's JWT before authorizing communication between services
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] meta: Specifies key-value pairs to add to the KV store.
        :param pulumi.Input[str] name: Specifies the name of a JWT provider defined in the Name field of the jwt-provider configuration entry.
        :param pulumi.Input[str] namespace: Specifies the traffic source namespace that the intention allows or denies traffic from.
        :param pulumi.Input[str] partition: Specifies the name of an admin partition that the intention allows or denies traffic from.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsSourceArgs']]]] sources: List of configurations that define intention sources and the authorization granted to the sources.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ConfigEntryServiceIntentionsArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        jwt_provider = consul.ConfigEntry("jwtProvider",
            kind="jwt-provider",
            config_json=json.dumps({
                "ClockSkewSeconds": 30,
                "Issuer": "test-issuer",
                "JSONWebKeySet": {
                    "Remote": {
                        "URI": "https://127.0.0.1:9091",
                        "FetchAsynchronously": True,
                    },
                },
            }))
        web = consul.ConfigEntryServiceIntentions("web",
            jwts=[consul.ConfigEntryServiceIntentionsJwtArgs(
                providers=[consul.ConfigEntryServiceIntentionsJwtProviderArgs(
                    name=jwt_provider.name,
                    verify_claims=[consul.ConfigEntryServiceIntentionsJwtProviderVerifyClaimArgs(
                        paths=[
                            "perms",
                            "role",
                        ],
                        value="admin",
                    )],
                )],
            )],
            sources=[
                consul.ConfigEntryServiceIntentionsSourceArgs(
                    name="frontend-webapp",
                    type="consul",
                    action="allow",
                ),
                consul.ConfigEntryServiceIntentionsSourceArgs(
                    name="nightly-cronjob",
                    type="consul",
                    action="deny",
                ),
            ])
        ```

        :param str resource_name: The name of the resource.
        :param ConfigEntryServiceIntentionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigEntryServiceIntentionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 jwts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsJwtArgs']]]]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsSourceArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigEntryServiceIntentionsArgs.__new__(ConfigEntryServiceIntentionsArgs)

            __props__.__dict__["jwts"] = jwts
            __props__.__dict__["meta"] = meta
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["partition"] = partition
            __props__.__dict__["sources"] = sources
        super(ConfigEntryServiceIntentions, __self__).__init__(
            'consul:index/configEntryServiceIntentions:ConfigEntryServiceIntentions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            jwts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsJwtArgs']]]]] = None,
            meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            partition: Optional[pulumi.Input[str]] = None,
            sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsSourceArgs']]]]] = None) -> 'ConfigEntryServiceIntentions':
        """
        Get an existing ConfigEntryServiceIntentions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsJwtArgs']]]] jwts: Specifies a JSON Web Token provider configured in a JWT provider configuration entry, as well as additional configurations for verifying a service's JWT before authorizing communication between services
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] meta: Specifies key-value pairs to add to the KV store.
        :param pulumi.Input[str] name: Specifies the name of a JWT provider defined in the Name field of the jwt-provider configuration entry.
        :param pulumi.Input[str] namespace: Specifies the traffic source namespace that the intention allows or denies traffic from.
        :param pulumi.Input[str] partition: Specifies the name of an admin partition that the intention allows or denies traffic from.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigEntryServiceIntentionsSourceArgs']]]] sources: List of configurations that define intention sources and the authorization granted to the sources.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigEntryServiceIntentionsState.__new__(_ConfigEntryServiceIntentionsState)

        __props__.__dict__["jwts"] = jwts
        __props__.__dict__["meta"] = meta
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["partition"] = partition
        __props__.__dict__["sources"] = sources
        return ConfigEntryServiceIntentions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def jwts(self) -> pulumi.Output[Optional[Sequence['outputs.ConfigEntryServiceIntentionsJwt']]]:
        """
        Specifies a JSON Web Token provider configured in a JWT provider configuration entry, as well as additional configurations for verifying a service's JWT before authorizing communication between services
        """
        return pulumi.get(self, "jwts")

    @property
    @pulumi.getter
    def meta(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Specifies key-value pairs to add to the KV store.
        """
        return pulumi.get(self, "meta")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of a JWT provider defined in the Name field of the jwt-provider configuration entry.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the traffic source namespace that the intention allows or denies traffic from.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def partition(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the name of an admin partition that the intention allows or denies traffic from.
        """
        return pulumi.get(self, "partition")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Optional[Sequence['outputs.ConfigEntryServiceIntentionsSource']]]:
        """
        List of configurations that define intention sources and the authorization granted to the sources.
        """
        return pulumi.get(self, "sources")

