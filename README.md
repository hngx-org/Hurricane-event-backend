# hurricane-event-backend

This repository contains the backend code for the Hurricane Event project. 

## Installation
To run the _huricane-event-backend_ locally, follow these steps:

* Clone the repository and activate the virtual environment.
* Install required dependencies: `pip install -r requirements.txt`
* Setup the configuration, `config.py`
* Run the app: `flask run`

## Models
These are the models in the application
* User - Defines the User Entity
* Comment - Comments Entity
* Image - Defines the entity image added to Comments
* Event - Entity that defines the events available
* GroupEvent - Many to Many relationship of between Group and Event
* Group - Entity that defines types of group available
* InterestedEvent - Many to Many relationship between User and Event
* UserGroup - Many to many relationship table between User and Group

## Usage
The _huricane-event-backend_ provides a RESTful API for managing events and related data on the events app.
Some API endpoints include:
```angular2html

```
For a detailed documentation on this API, please refer to [DOCUMENTATION.md]()

## Contributing
Contributions to the Hurricane Event Backend are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Before contributing, please make sure to review the [contribution guidelines.]()

# Contact
For any inquiries or questions, please contact the team leads:

* Poject Team Lead Name here
  * Email: team.lead@example.com
  * GitHub: @Project_team_lead

* Backend Team Lead Name here
  * Email: team.lead@example.com
  * GitHub: @Project_backend_team_lead
