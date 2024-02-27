# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: model.j2

# AccelByte Gaming Services Dsm Controller Service

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from accelbyte_py_sdk.core import Model

from ..models.models_dsm_config_record import ModelsDSMConfigRecord


class ModelsListConfigResponse(Model):
    """Models list config response (models.ListConfigResponse)

    Properties:
        configs: (configs) REQUIRED List[ModelsDSMConfigRecord]
    """

    # region fields

    configs: List[ModelsDSMConfigRecord]  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_configs(
        self, value: List[ModelsDSMConfigRecord]
    ) -> ModelsListConfigResponse:
        self.configs = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "configs"):
            result["configs"] = [
                i0.to_dict(include_empty=include_empty) for i0 in self.configs
            ]
        elif include_empty:
            result["configs"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls, configs: List[ModelsDSMConfigRecord], **kwargs
    ) -> ModelsListConfigResponse:
        instance = cls()
        instance.configs = configs
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> ModelsListConfigResponse:
        instance = cls()
        if not dict_:
            return instance
        if "configs" in dict_ and dict_["configs"] is not None:
            instance.configs = [
                ModelsDSMConfigRecord.create_from_dict(i0, include_empty=include_empty)
                for i0 in dict_["configs"]
            ]
        elif include_empty:
            instance.configs = []
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, ModelsListConfigResponse]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[ModelsListConfigResponse]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[
        ModelsListConfigResponse,
        List[ModelsListConfigResponse],
        Dict[Any, ModelsListConfigResponse],
    ]:
        if many:
            if isinstance(any_, dict):
                return cls.create_many_from_dict(any_, include_empty=include_empty)
            elif isinstance(any_, list):
                return cls.create_many_from_list(any_, include_empty=include_empty)
            else:
                raise ValueError()
        else:
            return cls.create_from_dict(any_, include_empty=include_empty)

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "configs": "configs",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "configs": True,
        }

    # endregion static methods
