
# Authentication Routes Documentation


This documentation provides an overview of the login authentication routes and signup route implemented in the Flask application.

## Introduction
The code verifies the user's existence in the database and retrieves their information; in the absence of an existing user, it initiates the creation of a new user.

## Route Overview

### Signin (`/auth/login` - POST)

- **Description**: checks if data in the token matches request body data, then returns user id and a new token
- **Endpoint**: `/users/login`
- **Method**: POST 
- **Content-Type**: application/json 
- **Authorization**: <authorization_token>
- **Request body**: 

  ```json
  {
  "email": "user@example.com",
  "name": "John Doe",
  "avatar": "https://example.com/avatar.jpg"
  }
- **Returns**: returns User details and token.

  ```json
  {
      "user_id": "user id",
      "name": "token"
  }

### Signin (`/auth/signup` - POST)

- **Description**:creates new user, then returns user id and a new token
- **Endpoint**: `/users/signup`
- **Method**: POST 
- **Content-Type**: application/json 
- **Authorization**: <authorization_token>
- **Request body**: 

  ```json
  {
  "email": "user@example.com",
  "name": "John Doe",
  "avatar": "https://example.com/avatar.jpg"
  }
- **Returns**: returns User details and token.

  ```json
  {
      "user_id": "user id",
      "name": "token"
  }
  
### Decorator: `token_required`

The `token_required` decorator is used to ensure that certain routes require a valid authorization token for access. If no token is provided, the decorator returns an error response.

### How to Use
* Send a POST request to /auth/login with valid JSON data containing an email and an authorization token in the headers.

* Send a POST request to /auth/signup with valid JSON data containing an email, name, and avatar to create a new user.