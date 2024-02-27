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

from ..models.accountcommon_client_permission import AccountcommonClientPermission


class AccountcommonClientPermissions(Model):
    """Accountcommon client permissions (accountcommon.ClientPermissions)

    Properties:
        permissions: (Permissions) REQUIRED List[AccountcommonClientPermission]
    """

    # region fields

    permissions: List[AccountcommonClientPermission]  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_permissions(
        self, value: List[AccountcommonClientPermission]
    ) -> AccountcommonClientPermissions:
        self.permissions = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "permissions"):
            result["Permissions"] = [
                i0.to_dict(include_empty=include_empty) for i0 in self.permissions
            ]
        elif include_empty:
            result["Permissions"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls, permissions: List[AccountcommonClientPermission], **kwargs
    ) -> AccountcommonClientPermissions:
        instance = cls()
        instance.permissions = permissions
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> AccountcommonClientPermissions:
        instance = cls()
        if not dict_:
            return instance
        if "Permissions" in dict_ and dict_["Permissions"] is not None:
            instance.permissions = [
                AccountcommonClientPermission.create_from_dict(
                    i0, include_empty=include_empty
                )
                for i0 in dict_["Permissions"]
            ]
        elif include_empty:
            instance.permissions = []
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, AccountcommonClientPermissions]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[AccountcommonClientPermissions]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[
        AccountcommonClientPermissions,
        List[AccountcommonClientPermissions],
        Dict[Any, AccountcommonClientPermissions],
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
            "Permissions": "permissions",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "Permissions": True,
        }

    # endregion static methods
