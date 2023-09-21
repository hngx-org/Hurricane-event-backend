## Comments API documentation

This documentation provides details on the Comments API, which allows you to manage the comments on particular events.

## API Base URL

The base URL for this API is `/comments`. All endpoints described below are relative to this base URL.

## Endpoints

### Returns a list of comments for an event

- **Endpoint**: `/coments/<comment_id>/images`
- **HTTP Method**: POST
- **Request URL**: STR
  - `comment_id` (string, required): The id of the comment to check images for.
- **Response**: dictionary containing image objects associated with the comment.

#### Example Request

    curl "http://addresHost/comment/:commentId/images"

**Response**

```json
{
    {
        "image_url": "/url",
        "comment_id": [ 64e618da53ec0d4716662127]
    }
}
```
