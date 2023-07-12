# StartJobRequest

Job start definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **dict(str, str)** | All arguments needed for the Job to run | [optional] 
**notifications** | [**list[Notification]**](Notification.md) | Notifications for this Job | [optional] 
**use_as_auth** | **str** | Id of user associated with schedule. All calls to FINBOURNE services  as part of execution of this schedule will be authenticated as this   user. Can be null, in which case we&#39;ll default to that of the user   making this request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


