# ImageSummary

Represents the metadata of an image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the image | [optional] 
**push_time** | **datetime** | The push time of the image | [optional] 
**pull_time** | **datetime** | The latest pull time of the image | [optional] 
**digest** | **str** | The digest of the image | [optional] 
**size** | **int** | The size of the image (in bytes) | [optional] 
**tags** | [**list[Tag]**](Tag.md) | The tags of the image | [optional] 
**scan_status** | **str** | The Scan Status of the stated image | [optional] 
**scan_summary** | [**ScanSummary**](ScanSummary.md) |  | [optional] 
**link** | [**Link**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


