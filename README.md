# FT9ja
# Table of contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Admin Dashboard](#admin-dashboard)
- [Contributing](#contributing)
- [License](#license)

## Description

This is a demo forex trading website built using Django, showcasing a basic trading simulation environment. Users can log into the dashboard to view their randomly generated profit/loss over time and visualize it with graphical representation. The admin can track user progress through the provided admin dashboard.

## Features

- User authentication and registration.
- Dashboard for users to view their random profit/loss and graphical representation.
- Admin dashboard to track user progress and activities.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/forex-trading-demo.git
   cd forex-trading-demo
   
2. Create a virtual environment and install dependencies:

     ```
     python -m venv venv
     source venv/bin/activate   # On Windows: venv\Scripts\activate
     pip install -r requirements.txt
     ```
3. Run migrations to set up the database:

    ```
    python manage.py migrate
    ```
 4. Create a superuser for the admin panel:

    ```
    python manage.py createsuperuser
    ```
 5. Start the development server:

    ```
    python manage.py runserver
    ```

# Usage
1. Access the website by navigating to http://localhost:8000 in your web browser.
2. Register as a user or log in using your credentials.
3. Explore the dashboard to view your random profit/loss and graphical representation.

# Admin Dashboard
To access the admin dashboard:
1. Navigate to http://localhost:8000/user/admin_dashboard in your web browser.
2. Log in using the superuser credentials you created earlier.
3. Monitor and manage user progress, activities, and other relevant data.

# Contributing
Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License.
