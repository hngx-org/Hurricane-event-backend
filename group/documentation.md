# Group API Documentation

This documentation provides details on the Group API, which allows you to manage groups. The API supports the creation of new groups and provides the ability to retrieve a list of existing groups.

## API Base URL

The base URL for this API is `/api/groups`. All endpoints described below are relative to this base URL.

## Endpoints

### Create a New Group

- **Endpoint**: `/api/groups`
- **HTTP Method**: POST
- **Request Body**: JSON
  - `title` (string, required): The title or name of the group.
- **Response**: Returns the ID and title of the created group if successful.

#### Example Request Body

```json
{
    "title": "My Group"
}
