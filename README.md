# Hurricane Event Backend

This repository contains the backend code for the Hurricane Event project, which provides a RESTful API for managing events and related data on the events app.

## Installation

To run the Hurricane Event Backend locally, follow these steps:

1. **Clone the Repository and Activate the Virtual Environment:** 
   ```bash
   git clone https://github.com/your-username/hurricane-event-backend.git
   cd hurricane-event-backend
   virtualenv venv   # Create a virtual environment
   source venv/bin/activate  # Activate the virtual environment (Windows users: use venv\Scripts\activate)
   ```

2. **Install Required Dependencies:** 
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Configuration:** 
   - Create a `config.py` file and configure the necessary environment variables, such as database connection details, API keys, and other configuration settings.

4. **Run the App:** 
   ```bash
   flask run
   ```

## Usage

The Hurricane Event Backend provides a set of API endpoints for managing events and related data in the events app. Some of the key API endpoints include:

- `/api/events`: Retrieve and manage events.
- `/api/users`: Manage user accounts.
- `/api/locations`: Manage event locations.
- `/api/categories`: Manage event categories.
- ...

For detailed documentation on these API endpoints and their usage, please refer to the [DOCUMENTATION.md](DOCUMENTATION.md) file.

## Contributing

Contributions to the Hurricane Event Backend are welcome! If you encounter any issues, have suggestions for improvements, or want to contribute to the project, please follow these guidelines:

1. **Check for Existing Issues:** Before creating a new issue or submitting a pull request, check if a similar issue or pull request already exists.

2. **Create a New Branch:** When working on a contribution, create a new branch from the `main` branch.

3. **Submit a Pull Request:** After making your changes, submit a pull request, providing a clear description of the changes you've made and why they are beneficial.

Before contributing, please review the detailed [Contribution Guidelines](CONTRIBUTING.md) for more information.

## Contact

For any inquiries or questions related to the Hurricane Event Backend, please feel free to contact the project and backend team leads:

### Project Team Lead

- **Name:** [Your Project Team Lead Name]
- **Email:** team.lead@example.com
- **GitHub:** [@Project_team_lead](https://github.com/Project_team_lead)

### Backend Team Lead

- **Name:** [Your Backend Team Lead Name]
- **Email:** team.lead@example.com
- **GitHub:** [@Project_backend_team_lead](https://github.com/Project_backend_team_lead)

Your README is now organized, informative, and user-friendly, making it easier for contributors and users to understand and use your Hurricane Event Backend.
