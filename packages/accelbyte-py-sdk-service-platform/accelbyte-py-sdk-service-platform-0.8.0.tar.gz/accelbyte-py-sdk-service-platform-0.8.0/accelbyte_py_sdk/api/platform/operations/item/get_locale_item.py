# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# template file: operation.j2

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

# AccelByte Gaming Services Platform Service

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from accelbyte_py_sdk.core import Operation
from accelbyte_py_sdk.core import HeaderStr
from accelbyte_py_sdk.core import HttpResponse

from ...models import ErrorEntity
from ...models import PopulatedItemInfo


class GetLocaleItem(Operation):
    """Get an item in locale (getLocaleItem)

    This API is used to get an item in specific locale. If item not exist in specific region, default region item will return.

    Other detail info:

      * Required permission : resource="ADMIN:NAMESPACE:{namespace}:ITEM", action=2 (READ)
      *  Returns : item data

    Required Permission(s):
        - ADMIN:NAMESPACE:{namespace}:ITEM [READ]

    Properties:
        url: /platform/admin/namespaces/{namespace}/items/{itemId}/locale

        method: GET

        tags: ["Item"]

        consumes: []

        produces: ["application/json"]

        securities: [BEARER_AUTH] or [BEARER_AUTH]

        item_id: (itemId) REQUIRED str in path

        namespace: (namespace) REQUIRED str in path

        active_only: (activeOnly) OPTIONAL bool in query

        language: (language) OPTIONAL str in query

        populate_bundle: (populateBundle) OPTIONAL bool in query

        region: (region) OPTIONAL str in query

        store_id: (storeId) OPTIONAL str in query

    Responses:
        200: OK - PopulatedItemInfo (successful operation)

        404: Not Found - ErrorEntity (30141: Store [{storeId}] does not exist in namespace [{namespace}] | 30142: Published store does not exist in namespace [{namespace}] | 30341: Item [{itemId}] does not exist in namespace [{namespace}])
    """

    # region fields

    _url: str = "/platform/admin/namespaces/{namespace}/items/{itemId}/locale"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _securities: List[List[str]] = [["BEARER_AUTH"], ["BEARER_AUTH"]]
    _location_query: str = None

    item_id: str  # REQUIRED in [path]
    namespace: str  # REQUIRED in [path]
    active_only: bool  # OPTIONAL in [query]
    language: str  # OPTIONAL in [query]
    populate_bundle: bool  # OPTIONAL in [query]
    region: str  # OPTIONAL in [query]
    store_id: str  # OPTIONAL in [query]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def securities(self) -> List[List[str]]:
        return self._securities

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "item_id"):
            result["itemId"] = self.item_id
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "active_only"):
            result["activeOnly"] = self.active_only
        if hasattr(self, "language"):
            result["language"] = self.language
        if hasattr(self, "populate_bundle"):
            result["populateBundle"] = self.populate_bundle
        if hasattr(self, "region"):
            result["region"] = self.region
        if hasattr(self, "store_id"):
            result["storeId"] = self.store_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_item_id(self, value: str) -> GetLocaleItem:
        self.item_id = value
        return self

    def with_namespace(self, value: str) -> GetLocaleItem:
        self.namespace = value
        return self

    def with_active_only(self, value: bool) -> GetLocaleItem:
        self.active_only = value
        return self

    def with_language(self, value: str) -> GetLocaleItem:
        self.language = value
        return self

    def with_populate_bundle(self, value: bool) -> GetLocaleItem:
        self.populate_bundle = value
        return self

    def with_region(self, value: str) -> GetLocaleItem:
        self.region = value
        return self

    def with_store_id(self, value: str) -> GetLocaleItem:
        self.store_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "item_id") and self.item_id:
            result["itemId"] = str(self.item_id)
        elif include_empty:
            result["itemId"] = ""
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = ""
        if hasattr(self, "active_only") and self.active_only:
            result["activeOnly"] = bool(self.active_only)
        elif include_empty:
            result["activeOnly"] = False
        if hasattr(self, "language") and self.language:
            result["language"] = str(self.language)
        elif include_empty:
            result["language"] = ""
        if hasattr(self, "populate_bundle") and self.populate_bundle:
            result["populateBundle"] = bool(self.populate_bundle)
        elif include_empty:
            result["populateBundle"] = False
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = ""
        if hasattr(self, "store_id") and self.store_id:
            result["storeId"] = str(self.store_id)
        elif include_empty:
            result["storeId"] = ""
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(
        self, code: int, content_type: str, content: Any
    ) -> Tuple[Union[None, PopulatedItemInfo], Union[None, ErrorEntity, HttpResponse]]:
        """Parse the given response.

        200: OK - PopulatedItemInfo (successful operation)

        404: Not Found - ErrorEntity (30141: Store [{storeId}] does not exist in namespace [{namespace}] | 30142: Published store does not exist in namespace [{namespace}] | 30341: Item [{itemId}] does not exist in namespace [{namespace}])

        ---: HttpResponse (Undocumented Response)

        ---: HttpResponse (Unexpected Content-Type Error)

        ---: HttpResponse (Unhandled Error)
        """
        pre_processed_response, error = self.pre_process_response(
            code=code, content_type=content_type, content=content
        )
        if error is not None:
            return None, None if error.is_no_content() else error
        code, content_type, content = pre_processed_response

        if code == 200:
            return PopulatedItemInfo.create_from_dict(content), None
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)

        return self.handle_undocumented_response(
            code=code, content_type=content_type, content=content
        )

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        item_id: str,
        namespace: str,
        active_only: Optional[bool] = None,
        language: Optional[str] = None,
        populate_bundle: Optional[bool] = None,
        region: Optional[str] = None,
        store_id: Optional[str] = None,
        **kwargs,
    ) -> GetLocaleItem:
        instance = cls()
        instance.item_id = item_id
        instance.namespace = namespace
        if active_only is not None:
            instance.active_only = active_only
        if language is not None:
            instance.language = language
        if populate_bundle is not None:
            instance.populate_bundle = populate_bundle
        if region is not None:
            instance.region = region
        if store_id is not None:
            instance.store_id = store_id
        if x_flight_id := kwargs.get("x_flight_id", None):
            instance.x_flight_id = x_flight_id
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> GetLocaleItem:
        instance = cls()
        if "itemId" in dict_ and dict_["itemId"] is not None:
            instance.item_id = str(dict_["itemId"])
        elif include_empty:
            instance.item_id = ""
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = ""
        if "activeOnly" in dict_ and dict_["activeOnly"] is not None:
            instance.active_only = bool(dict_["activeOnly"])
        elif include_empty:
            instance.active_only = False
        if "language" in dict_ and dict_["language"] is not None:
            instance.language = str(dict_["language"])
        elif include_empty:
            instance.language = ""
        if "populateBundle" in dict_ and dict_["populateBundle"] is not None:
            instance.populate_bundle = bool(dict_["populateBundle"])
        elif include_empty:
            instance.populate_bundle = False
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = ""
        if "storeId" in dict_ and dict_["storeId"] is not None:
            instance.store_id = str(dict_["storeId"])
        elif include_empty:
            instance.store_id = ""
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "itemId": "item_id",
            "namespace": "namespace",
            "activeOnly": "active_only",
            "language": "language",
            "populateBundle": "populate_bundle",
            "region": "region",
            "storeId": "store_id",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "itemId": True,
            "namespace": True,
            "activeOnly": False,
            "language": False,
            "populateBundle": False,
            "region": False,
            "storeId": False,
        }

    # endregion static methods
