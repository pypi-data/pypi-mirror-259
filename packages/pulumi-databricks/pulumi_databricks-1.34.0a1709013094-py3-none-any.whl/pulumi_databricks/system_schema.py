# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SystemSchemaArgs', 'SystemSchema']

@pulumi.input_type
class SystemSchemaArgs:
    def __init__(__self__, *,
                 schema: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SystemSchema resource.
        :param pulumi.Input[str] schema: Full name of the system schema.
        :param pulumi.Input[str] state: The current state of enablement for the system schema.
        """
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        Full name of the system schema.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of enablement for the system schema.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class _SystemSchemaState:
    def __init__(__self__, *,
                 metastore_id: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SystemSchema resources.
        :param pulumi.Input[str] schema: Full name of the system schema.
        :param pulumi.Input[str] state: The current state of enablement for the system schema.
        """
        if metastore_id is not None:
            pulumi.set(__self__, "metastore_id", metastore_id)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "metastore_id")

    @metastore_id.setter
    def metastore_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metastore_id", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        Full name of the system schema.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of enablement for the system schema.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class SystemSchema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        > **Public Preview** This feature is in [Public Preview](https://docs.databricks.com/release-notes/release-types.html).

        > **Note** This resource could be only used with workspace-level provider!

        Manages system tables enablement. System tables are a Databricks-hosted analytical store of your account’s operational data. System tables can be used for historical observability across your account. System tables must be enabled by an account admin.

        ## Example Usage

        Enable the system schema `access`

        ```python
        import pulumi
        import pulumi_databricks as databricks

        this = databricks.SystemSchema("this", schema="access")
        ```

        ## Import

        This resource can be imported by the metastore id and schema name

         bash

        ```sh
        $ pulumi import databricks:index/systemSchema:SystemSchema this <metastore_id>|<schema_name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] schema: Full name of the system schema.
        :param pulumi.Input[str] state: The current state of enablement for the system schema.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SystemSchemaArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **Public Preview** This feature is in [Public Preview](https://docs.databricks.com/release-notes/release-types.html).

        > **Note** This resource could be only used with workspace-level provider!

        Manages system tables enablement. System tables are a Databricks-hosted analytical store of your account’s operational data. System tables can be used for historical observability across your account. System tables must be enabled by an account admin.

        ## Example Usage

        Enable the system schema `access`

        ```python
        import pulumi
        import pulumi_databricks as databricks

        this = databricks.SystemSchema("this", schema="access")
        ```

        ## Import

        This resource can be imported by the metastore id and schema name

         bash

        ```sh
        $ pulumi import databricks:index/systemSchema:SystemSchema this <metastore_id>|<schema_name>
        ```

        :param str resource_name: The name of the resource.
        :param SystemSchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SystemSchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SystemSchemaArgs.__new__(SystemSchemaArgs)

            __props__.__dict__["schema"] = schema
            __props__.__dict__["state"] = state
            __props__.__dict__["metastore_id"] = None
        super(SystemSchema, __self__).__init__(
            'databricks:index/systemSchema:SystemSchema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            metastore_id: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'SystemSchema':
        """
        Get an existing SystemSchema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] schema: Full name of the system schema.
        :param pulumi.Input[str] state: The current state of enablement for the system schema.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SystemSchemaState.__new__(_SystemSchemaState)

        __props__.__dict__["metastore_id"] = metastore_id
        __props__.__dict__["schema"] = schema
        __props__.__dict__["state"] = state
        return SystemSchema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="metastoreId")
    def metastore_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "metastore_id")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[str]]:
        """
        Full name of the system schema.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of enablement for the system schema.
        """
        return pulumi.get(self, "state")

