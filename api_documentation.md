The overview of the API endpoints available.

# GET /api/v1/search/

Returns a collection of relevant users matching the query.

Results are not case sensitive all fields, including the ID, are checked for whether or not the query exists inside the value
and if it does the object is then present in the response.

## Resource URL

Default endpoint URL: `http://127.0.0.1:5000/api/v1/search/`

## Resource Information

Response Format: JSON

## Parameters

Parameter | Description
--- | ---
`query` | **required** - A UTF-8, URL-encoded search query
`sort_by` | *(optional)* - Column by which the results should be sorted. Value must be one of the following: `id`, `first_name`, `last_name`, `gender`, `email`, `job_title`.
`order` | *(required if using `sort_by`)* - how to order the sorted results, either ascending or descending value must be either `asc` or `desc`

## Example Request

`$ http GET http://127.0.0.1:5000/api/v1/search/ query=="Charlie"` (which is equivalent to `http://127.0.0.1:5000/api/v1/search/?query=Charlie`)

## Example Response

```
HTTP/1.0 200 OK
Content-Length: 221
Content-Type: application/json
Date: Sat, 11 Jun 2016 16:15:36 GMT
Server: Werkzeug/0.11.10 Python/2.7.11

{
    "results": [
        {
            "email": "dayman@paddys.com",
            "first_name": "Charlie",
            "gender": "Male",
            "id": 3,
            "job_title": "Environmental Specialist",
            "last_name": "Kelley"
        }
    ]
}

```

# GET /api/v1/sort/

Returns the sorted list of the default items. Does not accept custom objects to sort etc. If you want to sort the list of search results you need to make the appropriate GET request to the search endpoint and not the sort one.

## Resource URL

Default endpoint URL: `http://127.0.0.1:5000/api/v1/sort/`

## Resource Information

Response Format: JSON

## Parameters

Parameter | Description
--- | ---
`sort_by` | **required** - Column by which the list should be sorted. Value must be one of the following: `id`, `first_name`, `last_name`, `gender`, `email`, `job_title`.
`order` | *(optional)* - how to order the sorted list, either ascending or descending value must be either `asc` or `desc`

## Example Request

`$ http GET http://127.0.0.1:5000/api/v1/sort/ sort_by=="id" order=="desc"`

## Example Response

```
HTTP/1.0 200 OK
Content-Length: 4933
Content-Type: application/json
Date: Sat, 11 Jun 2016 16:33:57 GMT
Server: Werkzeug/0.11.10 Python/2.7.11

{
    "results": [
        {
            "email": "jarnoldo@webnode.com",
            "first_name": "Janice",
            "gender": "Female",
            "id": 25,
            "job_title": "Programmer I",
            "last_name": "Arnold"
        },
        {
            "email": "slarsonn@wordpress.org",
            "first_name": "Sandra",
            "gender": "Female",
            "id": 24,
            "job_title": "Sales Associate",
            "last_name": "Larson"
        },
        ...
    ]
}
```

