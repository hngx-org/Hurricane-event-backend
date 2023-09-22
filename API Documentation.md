# API DOCUMENTATION
This file contains the documentation for `Team Hurricane event App Backend API`
## 3. User Authentication API
This API allows you to manage user's authentication, login and update to users details, including events interests users develop

### Base URL
The base URL for all the endpoints in this is:

### Endpoints


1. ***Create a new User**
* **URL** `/auth`
* **Method:** This endpoint is used to authenticate an old user or register a new user.
* **Request Body:**
  *  **email**: The user's email address
  *  **name:** The user's name
  *  **avatar:** The user'sprofile pic

* **Reponse:**:
   * **Status code**: 201 (Created)
   * **Body** This endpoint returns the JSON representation of ``user_id` on success or a message `No email found` or `No name found` and returns a `412 status code`

**Sample usage**
    curl -X POST -d '({"name": "Jon", "email": "jonSnow@GOT.com", "avatar": "htpps://imgr.imgas234"})' "https://Hurricane-event.onrender.com/api/auth"

    - Response

    {
        "user_id": "1913e2847-39c4-4e34-905a-a23dca11b922"
    }

2. **Get a user profile**
* **URL:** `/users/<user_id>`
* **Method:** GET
* **Description:** This endpoint gets a user's profile from the database.
* **Request Body:**
  * **user_id(string, required):** This is the user_id used to identify the user

* **Reponse:**
* * **Status Code:** 200
* * **Body** This endpoint returns the user's dictionary if found details on success and a message `User  ID does not exist`

**sample usage**
    curl "https:hurricane-event.onrender.com/api/users/913e2847-39c4-4e34-905a-a23dca11b922"

    -Responnse

    {
        "message": User ID does not exist
    }

**PUT** `/api/users/<user_id>` : This endpoint updates a user'sdetails 
**params**
    user_id : This is the user_id used to identfy the user

**Returns**: It returns `Update was succesful` on success or a message `Uchanged` if the new details are not supplied or `User ID does not exist` if user is not found

**sample usage**
    curl -X PUT -d '{"name": "Tirion", "email": "TirionLannister@got.com"}' "https:hurricane-event.onrender.com/api/users/913e2847-39c4-4e34-905a-a23dca11b922"

    -Responnse

    {
        "message": Update was successful
    }
    
**POST** `/api/users/<user_id>/interests/<event_id>` : This endpoint adds an event to a users list of events if the users shows interests in it
**params**
    user_id : This is the user who express interest
    event_id : This is the i of the event the users express interest in

**Returns**: The endpoint return a a message `success` if the event has been added to their list of events or `Unvalid User ID` if the user ID is not correct or `Invalid Event ID` if the event ID is invalid

**sample usage**
    curl -X POST "url/users/913es9q8783-2947-uew-234c-239848193/interests/90234-24y2-7s32-29847f24u3"

    - Response
    {
        "message": "success"
    }

**DELETE** `/api/users/<user_id>/interests/<event_id>` : This endpoint removes an event from a users list of events if the users shows dis-interests in it
**params**
    user_id : This is the user who express dis-interest
    event_id : This is the id of the event the users express idis-interest in

**Returns**: The endpoint return a a message `success` if the event has been removed from their list of events or `Unvalid User ID` if the user ID is not correct or `Invalid Event ID` if the event ID is invalid

**sample usage**
    curl -X DELETE "url/users/913es9q8783-2947-uew-234c-239848193/interests/90234-24y2-7s32-29847f24u3"

    - Response
    {
        "message": "success"
    }

**POST** `/api/events/<event_id>/comments` : This endpoint adds a comment to an event
**params**
    event_id : The event onto which the comment is added
    body : The body of the comment which is the message
    user_id : the user who adds the comment
    image : The image which is optional and can be added to comments

**Returns** : Returns `Invalid Event ID` and a status code of 404 if the ID of the event is not correct otherwise adds the comment and returns `success` and a status code of 201 or `Incomplete comment details` if the details are not complete and a status code of 412.

**sample usage**
    curl -X POST -d '{"body": "You know nothing, Jon Snow", "user_id": "Y130385403g-r374-i45t-t224e03958"}' "url/events/913es9q8783-2947-uew-234c-239848193/comments"

    - Response
    {
        "message": "success"
    }

**GET** `/api/events/<event_id>/comments` : This endpoint get the details of a comment
**params**
    event_id : Gets all comments in an event

**Returns** : Returns all the comments in an event or a message `Invalid Event ID` if the event id is incorrect and a status code of 404

**sample usage**
    curl "url/events/913es9q8783-2947-uew-234c-239848193/comments"

    -Response
    {
        "body": "You know nothing, Jon snow",
        "user_id" : "913es9q8783-2947-uew-234c-239848193"
        ...
    }
**POST** `api/comments/<comment_id/images` :This endpoint adds a comment image
**params**
    comment_id: The comment to which the image is to be added
    image: the image to add

**Returns**: It returns `success` if the image can be added or `image url not passed` if there is no url for the image and a status code of 412, or `Invalid comment ID` and a status code of 404

**sample usage**
    curl -X POST -d '{"image: :img url"} "url/comments/913es9q8783-2947-uew-234c-239848193/images

    -Response

    {
        "message": "success"
    }

**GET** `api/comments/<comment_id/images` :This endpoint gets a comment image
**params**
    comment_id: The comment to which the image is to be recovered

**Returns**: It returns `the comment_id nd image url` on success, or `Invalid comment ID` and a status code of 404

**sample usage**
    curl -X POST -d '{"image: :img url"} "url/comments/913es9q8783-2947-uew-234c-239848193/images

    -Response

    {
        "image_url": "img_url.com",
        "comment_id": "13es9q8783-2947-uew-234c-239848193"
    }