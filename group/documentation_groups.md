# Group API Documentation

This documentation provides details on the Group API, which allows you to manage groups. The API supports the creation of new groups, updating a group name, deleting a group, and  provides the ability to retrieve a list of existing groups.

## API Base URL

The base URL for this API is `/groups`. All endpoints described below are relative to this base URL.

## Endpoints

### Create a New Group

- **Endpoint**: `/groups`
- **HTTP Method**: POST
- **Request Body**: JSON
  - `title` (string, required): The title or name of the group.
- **Response**: Returns the ID and title of the created group if successful.

#### Example Request Body

```json
{
    "title": "My Group"
}
```

### Update a group

- **Endpoint**: `/groups/:groupID`
- **HTTP Method**: PUT
- **Request Body**: JSON
  - `title` (string, required): The new title of the group
- **Response**: Returns thee new group details if successful other returns an error message

#### Example Request

``` curl -X PUT -d '{"title": "New Name"}' "http://addresshost/groups/groupId"```

**Response**

```json
{
  "id": "120vbsf-dsebbv-sw-h344",
  "title": "New Name"
}
```

### Get all groups a user is in

This documentation provides an API that provide Groups a user is currently in using userid. The API also retrieves a list of all groups ,if more than one exists.

## API Base URL

The base URL for this API is `/groups/<int:userid>/groups`. The endpoint described below are relative to this base URL.

## Endpoints

- **Endpoint**: `/groups/<int:userid>/groups`
- **HTTP Method**: GET
- **Response**: Returns the user_id and list of groups the user is currently in.
- **Request URL**: JSON
  - `User_id` (string, required): The user_id of the User


#### Example Request
  curl "http://address+Host/groups/user_id/groups

**Response**

```json
user_id :{
      "group_id": "Group name",
      ...
  }
```
