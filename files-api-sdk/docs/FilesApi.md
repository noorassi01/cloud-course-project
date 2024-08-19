# files_api_sdk.FilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /files/{file_path} | Delete File
[**files_upload_file**](FilesApi.md#files_upload_file) | **PUT** /files/{file_path} | Upload File
[**get_file**](FilesApi.md#get_file) | **GET** /files/{file_path} | Get File
[**get_files_list**](FilesApi.md#get_files_list) | **GET** /files | List Files
[**retrieve_file**](FilesApi.md#retrieve_file) | **HEAD** /files/{file_path} | Get File Metadata


# **delete_file**
> object delete_file(file_path)

Delete File

Delete a file.  NOTE: DELETE requests MUST NOT return a body in the response.

### Example

```python
import time
import os
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
    except Exception as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_upload_file**
> PutFileResponse files_upload_file(file_path, file_content)

Upload File

Upload a file.

### Example

```python
import time
import os
import files_api_sdk
from files_api_sdk.models.put_file_response import PutFileResponse
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
    file_content = None # bytearray | 

    try:
        # Upload File
        api_response = api_instance.files_upload_file(file_path, file_content)
        print("The response of FilesApi->files_upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->files_upload_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**|  | 
 **file_content** | **bytearray**|  | 

### Return type

[**PutFileResponse**](PutFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**201** | Created |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> object get_file(file_path)

Get File

Retrieve a file.

### Example

```python
import time
import os
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
        # Get File
        api_response = api_instance.get_file(file_path)
        print("The response of FilesApi->get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_list**
> GetFilesResponse get_files_list(page_size=page_size, directory=directory, page_token=page_token)

List Files

List files with pagination.

### Example

```python
import time
import os
import files_api_sdk
from files_api_sdk.models.get_files_response import GetFilesResponse
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
    page_size = 10 # int |  (optional) (default to 10)
    directory = 'directory_example' # str |  (optional)
    page_token = 'page_token_example' # str |  (optional)

    try:
        # List Files
        api_response = api_instance.get_files_list(page_size=page_size, directory=directory, page_token=page_token)
        print("The response of FilesApi->get_files_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_files_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**|  | [optional] [default to 10]
 **directory** | **str**|  | [optional] 
 **page_token** | **str**|  | [optional] 

### Return type

[**GetFilesResponse**](GetFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_file**
> object retrieve_file(file_path)

Get File Metadata

Retrieve file metadata.  Note: by convention, HEAD requests MUST NOT return a body in the response.

### Example

```python
import time
import os
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
        # Get File Metadata
        api_response = api_instance.retrieve_file(file_path)
        print("The response of FilesApi->retrieve_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->retrieve_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

