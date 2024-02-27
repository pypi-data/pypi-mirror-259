"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import job_status as shared_job_status
from ...models.shared import variation_type as shared_variation_type
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import List, Optional


@dataclasses.dataclass
class GetVariationByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""\\"id\\" is required"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GeneratedImageVariationGeneric:
    r"""columns and relationships of \\"generated_image_variation_generic\\" """
    UNSET='__SPEAKEASY_UNSET__'
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is GeneratedImageVariationGeneric.UNSET }})
    status: Optional[shared_job_status.JobStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the current task."""
    transform_type: Optional[shared_variation_type.VariationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transformType'), 'exclude': lambda f: f is None }})
    r"""The type of variation."""
    url: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is GeneratedImageVariationGeneric.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetVariationByIDResponseBody:
    r"""Responses for GET /variations/{id}"""
    generated_image_variation_generic: Optional[List[GeneratedImageVariationGeneric]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generated_image_variation_generic'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetVariationByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[GetVariationByIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for GET /variations/{id}"""
    

