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
