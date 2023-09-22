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
