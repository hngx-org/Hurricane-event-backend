## Event API documentation

* keep your documentation well defined

This documentation provides details on the Event API, which allows you to manage evens. The API supports the creation of new events, updating an event, deleting an event, and  provides the ability to retrieve a list of existing events.

## API Base URL

The base URL for this API is `/event`. All endpoints described below are relative to this base URL.

## Endpoints

### Returns a list of comments for an event

- **Endpoint**: `/events/<event_id>/comments`
- **HTTP Method**: GET
- **Request URL**: STR
  - `event_id` (string, required): The id of the event
- **Response**: Returns the ID and list of comments in the events

#### Example Request

    curl "http://addresHost/events/:eventId/comments"

**Response**

```json
{
    "event_id": 1294dfg-2344653f-stgu64,
    "comments": [
        "i love this event",
        "OMG",
        ...
    ]
}
```


###  Get Images for a Comment
- **Route**: `GET /api/comments/<comment_id>/images`
- **Description**: Retrieve images associated with a specific comment.
- **Request Parameters**:
  - `comment_id` (URL parameter): The unique identifier for the comment.
- **Response**:
  - **Success (HTTP Status 200 OK)**:
    - JSON response with images for the specified comment.
    ```json
    {
        "comment_id": "<comment_id>",
        "images": [
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg",
            ...
        ]
    }
    ```
  - **Error (HTTP Status 404 Not Found)**:
    - If the specified comment does not exist:
      ```json
      {
          "error": "Comment not found"
      }
      ```
