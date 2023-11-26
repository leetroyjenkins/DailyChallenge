#!/usr/bin/env python3

# https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction

import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

try:
    print('\nPytest log upload to Azure blob script starting.')

    # Quickstart code goes here
    account_url = 'https://pastrychefazurestorage.blob.core.windows.net'
    default_credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=default_credential)

    # Check for existing container names
    container_list = [i for i in blob_service_client.list_containers()]

    # Declare the container name used. Can be updated to be passed in future versions
    container_name = 'pytest-logs'

    # Check if <pytest-results> exists
    match = any(container.name == container_name for container in container_list)

    # Create container if not exists
    while not match:
        container_client = blob_service_client.create_container(container_name)

        # Check if <pytest-results> exists after container creation
        match = any(container.name == container_name for container in container_list)

        # added a break statement for debugging
        if match:
            break

    # Check that log file exists
    local_path = f'.//{container_name}'
    if not os.path.exists(local_path):
        os.mkdir(local_path)

    # Check for files in the <pytest_logs> dir
    logfiles = [file for file in os.listdir(local_path) if os.path.isfile(os.path.join(local_path, file))]


    # Check if the files exist in the container
    for file in logfiles:
        upload_file_path = os.path.join(local_path, file)

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file)
        print('\nProcessing files.')

        # Upload the files
        try:
            print(f'\n\t{file}:')
            print('\t\tUploading to Azure Storage as blob.')
            with open(file=upload_file_path, mode='rb') as data:
                blob_client.upload_blob(data)
            print('\t\tUpload successful.')
            # Write record of upload to log file

        except Exception as e:
            print(f'\n\t\\tError uploading {file}: {e}')

        #Clean up
        finally:
            print(f'\t\tDeleting local copy.')
            os.remove(upload_file_path)

    print('\nAll files successfully uploaded. Starting clean up.')

    os.rmdir(local_path)
    print(f'\nDeleting directory from local environment...\n\t{local_path} directory deleted.')

except Exception as ex:
    print('\n\tException:')
    print(ex)

finally:
    print('\nEnd of Pytest log upload to Azure blob script.')