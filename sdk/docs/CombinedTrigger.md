# CombinedTrigger

A file based triggered constrained by a time window  Supports the ability to specify multiple trigger files,  to choose whether a schedule is triggered for every file or first file,  has the option to trigger the schedule at the end of the time window, if any or no files arrived

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | The start of the time window when a file can arrive to trigger the schedule  Cannot exceed 24 hours | 
**end_time** | **str** | The end of the time window when a file can arrive to trigger the schedule  Must be after the Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.StartTime and cannot exceed 24 hours | 
**file** | **str** | The file name or partial path of the file that will trigger the job  E.G: &#x60;fileName&#x60; or &#x60;folder1/folder2/someFileName&#x60; | 
**poll_period** | **int** | The frequency, in seconds, at which to poll the S3 bucket for the file.  Must be lower than the difference in seconds between Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.EndTime and Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.StartTime  Defaults to 5. | [optional] 
**bucket** | **str** | The S3 bucket where to watch for the trigger file | 
**trigger_every_file** | **bool** | Specify whether to trigger every time the file is updated | [optional] 
**end_of_time_window_option** | **str** | Specifies the behaviour of the trigger when the time window ends  Available options are \&quot;Always\&quot;, \&quot;NoFile\&quot;, \&quot;FileReceived\&quot;, \&quot;Never\&quot;  Finbourne.Scheduler.WebApi.Dtos.CombinedTrigger.EndOfTimeWindowOption | 
**days_available** | [**DaysOfWeek**](DaysOfWeek.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


