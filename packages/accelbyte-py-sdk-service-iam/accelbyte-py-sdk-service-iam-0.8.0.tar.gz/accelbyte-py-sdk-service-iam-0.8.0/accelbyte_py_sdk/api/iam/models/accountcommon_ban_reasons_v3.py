# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: model.j2

# AccelByte Gaming Services Iam Service

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

from ..models.accountcommon_ban_reason_v3 import AccountcommonBanReasonV3


class AccountcommonBanReasonsV3(Model):
    """Accountcommon ban reasons V3 (accountcommon.BanReasonsV3)

    Properties:
        reasons: (reasons) REQUIRED List[AccountcommonBanReasonV3]
    """

    # region fields

    reasons: List[AccountcommonBanReasonV3]  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_reasons(
        self, value: List[AccountcommonBanReasonV3]
    ) -> AccountcommonBanReasonsV3:
        self.reasons = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "reasons"):
            result["reasons"] = [
                i0.to_dict(include_empty=include_empty) for i0 in self.reasons
            ]
        elif include_empty:
            result["reasons"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls, reasons: List[AccountcommonBanReasonV3], **kwargs
    ) -> AccountcommonBanReasonsV3:
        instance = cls()
        instance.reasons = reasons
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> AccountcommonBanReasonsV3:
        instance = cls()
        if not dict_:
            return instance
        if "reasons" in dict_ and dict_["reasons"] is not None:
            instance.reasons = [
                AccountcommonBanReasonV3.create_from_dict(
                    i0, include_empty=include_empty
                )
                for i0 in dict_["reasons"]
            ]
        elif include_empty:
            instance.reasons = []
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, AccountcommonBanReasonsV3]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[AccountcommonBanReasonsV3]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[
        AccountcommonBanReasonsV3,
        List[AccountcommonBanReasonsV3],
        Dict[Any, AccountcommonBanReasonsV3],
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
            "reasons": "reasons",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "reasons": True,
        }

    # endregion static methods
