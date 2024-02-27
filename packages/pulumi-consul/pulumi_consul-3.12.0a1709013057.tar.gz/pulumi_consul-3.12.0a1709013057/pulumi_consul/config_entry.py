# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ConfigEntryArgs', 'ConfigEntry']

@pulumi.input_type
class ConfigEntryArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 config_json: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConfigEntry resource.
        :param pulumi.Input[str] kind: The kind of configuration entry to register.
        :param pulumi.Input[str] config_json: An arbitrary map of configuration values.
        :param pulumi.Input[str] name: The name of the configuration entry being registered.
        :param pulumi.Input[str] namespace: The namespace to create the config entry within.
        :param pulumi.Input[str] partition: The partition the config entry is associated with.
        """
        pulumi.set(__self__, "kind", kind)
        if config_json is not None:
            pulumi.set(__self__, "config_json", config_json)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of configuration entry to register.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> Optional[pulumi.Input[str]]:
        """
        An arbitrary map of configuration values.
        """
        return pulumi.get(self, "config_json")

    @config_json.setter
    def config_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_json", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the configuration entry being registered.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the config entry within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        The partition the config entry is associated with.
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)


@pulumi.input_type
class _ConfigEntryState:
    def __init__(__self__, *,
                 config_json: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConfigEntry resources.
        :param pulumi.Input[str] config_json: An arbitrary map of configuration values.
        :param pulumi.Input[str] kind: The kind of configuration entry to register.
        :param pulumi.Input[str] name: The name of the configuration entry being registered.
        :param pulumi.Input[str] namespace: The namespace to create the config entry within.
        :param pulumi.Input[str] partition: The partition the config entry is associated with.
        """
        if config_json is not None:
            pulumi.set(__self__, "config_json", config_json)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> Optional[pulumi.Input[str]]:
        """
        An arbitrary map of configuration values.
        """
        return pulumi.get(self, "config_json")

    @config_json.setter
    def config_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_json", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of configuration entry to register.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the configuration entry being registered.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the config entry within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        The partition the config entry is associated with.
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)


class ConfigEntry(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        proxy_defaults = consul.ConfigEntry("proxyDefaults",
            kind="proxy-defaults",
            config_json=json.dumps({
                "Config": {
                    "local_connect_timeout_ms": 1000,
                    "handshake_timeout_ms": 10000,
                },
            }))
        web = consul.ConfigEntry("web",
            kind="service-defaults",
            config_json=json.dumps({
                "Protocol": "http",
            }))
        admin = consul.ConfigEntry("admin",
            kind="service-defaults",
            config_json=json.dumps({
                "Protocol": "http",
            }))
        service_resolver = consul.ConfigEntry("serviceResolver",
            kind="service-resolver",
            config_json=json.dumps({
                "DefaultSubset": "v1",
                "Subsets": {
                    "v1": {
                        "Filter": "Service.Meta.version == v1",
                    },
                    "v2": {
                        "Filter": "Service.Meta.version == v2",
                    },
                },
            }))
        service_splitter = consul.ConfigEntry("serviceSplitter",
            kind="service-splitter",
            config_json=json.dumps({
                "Splits": [
                    {
                        "Weight": 90,
                        "ServiceSubset": "v1",
                    },
                    {
                        "Weight": 10,
                        "ServiceSubset": "v2",
                    },
                ],
            }))
        service_router = consul.ConfigEntry("serviceRouter",
            kind="service-router",
            config_json=json.dumps({
                "Routes": [{
                    "Match": {
                        "HTTP": {
                            "PathPrefix": "/admin",
                        },
                    },
                    "Destination": {
                        "Service": "admin",
                    },
                }],
            }))
        ingress_gateway = consul.ConfigEntry("ingressGateway",
            kind="ingress-gateway",
            config_json=json.dumps({
                "TLS": {
                    "Enabled": True,
                },
                "Listeners": [{
                    "Port": 8000,
                    "Protocol": "http",
                    "Services": [{
                        "Name": "*",
                    }],
                }],
            }))
        terminating_gateway = consul.ConfigEntry("terminatingGateway",
            kind="terminating-gateway",
            config_json=json.dumps({
                "Services": [{
                    "Name": "billing",
                }],
            }))
        ```
        ### `service-intentions` config entry

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        service_intentions = consul.ConfigEntry("serviceIntentions",
            kind="service-intentions",
            config_json=json.dumps({
                "Sources": [
                    {
                        "Action": "allow",
                        "Name": "frontend-webapp",
                        "Precedence": 9,
                        "Type": "consul",
                    },
                    {
                        "Action": "allow",
                        "Name": "nightly-cronjob",
                        "Precedence": 9,
                        "Type": "consul",
                    },
                ],
            }))
        ```

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        sd = consul.ConfigEntry("sd",
            kind="service-defaults",
            config_json=json.dumps({
                "Protocol": "http",
            }))
        jwt_provider = consul.ConfigEntry("jwtProvider",
            kind="jwt-provider",
            config_json=json.dumps({
                "Issuer": "test-issuer",
                "JSONWebKeySet": {
                    "Remote": {
                        "URI": "https://127.0.0.1:9091",
                        "FetchAsynchronously": True,
                    },
                },
                "Forwarding": {
                    "HeaderName": "test-token",
                },
            }))
        service_intentions = consul.ConfigEntry("serviceIntentions",
            kind="service-intentions",
            config_json=jwt_provider.name.apply(lambda name: json.dumps({
                "Sources": [
                    {
                        "Name": "contractor-webapp",
                        "Permissions": [{
                            "Action": "allow",
                            "HTTP": {
                                "Methods": [
                                    "GET",
                                    "HEAD",
                                ],
                                "PathExact": "/healtz",
                            },
                            "JWT": {
                                "Providers": [{
                                    "Name": name,
                                }],
                            },
                        }],
                        "Precedence": 9,
                        "Type": "consul",
                    },
                    {
                        "Name": "admin-dashboard-webapp",
                        "Permissions": [
                            {
                                "Action": "deny",
                                "HTTP": {
                                    "PathPrefix": "/debugz",
                                },
                            },
                            {
                                "Action": "allow",
                                "HTTP": {
                                    "PathPrefix": "/",
                                },
                            },
                        ],
                        "Precedence": 9,
                        "Type": "consul",
                    },
                ],
            })))
        ```
        ### `exported-services` config entry

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        exported_services = consul.ConfigEntry("exportedServices",
            kind="exported-services",
            config_json=json.dumps({
                "Services": [{
                    "Name": "test",
                    "Namespace": "default",
                    "Consumers": [{
                        "Partition": "default",
                    }],
                }],
            }))
        ```
        ### `mesh` config entry

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        mesh = consul.ConfigEntry("mesh",
            kind="mesh",
            partition="default",
            config_json=json.dumps({
                "TransparentProxy": {
                    "MeshDestinationsOnly": True,
                },
            }))
        ```
        ### `jwt-provider` config entry

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        jwt_provider = consul.ConfigEntry("jwtProvider",
            kind="jwt-provider",
            config_json=json.dumps({
                "Issuer": "https://your.issuer.com",
                "JSONWebKeySet": {
                    "Remote": {
                        "URI": "https://your-remote.jwks.com",
                        "FetchAsynchronously": True,
                        "CacheDuration": "10s",
                    },
                },
                "Forwarding": {
                    "HeaderName": "test-token",
                },
            }))
        ```

        ## Import

        `consul_config_entry` can be imported using the syntax `<kind>/<name>` if the config entry is in the default partition and default namespace, or `<partition>/<namespace>/<kind>/<name>` for config entries in a non-default partition or namespace:

        ```sh
         $ pulumi import consul:index/configEntry:ConfigEntry service_splitter 816a195f-6cb1-2e8d-92af-3011ae706318
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config_json: An arbitrary map of configuration values.
        :param pulumi.Input[str] kind: The kind of configuration entry to register.
        :param pulumi.Input[str] name: The name of the configuration entry being registered.
        :param pulumi.Input[str] namespace: The namespace to create the config entry within.
        :param pulumi.Input[str] partition: The partition the config entry is associated with.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigEntryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        proxy_defaults = consul.ConfigEntry("proxyDefaults",
            kind="proxy-defaults",
            config_json=json.dumps({
                "Config": {
                    "local_connect_timeout_ms": 1000,
                    "handshake_timeout_ms": 10000,
                },
            }))
        web = consul.ConfigEntry("web",
            kind="service-defaults",
            config_json=json.dumps({
                "Protocol": "http",
            }))
        admin = consul.ConfigEntry("admin",
            kind="service-defaults",
            config_json=json.dumps({
                "Protocol": "http",
            }))
        service_resolver = consul.ConfigEntry("serviceResolver",
            kind="service-resolver",
            config_json=json.dumps({
                "DefaultSubset": "v1",
                "Subsets": {
                    "v1": {
                        "Filter": "Service.Meta.version == v1",
                    },
                    "v2": {
                        "Filter": "Service.Meta.version == v2",
                    },
                },
            }))
        service_splitter = consul.ConfigEntry("serviceSplitter",
            kind="service-splitter",
            config_json=json.dumps({
                "Splits": [
                    {
                        "Weight": 90,
                        "ServiceSubset": "v1",
                    },
                    {
                        "Weight": 10,
                        "ServiceSubset": "v2",
                    },
                ],
            }))
        service_router = consul.ConfigEntry("serviceRouter",
            kind="service-router",
            config_json=json.dumps({
                "Routes": [{
                    "Match": {
                        "HTTP": {
                            "PathPrefix": "/admin",
                        },
                    },
                    "Destination": {
                        "Service": "admin",
                    },
                }],
            }))
        ingress_gateway = consul.ConfigEntry("ingressGateway",
            kind="ingress-gateway",
            config_json=json.dumps({
                "TLS": {
                    "Enabled": True,
                },
                "Listeners": [{
                    "Port": 8000,
                    "Protocol": "http",
                    "Services": [{
                        "Name": "*",
                    }],
                }],
            }))
        terminating_gateway = consul.ConfigEntry("terminatingGateway",
            kind="terminating-gateway",
            config_json=json.dumps({
                "Services": [{
                    "Name": "billing",
                }],
            }))
        ```
        ### `service-intentions` config entry

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        service_intentions = consul.ConfigEntry("serviceIntentions",
            kind="service-intentions",
            config_json=json.dumps({
                "Sources": [
                    {
                        "Action": "allow",
                        "Name": "frontend-webapp",
                        "Precedence": 9,
                        "Type": "consul",
                    },
                    {
                        "Action": "allow",
                        "Name": "nightly-cronjob",
                        "Precedence": 9,
                        "Type": "consul",
                    },
                ],
            }))
        ```

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        sd = consul.ConfigEntry("sd",
            kind="service-defaults",
            config_json=json.dumps({
                "Protocol": "http",
            }))
        jwt_provider = consul.ConfigEntry("jwtProvider",
            kind="jwt-provider",
            config_json=json.dumps({
                "Issuer": "test-issuer",
                "JSONWebKeySet": {
                    "Remote": {
                        "URI": "https://127.0.0.1:9091",
                        "FetchAsynchronously": True,
                    },
                },
                "Forwarding": {
                    "HeaderName": "test-token",
                },
            }))
        service_intentions = consul.ConfigEntry("serviceIntentions",
            kind="service-intentions",
            config_json=jwt_provider.name.apply(lambda name: json.dumps({
                "Sources": [
                    {
                        "Name": "contractor-webapp",
                        "Permissions": [{
                            "Action": "allow",
                            "HTTP": {
                                "Methods": [
                                    "GET",
                                    "HEAD",
                                ],
                                "PathExact": "/healtz",
                            },
                            "JWT": {
                                "Providers": [{
                                    "Name": name,
                                }],
                            },
                        }],
                        "Precedence": 9,
                        "Type": "consul",
                    },
                    {
                        "Name": "admin-dashboard-webapp",
                        "Permissions": [
                            {
                                "Action": "deny",
                                "HTTP": {
                                    "PathPrefix": "/debugz",
                                },
                            },
                            {
                                "Action": "allow",
                                "HTTP": {
                                    "PathPrefix": "/",
                                },
                            },
                        ],
                        "Precedence": 9,
                        "Type": "consul",
                    },
                ],
            })))
        ```
        ### `exported-services` config entry

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        exported_services = consul.ConfigEntry("exportedServices",
            kind="exported-services",
            config_json=json.dumps({
                "Services": [{
                    "Name": "test",
                    "Namespace": "default",
                    "Consumers": [{
                        "Partition": "default",
                    }],
                }],
            }))
        ```
        ### `mesh` config entry

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        mesh = consul.ConfigEntry("mesh",
            kind="mesh",
            partition="default",
            config_json=json.dumps({
                "TransparentProxy": {
                    "MeshDestinationsOnly": True,
                },
            }))
        ```
        ### `jwt-provider` config entry

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        jwt_provider = consul.ConfigEntry("jwtProvider",
            kind="jwt-provider",
            config_json=json.dumps({
                "Issuer": "https://your.issuer.com",
                "JSONWebKeySet": {
                    "Remote": {
                        "URI": "https://your-remote.jwks.com",
                        "FetchAsynchronously": True,
                        "CacheDuration": "10s",
                    },
                },
                "Forwarding": {
                    "HeaderName": "test-token",
                },
            }))
        ```

        ## Import

        `consul_config_entry` can be imported using the syntax `<kind>/<name>` if the config entry is in the default partition and default namespace, or `<partition>/<namespace>/<kind>/<name>` for config entries in a non-default partition or namespace:

        ```sh
         $ pulumi import consul:index/configEntry:ConfigEntry service_splitter 816a195f-6cb1-2e8d-92af-3011ae706318
        ```

        :param str resource_name: The name of the resource.
        :param ConfigEntryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigEntryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigEntryArgs.__new__(ConfigEntryArgs)

            __props__.__dict__["config_json"] = config_json
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["partition"] = partition
        super(ConfigEntry, __self__).__init__(
            'consul:index/configEntry:ConfigEntry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config_json: Optional[pulumi.Input[str]] = None,
            kind: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            partition: Optional[pulumi.Input[str]] = None) -> 'ConfigEntry':
        """
        Get an existing ConfigEntry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config_json: An arbitrary map of configuration values.
        :param pulumi.Input[str] kind: The kind of configuration entry to register.
        :param pulumi.Input[str] name: The name of the configuration entry being registered.
        :param pulumi.Input[str] namespace: The namespace to create the config entry within.
        :param pulumi.Input[str] partition: The partition the config entry is associated with.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigEntryState.__new__(_ConfigEntryState)

        __props__.__dict__["config_json"] = config_json
        __props__.__dict__["kind"] = kind
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["partition"] = partition
        return ConfigEntry(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> pulumi.Output[Optional[str]]:
        """
        An arbitrary map of configuration values.
        """
        return pulumi.get(self, "config_json")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of configuration entry to register.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the configuration entry being registered.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace to create the config entry within.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def partition(self) -> pulumi.Output[Optional[str]]:
        """
        The partition the config entry is associated with.
        """
        return pulumi.get(self, "partition")

