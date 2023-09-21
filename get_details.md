### Retrieve Group Details Documentaion

## Description
The /api/groups/<group_id> endpoint is a RESTful API route that retrieves group information from the server based on the unique identifier (group_id) provided in the URL.

## Endpoint URL
GET /api/groups/<group_id>

## Responses
Status Code: 200
Response Body: json
Description: Retrieves information about a specific group, which is identified by the group_id.

## Error Responses
Status Code: 404
Response Body: json that contains the error message
Description: 
Group doesn't exist: This error occurs when the given group_id doesn't match an existing group in the db.


Example Request
curl --location '/api/groups/<group_id>'

## Example Response
```json
    Status: 200 OK
    json
    {
    "details": {
        "events": [
        {
            "id": 2,
            "title": "Wedding",
            "description": "A special and memorable celebration",
            ...
        },
        {
            "description": "A big birthday",
            "id": 1,
            "title": "Birthday",
            ...
        },
        ...
        ],
        "images": [
        {
            "id": 2,
            "url_name": "Sea"
        },
        ...
        ],
        "name": "Dragon",
        "users": [
        {
            "email": "steph@gmail.com",
            "id": 2,
            "name": "Stephen",
            ...
        },
        ...
        ]
    }
    }
```

# Check the response status code
if response.status_code == 201:
    print('Group details successfully retrieved')
elif response.status_code == 404:
    print('Group doesn't exist in the db.')


Author: [Zainab Wuraola Mahmud](https://github.com/zee467)
Email: wura.mahmud@gmail.com