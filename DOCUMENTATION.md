# Database Model Documentation

This document provides documentation for the database model used in the Flask Event App, along with explanations of how it is used according to the provided schema.

## User Model

The `User` model represents a user in the system.

Attributes:
- `id` (UUID): The unique identifier for the user.
- `name` (str): The user's name.
- `email` (str): The user's email address.
- `avatar` (str): URL to the user's avatar.

## Group Model

The `Group` model represents a group or community in the system.

Attributes:
- `id` (UUID): The unique identifier for the group.
- `title` (str): The title or name of the group.

## UserGroup Model

The `UserGroup` model represents the relationship between users and groups.

Attributes:
- `user_id` (UUID): The foreign key to the `User` model.
- `group_id` (UUID): The foreign key to the `Group` model.

## Event Model

The `Event` model represents an event in the system.

Attributes:
- `id` (UUID): The unique identifier for the event.
- `title` (str): The title or name of the event.
- `description` (str): A description of the event.
- `creator` (UUID): The foreign key to the `User` model representing the event's creator.
- `location` (str): The location of the event.
- `start_date` (date): The date when the event starts.
- `end_date` (date): The date when the event ends.
- `start_time` (timestamp): The timestamp when the event starts.
- `end_time` (timestamp): The timestamp when the event ends.
- `thumbnail` (str): URL to the event's thumbnail image.

## GroupEvent Model

The `GroupEvent` model represents the relationship between groups and events.

Attributes:
- `event_id` (UUID): The foreign key to the `Event` model.
- `group_id` (UUID): The foreign key to the `Group` model.

## InterestedEvent Model

The `InterestedEvent` model represents the relationship between users and events they are interested in.

Attributes:
- `user_id` (UUID): The foreign key to the `User` model.
- `event_id` (UUID): The foreign key to the `Event` model.

## Comment Model

The `Comment` model represents a comment on an event.

Attributes:
- `id` (UUID): The unique identifier for the comment.
- `body` (str): Text content of the comment.
- `user_id` (UUID): The foreign key to the `User` model representing the comment's author.
- `event_id` (UUID): The foreign key to the `Event` model representing the event the comment is on.

## Image Model

The `Image` model represents an image associated with a comment.

Attributes:
- `id` (UUID): The unique identifier for the image.
- `comment_id` (UUID): The foreign key to the `Comment` model representing the comment the image is associated with.
- `image_url` (str): URL to the image.

---

## Usage with Provided Schema

This database models provided in this documentation are designed to match the schema provided. Here's how they are used according to the schema:

- `User`, `Group`, `Event`, `Comment`, and `Image` models represent the core entities in the schema, each with their attributes.
- `UserGroup` and `GroupEvent` models are pivot tables that establish many-to-many relationships between users and groups, and events and groups, respectively.
- `InterestedEvent` model represents the relationship between users and events they are interested in.

The models can be used to create, retrieve, update, and delete data in the database. You can define routes and application logic in your Flask application (`app.py`) to interact with these models and provide the desired functionality for your event management application.

For example, you can create routes to:
- Create and manage user profiles.
- Create and manage events and groups.
- Allow users to join groups or express interest in events.
- Add comments and images to events.
- Retrieve event details and list events in various ways based on user interactions.



# Event Creation API Documentation

## Overview

This documentation provides information on how to use the Event Creation API. The API allows users to create events by sending a POST request to the `/api/events` endpoint. It includes JWT (JSON Web Token) authentication for user validation and SQLAlchemy for interacting with the SQL database.

## API Endpoints

### Create Event

- **Endpoint:** `/api/events`
- **HTTP Method:** POST
- **Authentication:** JWT required

#### Request Parameters

The API accepts the following form data parameters:

1. `title` (string, required): The title of the event.
2. `description` (string, required): A description of the event.
3. `location` (string, required): The location of the event.
4. `start_date` (string, required): The start date of the event in the format 'YYYY-MM-DD'.
5. `start_time` (string, required): The start time of the event in the format 'HH:MM:SS'.
6. `end_date` (string, required): The end date of the event in the format 'YYYY-MM-DD'.
7. `end_time` (string, required): The end time of the event in the format 'HH:MM:SS'.
8. `thumbnail_img_url` (string): The URL of the event's thumbnail image.
9. `user_id` (integer): User ID obtained from JWT authentication.

#### Example Request

```http
POST /api/events
Content-Type: application/x-www-form-urlencoded
Authorization: Bearer YOUR_JWT_TOKEN

title=Sample Event&description=This is a sample event&location=Sample Location&start_date=2023-09-20&start_time=09:00:00&end_date=2023-09-21&end_time=17:00:00&thumbnail_img_url=https://example.com/thumbnail.jpg&user_id=1
```

#### Successful Response (HTTP 201)

```json
{
    "message": "Event created successfully"
}
```

#### Error Response (HTTP 400)

```json
{
    "error": "Error message details"
}
```

## Database Model

The API uses an SQLAlchemy model for events, which includes the following fields:

- `id` (integer, primary key): Unique identifier for the event.
- `title` (string): The title of the event.
- `description` (text): A detailed description of the event.
- `location` (string): The location where the event takes place.
- `start_datetime` (datetime): The combined start date and time of the event.
- `end_datetime` (datetime): The combined end date and time of the event.
- `thumbnail_url` (string): URL of the event's thumbnail image.
- `user_id` (integer): The ID of the user who created the event.

## Running the Application

To run the Flask application locally, execute the following command in your terminal:

```
python app.py
```

This will start the development server, and you can access the API at `http://localhost:5000`.

## Dependencies

The API relies on the following Python packages:

- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLAlchemy

Install these dependencies using `pip` before running the application.

