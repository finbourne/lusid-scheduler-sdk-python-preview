# ScanReport

Represents the details of a security scan of an image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | The overall severity. For example : \&quot;High\&quot; or \&quot;None\&quot; | [optional] 
**status** | **str** | The status of the report | [optional] 
**start_time** | **datetime** | The start time of the scanning process | [optional] 
**end_time** | **datetime** | The end time of the scanning process | [optional] 
**scan_duration** | **int** | The duration of the scan in seconds | [optional] 
**summary** | [**ScanSummary**](ScanSummary.md) |  | [optional] 
**vulnerabilities** | [**list[Vulnerability]**](Vulnerability.md) | List of Finbourne.Scheduler.WebApi.Dtos.Images.Vulnerability | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


