# Approved file structure.

* All API calls will be written in their respective API folder.

  for API calls that deals with events it's in the events/routes.py
  
  Calls that deals with groups are in group/routes.py

* All models should be in seperate files under the models folder (This has been completed).

* The models.engine folder is where we'll connect to the db from. So if you need the db in your implementation, just ```import models```

then whenever you need it for get, get all, delete, new, save call ```models.storage.get()....``` 

Read the documentation of the (models.storage)[models/Documentation.md]

* The settings folder contains the config files and other requirements for the backend.

* All authentication should be done in the auth folder.
* All input data are in **JSON** Format
* **ALWAYS PERFORM A PULL BEFORE A PR**
* Do not initialize your own flask app.
  
  Note, only create a new file if the required file is not present during the most recent pull.

  That is, if you're working on EVENTS-related endpoints, your endpoints must be in the events/routes.py file.

  There should be **only one file to house all API calls, do not for whatever reason touch a task not assigned to you until request for help is made or approval is given**.

  This is to prevent merge conflicts.
  
<<<<<<< HEAD
  If your file structure do not follow this procedure, you task will not be accepted nor merged.

    you can write different file for each api call, it'll be combined into one file during pull requests.
    Note, only create a new file if the required file is not present during the most Recent pull.
    If you file structure do not follow this procedure, you work will not be accepted nor merged.
=======
  If your file structure does not follow this procedure, your task will not be accepted nor merged.
>>>>>>> upstream/dev
