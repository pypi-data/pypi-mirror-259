# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SchemaArgs', 'Schema']

@pulumi.input_type
class SchemaArgs:
    def __init__(__self__, *,
                 catalog_name: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 storage_root: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Schema resource.
        :param pulumi.Input[str] catalog_name: Name of parent catalog. Change forces creation of a new resource.
        :param pulumi.Input[str] comment: User-supplied free-form text.
        :param pulumi.Input[bool] force_destroy: Delete schema regardless of its contents.
        :param pulumi.Input[str] name: Name of Schema relative to parent catalog. Change forces creation of a new resource.
        :param pulumi.Input[str] owner: Username/groupname/sp application_id of the schema owner.
        :param pulumi.Input[Mapping[str, Any]] properties: Extensible Schema properties.
        :param pulumi.Input[str] storage_root: Managed location of the schema. Location in cloud storage where data for managed tables will be stored. If not specified, the location will default to the catalog root location. Change forces creation of a new resource.
        """
        pulumi.set(__self__, "catalog_name", catalog_name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if metastore_id is not None:
            pulumi.set(__self__, "metastore_id", metastore_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if storage_root is not None:
            pulumi.set(__self__, "storage_root", storage_root)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Input[str]:
        """
        Name of parent catalog. Change forces creation of a new resource.
        """
        return pulumi.get(self, "catalog_name")

    @catalog_name.setter
    def catalog_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "catalog_name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        User-supplied free-form text.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Delete schema regardless of its contents.
        """
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metastore_id")

    @metastore_id.setter
    def metastore_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Schema relative to parent catalog. Change forces creation of a new resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Username/groupname/sp application_id of the schema owner.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Extensible Schema properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="storageRoot")
    def storage_root(self) -> Optional[pulumi.Input[str]]:
        """
        Managed location of the schema. Location in cloud storage where data for managed tables will be stored. If not specified, the location will default to the catalog root location. Change forces creation of a new resource.
        """
        return pulumi.get(self, "storage_root")

    @storage_root.setter
    def storage_root(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_root", value)


@pulumi.input_type
class _SchemaState:
    def __init__(__self__, *,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 storage_root: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Schema resources.
        :param pulumi.Input[str] catalog_name: Name of parent catalog. Change forces creation of a new resource.
        :param pulumi.Input[str] comment: User-supplied free-form text.
        :param pulumi.Input[bool] force_destroy: Delete schema regardless of its contents.
        :param pulumi.Input[str] name: Name of Schema relative to parent catalog. Change forces creation of a new resource.
        :param pulumi.Input[str] owner: Username/groupname/sp application_id of the schema owner.
        :param pulumi.Input[Mapping[str, Any]] properties: Extensible Schema properties.
        :param pulumi.Input[str] storage_root: Managed location of the schema. Location in cloud storage where data for managed tables will be stored. If not specified, the location will default to the catalog root location. Change forces creation of a new resource.
        """
        if catalog_name is not None:
            pulumi.set(__self__, "catalog_name", catalog_name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if metastore_id is not None:
            pulumi.set(__self__, "metastore_id", metastore_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if storage_root is not None:
            pulumi.set(__self__, "storage_root", storage_root)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of parent catalog. Change forces creation of a new resource.
        """
        return pulumi.get(self, "catalog_name")

    @catalog_name.setter
    def catalog_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        User-supplied free-form text.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Delete schema regardless of its contents.
        """
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metastore_id")

    @metastore_id.setter
    def metastore_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Schema relative to parent catalog. Change forces creation of a new resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Username/groupname/sp application_id of the schema owner.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Extensible Schema properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="storageRoot")
    def storage_root(self) -> Optional[pulumi.Input[str]]:
        """
        Managed location of the schema. Location in cloud storage where data for managed tables will be stored. If not specified, the location will default to the catalog root location. Change forces creation of a new resource.
        """
        return pulumi.get(self, "storage_root")

    @storage_root.setter
    def storage_root(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_root", value)


class Schema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 storage_root: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        > **Note** This resource could be only used with workspace-level provider!

        Within a metastore, Unity Catalog provides a 3-level namespace for organizing data: Catalogs, Databases (also called Schemas), and Tables / Views.

        A `Schema` is contained within Catalog and can contain tables & views.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_databricks as databricks

        sandbox = databricks.Catalog("sandbox",
            comment="this catalog is managed by terraform",
            properties={
                "purpose": "testing",
            })
        things = databricks.Schema("things",
            catalog_name=sandbox.id,
            comment="this database is managed by terraform",
            properties={
                "kind": "various",
            })
        ```
        ## Related Resources

        The following resources are used in the same context:

        * get_tables data to list tables within Unity Catalog.
        * get_schemas data to list schemas within Unity Catalog.
        * get_catalogs data to list catalogs within Unity Catalog.

        ## Import

        This resource can be imported by its full name:

         bash

        ```sh
        $ pulumi import databricks:index/schema:Schema this <catalog_name>.<name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] catalog_name: Name of parent catalog. Change forces creation of a new resource.
        :param pulumi.Input[str] comment: User-supplied free-form text.
        :param pulumi.Input[bool] force_destroy: Delete schema regardless of its contents.
        :param pulumi.Input[str] name: Name of Schema relative to parent catalog. Change forces creation of a new resource.
        :param pulumi.Input[str] owner: Username/groupname/sp application_id of the schema owner.
        :param pulumi.Input[Mapping[str, Any]] properties: Extensible Schema properties.
        :param pulumi.Input[str] storage_root: Managed location of the schema. Location in cloud storage where data for managed tables will be stored. If not specified, the location will default to the catalog root location. Change forces creation of a new resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SchemaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **Note** This resource could be only used with workspace-level provider!

        Within a metastore, Unity Catalog provides a 3-level namespace for organizing data: Catalogs, Databases (also called Schemas), and Tables / Views.

        A `Schema` is contained within Catalog and can contain tables & views.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_databricks as databricks

        sandbox = databricks.Catalog("sandbox",
            comment="this catalog is managed by terraform",
            properties={
                "purpose": "testing",
            })
        things = databricks.Schema("things",
            catalog_name=sandbox.id,
            comment="this database is managed by terraform",
            properties={
                "kind": "various",
            })
        ```
        ## Related Resources

        The following resources are used in the same context:

        * get_tables data to list tables within Unity Catalog.
        * get_schemas data to list schemas within Unity Catalog.
        * get_catalogs data to list catalogs within Unity Catalog.

        ## Import

        This resource can be imported by its full name:

         bash

        ```sh
        $ pulumi import databricks:index/schema:Schema this <catalog_name>.<name>
        ```

        :param str resource_name: The name of the resource.
        :param SchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 storage_root: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SchemaArgs.__new__(SchemaArgs)

            if catalog_name is None and not opts.urn:
                raise TypeError("Missing required property 'catalog_name'")
            __props__.__dict__["catalog_name"] = catalog_name
            __props__.__dict__["comment"] = comment
            __props__.__dict__["force_destroy"] = force_destroy
            __props__.__dict__["metastore_id"] = metastore_id
            __props__.__dict__["name"] = name
            __props__.__dict__["owner"] = owner
            __props__.__dict__["properties"] = properties
            __props__.__dict__["storage_root"] = storage_root
        super(Schema, __self__).__init__(
            'databricks:index/schema:Schema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            catalog_name: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            force_destroy: Optional[pulumi.Input[bool]] = None,
            metastore_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            storage_root: Optional[pulumi.Input[str]] = None) -> 'Schema':
        """
        Get an existing Schema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] catalog_name: Name of parent catalog. Change forces creation of a new resource.
        :param pulumi.Input[str] comment: User-supplied free-form text.
        :param pulumi.Input[bool] force_destroy: Delete schema regardless of its contents.
        :param pulumi.Input[str] name: Name of Schema relative to parent catalog. Change forces creation of a new resource.
        :param pulumi.Input[str] owner: Username/groupname/sp application_id of the schema owner.
        :param pulumi.Input[Mapping[str, Any]] properties: Extensible Schema properties.
        :param pulumi.Input[str] storage_root: Managed location of the schema. Location in cloud storage where data for managed tables will be stored. If not specified, the location will default to the catalog root location. Change forces creation of a new resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SchemaState.__new__(_SchemaState)

        __props__.__dict__["catalog_name"] = catalog_name
        __props__.__dict__["comment"] = comment
        __props__.__dict__["force_destroy"] = force_destroy
        __props__.__dict__["metastore_id"] = metastore_id
        __props__.__dict__["name"] = name
        __props__.__dict__["owner"] = owner
        __props__.__dict__["properties"] = properties
        __props__.__dict__["storage_root"] = storage_root
        return Schema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Output[str]:
        """
        Name of parent catalog. Change forces creation of a new resource.
        """
        return pulumi.get(self, "catalog_name")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        User-supplied free-form text.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        Delete schema regardless of its contents.
        """
        return pulumi.get(self, "force_destroy")

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "metastore_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of Schema relative to parent catalog. Change forces creation of a new resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        Username/groupname/sp application_id of the schema owner.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Extensible Schema properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="storageRoot")
    def storage_root(self) -> pulumi.Output[Optional[str]]:
        """
        Managed location of the schema. Location in cloud storage where data for managed tables will be stored. If not specified, the location will default to the catalog root location. Change forces creation of a new resource.
        """
        return pulumi.get(self, "storage_root")

