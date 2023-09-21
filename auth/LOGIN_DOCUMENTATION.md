
# Authentication Routes Documentation


This documentation provides an overview of the login authentication routes implemented in the Flask application.

## Introduction

The code provided defines authentication routes using Flask, OAuth2 for Google authentication, and JWT (JSON Web Tokens) for user authentication. These routes allow users to sign in using their Google accounts and handle user authentication.

## Prerequisites

Before using these authentication routes, make sure to set the following environment variables:

- `client_id`: The client ID obtained from Google.
- `client_secret`: The client secret obtained from Google.

## Route Overview

### Signin (`/users/login` - GET)

- **Description**: Initiates the Google OAuth2 authentication process.
- **Endpoint**: `/users/login`
- **Method**: GET
- **Returns**: Redirects the user to the Google authentication page.

### Callback (`/users/login/callback` - GET)

- **Description**: Handles the callback from Google after successful authentication.
- **Endpoint**: `/users/login/callback`
- **Method**: GET
- **Returns**: User information (email) in JSON format, along with a URL for POST login.


### Login (`/users/login` - POST)

- **Description**: Handles user login. Checks if the email already exists in the database, and creates an access token.
- **Endpoint**: `/users/login`
- **Method**: POST
- **request body(JSON)**:
  - `email`: User's email address.

  `{
    "email": "user@example.com",
   }`
 

- **Response**: User information (access token, name, email) in JSON format. If a user exist, returns a 200 status code.
    * **if user exists**:
        * **status code**: 200
      
        ``` 
      {
            "email": "user@example.com",
            "access_token": 'token',
            "name": "name of user",
            "response": "Logged in successfully"
        }
    * **else**:
        * **status code**: 307
      
        ```
      {
            "redirect_url": '/users/signup",
            "error": "user should be redirected"
        }

# Logout Endpoint Documentation

## Introduction

The `users/logout` endpoint in this Flask application allows authenticated users to log out by ending their session. This documentation provides an overview of how to use the endpoint.

## Endpoint Details

- **Endpoint:** `users/logout`
- **Method:** POST
- **Authentication Required:** Yes (Requires a valid access token)
- **Response:** JSON response indicating a successful logout.

## Usage

To log out a user, follow these steps:

1. Ensure you have a valid access token.
   - You should include the access token in the `Authorization` header of your POST request.

2. Send a POST request to the `users/logout` endpoint.

   ```http
   POST /logout
   Host: your-api-host.com
   Authorization: your-access-token

## Middleware

### Token Required

- Description: Decorator function for protecting routes that require authentication.
- Function: `token_required(func)`
- Usage: Apply this decorator to any route function that should only be accessible to authenticated users. It checks for the presence and validity of an access token.
  `GET /some-protected-route
headers={Authorization: your_access_token_here}
`
## Usage

To use these authentication routes, follow these steps:

1. Set the `client_id` and `client_secret` environment variables.
2. Initialize the Flask app and register the `auth` blueprint.
3. Apply the `token_required` decorator to any route that requires authentication.
4. Use the `/users/login` route to initiate the authentication process.

## Error Responses

The `token_required` decorator provides error responses in case of various token-related issues:

### Missing Access Token

- **Error:** `access_token is missing`
- **Status Code:** 401 (Unauthorized)
- **Response:**

  ```json
  {
      "error": "access_token is missing",
      "redirect_url": "URL for the login page"
  }

### Invalid Access Token
- **Error:** `invalid access_token`
- **Status Code:** 401 (Unauthorized)
- **Response:**

  ```json
  {
      "error": "invalid access_token",
      "redirect_url": "URL for the login page"
  }


### Expired token
- **Error:** `token has expired`
- **Status Code:** 401 (Unauthorized)
- **Response:**

  ```json
  {
      "error": "token has expired",
      "redirect_url": "URL for the login page"
  }
