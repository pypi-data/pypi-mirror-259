# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('cloudamqp')


class _ExportableConfig(types.ModuleType):
    @property
    def apikey(self) -> Optional[str]:
        """
        Key used to authentication to the CloudAMQP Customer API
        """
        return __config__.get('apikey')

    @property
    def baseurl(self) -> Optional[str]:
        """
        Base URL to CloudAMQP Customer website
        """
        return __config__.get('baseurl')

    @property
    def enable_faster_instance_destroy(self) -> Optional[bool]:
        return __config__.get_bool('enableFasterInstanceDestroy')

