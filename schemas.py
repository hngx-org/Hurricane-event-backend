from marshmallow import Schema, fields


class UserSchema(Schema):
    pass


class EventSchema(Schema):
    """
    Schema for serializing and deserializing events data, including their creators' information.

    Attributes:
        id (UUID): Unique identifier for the event (read-only).
        title (str): Title of the event (required).
        description (str): Description of the event (required).
        location (str): Location of the event (required).
        start_date (date): Start date of the event (required, format: 'YYYY-MM-DD').
        end_date (date): End date of the event (required, format: 'YYYY-MM-DD').
        start_time (time): Start time of the event (required, format: 'HH:MM:SS').
        end_time (time): End time of the event (required, format: 'HH:MM:SS').
        thumbnail (str): URL to the event's thumbnail image (required).
        creator_id (UUID): ID of the user who created the event (required).
        creator (UserSchema): Nested schema for the event's creator information (read-only).

    Usage:
        - Use this schema to serialize event data before sending responses.
        - Use it to deserialize incoming JSON data into EventModel objects.

    Example:
        {
            'id': '6f84df90-49cc-4bd1-8a78-8f178164e093',
            'title': 'Sample Event',
            'description': 'This is a sample event description.',
            'location': 'Sample Location',
            'start_date': '2023-09-20',
            'end_date': '2023-09-20',
            'start_time': '10:00:00',
            'end_time': '12:00:00',
            'thumbnail': 'https://example.com/thumbnail.jpg',
            'creator_id': 'a61e24bd-8243-4ecb-becb-3f2621a019e7'
        }

    """
    id = fields.UUID(dump_only=True, required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    start_date = fields.Date(format='%Y-%m-%d', required=True)
    end_date = fields.Date(format='%Y-%m-%d', required=True)
    start_time = fields.Time(format='%H:%M:%S', required=True)
    end_time = fields.Time(format='%H:%M:%S', required=True)
    thumbnail = fields.Str(data_key='thumbnail', attribute='thumbnail', required=True)
    creator_id = fields.UUID(required=True)
    creator = fields.Nested(UserSchema, required=True)


class EventUpdateSchema(Schema):
    """
    Schema for partial updates of event data.

    Attributes:
        title (str): Updated title of the event (optional).
        description (str): Updated description of the event (optional).
        location (str): Updated location of the event (optional).
        start_date (date): Updated start date of the event (optional, format: 'YYYY-MM-DD').
        end_date (date): Updated end date of the event (optional, format: 'YYYY-MM-DD').
        start_time (time): Updated start time of the event (optional, format: 'HH:MM:SS').
        end_time (time): Updated end time of the event (optional, format: 'HH:MM:SS').

    Usage:
        - Use this schema to deserialize incoming JSON data for partial updates of event objects.

    Example:
        {
            'title': 'Updated Title',
            'description': 'Updated description',
            'location': 'Updated Location',
            'start_date': '2023-09-21',
            'end_date': '2023-09-21',
            'start_time': '11:00:00',
            'end_time': '13:00:00'
        }

    Note: This schema is intended for updating event data with partial information.
    """
    title = fields.Str()
    description = fields.Str()
    location = fields.Str()
    start_date = fields.Date(format='%Y-%m-%d')
    end_date = fields.Date(format='%Y-%m-%d')
    start_time = fields.Time(format='%H:%M:%S')
    end_time = fields.Time(format='%H:%M:%S')