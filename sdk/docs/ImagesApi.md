# lusid_scheduler.ImagesApi

All URIs are relative to *https://fbn-ci.lusid.com/scheduler2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_image**](ImagesApi.md#delete_image) | **DELETE** /api/images/{name} | [EXPERIMENTAL] DeleteImage: Delete an image from Harbor
[**download_image**](ImagesApi.md#download_image) | **GET** /api/images/{name}/contents | [EXPERIMENTAL] DownloadImage: Download the file from Harbor
[**get_image**](ImagesApi.md#get_image) | **GET** /api/images/{name} | [EXPERIMENTAL] GetImage: Get an image metadata from Harbor
[**list_images**](ImagesApi.md#list_images) | **GET** /api/images/repository/{name} | [EXPERIMENTAL] ListImages: List all images in a Repository
[**list_repositories**](ImagesApi.md#list_repositories) | **GET** /api/images/repository | [EXPERIMENTAL] ListRepositories: List all repositories
[**upload_image**](ImagesApi.md#upload_image) | **POST** /api/images | [EXPERIMENTAL] UploadImage: Uploads an image to be used for Scheduler jobs


# **delete_image**
> str delete_image(name)

[EXPERIMENTAL] DeleteImage: Delete an image from Harbor

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
    api_instance = lusid_scheduler.ImagesApi(api_client)
    name = 'name_example' # str | The name and tag of the image of the image. Format \"ExampleImageName:latest,0.1,0.2\"

    try:
        # [EXPERIMENTAL] DeleteImage: Delete an image from Harbor
        api_response = api_instance.delete_image(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->delete_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of the image of the image. Format \&quot;ExampleImageName:latest,0.1,0.2\&quot; | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No image with this name and tag exists |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_image**
> file download_image(name)

[EXPERIMENTAL] DownloadImage: Download the file from Harbor

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
    api_instance = lusid_scheduler.ImagesApi(api_client)
    name = 'name_example' # str | The name and tag of the image of the image. Format \"ExampleImageName:latest\"

    try:
        # [EXPERIMENTAL] DownloadImage: Download the file from Harbor
        api_response = api_instance.download_image(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->download_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of the image of the image. Format \&quot;ExampleImageName:latest\&quot; | 

### Return type

**file**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> Image get_image(name)

[EXPERIMENTAL] GetImage: Get an image metadata from Harbor

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
    api_instance = lusid_scheduler.ImagesApi(api_client)
    name = 'name_example' # str | The name and tag of the image of the image. Format \"ExampleImageName:latest\"

    try:
        # [EXPERIMENTAL] GetImage: Get an image metadata from Harbor
        api_response = api_instance.get_image(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name and tag of the image of the image. Format \&quot;ExampleImageName:latest\&quot; | 

### Return type

[**Image**](Image.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_images**
> ResourceListOfImageSummary list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListImages: List all images in a Repository

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
    api_instance = lusid_scheduler.ImagesApi(api_client)
    name = 'name_example' # str | The name of the Repository
page = 'page_example' # str | The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified (optional) (default to 2000)
filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # [EXPERIMENTAL] ListImages: List all images in a Repository
        api_response = api_instance.list_images(name, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->list_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Repository | 
 **page** | **str**| The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfImageSummary**](ResourceListOfImageSummary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repositories**
> ResourceListOfRepository list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListRepositories: List all repositories

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
    api_instance = lusid_scheduler.ImagesApi(api_client)
    page = 'page_example' # str | The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 2000 # int | When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified (optional) (default to 2000)
filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # [EXPERIMENTAL] ListRepositories: List all repositories
        api_response = api_instance.list_repositories(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->list_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing images from a previous call to list images.              This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfRepository**](ResourceListOfRepository.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image**
> UploadImageInstructions upload_image(upload_image_request)

[EXPERIMENTAL] UploadImage: Uploads an image to be used for Scheduler jobs

Every image must have at least one tag

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
    api_instance = lusid_scheduler.ImagesApi(api_client)
    upload_image_request = {"imageName":"example-image-name:0.0.1"} # UploadImageRequest | Request to upload image

    try:
        # [EXPERIMENTAL] UploadImage: Uploads an image to be used for Scheduler jobs
        api_response = api_instance.upload_image(upload_image_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->upload_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_image_request** | [**UploadImageRequest**](UploadImageRequest.md)| Request to upload image | 

### Return type

[**UploadImageInstructions**](UploadImageInstructions.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

