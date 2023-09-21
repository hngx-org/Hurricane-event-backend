
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

- Description: Initiates the Google OAuth2 authentication process.
- Endpoint: `/users/login`
- Method: GET
- Returns: Redirects the user to the Google authentication page.

### Callback (`/users/login/callback` - GET)

- Description: Handles the callback from Google after successful authentication.
- Endpoint: `/users/login/callback`
- Method: GET
- Returns: User information (email) in JSON format, along with a URL for POST login.

### Login (`/users/login` - POST)

- Description: Handles user login. Checks if the email already exists in the database, and creates an access token.
- Endpoint: `/users/login`
- Method: POST
- request body(JSON):
  - `email`: User's email address.
  - `name`: User's name.
  - `picture`: URL of the user's profile picture.
- Returns: User information (access token, name, email) in JSON format. If a new user is created, returns a 201 status code.

## Middleware

### Token Required

- Description: Decorator function for protecting routes that require authentication.
- Function: `token_required(func)`
- Usage: Apply this decorator to any route function that should only be accessible to authenticated users. It checks for the presence and validity of an access token.
  `GET /some-protected-route
headers={Access_token: your_access_token_here}
`
## Usage

To use these authentication routes, follow these steps:

1. Set the `client_id` and `client_secret` environment variables.
2. Initialize the Flask app and register the `auth` blueprint.
3. Apply the `token_required` decorator to any route that requires authentication.
4. Use the `/users/login` route to initiate the authentication process.

Example usage can be found in the provided code.



### LOG-OUT DOCUMENTATION

User Logout Endpoint Documentation
Description
The /api/logout endpoint is used to log a user out of their session by invalidating the JWT (JSON Web Token) token provided in the request header. This action effectively revokes the user's access to protected resources until they log in again.

Endpoint URL

POST /api/logout

Request Format

Headers
Authorization (Required): Include a valid JWT token(JSON web token) as a Bearer token in the Authorization header.

Responses
Success Response (HTTP Status 302 - Redirect)
Status Code: 302
Response Body: None
Description: If the provided JWT token(JSON web token) is valid and associated with a logged-in user, they will be logged out. The endpoint will then redirect the user to the login page specified by the login_page route.

Error Responses
Status Code: 401
Response Body: A text message indicating the reason for the error.
Description:
No token provided: If the Authorization header is missing from the request.
Token has expired: If the provided JWT token has expired.
Invalid token: If the provided JWT token is invalid, such as having an incorrect signature.

Example Usage

import requests

# Define the URL of the logout endpoint
logout_url = 'http://localhost:5000/auth/logout'

# Provide a valid JWT token in the Authorization header
headers = {'Authorization': 'Bearer YOUR_VALID_JWT_TOKEN'}

# Send a POST request to log the user out
response = requests.post(logout_url, headers=headers)

# Check the response status code
if response.status_code == 302:
    print('Logout successful. User is redirected to the login page.')
else:
    print(f'Logout failed. Error message: {response.text}')

    security

    Keep the SECRET_KEY used for JWT token encoding secret and secure. It should never be exposed or shared publicly.

    Author: Idris Adebayo
    email: adebayoidris051@gmail.com.
   github: Ade3164
