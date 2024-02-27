# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: model.j2

# AccelByte Gaming Services Session Service

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


class ApimodelsPlayerPlatform(Model):
    """Apimodels player platform (apimodels.PlayerPlatform)

    Properties:
        current_platform: (currentPlatform) REQUIRED str

        user_id: (userID) REQUIRED str

        crossplay_enabled: (crossplayEnabled) OPTIONAL bool
    """

    # region fields

    current_platform: str  # REQUIRED
    user_id: str  # REQUIRED
    crossplay_enabled: bool  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_current_platform(self, value: str) -> ApimodelsPlayerPlatform:
        self.current_platform = value
        return self

    def with_user_id(self, value: str) -> ApimodelsPlayerPlatform:
        self.user_id = value
        return self

    def with_crossplay_enabled(self, value: bool) -> ApimodelsPlayerPlatform:
        self.crossplay_enabled = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "current_platform"):
            result["currentPlatform"] = str(self.current_platform)
        elif include_empty:
            result["currentPlatform"] = ""
        if hasattr(self, "user_id"):
            result["userID"] = str(self.user_id)
        elif include_empty:
            result["userID"] = ""
        if hasattr(self, "crossplay_enabled"):
            result["crossplayEnabled"] = bool(self.crossplay_enabled)
        elif include_empty:
            result["crossplayEnabled"] = False
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        current_platform: str,
        user_id: str,
        crossplay_enabled: Optional[bool] = None,
        **kwargs,
    ) -> ApimodelsPlayerPlatform:
        instance = cls()
        instance.current_platform = current_platform
        instance.user_id = user_id
        if crossplay_enabled is not None:
            instance.crossplay_enabled = crossplay_enabled
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> ApimodelsPlayerPlatform:
        instance = cls()
        if not dict_:
            return instance
        if "currentPlatform" in dict_ and dict_["currentPlatform"] is not None:
            instance.current_platform = str(dict_["currentPlatform"])
        elif include_empty:
            instance.current_platform = ""
        if "userID" in dict_ and dict_["userID"] is not None:
            instance.user_id = str(dict_["userID"])
        elif include_empty:
            instance.user_id = ""
        if "crossplayEnabled" in dict_ and dict_["crossplayEnabled"] is not None:
            instance.crossplay_enabled = bool(dict_["crossplayEnabled"])
        elif include_empty:
            instance.crossplay_enabled = False
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, ApimodelsPlayerPlatform]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[ApimodelsPlayerPlatform]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[
        ApimodelsPlayerPlatform,
        List[ApimodelsPlayerPlatform],
        Dict[Any, ApimodelsPlayerPlatform],
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
            "currentPlatform": "current_platform",
            "userID": "user_id",
            "crossplayEnabled": "crossplay_enabled",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "currentPlatform": True,
            "userID": True,
            "crossplayEnabled": False,
        }

    # endregion static methods
