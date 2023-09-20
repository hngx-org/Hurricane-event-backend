
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

