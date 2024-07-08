# FileMetadata

Metadata of a file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** | The path of the file. | 
**last_modified** | **datetime** | The last modified date of the file. | 
**size_bytes** | **int** | The size of the file in Bytes. | 

## Example

```python
from files_api_sdk.models.file_metadata import FileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FileMetadata from a JSON string
file_metadata_instance = FileMetadata.from_json(json)
# print the JSON string representation of the object
print FileMetadata.to_json()

# convert the object into a dict
file_metadata_dict = file_metadata_instance.to_dict()
# create an instance of FileMetadata from a dict
file_metadata_from_dict = FileMetadata.from_dict(file_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


