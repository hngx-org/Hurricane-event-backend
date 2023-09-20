from flask import Flask, request, redirect, url_for
import jwt

app = Flask(__name__)

# This secret key should be kept secret and should match the one used for JWT encoding.
SECRET_KEY = 'your_secret_key'

# Simulated database to store logged-in users and their tokens (in-memory for simplicity).
# In a real application, you'd use a proper database.
logged_in_users = {}

@app.route('/api/logout', methods=['POST'])
def logout():
    # Get the JWT token from the request headers.
    token = request.headers.get('Authorization')

    if not token:
        return 'No token provided', 401

    # Verify the token to ensure it's valid.
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return 'Expired Token', 401
    except jwt.DecodeError:
        return 'Invalid token', 401

    # Check if the user is logged in.
    user_id = payload.get('user_id')
    if user_id in logged_in_users:
        # Remove the user from the logged-in users list (logout).
        del logged_in_users[user_id]

    # Redirect the user to the login page after logging out.
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET'])
def login_page():
    # You can render your login page here.
    return 'This is the login page'

if __name__ == '__main__':
    app.run(debug=True)