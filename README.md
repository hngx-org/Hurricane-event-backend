# hurricane-event-backend

This repository contains the backend code for the Hurricane Event project. 

## Installation
To run the _huricane-event-backend_ locally, follow these steps:

* Clone the repository and activate the virtual environment.
* Install required dependencies: `pip install -r requirements.txt`
* Setup the configuration, `config.py`
* Run the app: `flask run`

## Models
These are the models in the application
* [User](models/user.py) - Defines the User Entity
* [Comment](models/comment.py) - Comments Entity
* [Image](models/image.py) - Defines the entity image added to Comments
* [Event](models/event.py) - Entity that defines the events available
* [GroupEvent](models/group_event.py) - Many to Many relationship of between Group and Event
* [Group](models/group.py) - Entity that defines types of group available
* [InterestedEvent](models/interested_event.py) - Many to Many relationship between User and Event
* [UserGroup](models/user_group.py) - Many to many relationship table between User and Group

## DATABASE
The database for this project is defined in this [here](models/engine/database.py)...
`import models`

`in order to perform query operations`
`models.storage.query(User).filter_by(email=email).first()`

## Usage
The _huricane-event-backend_ provides a RESTful API for managing events and related data on the events app.
Some API endpoints include:
* `/api/v1/events/:event_id/comments` (`POST`) - Add new comments to the event with `event_id`.
* `api/v1/:event_id/comments` (`GET`) - Gets all comments of an event with id `event_id`.
* `api/v1/comments/:comment_id/images` (`POST`) - Adds an image to a comment with id `comment_id`.
* `api/v1/comments/:comment_id/images` (`GET`) - Gets an image of the comment with `comment_id`.
* `api/v1/events` (`POST`) - Creates a new event
* `api/v1/events` (`GET`) - Gets all events available
* `api/v1/events/:event_id` (`GET`) - Gets the event with id `event_id`
* `api/v1/events/:event_id` (`PUT`) - Updates the event with id `event_id`
* `api/v1/events/:event_id` (`DELETE`) - Deletes the event with id `event_id`
* `api/v1/events/:user_id/events` - (`GET`) - Gets all events the user with id `user_id` is interested in
* `api/v1/groups` (`POST`) - Creates a new group
* `api/v1/groups/:group_id` (`GET`) - Gets the group with id `group_id`
* `api/v1/groups/:group_id` (`PUT`) - Updates the group with the id `group_id`
* `api/v1/groups/:group_id` (`DELETE`) - Deletes the group with the id `group_id`
* `api/v1/groups/:group_id/members/:user_id` (`POST`) - Adds user with id `user_id` to the group with id `group_id`
*  `api/v1/groups/:group_id/members/:user_id` (`DELETE`) - Removes user with id `user_id` from the group with id `group_id`
#### User 
* `api/vi/auth` - (`POST`) - Authenticates a user
* `api/v1/users/:user_id` (`GET`) - Gets profile of user with id `user_id`
* `api/v1/users/:user_id` (`PUT`) - Updates profile of user with id `user_id`.
* `api/v1//users/:user_id/interests/:event_id` - Adds the event with id `event_id` to user with id `user_id` interests
* `api/v1//users/:user_id/interests/:event_id` - Removes the event with id `event_id` from user with id `user_id` interests
```angular2html

```
For a detailed documentation on this API, please refer to [DOCUMENTATION.md](DOCUMENTATION.md).

## Contributing
Contributions to the Hurricane Event Backend are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Before contributing, please make sure to review the [contribution guidelines.]().

**And ensure you read the [file structure](BACKEND_DEVS.md).**

# Contact
For any inquiries or questions, please contact the team leads:

* Poject Team Lead Name here
  * Email: team.lead@example.com
  * GitHub: @Project_team_lead

* Backend Team Lead Name here
  * Email: team.lead@example.com
  * GitHub: @Project_backend_team_lead
