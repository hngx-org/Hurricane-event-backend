## This are the changes affected with this pull request.
1. Added a .json() method to comment and group to aid serialization, other classes will come up in subsequent changes.
2. Deleted  `api/logout.py`, and merged it with login in the `auth/routes.py`.
3. Updated the BBACKEND_DEVs.md file, kindly go thorugh it.
4. Added [documentation_groups](group/documentation_groups.md) and [documentation_events](events/documentation_events.md) for their respective endpoints
5. Registered a blueprint for [groups](app.py), [events](app.py), [auth](app.py) in the [app.py](app.py) File. This way we can all focus on writing only endpoints and not always initializing the flask app on our file.
6. Added `flask-user` to the requirement.txt file, flask-user has a dependency auth-lib, that is needed for google authentication of users.
7. Deleted User-Groups and merged it with [group/routes.py](group/routes.py)
8. Added a method getUser in the [database](models/engine/database.py) to enable checking of user's credentials on the database by using email.
P.S: Can't think of a better less stressful to implement that, if you have an idea on how to do that, create an issue
9. [Login_documentation](auth/LOGIN_DOCUMENTATION.md) and [logout_documentation](auth/LOGIN_DOCUMENTATION.md) where also merged, reviews of their contents will be done shortly.
10. The [api](api) directory is to be left bare till further notice, make use of the given packages for your endpoints.
11. DB session is in `models/engine/database.py`, not `db_connection/connection.py`
12. If you need access to query please read the [DB_documentation](models/Documentation.md) on how to achieve that, don't write ~models.storage.session.query~
13. I also made a change to the __init__ of [database](models/engine/database.py) to create a sqlite db named `sampleEVENTAPP.db`. Help is need to populate it with testing data, pending when we go live. so we can test our endpoints.
14. All endpoints on users can be in the `auth/routes.py` 
15. All endpoints on things groups in `group/routes.py`
16. All endpoints on things evens in `events/routes.py`


## The following are the list of endpoint we have

1. [Login/Create_user](auth/routes.py): Signup is strictly done by google auth, the payload data's received will be used to login. and subsequesnt logins are operated on by the endpoint.
2. [Logout](auth/routes.py): Signout/Logout endpoint is also available albeit they may be discrepancies due to how the session login token was stored and how they are retrieed by the team working on logout, this discrepancies will be meddled out ASAP.
3. [callback](auth/routes.py): Part o the signup package
4. [Get_comments_on_an_event](events/routes.py): Gets the comments made on a specific event
5. [create_group](group/routes.py): Creates a new group
6. [Update_group](group/routes.py): Updates a group name
7. [Get_users_group](group/routes.py): Gets the groups a specific user is at


## Issues already assigned and not done

1. Add like to a comment
2. Update user details
3. Get user details
4. Delete group from user groups
5. Add images to a comment
6. Add a comment to an event
7. Add a user to an  event
8. Delete an event
9. Add an event to a specific group
10. Get all events in the db
11. Add a user to a specific group
12. Remove a user from a specific group
and many more... go to the issues, pick an issue, first to make a valid PR will be the first to get merged.

* if i make a comment on your PR please kindly resolve it as soon as possible

## The PR available at this time are 10, i'll start looking at them now, and give you feedback.
### Ensure your code/file from now follow this format to make things easy for us all.
