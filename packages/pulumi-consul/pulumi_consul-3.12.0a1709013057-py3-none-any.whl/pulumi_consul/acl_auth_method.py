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

__all__ = ['AclAuthMethodArgs', 'AclAuthMethod']

@pulumi.input_type
class AclAuthMethodArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 max_token_ttl: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 namespace_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AclAuthMethodNamespaceRuleArgs']]]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 token_locality: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AclAuthMethod resource.
        :param pulumi.Input[str] type: The type of the ACL auth method.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: The raw configuration for this ACL auth method.
        :param pulumi.Input[str] config_json: The raw configuration for this ACL auth method.
        :param pulumi.Input[str] description: A free form human readable description of the auth method.
        :param pulumi.Input[str] display_name: An optional name to use instead of the name attribute when displaying information about this auth method.
        :param pulumi.Input[str] max_token_ttl: The maximum life of any token created by this auth method. **This attribute is required and must be set to a nonzero for the OIDC auth method.**
        :param pulumi.Input[str] name: The name of the ACL auth method.
        :param pulumi.Input[str] namespace: The namespace in which to create the auth method.
        :param pulumi.Input[Sequence[pulumi.Input['AclAuthMethodNamespaceRuleArgs']]] namespace_rules: A set of rules that control which namespace tokens created via this auth method will be created within.
        :param pulumi.Input[str] partition: The partition the ACL auth method is associated with.
        :param pulumi.Input[str] token_locality: The kind of token that this auth method produces. This can be either 'local' or 'global'.
        """
        pulumi.set(__self__, "type", type)
        if config is not None:
            warnings.warn("""The config attribute is deprecated, please use `config_json` instead.""", DeprecationWarning)
            pulumi.log.warn("""config is deprecated: The config attribute is deprecated, please use `config_json` instead.""")
        if config is not None:
            pulumi.set(__self__, "config", config)
        if config_json is not None:
            pulumi.set(__self__, "config_json", config_json)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if max_token_ttl is not None:
            pulumi.set(__self__, "max_token_ttl", max_token_ttl)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if namespace_rules is not None:
            pulumi.set(__self__, "namespace_rules", namespace_rules)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)
        if token_locality is not None:
            pulumi.set(__self__, "token_locality", token_locality)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the ACL auth method.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The raw configuration for this ACL auth method.
        """
        warnings.warn("""The config attribute is deprecated, please use `config_json` instead.""", DeprecationWarning)
        pulumi.log.warn("""config is deprecated: The config attribute is deprecated, please use `config_json` instead.""")

        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> Optional[pulumi.Input[str]]:
        """
        The raw configuration for this ACL auth method.
        """
        return pulumi.get(self, "config_json")

    @config_json.setter
    def config_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_json", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A free form human readable description of the auth method.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        An optional name to use instead of the name attribute when displaying information about this auth method.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="maxTokenTtl")
    def max_token_ttl(self) -> Optional[pulumi.Input[str]]:
        """
        The maximum life of any token created by this auth method. **This attribute is required and must be set to a nonzero for the OIDC auth method.**
        """
        return pulumi.get(self, "max_token_ttl")

    @max_token_ttl.setter
    def max_token_ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "max_token_ttl", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ACL auth method.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace in which to create the auth method.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="namespaceRules")
    def namespace_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AclAuthMethodNamespaceRuleArgs']]]]:
        """
        A set of rules that control which namespace tokens created via this auth method will be created within.
        """
        return pulumi.get(self, "namespace_rules")

    @namespace_rules.setter
    def namespace_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AclAuthMethodNamespaceRuleArgs']]]]):
        pulumi.set(self, "namespace_rules", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        The partition the ACL auth method is associated with.
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)

    @property
    @pulumi.getter(name="tokenLocality")
    def token_locality(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of token that this auth method produces. This can be either 'local' or 'global'.
        """
        return pulumi.get(self, "token_locality")

    @token_locality.setter
    def token_locality(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_locality", value)


@pulumi.input_type
class _AclAuthMethodState:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 max_token_ttl: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 namespace_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AclAuthMethodNamespaceRuleArgs']]]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 token_locality: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AclAuthMethod resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: The raw configuration for this ACL auth method.
        :param pulumi.Input[str] config_json: The raw configuration for this ACL auth method.
        :param pulumi.Input[str] description: A free form human readable description of the auth method.
        :param pulumi.Input[str] display_name: An optional name to use instead of the name attribute when displaying information about this auth method.
        :param pulumi.Input[str] max_token_ttl: The maximum life of any token created by this auth method. **This attribute is required and must be set to a nonzero for the OIDC auth method.**
        :param pulumi.Input[str] name: The name of the ACL auth method.
        :param pulumi.Input[str] namespace: The namespace in which to create the auth method.
        :param pulumi.Input[Sequence[pulumi.Input['AclAuthMethodNamespaceRuleArgs']]] namespace_rules: A set of rules that control which namespace tokens created via this auth method will be created within.
        :param pulumi.Input[str] partition: The partition the ACL auth method is associated with.
        :param pulumi.Input[str] token_locality: The kind of token that this auth method produces. This can be either 'local' or 'global'.
        :param pulumi.Input[str] type: The type of the ACL auth method.
        """
        if config is not None:
            warnings.warn("""The config attribute is deprecated, please use `config_json` instead.""", DeprecationWarning)
            pulumi.log.warn("""config is deprecated: The config attribute is deprecated, please use `config_json` instead.""")
        if config is not None:
            pulumi.set(__self__, "config", config)
        if config_json is not None:
            pulumi.set(__self__, "config_json", config_json)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if max_token_ttl is not None:
            pulumi.set(__self__, "max_token_ttl", max_token_ttl)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if namespace_rules is not None:
            pulumi.set(__self__, "namespace_rules", namespace_rules)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)
        if token_locality is not None:
            pulumi.set(__self__, "token_locality", token_locality)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The raw configuration for this ACL auth method.
        """
        warnings.warn("""The config attribute is deprecated, please use `config_json` instead.""", DeprecationWarning)
        pulumi.log.warn("""config is deprecated: The config attribute is deprecated, please use `config_json` instead.""")

        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> Optional[pulumi.Input[str]]:
        """
        The raw configuration for this ACL auth method.
        """
        return pulumi.get(self, "config_json")

    @config_json.setter
    def config_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_json", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A free form human readable description of the auth method.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        An optional name to use instead of the name attribute when displaying information about this auth method.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="maxTokenTtl")
    def max_token_ttl(self) -> Optional[pulumi.Input[str]]:
        """
        The maximum life of any token created by this auth method. **This attribute is required and must be set to a nonzero for the OIDC auth method.**
        """
        return pulumi.get(self, "max_token_ttl")

    @max_token_ttl.setter
    def max_token_ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "max_token_ttl", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ACL auth method.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace in which to create the auth method.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="namespaceRules")
    def namespace_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AclAuthMethodNamespaceRuleArgs']]]]:
        """
        A set of rules that control which namespace tokens created via this auth method will be created within.
        """
        return pulumi.get(self, "namespace_rules")

    @namespace_rules.setter
    def namespace_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AclAuthMethodNamespaceRuleArgs']]]]):
        pulumi.set(self, "namespace_rules", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        The partition the ACL auth method is associated with.
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)

    @property
    @pulumi.getter(name="tokenLocality")
    def token_locality(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of token that this auth method produces. This can be either 'local' or 'global'.
        """
        return pulumi.get(self, "token_locality")

    @token_locality.setter
    def token_locality(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_locality", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the ACL auth method.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class AclAuthMethod(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 max_token_ttl: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 namespace_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclAuthMethodNamespaceRuleArgs']]]]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 token_locality: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Starting with Consul 1.5.0, the `AclAuthMethod` resource can be used to managed [Consul ACL auth methods](https://www.consul.io/docs/acl/auth-methods).

        ## Example Usage

        Define a `kubernetes` auth method:

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        minikube = consul.AclAuthMethod("minikube",
            type="kubernetes",
            description="dev minikube cluster",
            config_json=json.dumps({
                "Host": "https://192.0.2.42:8443",
                "CACert": \"\"\"-----BEGIN CERTIFICATE-----
        ...-----END CERTIFICATE-----
        \"\"\",
                "ServiceAccountJWT": "eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9...",
            }))
        ```

        Define a `jwt` auth method:

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        oidc = consul.AclAuthMethod("oidc",
            type="oidc",
            max_token_ttl="5m",
            config_json=json.dumps({
                "AllowedRedirectURIs": [
                    "http://localhost:8550/oidc/callback",
                    "http://localhost:8500/ui/oidc/callback",
                ],
                "BoundAudiences": ["V1RPi2MYptMV1RPi2MYptMV1RPi2MYpt"],
                "ClaimMappings": {
                    "http://example.com/first_name": "first_name",
                    "http://example.com/last_name": "last_name",
                },
                "ListClaimMappings": {
                    "http://consul.com/groups": "groups",
                },
                "OIDCClientID": "V1RPi2MYptMV1RPi2MYptMV1RPi2MYpt",
                "OIDCClientSecret": "...(omitted)...",
                "OIDCDiscoveryURL": "https://my-corp-app-name.auth0.com/",
            }))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: The raw configuration for this ACL auth method.
        :param pulumi.Input[str] config_json: The raw configuration for this ACL auth method.
        :param pulumi.Input[str] description: A free form human readable description of the auth method.
        :param pulumi.Input[str] display_name: An optional name to use instead of the name attribute when displaying information about this auth method.
        :param pulumi.Input[str] max_token_ttl: The maximum life of any token created by this auth method. **This attribute is required and must be set to a nonzero for the OIDC auth method.**
        :param pulumi.Input[str] name: The name of the ACL auth method.
        :param pulumi.Input[str] namespace: The namespace in which to create the auth method.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclAuthMethodNamespaceRuleArgs']]]] namespace_rules: A set of rules that control which namespace tokens created via this auth method will be created within.
        :param pulumi.Input[str] partition: The partition the ACL auth method is associated with.
        :param pulumi.Input[str] token_locality: The kind of token that this auth method produces. This can be either 'local' or 'global'.
        :param pulumi.Input[str] type: The type of the ACL auth method.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AclAuthMethodArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Starting with Consul 1.5.0, the `AclAuthMethod` resource can be used to managed [Consul ACL auth methods](https://www.consul.io/docs/acl/auth-methods).

        ## Example Usage

        Define a `kubernetes` auth method:

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        minikube = consul.AclAuthMethod("minikube",
            type="kubernetes",
            description="dev minikube cluster",
            config_json=json.dumps({
                "Host": "https://192.0.2.42:8443",
                "CACert": \"\"\"-----BEGIN CERTIFICATE-----
        ...-----END CERTIFICATE-----
        \"\"\",
                "ServiceAccountJWT": "eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9...",
            }))
        ```

        Define a `jwt` auth method:

        ```python
        import pulumi
        import json
        import pulumi_consul as consul

        oidc = consul.AclAuthMethod("oidc",
            type="oidc",
            max_token_ttl="5m",
            config_json=json.dumps({
                "AllowedRedirectURIs": [
                    "http://localhost:8550/oidc/callback",
                    "http://localhost:8500/ui/oidc/callback",
                ],
                "BoundAudiences": ["V1RPi2MYptMV1RPi2MYptMV1RPi2MYpt"],
                "ClaimMappings": {
                    "http://example.com/first_name": "first_name",
                    "http://example.com/last_name": "last_name",
                },
                "ListClaimMappings": {
                    "http://consul.com/groups": "groups",
                },
                "OIDCClientID": "V1RPi2MYptMV1RPi2MYptMV1RPi2MYpt",
                "OIDCClientSecret": "...(omitted)...",
                "OIDCDiscoveryURL": "https://my-corp-app-name.auth0.com/",
            }))
        ```

        :param str resource_name: The name of the resource.
        :param AclAuthMethodArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AclAuthMethodArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 max_token_ttl: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 namespace_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclAuthMethodNamespaceRuleArgs']]]]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 token_locality: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AclAuthMethodArgs.__new__(AclAuthMethodArgs)

            __props__.__dict__["config"] = config
            __props__.__dict__["config_json"] = config_json
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["max_token_ttl"] = max_token_ttl
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["namespace_rules"] = namespace_rules
            __props__.__dict__["partition"] = partition
            __props__.__dict__["token_locality"] = token_locality
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(AclAuthMethod, __self__).__init__(
            'consul:index/aclAuthMethod:AclAuthMethod',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            config_json: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            max_token_ttl: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            namespace_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclAuthMethodNamespaceRuleArgs']]]]] = None,
            partition: Optional[pulumi.Input[str]] = None,
            token_locality: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'AclAuthMethod':
        """
        Get an existing AclAuthMethod resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: The raw configuration for this ACL auth method.
        :param pulumi.Input[str] config_json: The raw configuration for this ACL auth method.
        :param pulumi.Input[str] description: A free form human readable description of the auth method.
        :param pulumi.Input[str] display_name: An optional name to use instead of the name attribute when displaying information about this auth method.
        :param pulumi.Input[str] max_token_ttl: The maximum life of any token created by this auth method. **This attribute is required and must be set to a nonzero for the OIDC auth method.**
        :param pulumi.Input[str] name: The name of the ACL auth method.
        :param pulumi.Input[str] namespace: The namespace in which to create the auth method.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclAuthMethodNamespaceRuleArgs']]]] namespace_rules: A set of rules that control which namespace tokens created via this auth method will be created within.
        :param pulumi.Input[str] partition: The partition the ACL auth method is associated with.
        :param pulumi.Input[str] token_locality: The kind of token that this auth method produces. This can be either 'local' or 'global'.
        :param pulumi.Input[str] type: The type of the ACL auth method.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AclAuthMethodState.__new__(_AclAuthMethodState)

        __props__.__dict__["config"] = config
        __props__.__dict__["config_json"] = config_json
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["max_token_ttl"] = max_token_ttl
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["namespace_rules"] = namespace_rules
        __props__.__dict__["partition"] = partition
        __props__.__dict__["token_locality"] = token_locality
        __props__.__dict__["type"] = type
        return AclAuthMethod(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The raw configuration for this ACL auth method.
        """
        warnings.warn("""The config attribute is deprecated, please use `config_json` instead.""", DeprecationWarning)
        pulumi.log.warn("""config is deprecated: The config attribute is deprecated, please use `config_json` instead.""")

        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> pulumi.Output[Optional[str]]:
        """
        The raw configuration for this ACL auth method.
        """
        return pulumi.get(self, "config_json")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A free form human readable description of the auth method.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        An optional name to use instead of the name attribute when displaying information about this auth method.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="maxTokenTtl")
    def max_token_ttl(self) -> pulumi.Output[Optional[str]]:
        """
        The maximum life of any token created by this auth method. **This attribute is required and must be set to a nonzero for the OIDC auth method.**
        """
        return pulumi.get(self, "max_token_ttl")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the ACL auth method.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace in which to create the auth method.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="namespaceRules")
    def namespace_rules(self) -> pulumi.Output[Optional[Sequence['outputs.AclAuthMethodNamespaceRule']]]:
        """
        A set of rules that control which namespace tokens created via this auth method will be created within.
        """
        return pulumi.get(self, "namespace_rules")

    @property
    @pulumi.getter
    def partition(self) -> pulumi.Output[Optional[str]]:
        """
        The partition the ACL auth method is associated with.
        """
        return pulumi.get(self, "partition")

    @property
    @pulumi.getter(name="tokenLocality")
    def token_locality(self) -> pulumi.Output[Optional[str]]:
        """
        The kind of token that this auth method produces. This can be either 'local' or 'global'.
        """
        return pulumi.get(self, "token_locality")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the ACL auth method.
        """
        return pulumi.get(self, "type")

