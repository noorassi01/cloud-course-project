# coding: utf-8

"""
    Files API

    ![Maintained by: Noor Assi](https://img.shields.io/badge/Maintained%20by-MLOps%20Club-05998B?style=for-the-badge)  | Helpful Links | Notes | | --- | --- | | [Course Homepage](https://mlops-club.org) | | | [Course Student Portal](https://courses.mlops-club.org) | | | [Course Materials Repo](https://github.com/mlops-club/python-on-aws-course.git) | `mlops-club/python-on-aws-course` | | [Course Reference Project Repo](https://github.com/mlops-club/cloud-course-project.git) | `mlops-club/cloud-course-project` | | [FastAPI Documentation](https://fastapi.tiangolo.com/) | | | [Learn to make \"badges\"](https://shields.io/) | Example: <img alt=\"Awesome Badge\" src=\"https://img.shields.io/badge/Awesome-😎-blueviolet?style=for-the-badge\"> | 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime

from pydantic import BaseModel, Field, StrictInt, StrictStr

class FileMetadata(BaseModel):
    """
    Metadata of a file.  # noqa: E501
    """
    file_path: StrictStr = Field(default=..., description="The path of the file.")
    last_modified: datetime = Field(default=..., description="The last modified date of the file.")
    size_bytes: StrictInt = Field(default=..., description="The size of the file in Bytes.")
    __properties = ["file_path", "last_modified", "size_bytes"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FileMetadata:
        """Create an instance of FileMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FileMetadata:
        """Create an instance of FileMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FileMetadata.parse_obj(obj)

        _obj = FileMetadata.parse_obj({
            "file_path": obj.get("file_path"),
            "last_modified": obj.get("last_modified"),
            "size_bytes": obj.get("size_bytes")
        })
        return _obj


