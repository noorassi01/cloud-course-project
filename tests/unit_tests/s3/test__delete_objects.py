from moto import mock_aws

from files_api.s3.delete_objects import delete_s3_object
from files_api.s3.read_objects import object_exists_in_s3
from files_api.s3.write_objects import upload_s3_object
from tests.consts import TEST_BUCKET_NAME


@mock_aws()
def test_delete_non_existing_s3_object(mocked_aws: None):
    object_key = "test.txt"
    file_content: bytes = b"Test Delete"
    upload_s3_object(
        bucket_name=TEST_BUCKET_NAME,
        object_key=object_key,
        file_content=file_content,
    )
    # Delete File
    delete_s3_object(
        bucket_name=TEST_BUCKET_NAME,
        object_key=object_key,
    )
    # Delete again -- nothing should happen
    delete_s3_object(
        bucket_name=TEST_BUCKET_NAME,
        object_key=object_key,
    )

    assert object_exists_in_s3(bucket_name=TEST_BUCKET_NAME, object_key=object_key) is False
