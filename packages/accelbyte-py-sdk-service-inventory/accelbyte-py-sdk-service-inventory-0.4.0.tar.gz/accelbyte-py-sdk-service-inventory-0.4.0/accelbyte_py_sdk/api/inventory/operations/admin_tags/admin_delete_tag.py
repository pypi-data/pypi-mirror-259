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

# AccelByte Gaming Services Inventory Service

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from accelbyte_py_sdk.core import Operation
from accelbyte_py_sdk.core import HeaderStr
from accelbyte_py_sdk.core import HttpResponse

from ...models import ApimodelsErrorResponse


class AdminDeleteTag(Operation):
    """To delete a tag (AdminDeleteTag)

    This endpoint will delete a tag by tagName in a specified namespace.
    If the tagName doesn't exist in a namespace, it'll return not found.

    Permission: ADMIN:NAMESPACE:{namespace}:INVENTORY:TAG [DELETE]

    Required Permission(s):
        - ADMIN:NAMESPACE:{namespace}:INVENTORY:TAG [DELETE]

    Properties:
        url: /inventory/v1/admin/namespaces/{namespace}/tags/{tagName}

        method: DELETE

        tags: ["Admin Tags"]

        consumes: ["application/json"]

        produces: ["application/json"]

        securities: [BEARER_AUTH]

        namespace: (namespace) REQUIRED str in path

        tag_name: (tagName) REQUIRED str in path

    Responses:
        204: No Content - (No Content)

        404: Not Found - ApimodelsErrorResponse (Not Found)

        500: Internal Server Error - ApimodelsErrorResponse (Internal Server Error)
    """

    # region fields

    _url: str = "/inventory/v1/admin/namespaces/{namespace}/tags/{tagName}"
    _method: str = "DELETE"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _securities: List[List[str]] = [["BEARER_AUTH"]]
    _location_query: str = None

    namespace: str  # REQUIRED in [path]
    tag_name: str  # REQUIRED in [path]

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
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "tag_name"):
            result["tagName"] = self.tag_name
        return result

    # endregion get_x_params methods

    # region is/has methods

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> AdminDeleteTag:
        self.namespace = value
        return self

    def with_tag_name(self, value: str) -> AdminDeleteTag:
        self.tag_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = ""
        if hasattr(self, "tag_name") and self.tag_name:
            result["tagName"] = str(self.tag_name)
        elif include_empty:
            result["tagName"] = ""
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(
        self, code: int, content_type: str, content: Any
    ) -> Tuple[None, Union[None, ApimodelsErrorResponse, HttpResponse]]:
        """Parse the given response.

        204: No Content - (No Content)

        404: Not Found - ApimodelsErrorResponse (Not Found)

        500: Internal Server Error - ApimodelsErrorResponse (Internal Server Error)

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

        if code == 204:
            return None, None
        if code == 404:
            return None, ApimodelsErrorResponse.create_from_dict(content)
        if code == 500:
            return None, ApimodelsErrorResponse.create_from_dict(content)

        return self.handle_undocumented_response(
            code=code, content_type=content_type, content=content
        )

    # endregion response methods

    # region static methods

    @classmethod
    def create(cls, namespace: str, tag_name: str, **kwargs) -> AdminDeleteTag:
        instance = cls()
        instance.namespace = namespace
        instance.tag_name = tag_name
        if x_flight_id := kwargs.get("x_flight_id", None):
            instance.x_flight_id = x_flight_id
        return instance

    @classmethod
    def create_from_dict(
        cls, dict_: dict, include_empty: bool = False
    ) -> AdminDeleteTag:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = ""
        if "tagName" in dict_ and dict_["tagName"] is not None:
            instance.tag_name = str(dict_["tagName"])
        elif include_empty:
            instance.tag_name = ""
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "tagName": "tag_name",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "namespace": True,
            "tagName": True,
        }

    # endregion static methods
