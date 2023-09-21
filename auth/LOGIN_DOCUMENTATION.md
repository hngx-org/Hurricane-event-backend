
# Authentication Routes Documentation


This documentation provides an overview of the login authentication routes implemented in the Flask application.

## Introduction
The code verifies the user's existence in the database and retrieves their information; in the absence of an existing user, it initiates the creation of a new user.

## Route Overview

### Signin (`/users/login` - POST)

- **Description**: Checks if the User exist and also creates new user if it does not exist in the database.
- **Endpoint**: `/users/login`
- **Method**: POST
- **Request body**: 
  ```json
  {
      "payload": "user data gotten from google auth"
  }
- **Returns**: and returns User details.

  ```json
  {
      "user_id": "user id",
      "name": "user name",
      "email": "user email",
      "avatar": "user picture"
  }
