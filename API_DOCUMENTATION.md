# API Documentation

## 1. Event Management API
This API allows you to manage events, including creating, retrieving, updating, and deleting events. It also provides functionality to get the list of events a user is interested in.

### Base URL
The base URL for all API endpoints is: 

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
        * **creator_id (integer):** The ID of the event creator.
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
      * **id (integer):** The ID of the event.
      * **title (string):** The title of the event.
      * **description (string):** A description of the event.
      * **start_date (string):** The start date of the event.
      * **creator_id (integer):** The ID of the event creator.

3. **Get an Event**
* **URL:** `/events/<event_id> `
* **Method:** GET.
* **Description:** Retrieves information about a specific event.
* **Path Parameter:** `event_id (integer)`: The ID of the event to retrieve.
  * **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** An object representing the event with the following properties:
    * **id (integer):** The ID of the event.
    * **title (string):** The title of the event.
    * **description (string):** A description of the event.
    * **start_date (string):** The start date of the event
    * **end_date (string):** The end date of the event 
    * **start_time (string):** The start time of the event
    * **end_time (string):** The end time of the event
    * **location (string):** The location of the event.
    * **creator_id (integer):** The ID of the event creator.
    * **thumbnail (string):** URL or path to the event thumbnail image.

4. **Update an Event**

* **URL:** `/events/<event_id>  `
* **Method:** PUT
* **Description:** Updates information about a specific event.
* **Path Parameter:** event_id (integer): The ID of the event to update.
* **Request Body:** (same fields as in event creation)
* **Response:**
  * **Status Code:** 202 (Accepted)
  * **Body:** `{"message": "success"}` if the event is updated successfully.

5. **Delete an Event**
* **URL:** `/events/<event_id>`
* **Method:** DELETE
* **Description:** Deletes a specific event.
* **Path Parameter:** `event_id (integer)`: The ID of the event to delete.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** `{"message": "success"}` if the event is deleted successfully.
  * **Status Code:** 404 (Not Found)
  * **Body:** `{"message": "Resource UID not found"}`if the event with the specified ID is not found.


6. **Get Interested Events for a User**
* **URL:** `/events/<user_id>/events `
* **Method:** GET
* **Description:** Retrieves a list of events that a specific user is interested in.
* **Path Parameter:** `user_id (integer)`: The ID of the user.
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
    * **id (integer):** The ID of the group.
    * **title (string):** The title of the group.
    * **image (string):** URL or path to the group image.



2. **Get a Group**
* **URL:** `/groups/<group_id> `
* **Method:** GET
* **Description:** Retrieves information about a specific group.
* **Path Parameter:** `group_id (integer)`: The ID of the group to retrieve.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** The JSON representation of the group, including the following properties:
      * **id (integer):** The ID of the group.
      * **title (string):** The title of the group.
      * **image (string):** URL or path to the group image.

3. **Update a Group**
* **URL:** `/groups/<group_id>`
* **Method:** PUT
* **Description:** Updates information about a specific group.
* **Path Parameter:** `group_id (integer)`: The ID of the group to update.
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
* **Path Parameter:** `group_id (integer)`: The ID of the group to delete.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** `{"message": "success"}` if the group is deleted successfully.

5. **Add User to a Group**
* **URL:** `/groups/<group_id>/members/<user_id> `
* **Method:** POST
* **Description:** Adds a user to a group.
* **Path Parameters:** 
  * `group_id (integer)`: The ID of the group.
  * `user_id (integer)`: The ID of the user to add.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** `{"message": "success"}` if the user is added to the group successfully.

6. **Remove User from a Group**
* **URL:** `/groups/<group_id>/members/<user_id> `
* **Method:** DELETE
* **Description:** Removes a user from a group.
* **Path Parameters:**
  * `group_id (integer):` The ID of the group.
  * `user_id (integer): `The ID of the user to remove.
* **Response:**
  * **Status Code:** 200 (OK)
  * **Body:** `{"message": "success"}` if the user is removed from the group successfully.

