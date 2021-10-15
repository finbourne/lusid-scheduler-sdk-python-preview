# CreateScheduleRequest

Create a schedule definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | [**ResourceId**](ResourceId.md) |  | 
**job_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | A display name for this Schedule | 
**description** | **str** | A description of the Schedule | 
**author** | **str** | Name of the author of this schedule | [optional] 
**owner** | **str** | Name of owner of this schedule | [optional] 
**arguments** | **dict(str, str)** | All arguments specified by this Schedule that will be passed in to the Job | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**notifications** | [**list[Notification]**](Notification.md) | Notifications for this Schedule | 
**enabled** | **bool** | Specify whether schedule is enabled or not  Defaults to true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


