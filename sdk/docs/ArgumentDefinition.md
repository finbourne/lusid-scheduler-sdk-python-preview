# ArgumentDefinition

Job argument definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Data type of the argument | 
**required** | **bool** | Optionality of the argument | [optional] 
**description** | **str** | Argument description | 
**order** | **int** | The order of the argument | 
**constraints** | **str** | Constrains of the argument value | [optional] 
**passed_as** | **str** | Specifies how this argument should be passed in  Allowed values are: CommandLine or EnvironmentVariable    Defaults to: CommandLine | 
**default_value** | **str** | Specify a default value for this argument if no value is provided  The value needs to be convertible to the associated data type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


