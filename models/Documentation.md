### Documentation for models

This is a documentation to use the models package
---

#### Creating an object (column)

To create a new entry to the database, you should:

- Import the Model
```python
# To create a User
from models.user import User

# To create a Comment
from models.comment import Comment

# To create an Event
from models.event import Event

# To create a Group
from models.group import Group

# To create an Image
from models.image import Image
```

- Create an instance of the Model and save it.
```python
# To create a User
user = User(name="", email="", access_token="", refresh_token="", avatar="")

user.save()

# To create a Comment
comment = Comment(body="", user_id="", event_id="")

comment.save()

# To create an Event
event = Event(title="", description="", location="", start_date="", end_date="", start_time="", end_time="", thumnail="", creator_id="")

event.save()

# To create a Group
group = Group(title="")

group.save()

# To create an Image
image = Image(image_url="", comment_id="")

image.save()
```
---

### Querying the Database
To get data from the database, you should access the global `storage` object.
```python
import models
models.storage
```

- Get all objects of all Models
To get all objects stored in the database, use the `storage.all()` method
```python
all_objects = models.storage.all()
```
This returns a list of all the objects in the session
```
[<User at 232xxx>, <Group at 232xxx>, <Comment at 121xxx>, ...]
```

- Get all objects of a particular Model
To get the objects of a single model eg `User`, use the `storage.all()` method
```python
# Using the Class
from models.user import User
...
users = models.storage.all(User)

# Using a string (recommended)
users = models.storage.all("User")
```
this returns a list of the users in the session
```
[<User at 232xxx>, <User at 989xxx>, ...]
```

- Get an object by ID
To get a particular object eg `User`, use the `storage.get()` method
```python
# Using the Class
from models.user import User
...
user = models.storage.get(User, id="")

# Using a string (recommended)
user = models.storage.get("User", id="")
```
This returns a single object
```
>>> print(user)
<User at 232xxx>
```

### Deleting from the Database
To delete from the database, there are two method:
- Delete using the `storage` object
    ```python
    import models
    ...
    user_id = ""
    models.storage.delete("User", id=user_id)
    ```
- Delete using the object instance
    ```python
    import models
    ...
    user = models.storage.get("User", id="")
    user.delete()
    ```

### Updating the Model
To update the instance (column), use the `update` method and pass key-value pairs (or unpack a dictionary)
```python
from models.user import User
...
user = User(name="", email="", access_token="", refresh_token="", avatar="")

user.save()

# To modify using key-value
user.update(name="", email="")

# To modify using dictionary
user.update(**{"name": "", "email": ""})

```

*Note:* When passing class strings to the methods, ensure that it starts with a capital letter and follows the format of the class.
Example:
- "User" for User or "RandomClass" for RandomClass is correct
- "user" for User or "randomclass" for RandomClass is incorrect
---

Written by [Ifechukwu001](https://github.com/Ifechukwu001)