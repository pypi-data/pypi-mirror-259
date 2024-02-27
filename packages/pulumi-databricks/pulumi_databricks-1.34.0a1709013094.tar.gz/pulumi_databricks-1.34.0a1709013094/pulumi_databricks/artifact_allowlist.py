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

__all__ = ['ArtifactAllowlistArgs', 'ArtifactAllowlist']

@pulumi.input_type
class ArtifactAllowlistArgs:
    def __init__(__self__, *,
                 artifact_matchers: pulumi.Input[Sequence[pulumi.Input['ArtifactAllowlistArtifactMatcherArgs']]],
                 artifact_type: pulumi.Input[str],
                 created_at: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ArtifactAllowlist resource.
        :param pulumi.Input[str] artifact_type: The artifact type of the allowlist. Can be `INIT_SCRIPT`, `LIBRARY_JAR` or `LIBRARY_MAVEN`. Change forces creation of a new resource.
        :param pulumi.Input[int] created_at: Time at which this artifact allowlist was set.
        :param pulumi.Input[str] created_by: Identity that set the artifact allowlist.
        :param pulumi.Input[str] metastore_id: ID of the parent metastore.
        """
        pulumi.set(__self__, "artifact_matchers", artifact_matchers)
        pulumi.set(__self__, "artifact_type", artifact_type)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if metastore_id is not None:
            pulumi.set(__self__, "metastore_id", metastore_id)

    @property
    @pulumi.getter(name="artifactMatchers")
    def artifact_matchers(self) -> pulumi.Input[Sequence[pulumi.Input['ArtifactAllowlistArtifactMatcherArgs']]]:
        return pulumi.get(self, "artifact_matchers")

    @artifact_matchers.setter
    def artifact_matchers(self, value: pulumi.Input[Sequence[pulumi.Input['ArtifactAllowlistArtifactMatcherArgs']]]):
        pulumi.set(self, "artifact_matchers", value)

    @property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> pulumi.Input[str]:
        """
        The artifact type of the allowlist. Can be `INIT_SCRIPT`, `LIBRARY_JAR` or `LIBRARY_MAVEN`. Change forces creation of a new resource.
        """
        return pulumi.get(self, "artifact_type")

    @artifact_type.setter
    def artifact_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "artifact_type", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[int]]:
        """
        Time at which this artifact allowlist was set.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        Identity that set the artifact allowlist.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the parent metastore.
        """
        return pulumi.get(self, "metastore_id")

    @metastore_id.setter
    def metastore_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore_id", value)


@pulumi.input_type
class _ArtifactAllowlistState:
    def __init__(__self__, *,
                 artifact_matchers: Optional[pulumi.Input[Sequence[pulumi.Input['ArtifactAllowlistArtifactMatcherArgs']]]] = None,
                 artifact_type: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ArtifactAllowlist resources.
        :param pulumi.Input[str] artifact_type: The artifact type of the allowlist. Can be `INIT_SCRIPT`, `LIBRARY_JAR` or `LIBRARY_MAVEN`. Change forces creation of a new resource.
        :param pulumi.Input[int] created_at: Time at which this artifact allowlist was set.
        :param pulumi.Input[str] created_by: Identity that set the artifact allowlist.
        :param pulumi.Input[str] metastore_id: ID of the parent metastore.
        """
        if artifact_matchers is not None:
            pulumi.set(__self__, "artifact_matchers", artifact_matchers)
        if artifact_type is not None:
            pulumi.set(__self__, "artifact_type", artifact_type)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if metastore_id is not None:
            pulumi.set(__self__, "metastore_id", metastore_id)

    @property
    @pulumi.getter(name="artifactMatchers")
    def artifact_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ArtifactAllowlistArtifactMatcherArgs']]]]:
        return pulumi.get(self, "artifact_matchers")

    @artifact_matchers.setter
    def artifact_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ArtifactAllowlistArtifactMatcherArgs']]]]):
        pulumi.set(self, "artifact_matchers", value)

    @property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> Optional[pulumi.Input[str]]:
        """
        The artifact type of the allowlist. Can be `INIT_SCRIPT`, `LIBRARY_JAR` or `LIBRARY_MAVEN`. Change forces creation of a new resource.
        """
        return pulumi.get(self, "artifact_type")

    @artifact_type.setter
    def artifact_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "artifact_type", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[int]]:
        """
        Time at which this artifact allowlist was set.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        Identity that set the artifact allowlist.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the parent metastore.
        """
        return pulumi.get(self, "metastore_id")

    @metastore_id.setter
    def metastore_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore_id", value)


class ArtifactAllowlist(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArtifactAllowlistArtifactMatcherArgs']]]]] = None,
                 artifact_type: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_databricks as databricks

        init_scripts = databricks.ArtifactAllowlist("initScripts",
            artifact_matchers=[databricks.ArtifactAllowlistArtifactMatcherArgs(
                artifact="/Volumes/inits",
                match_type="PREFIX_MATCH",
            )],
            artifact_type="INIT_SCRIPT")
        ```
        ## Related Resources

        The following resources are used in the same context:

        * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
        * Library to install a [library](https://docs.databricks.com/libraries/index.html) on databricks_cluster.

        ## Import

        This resource can be imported by name:

         bash

        ```sh
        $ pulumi import databricks:index/artifactAllowlist:ArtifactAllowlist this '<metastore_id>|<artifact_type>'
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] artifact_type: The artifact type of the allowlist. Can be `INIT_SCRIPT`, `LIBRARY_JAR` or `LIBRARY_MAVEN`. Change forces creation of a new resource.
        :param pulumi.Input[int] created_at: Time at which this artifact allowlist was set.
        :param pulumi.Input[str] created_by: Identity that set the artifact allowlist.
        :param pulumi.Input[str] metastore_id: ID of the parent metastore.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ArtifactAllowlistArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_databricks as databricks

        init_scripts = databricks.ArtifactAllowlist("initScripts",
            artifact_matchers=[databricks.ArtifactAllowlistArtifactMatcherArgs(
                artifact="/Volumes/inits",
                match_type="PREFIX_MATCH",
            )],
            artifact_type="INIT_SCRIPT")
        ```
        ## Related Resources

        The following resources are used in the same context:

        * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
        * Library to install a [library](https://docs.databricks.com/libraries/index.html) on databricks_cluster.

        ## Import

        This resource can be imported by name:

         bash

        ```sh
        $ pulumi import databricks:index/artifactAllowlist:ArtifactAllowlist this '<metastore_id>|<artifact_type>'
        ```

        :param str resource_name: The name of the resource.
        :param ArtifactAllowlistArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ArtifactAllowlistArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArtifactAllowlistArtifactMatcherArgs']]]]] = None,
                 artifact_type: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ArtifactAllowlistArgs.__new__(ArtifactAllowlistArgs)

            if artifact_matchers is None and not opts.urn:
                raise TypeError("Missing required property 'artifact_matchers'")
            __props__.__dict__["artifact_matchers"] = artifact_matchers
            if artifact_type is None and not opts.urn:
                raise TypeError("Missing required property 'artifact_type'")
            __props__.__dict__["artifact_type"] = artifact_type
            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["metastore_id"] = metastore_id
        super(ArtifactAllowlist, __self__).__init__(
            'databricks:index/artifactAllowlist:ArtifactAllowlist',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            artifact_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ArtifactAllowlistArtifactMatcherArgs']]]]] = None,
            artifact_type: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[int]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            metastore_id: Optional[pulumi.Input[str]] = None) -> 'ArtifactAllowlist':
        """
        Get an existing ArtifactAllowlist resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] artifact_type: The artifact type of the allowlist. Can be `INIT_SCRIPT`, `LIBRARY_JAR` or `LIBRARY_MAVEN`. Change forces creation of a new resource.
        :param pulumi.Input[int] created_at: Time at which this artifact allowlist was set.
        :param pulumi.Input[str] created_by: Identity that set the artifact allowlist.
        :param pulumi.Input[str] metastore_id: ID of the parent metastore.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ArtifactAllowlistState.__new__(_ArtifactAllowlistState)

        __props__.__dict__["artifact_matchers"] = artifact_matchers
        __props__.__dict__["artifact_type"] = artifact_type
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["metastore_id"] = metastore_id
        return ArtifactAllowlist(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="artifactMatchers")
    def artifact_matchers(self) -> pulumi.Output[Sequence['outputs.ArtifactAllowlistArtifactMatcher']]:
        return pulumi.get(self, "artifact_matchers")

    @property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> pulumi.Output[str]:
        """
        The artifact type of the allowlist. Can be `INIT_SCRIPT`, `LIBRARY_JAR` or `LIBRARY_MAVEN`. Change forces creation of a new resource.
        """
        return pulumi.get(self, "artifact_type")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[int]:
        """
        Time at which this artifact allowlist was set.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        Identity that set the artifact allowlist.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> pulumi.Output[str]:
        """
        ID of the parent metastore.
        """
        return pulumi.get(self, "metastore_id")

