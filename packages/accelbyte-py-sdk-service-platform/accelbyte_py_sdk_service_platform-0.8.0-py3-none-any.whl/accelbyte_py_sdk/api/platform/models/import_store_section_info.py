# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: model.j2

# AccelByte Gaming Services Platform Service

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


class ImportStoreSectionInfo(Model):
    """Import store section info (ImportStoreSectionInfo)

    Properties:
        name: (name) OPTIONAL str

        section_id: (sectionId) OPTIONAL str
    """

    # region fields

    name: str  # OPTIONAL
    section_id: str  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_name(self, value: str) -> ImportStoreSectionInfo:
        self.name = value
        return self

    def with_section_id(self, value: str) -> ImportStoreSectionInfo:
        self.section_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "name"):
            result["name"] = str(self.name)
        elif include_empty:
            result["name"] = ""
        if hasattr(self, "section_id"):
            result["sectionId"] = str(self.section_id)
        elif include_empty:
            result["sectionId"] = ""
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls, name: Optional[str] = None, section_id: Optional[str] = None, **kwargs
    ) -> ImportStoreSectionInfo:
        instance = cls()
        if name is not None:
            instance.name = name
        if section_id is not None:
            instance.section_id = section_id
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> ImportStoreSectionInfo:
        instance = cls()
        if not dict_:
            return instance
        if "name" in dict_ and dict_["name"] is not None:
            instance.name = str(dict_["name"])
        elif include_empty:
            instance.name = ""
        if "sectionId" in dict_ and dict_["sectionId"] is not None:
            instance.section_id = str(dict_["sectionId"])
        elif include_empty:
            instance.section_id = ""
        return instance

    @classmethod
    def create_many_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> Dict[str, ImportStoreSectionInfo]:
        return (
            {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_}
            if dict_
            else {}
        )

    @classmethod
    def create_many_from_list(
        cls, list_: list, include_empty: bool = False
    ) -> List[ImportStoreSectionInfo]:
        return (
            [cls.create_from_dict(i, include_empty=include_empty) for i in list_]
            if list_
            else []
        )

    @classmethod
    def create_from_any(
        cls, any_: any, include_empty: bool = False, many: bool = False
    ) -> Union[
        ImportStoreSectionInfo,
        List[ImportStoreSectionInfo],
        Dict[Any, ImportStoreSectionInfo],
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
            "name": "name",
            "sectionId": "section_id",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "name": False,
            "sectionId": False,
        }

    # endregion static methods
