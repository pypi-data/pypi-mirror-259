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

__all__ = ['ShareArgs', 'Share']

@pulumi.input_type
class ShareArgs:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 objects: Optional[pulumi.Input[Sequence[pulumi.Input['ShareObjectArgs']]]] = None,
                 owner: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Share resource.
        :param pulumi.Input[int] created_at: Time when the share was created.
        :param pulumi.Input[str] created_by: The principal that created the share.
        :param pulumi.Input[str] name: Name of share. Change forces creation of a new resource.
        :param pulumi.Input[str] owner: User name/group name/sp application_id of the share owner.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if objects is not None:
            pulumi.set(__self__, "objects", objects)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[int]]:
        """
        Time when the share was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The principal that created the share.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of share. Change forces creation of a new resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def objects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ShareObjectArgs']]]]:
        return pulumi.get(self, "objects")

    @objects.setter
    def objects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ShareObjectArgs']]]]):
        pulumi.set(self, "objects", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        User name/group name/sp application_id of the share owner.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)


@pulumi.input_type
class _ShareState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 objects: Optional[pulumi.Input[Sequence[pulumi.Input['ShareObjectArgs']]]] = None,
                 owner: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Share resources.
        :param pulumi.Input[int] created_at: Time when the share was created.
        :param pulumi.Input[str] created_by: The principal that created the share.
        :param pulumi.Input[str] name: Name of share. Change forces creation of a new resource.
        :param pulumi.Input[str] owner: User name/group name/sp application_id of the share owner.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if objects is not None:
            pulumi.set(__self__, "objects", objects)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[int]]:
        """
        Time when the share was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The principal that created the share.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of share. Change forces creation of a new resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def objects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ShareObjectArgs']]]]:
        return pulumi.get(self, "objects")

    @objects.setter
    def objects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ShareObjectArgs']]]]):
        pulumi.set(self, "objects", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        User name/group name/sp application_id of the share owner.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)


class Share(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_at: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 objects: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ShareObjectArgs']]]]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Share resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] created_at: Time when the share was created.
        :param pulumi.Input[str] created_by: The principal that created the share.
        :param pulumi.Input[str] name: Name of share. Change forces creation of a new resource.
        :param pulumi.Input[str] owner: User name/group name/sp application_id of the share owner.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ShareArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Share resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ShareArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ShareArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_at: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 objects: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ShareObjectArgs']]]]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ShareArgs.__new__(ShareArgs)

            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["name"] = name
            __props__.__dict__["objects"] = objects
            __props__.__dict__["owner"] = owner
        super(Share, __self__).__init__(
            'databricks:index/share:Share',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[int]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            objects: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ShareObjectArgs']]]]] = None,
            owner: Optional[pulumi.Input[str]] = None) -> 'Share':
        """
        Get an existing Share resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] created_at: Time when the share was created.
        :param pulumi.Input[str] created_by: The principal that created the share.
        :param pulumi.Input[str] name: Name of share. Change forces creation of a new resource.
        :param pulumi.Input[str] owner: User name/group name/sp application_id of the share owner.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ShareState.__new__(_ShareState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["name"] = name
        __props__.__dict__["objects"] = objects
        __props__.__dict__["owner"] = owner
        return Share(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[int]:
        """
        Time when the share was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        The principal that created the share.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of share. Change forces creation of a new resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def objects(self) -> pulumi.Output[Optional[Sequence['outputs.ShareObject']]]:
        return pulumi.get(self, "objects")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional[str]]:
        """
        User name/group name/sp application_id of the share owner.
        """
        return pulumi.get(self, "owner")

