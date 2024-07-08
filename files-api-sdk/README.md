# files-api-sdk
![Maintained by](https://img.shields.io/badge/Maintained%20by-MLOps%20Club-05998B?style=for-the-badge)

| Helpful Links | Notes |
| --- | --- |
| [Course Homepage](https://mlops-club.org) | |
| [Course Student Portal](https://courses.mlops-club.org) | |
| [Course Materials Repo](https://github.com/mlops-club/python-on-aws-course.git) | `mlops-club/python-on-aws-course` |
| [Course Reference Project Repo](https://github.com/mlops-club/cloud-course-project.git) | `mlops-club/cloud-course-project` |
| [FastAPI Documentation](https://fastapi.tiangolo.com/) | |
| [Learn to make \"badges\"](https://shields.io/) | Example: <img alt=\"Awesome Badge\" src=\"https://img.shields.io/badge/Awesome-😎-blueviolet?style=for-the-badge\"> |


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Generator version: 7.8.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import files_api_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import files_api_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import files_api_sdk
from files_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = files_api_sdk.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with files_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api_sdk.FilesApi(api_client)
    file_path = 'file_path_example' # str | 

    try:
        # Delete File
        api_response = api_instance.delete_file(file_path)
        print("The response of FilesApi->delete_file:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FilesApi* | [**delete_file**](docs/FilesApi.md#delete_file) | **DELETE** /files/{file_path} | Delete File
*FilesApi* | [**get_file**](docs/FilesApi.md#get_file) | **GET** /files/{file_path} | Get File
*FilesApi* | [**get_files_list**](docs/FilesApi.md#get_files_list) | **GET** /files | List Files
*FilesApi* | [**put_file**](docs/FilesApi.md#put_file) | **PUT** /files/{file_path} | Upload File
*FilesApi* | [**retrieve_file**](docs/FilesApi.md#retrieve_file) | **HEAD** /files/{file_path} | Get File Metadata


## Documentation For Models

 - [FileMetadata](docs/FileMetadata.md)
 - [GetFilesResponse](docs/GetFilesResponse.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [PutFileResponse](docs/PutFileResponse.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author



