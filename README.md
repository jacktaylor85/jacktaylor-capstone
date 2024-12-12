# MyBook

## Welcome to the MyBook App

![Am I Responsive Image](docs/images/Opera%20Snapshot_2024-12-11_195507_ui.dev.png)

Live Link here:

## Index

- UX/User Stories
- Features
- Design
- Testing
- Deployment
- Technologies Used
- Credits

## UX / User Stories

### <i>Must Haves:</i>

<b>Account Creation:</b>

As a User I can make an account so that I can create bookings and view bookings I have made in the past.

Acceptance Criteria:

- Be able to make an account (username + password)
- Be able to view previous bookings

<b>Admin Management:</b>

As an Admin I can access a dashboard so that I can manage booking and users.

Acceptance Criteria:

- Accessing dashboard as superuser
- Manage bookings
- Manage users

<b>Service Listing:</b>

As a user, I must be able to view a list of services available for booking so that I can choose the one I need.

Acceptance Criteria:

- Be able to a view a list of services
- Be able to choose a service

<b>Booking Management for the User:</b>

As a user, I must be able to view my current bookings and cancel them if needed.

Acceptance Criteria:

- Be able to view current bookings
- Be able to cancel current bookings

<b>Booking Management for the Admin:</b>

As an admin , I must be able to view my current bookings and cancel them if needed.

Acceptance Criteria:

- Be able to view current bookings
- Be able to cancel current bookings

<b>Booking Creation:</b>

As a user, I must be able to select a service, choose a date and time, and confirm my booking so that my reservation is secured.

Acceptance Criteria:

- Be able to select a service
- Be able to choose a date and time
- Be able to confirm a booking

### <i>Should Haves:</i>

<b>Notifications for the User:</b>

As a user, I should receive email notifications to confirm my booking and remind me of upcoming appointments.

Acceptance Criteria:

- Be able to receive email notifications to confirm bookings
- Be able to receive reminders for upcoming bookings

<b>Notifications for the Admin:</b>

As an admin, I should receive notifications about new bookings or cancellations.

Acceptance Criteria:

- Be able to receive notifications about new bookings
- Be able to receive notifications about new cancellations

<b>Search & Filters:</b>

As a user, I should be able to search for services and filter them by category, availability, or price.

Acceptance Criteria:

- Be able to search for services
- Be able to filter by category, availability and price

<b>Calendar for the User:</b>

As a user, I should be able to view my bookings on a calendar for better organization.

Acceptance Criteria:

- Be able to view bookings on the calendar

<b>Calendar for the Admin:</b>

As an admin, I should see a calendar of all bookings to manage conflicts.

Acceptance Criteria:

- Be able to see a calendar including all user bookings

### <i>Could Haves:</i>

<b>User Reviews & Ratings:</b>

As a user, I could leave reviews and ratings for the services I book to share feedback.

Acceptance Criteria:

- Be able to reviews and ratings
- Be able to share feedback on services

<b>Mobile App Integration:</b>

As a user, I could use a mobile app for a more convenient booking experience.

Acceptance Criteria:

- Be able to use the app on mobile devices

### <i>Won't Haves:</i>

<b>Third Party Integrations:</b>

As a user, I won’t have integrations with third-party calendars (e.g., Google Calendar) in the initial version but might have it in the future.

Acceptance Criteria:

- Integrate a third party calendar

## Planning

### Wireframes
Home Page:
![Capstone Homepage](docs/wireframes/Capstone%20HomePage.png)


Mobile Page:
![Capstone Mobile](docs/wireframes/Capstone%20Mobile.png)
### Agile Development
Kanban Board:
![Kanban board](docs/agile/Agile%20Development%20Snapshot.png)

### Entity Relationship Diagram
![ERD](docs/erd/Untitled.png)
## Features

### Background Image

The background images showcases a couple using a laptop to make a booking. This is to enhance the user's experience and this is likely to make the user think that there is a positive reaction to using my site. 
![Background Image](static/images/bruce-mars-ieIY61ZHhs8-unsplash.jpg)

### Services Section

The services section showcases available bookings and allows the user to filter these bookings by location, minimum and maximum price. These bookings were paginated by 6 to show a good amount of content on all screen sizes. 
![Services Image](docs/images/Opera%20Snapshot_2024-12-11_191006_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)

### Navbar

The Navbar allows the user to see all the links to the information with descriptive titles so that the user knows where the link will take them. These were made as simple as possible while also allowing the user to know what information they will gain by using the link.

![Navbar Image](docs/images/Opera%20Snapshot_2024-12-11_191402_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)

### Profiles

There is a few profile pages. Firstly, using the navbar link Login. You are able to login to an account and new users are able to register if they do not have an account. These can also be accessed by an unauthorised user if they use the click on the profile image in the center of the navbar. When the user is logged in and they are authorised then their own bookings can be accessed using the profile image. The user is shown information on their current booking and they are able to cancel or update them. When the user would like to logout then they are able to do so by using the logout navbar link that shows when the user is authenticated. 

### Profile Login:
![Profile Login](docs/images/Opera%20Snapshot_2024-12-11_191402_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)
### Login Page
![Profile Login](docs/images/Opera%20Snapshot_2024-12-11_191830_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)
### Registration Page:
![Profile Register](docs/images/Opera%20Snapshot_2024-12-11_191925_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)
### Authenticated Navbar
![Navbar LoggedIn](docs/images/Opera%20Snapshot_2024-12-11_192036_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)
### Profile Page:
![Profile Page](docs/images/Opera%20Snapshot_2024-12-11_192204_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)

### About Us

The about us page showcases what the site does and uses the same template as the homepage with different text.

![About us](docs/images/Opera%20Snapshot_2024-12-11_192334_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)

### Booking

When you click on the book now button on the services card, it takes you to this page where you can choose your clock-in and clock-out dates, add guests and then the total price is calculated for you in the profile page.

![Booking](docs/images/Opera%20Snapshot_2024-12-11_192448_8000-jacktaylor8-jacktaylorc-89cis3ew7jf.ws.codeinstitute-ide.net.png)

## Testing

### HTML Validation

My HTML Validation threw some errors due to my buttons being anchored so that the links would work within them. This was the only issue with my HTML validation as the rest of the code was valid.
![HTML Validation](docs/images/Opera%20Snapshot_2024-12-12_121429_validator.w3.org.png)

### CSS Validation

![CSS Validation](docs/images/Opera%20Snapshot_2024-12-11_193717_jigsaw.w3.org.png)

### Accessability and Performance Validation

![Lighthouse](docs/images/Screenshot%202024-12-11%20194721.png)

![Wave Accessibility](docs/images/Opera%20Snapshot_2024-12-11_195133_wave.webaim.org.png)

### Pep8 Validation

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
| Booking  | [no errors] | [no errors] | [no errors] | [no errors] | [no errors] |
| Profile | [no errors] | [no errors] | [no errors] | [no errors] | [no errors] |
| Services | [no errors] | [no errors] | [no errors] | [no errors] | [no errors] |


### Known Bugs

A few known bugs are; If the user is not authenticated then the profile image will cause an error if clicked on, this is because of the url being profile and that requires user authentification. There a few viewing bugs such as if the screen is shrunk there can be grey space underneath the image on the home page. On laptops there is a possibility that the footer can overlap with the paginate next & last feature making it difficult to change page. On Mobile there can be issues with logging in and out but this is fixable with refreshing. On mobile the burger dropdown doesn't work if you are in the register or login pages.

## Deployment

### Starting Your Project with a GitHub Template
1. To begin your project from the ground up, create a new GitHub repository using the Code Institute Full Template. This template comes pre-configured with essential tools for development. Follow these steps to get started:

2. Sign in to your GitHub account or register for a new one if needed.
3. Go to the Code Institute Full Template linked above.
4. Click on the 'Use this template' button and select 'Create a new repository'.
5. Provide a name for your new repository, then click 'Create repository from template'.
6. Open your newly created repository using the code button to initialize a new workspace.


### Django Setup

1. Install Django and Necessary Packages:
Run the following command to install Django (below version 4) and Gunicorn:
- pip3 install 'django<4' gunicorn
Install additional database-related libraries:
- pip3 install dj_database_url psycopg2
Add support for cloud storage using:
- pip3 install dj3-cloudinary-storage

2. Generate a Requirements File:
After installing the required dependencies, create a requirements.txt file to list all the libraries in use. Run:
- pip3 freeze --local > requirements.txt

3. Start a Django Project:
Create a new project using the following terminal command:
- django-admin startproject projectname .

4. Create a New Django App:
Use the following command to generate a new app:
- python3 manage.py startapp appname

5. Register Your App:
Add 'appname' to the INSTALLED_APPS list in the settings.py file.

6. Create an Admin User:
To manage the project, create a superuser with:
- python3 manage.py createsuperuser
Follow the prompts to set up login credentials.

7. Apply Database Migrations:
Run the following command to apply all migrations:
- python3 manage.py migrate

8. Protect Sensitive Data with env.py:
Create an env.py file to store sensitive information like DATABASE_URL and SECRET_KEY.
Add the following lines to env.py:
import os
os.environ["DATABASE_URL"] = "<your_database_url>"
os.environ["SECRET_KEY"] = "your_super_secret_key"
Ensure this file is listed in your .gitignore to prevent exposing sensitive data.
In your settings.py file, include the following:
import os
import dj_database_url
if os.path.exists("env.py"):
    import env

SECRET_KEY = os.environ.get('SECRET_KEY')

9. Configure the Database:
Replace the DATABASES section in settings.py with:
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
10. Set Up the Templates Directory:
Add the following under BASE_DIR in settings.py:
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
Update the TEMPLATES configuration:
'DIRS': [
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'templates', 'allauth'),
]
Create directories for media, static, and templates at the root level of your project.
11. Add a Procfile:
To prepare for Heroku deployment, create a Procfile and add:
web: gunicorn projectname.wsgi
12. Apply Migrations Again:
Ensure any changes are migrated using:
- python3 manage.py migrate


### Deploying to Heroku
1. Log in to Heroku or create an account if needed.

2. On the Heroku Dashboard, click the New button and select Create New App.

3. Provide a unique app name, choose your region, and click Create App.

4. Under the Settings tab, locate Config Vars and click Reveal Config Vars to add the following key-value pairs:

- CLOUDINARY_URL: Your Cloudinary URL
- DATABASE_URL: Your database connection URL
- DISABLE_COLLECTSTATIC: Set this to 1 temporarily (remove it before deployment).
- SECRET_KEY: Your project's secret key

5. Update the ALLOWED_HOSTS in settings.py to include:
ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com', 'localhost']
Once all files (including requirements.txt and Procfile) are ready, ensure DEBUG is set to False. Save your work, commit your changes, and push to GitHub.

On the Deploy tab in Heroku, choose GitHub as the deployment method and follow the prompts.





## Technologies Used

- HTML5
- CSS
- PYTHON
- asgiref==3.8.1
- cloudinary==1.41.0
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==4.2.16
- gunicorn==20.1.0
- psycopg==3.2.3
- sqlparse==0.5.2
- urllib3==1.26.20
- whitenoise==5.3.0

## Credits

- [Bootstrap](https://getbootstrap.com)
- [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adid=606528222178&adposition=&gad_source=1&gclid=Cj0KCQiAsOq6BhDuARIsAGQ4-zj6owc_EYiRBtJdiTAgCwBxVZgwHmBoPlEBGTiEgIuhQxUq7c6XjVoaAhBqEALw_wcB)
- [ChatGPT](https://chatgpt.com)
- [Balsamiq](https://balsamiq.com/?gad_source=1&gclid=Cj0KCQiAsOq6BhDuARIsAGQ4-zjrJbT-mGftS-hMHU9VHOWeDgSx3O7j6gHknLD-ss74QM1dTaUPuf0aAtXzEALw_wcB)
- [Unsplash](https://unsplash.com)
- [Booking.com](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiG1eSSmqKKAxWOklAGHQI_CdIYABAAGgJkZw&ae=2&co=1&gclid=Cj0KCQiAsOq6BhDuARIsAGQ4-zhlHqEZXhue4zugI9yuxXt316u_Jie_IlTdOe9DOw7gI72UPVtZWgkaAjDTEALw_wcB&ohost=www.google.com&cid=CAESVeD2zppeuV-1E__0ZN2sf86yIxfQVUKrfRKnTtAvaRoBzIf8-mXr9yQnwNEye8WCpLY1MLjCExNa384tBnxPOnyGOrH2WMmX57Ssuxj0b1WMhrFpdvk&sig=AOD64_01W-eJkPcgCgRyR2nyrxxMZX-BVA&q&adurl&ved=2ahUKEwjMvN6SmqKKAxWGXEEAHR5kH2gQ0Qx6BAgKEAE)