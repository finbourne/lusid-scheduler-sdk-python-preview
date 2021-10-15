# lusid_scheduler.SchedulesApi

All URIs are relative to *https://fbn-ci.lusid.com/scheduler2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](SchedulesApi.md#create_schedule) | **POST** /api/schedules | [EXPERIMENTAL] CreateSchedule: Create a Schedule for a job
[**delete_schedule**](SchedulesApi.md#delete_schedule) | **DELETE** /api/schedules/{scope}/{code} | [EXPERIMENTAL] DeleteSchedule: Delete a schedule
[**enabled_schedule**](SchedulesApi.md#enabled_schedule) | **PUT** /api/schedules/{scope}/{code}/enabled | [EXPERIMENTAL] EnabledSchedule: Enable/disable a schedule
[**get_schedule**](SchedulesApi.md#get_schedule) | **GET** /api/schedules/{scope}/{code} | [EXPERIMENTAL] GetSchedule: Get a single Schedule
[**list_schedules**](SchedulesApi.md#list_schedules) | **GET** /api/schedules | [EXPERIMENTAL] ListSchedules: List the available Schedules
[**run_schedule**](SchedulesApi.md#run_schedule) | **POST** /api/schedules/{scope}/{code}/$run | [EXPERIMENTAL] RunSchedule: Run a schedule immediately
[**update_schedule**](SchedulesApi.md#update_schedule) | **PUT** /api/schedules/{scope}/{code} | [EXPERIMENTAL] UpdateSchedule: Update a schedule.


# **create_schedule**
> ScheduleDefinition create_schedule(create_schedule_request)

[EXPERIMENTAL] CreateSchedule: Create a Schedule for a job

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/scheduler2
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_scheduler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_scheduler.SchedulesApi(api_client)
    create_schedule_request = {"scheduleId":{"scope":"ScheduleScope","code":"ScheduleCode"},"jobId":{"scope":"JobScope","code":"JobCode"},"name":"Schedule name","description":"Schedule description","author":"Schedule author","owner":"Schedule owner","arguments":{"argument":"Argument value"},"trigger":{"bucketWatcherTrigger":{"file":"FileName","pollPeriod":5,"bucket":"fbn-ci-schedulertest"}},"notifications":[{"fireOn":"Completed","transport":"Email","destination":["destination"]},{"fireOn":"Failed","transport":"SMS","destination":["destination1","destination2"]}],"enabled":true} # CreateScheduleRequest | 

    try:
        # [EXPERIMENTAL] CreateSchedule: Create a Schedule for a job
        api_response = api_instance.create_schedule(create_schedule_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchedulesApi->create_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_schedule_request** | [**CreateScheduleRequest**](CreateScheduleRequest.md)|  | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created schedule |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule**
> delete_schedule(scope, code)

[EXPERIMENTAL] DeleteSchedule: Delete a schedule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/scheduler2
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_scheduler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_scheduler.SchedulesApi(api_client)
    scope = 'scope_example' # str | Scope of the schedule to be deleted
code = 'code_example' # str | Code of the schedule to be deleted

    try:
        # [EXPERIMENTAL] DeleteSchedule: Delete a schedule
        api_instance.delete_schedule(scope, code)
    except ApiException as e:
        print("Exception when calling SchedulesApi->delete_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be deleted | 
 **code** | **str**| Code of the schedule to be deleted | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enabled_schedule**
> ScheduleDefinition enabled_schedule(scope, code, enable)

[EXPERIMENTAL] EnabledSchedule: Enable/disable a schedule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/scheduler2
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_scheduler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_scheduler.SchedulesApi(api_client)
    scope = 'scope_example' # str | Scope of the schedule to be enabled/disabled
code = 'code_example' # str | Code of the schedule to be enabled/disabled
enable = True # bool | Specify whether to enable or disable the schedule

    try:
        # [EXPERIMENTAL] EnabledSchedule: Enable/disable a schedule
        api_response = api_instance.enabled_schedule(scope, code, enable)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchedulesApi->enabled_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be enabled/disabled | 
 **code** | **str**| Code of the schedule to be enabled/disabled | 
 **enable** | **bool**| Specify whether to enable or disable the schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule**
> ScheduleDefinition get_schedule(scope, code)

[EXPERIMENTAL] GetSchedule: Get a single Schedule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/scheduler2
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_scheduler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_scheduler.SchedulesApi(api_client)
    scope = 'scope_example' # str | The scope of Schedule
code = 'code_example' # str | The code of the Schedule

    try:
        # [EXPERIMENTAL] GetSchedule: Get a single Schedule
        api_response = api_instance.get_schedule(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchedulesApi->get_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of Schedule | 
 **code** | **str**| The code of the Schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedules**
> ResourceListOfScheduleDefinition list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListSchedules: List the available Schedules

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/scheduler2
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_scheduler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_scheduler.SchedulesApi(api_client)
    page = 'page_example' # str | The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified (optional) (default to 2000)
filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # [EXPERIMENTAL] ListSchedules: List the available Schedules
        api_response = api_instance.list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchedulesApi->list_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing instruments from a previous call to list instruments.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_schedule**
> StartScheduleResponse run_schedule(scope, code)

[EXPERIMENTAL] RunSchedule: Run a schedule immediately

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/scheduler2
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_scheduler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_scheduler.SchedulesApi(api_client)
    scope = 'scope_example' # str | The schedule scope
code = 'code_example' # str | The schedule cde

    try:
        # [EXPERIMENTAL] RunSchedule: Run a schedule immediately
        api_response = api_instance.run_schedule(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchedulesApi->run_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The schedule scope | 
 **code** | **str**| The schedule cde | 

### Return type

[**StartScheduleResponse**](StartScheduleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule**
> ScheduleDefinition update_schedule(scope, code, update_schedule_request)

[EXPERIMENTAL] UpdateSchedule: Update a schedule.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_scheduler
from lusid_scheduler.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/scheduler2
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_scheduler.Configuration(
    host = "https://fbn-ci.lusid.com/scheduler2"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_scheduler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_scheduler.SchedulesApi(api_client)
    scope = 'scope_example' # str | Scope of the schedule to be updated
code = 'code_example' # str | Code of the schedule to be updated
update_schedule_request = {"jobId":{"scope":"JobScope","code":"JobCode"},"name":"UpdatedSchedule","description":"Updated description","author":"Updated author","owner":"Updated owner","arguments":{"updatedArgument":"Updated value"},"trigger":{"bucketWatcherTrigger":{"file":"FileName","pollPeriod":5,"bucket":"fbn-ci-schedulertest"}},"notifications":[{"fireOn":"Completed","transport":"Email","destination":["destination"]},{"fireOn":"Failed","transport":"SMS","destination":["destination1","destination2"]}],"enabled":true} # UpdateScheduleRequest | The updated schedule

    try:
        # [EXPERIMENTAL] UpdateSchedule: Update a schedule.
        api_response = api_instance.update_schedule(scope, code, update_schedule_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchedulesApi->update_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be updated | 
 **code** | **str**| Code of the schedule to be updated | 
 **update_schedule_request** | [**UpdateScheduleRequest**](UpdateScheduleRequest.md)| The updated schedule | 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

