"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostModels3dUploadRequestBody:
    r"""Query parameters can also be provided in the request body as a JSON object"""
    UNSET='__SPEAKEASY_UNSET__'
    model_extension: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelExtension'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is PostModels3dUploadRequestBody.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelAssetUploadOutput:
    UNSET='__SPEAKEASY_UNSET__'
    model_fields: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelFields'), 'exclude': lambda f: f is ModelAssetUploadOutput.UNSET }})
    model_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId'), 'exclude': lambda f: f is ModelAssetUploadOutput.UNSET }})
    model_key: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelKey'), 'exclude': lambda f: f is ModelAssetUploadOutput.UNSET }})
    model_url: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelUrl'), 'exclude': lambda f: f is ModelAssetUploadOutput.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostModels3dUploadResponseBody:
    r"""Responses for POST /api/rest/v1/models-3d/upload"""
    UNSET='__SPEAKEASY_UNSET__'
    upload_model_asset: Optional[ModelAssetUploadOutput] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploadModelAsset'), 'exclude': lambda f: f is PostModels3dUploadResponseBody.UNSET }})
    



@dataclasses.dataclass
class PostModels3dUploadResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[PostModels3dUploadResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /api/rest/v1/models-3d/upload"""
    

