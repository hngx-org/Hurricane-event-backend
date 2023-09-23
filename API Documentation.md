# API DOCUMENTATION
This file contains the documentation for `Team Hurricane event App Backend API`

## 1. Event Management API
This API allows you to manage events, including creating, retrieving, updating, and deleting events. It also provides functionality to get the list of events a user is interested in.

### Base URL
The base URL for all API endpoints is:

**`https://hurricane-event.onrender.com/api`**

### Endpoints

1. **Create an Event**

  * **URL:** `/events `
  * **Method:** POST
   * **Description:** Creates a new event.
   * **Request Body:**
  
        * **title (string, required):** The title of the event.
        * **description (string):** A description of the event.
        * **location (string):** The location of the event.
        * **start_date (string)**: The start date of the event 
        * **end_date (string):** The end date of the event 
        * **start_time (string):** The start time of the event
        * **end_time (string):** The end time of the event 
        * **creator_id (string):** The ID of the event creator.
        * **thumbnail (string):** URL or path to the event thumbnail image.
      * **Response:**
        * **Status Code:** 201 (Created)
        * **Body:** 
        `{"message": "success"}`
         if the event is created successfully.

2. **Get All Events**

  * **URL:** `/events`
  * **Method:** GET
  * **Description:** Retrieves a list of all events.
  * **Response:**
    * **Status Code:** 200 (OK)
    * **Body:** An array of event objects, each containing the following properties:
      * **id (string):** The ID of the event.
      * **title (string):** The title of the event.
      * **description (string):** A description of the event.
      * **start_date (string):** The start date of the event.
      * **creator_id (string):** The ID of the event creator.

3. **Get an Event**
* **URL:** `/events/<event_id> `
* **Method:** GET.
* **Description:** Retrieves information about a specific event.
* **Path Parameter:** `event_id (string)`: The ID of the event to retrieve.
  * **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** An object representing the event with the following properties:
    * **id (string):** The ID of the event.
    * **title (string):** The title of the event.
    * **description (string):** A description of the event.
    * **start_date (string):** The start date of the event
    * **end_date (string):** The end date of the event 
    * **start_time (string):** The start time of the event
    * **end_time (string):** The end time of the event
    * **location (string):** The location of the event.
    * **creator_id (string):** The ID of the event creator.
    * **thumbnail (string):** URL or path to the event thumbnail image.

4. **Update an Event**

* **URL:** `/events/<event_id>  `
* **Method:** PUT
* **Description:** Updates information about a specific event.
* **Path Parameter:** event_id (string): The ID of the event to update.
* **Request Body:** (same fields as in event creation)
* **Response:**
  * **Status Code:** 202 (Accepted)
  * **Body:** `{"message": "success"}` if the event is updated successfully.

5. **Delete an Event**
* **URL:** `/events/<event_id>`
* **Method:** DELETE
* **Description:** Deletes a specific event.
* **Path Parameter:** `event_id (string)`: The ID of the event to delete.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** `{"message": "success"}` if the event is deleted successfully.
  * **Status Code:** 404 (Not Found)
  * **Body:** `{"message": "Resource UID not found"}`if the event with the specified ID is not found.


6. **Get Interested Events for a User**
* **URL:** `/events/<user_id>/events `
* **Method:** GET
* **Description:** Retrieves a list of events that a specific user is interested in.
* **Path Parameter:** `user_id (string)`: The ID of the user.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** An object containing the following properties:
    * **user (string):** The name of the user.
    * **events (array):** An array of event objects that the user is interested in. Each event object has the same properties as described in the "Get an Event" endpoint.



## 2. Group Management API
This API allows you to manage groups, including creating, retrieving, updating, and deleting groups. It also provides functionality to add or remove users from a group.

### Base URL
The base URL for all API endpoints is:

### Endpoints

1. **Create a Group**
* **URL:** `/groups`
* **Method:** POST
* **Description:** Creates a new group.
* **Request Body:**
  * **title (string, required):** The title of the group.
  * **image (string):** URL or path to the group image.
* **Response:**
  * **Status Code**: 201 (Created)
  * **Body:** The JSON representation of the created group, including the following properties:
    * **id (string):** The ID of the group.
    * **title (string):** The title of the group.
    * **image (string):** URL or path to the group image.



2. **Get a Group**
* **URL:** `/groups/<group_id> `
* **Method:** GET
* **Description:** Retrieves information about a specific group.
* **Path Parameter:** `group_id (string)`: The ID of the group to retrieve.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** The JSON representation of the group, including the following properties:
      * **id (string):** The ID of the group.
      * **title (string):** The title of the group.
      * **image (string):** URL or path to the group image.

3. **Update a Group**
* **URL:** `/groups/<group_id>`
* **Method:** PUT
* **Description:** Updates information about a specific group.
* **Path Parameter:** `group_id (string)`: The ID of the group to update.
* **Request Body:**
  * **title (string):** The updated title of the group.
  * **image (string):** The updated URL or path to the group image.
* **Response:**
  * **Status Code:** 202 (Accepted)
  * **Body:** `{"message": "success"}` if the group is updated successfully.

4. **Delete a Group**
* **URL:** `/groups/<group_id> `
* **Method:** DELETE
* **Description:** Deletes a specific group.
* **Path Parameter:** `group_id (string)`: The ID of the group to delete.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** `{"message": "success"}` if the group is deleted successfully.

5. **Add User to a Group**
* **URL:** `/groups/<group_id>/members/<user_id> `
* **Method:** POST
* **Description:** Adds a user to a group.
* **Path Parameters:** 
  * `group_id (string)`: The ID of the group.
  * `user_id (string)`: The ID of the user to add.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** `{"message": "success"}` if the user is added to the group successfully.

6. **Remove User from a Group**
* **URL:** `/groups/<group_id>/members/<user_id> `
* **Method:** DELETE
* **Description:** Removes a user from a group.
* **Path Parameters:**
  * `group_id (string):` The ID of the group.
  * `user_id (string): `The ID of the user to remove.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** `{"message": "success"}` if the user is removed from the group successfully.


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

* **Sample usage**

    ```curl -X POST -d '({"name": "Jon", "email": "jonSnow@GOT.com", "avatar": "htpps://imgr.imgas234"})' "https://Hurricane-event.onrender.com/api/auth"```

    - Response
    ```json
    {
        "user_id": "1913e2847-39c4-4e34-905a-a23dca11b922"
    }
    ```

2. **Get a user profile**
* **URL:** `/users/<user_id>`
* **Method:** GET
* **Description:** This endpoint gets a user's profile from the database.
* **Request Body:**
  * **user_id(string, required):** This is the user_id used to identify the user

* **Reponse:**
* * **Status Code:** 200
* * **Body** This endpoint returns the JSON representation of the user's details if found with the following properties:
* **On success**
    * **id (string):** The id of the user
    * **Email (string):** The user's email
    * **Avatar (string):** The string url to the user's avatar
    * **Name (string):** The user's name details
   * **On Failure**
    * **message (string):** `User  ID does not exist`

* **sample usage**

    ```curl "https:hurricane-event.onrender.com/api/users/913e2847-39c4-4e34-905a-a23dca11b922"```

    - Response
    ```json
    {
        "message": "User ID does not exist"
    }
    ```

3. **Update a user's info**
* **URL:** `/users/<user_id>`
* **Method:** PUT
* **Description** This endpoint updates a user's details 
* **Request Body**
  * **user_id (string, required):** This is the user_id used to identfy the user
  * **Name (string, optional)** The name of to update with
  * **Avatar (string, optional):** The avatar to upate with
  * **Email (string, optional):** Th mail to replace with
* **Response**
  * **On success**
    * **Status Code** 202 (updated)
        * **message** Update was successful
  * **On failure**
    * **Status Code** 200 (Unchanged), 404 (Not Found)
    * **message** : Unchanged, User ID does not exist

* **sample usage**

    ```curl -X PUT -d '{"name": "Tirion", "email": "TirionLannister@got.com"}' "https:hurricane-event.onrender.com/api/users/913e2847-39c4-4e34-905a-a23dca11b922"``` 

    -Response
    ```json
    {
        "message": "Update was successful"
    }
    ```


4. **Adds an event to users event**
* **URL** `/users/<user_id>/interests/<event_id>``
* **Method** POST
* **Description** 
* **path_parameters** `user_id`, `event_id`
* **Request Body**
* **Response**
    * **On success**
        * **Status code:** 200
        * **message:** `success`
    * **On failure**
        * **Status Code:** 404
        * **Message:** `Invalid User ID`, `Invaalid Event ID`

* **sample usage**

    ```curl -X POST "url/users/913es9q8783-2947-uew-234c-239848193/interests/90234-24y2-7s32-29847f24u3"```


    - Response
    ```json
    {
        "message": "success"
    }
    ```

4. **Removes an event from users event**
* **URL** `/users/<user_id>/interests/<event_id>``
* **Method** DELETE
* **Description** 
* **path_parameters** `user_id`, `event_id`
* **Request Body**
* **Response**
    * **On success**
        * **Status code:** 200
        * **message:** `success`
    * **On failure**
        * **Status Code:** 404
        * **Message:** `Invalid User ID`, `Invaalid Event ID`

* **sample usage**

    ```curl -X DELETE "url/users/913es9q8783-2947-uew-234c-239848193/interests/90234-24y2-7s32-29847f24u3"```

    - Response
    ```json
    {
        "message": "success"
    }
    ```


5. **Add a comment to an event**
* **URL:** `/events/<event_id>/comments`
* **Method:** POST
* **Description:** Adds a comment to an event 
* **Request Body:**
  * **Body (string, required):** The main message of the comment
  * **image (string):** URL or path to the comment image.
  * **event_id:** The event ID of which the comment is to be added
  * **user_id:** The user id of the user that adds the comment

* **Response:**
    * **On success**
        * **Status Code**: 201 (Created)
        * **Message:** `Success`
    * **On Failure**
        * **Status Code:** 404 (Not found), 412(Not Complete)
        * **Message:** `Invalid Event ID`, `Incomplete comment details`

* **sample usage**

    ```curl -X POST -d '{"body": "You know nothing, Jon Snow", "user_id": "Y130385403g-r374-i45t-t224e03958"}' "url/events/913es9q8783-2947-uew-234c-239848193/comments"```

    - Response
    ```json
    {
        "message": "success"
    }
    ```

6. **Get a comments associated with an event**
* **URL:** `/events/<event_id>/comments`
* **Method:** GET
* **Description:** Gets all the comments associaated with an event
* **Path parameters:** `event ID`

* **Response:**
    * **On success**
        * **Status Code**: 201 (Created)
        * **Message:** `JSON representation of the comments 
    * **On Failure**
        * **Status Code:** 404 (Not found)
        * **Message:** `Invalid Event ID`

* **sample usage**

    ```curl "url/events/913es9q8783-2947-uew-234c-239848193/comments"```

    - Response
    ```json
    {
        "body": "You know nothing, Jon snow",
        "user_id" : "913es9q8783-2947-uew-234c-239848193"
        ...
    }
    ```

7. **Add an image to a comment**
* **URL:** `/comments/<comment_id/images`
* **Method:** POST
* **Description:** Adds an image to a comment
* **Request Body:**
  * **comment_id (string, required):** The id of the comment the image is to be added to
  * **image (string):** URL or path to the comment image.

* **Response:**
    * **On success**
        * **Status Code**: 201 (Created)
        * **Message:** `Success`
    * **On Failure**
        * **Status Code:** 404 (Not found), 412(Not Complete)
        * **Message:** `Invalid Comment ID`, `Image URL not passed`


* **sample usage**

    ```curl -X POST -d '{"image: :img url"} "url/comments/913es9q8783-2947-uew-234c-239848193/images```

    - Response

    ```json
    {
        "message": "success"
    }
    ```


8. **Gets the images of a comment**
* **URL:** `/comments/<comment_id/images`
* **Method:** GET
* **Description:** Gets the images of a comment
* **Request Body:**
  * **comment_id (string, required):** The id of the comment the image is to be gotten of

* **Response:**
    * **On success**
        * **Status Code**: 200
        * **Message:** A JSON representation showing the comment id and the images URL
    * **On Failure**
        * **Status Code:** 404 (Not found)
        * **Message:** `Invalid Comment ID`


* **sample usage**

    ```curl url/comments/913es9q8783-2947-uew-234c-239848193/images```

    - Response

    ```json
    {
        "image_url": "img_url.com",
        "comment_id": "13es9q8783-2947-uew-234c-239848193"
    }
    ```

 9. **Add a like to a comment**
* **URL:** `/<comment_id>/<user_id>/likes`
* **Method:** POST
* **Description:** Adds a like to an event
* **Path parameters:** `comment ID`, `user ID`
* **Request Body**

* **Response:**
    * **On success**
        * **Status Code**: 200 
        * **Message:** `Success`
    * **On Failure**
        * **Status Code:** 400 (Bad Request), 404 (Not Found), 500 (Internal Server Error)
        * **Message:** `User has already liked this comment`, `Comment not found`, `error description`

* **sample usage**

    ```curl -X POST \-H "Authorization: Bearer <YOUR_JWT_TOKEN>" \http://your-api-url/api/93586bjxnj568yb2e989/6504be151ab2e9ff5c476248/likes```

    - Response
    ```json
    {
        "success": True,
        "comment_id": <comment_id>,
        "likes": [<array of user_ids who have liked the comment>]
    }
    ```

10. **Removes like from a comment**
* **URL** `/<comment_id>/<user_id>/likes`
* **Method** DELETE
* **Description:** Unlikes Comment
* **path_parameters** `comment_id`, `user_id`
* **Request Body**
* **Response**
    * **On success**
        * **Status code:** 204
    * **On failure**
        * **Status Code:** 404
        * **Message:** `Comment not found`

* **sample usage**

    ```curl -X DELETE "url/api/913es9q8783-2947-uew-234c-239848193/90234-24y2-7s32-29847f24u3/likes"```

    - Response
    ```json
    {
       
    }
    ```
