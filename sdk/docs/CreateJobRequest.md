# CreateJobRequest

Definition of a job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | Name of the job | 
**author** | **str** | Author of the job | [optional] 
**date_created** | **datetime** | Date when job was created. Defaults to now. | [optional] 
**description** | **str** | Description of this job | 
**image_name** | **str** | The name of the Docker image that contains this job | 
**image_tag** | **str** | The tag of the Docker image that contains this job | 
**command** | **str** | The command for running this job | [optional] 
**ttl** | **int** | Time To Live of the job run in seconds  Defaults to 5 minutes(300) | [optional] 
**min_cpu** | **str** | Specifies  minimum number of CPUs to be allocated for the job  Default to 2 | [optional] 
**max_cpu** | **str** | Specifies  maximum number of CPUs to be allocated for the job | [optional] 
**min_memory** | **str** | Specifies the minimum amount of memory  to be allocated for the job | [optional] 
**max_memory** | **str** | Specifies the maximum amount of memory to be allocated for the job | [optional] 
**argument_definitions** | [**dict(str, ArgumentDefinition)**](ArgumentDefinition.md) | All arguments for this job to run | 
**command_line_argument_separator** | **str** | Value to separate command line arguments  e.g : If a job has a command line argument named &#39;folder&#39; and the runtime value is &#39;s3://path&#39; then this  would be supplied to the command as &#39;folder{separatorValue}s3://path&#39;  Default to a space | [optional] 
**required_resources** | [**RequiredResources**](RequiredResources.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


