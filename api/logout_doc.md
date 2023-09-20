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
logout_url = 'http://localhost:5000/api/logout'

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
