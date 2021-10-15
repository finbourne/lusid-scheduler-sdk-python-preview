# BucketWatcherTrigger

Trigger based on activity from an S3 bucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The file name or partial path of the file that will trigger the job  E.G: &#x60;fileName&#x60; or &#x60;folder1/folder2/someFileName&#x60; | [optional] 
**poll_period** | **int** | The frequency, in seconds, at which to poll the S3 bucket for the file.  Defaults to 5. | [optional] 
**bucket** | **str** | The S3 bucket where to watch for the trigger file | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


