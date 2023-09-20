# Approved file structure.

* All API calls will be written in the API folder.

* All models should be in seperate files under the models folder (This has been completed)

* The db_connection folder is where we'll connect to the db from. so if you need the db in your implementation just import db from db_connection.

* The settimgs folder contains the config files and other requirements for the backend.

* All authentication should be done in the auth folder.
* All input data are in **JSON** Format
* ALWAYS PERFORM A PULL BEFORE A PR



  You can write different file for each api call, it'll be combined into one file during pull requests.
  
  Note, only create a new file if the required file is not present during the most Recent pull.

  That is, if you're working on EVENTS related endpoints, there should be **only one file to house all API calls, do not for whatever reason touch a tasks not assigned to you until request for help is asked or approval is given**.

  This is to save merge conflicts
  
  If your file structure do not follow this procedure, you task will not be accepted nor merged.

    you can write different file for each api call, it'll be combined into one file during pull requests.
    Note, only create a new file if the required file is not present during the most Recent pull.
    If you file structure do not follow this procedure, you work will not be accepted nor merged.