 # Contacts Manager
# Overview
The Flask Contacts Manager is a simple web application for managing a list of contacts. Users can view, add, update, and delete contacts. This application uses Flask for the web framework and stores contacts in a sample list (which you can replace with a database in a real-world application).

# Features
View Contacts: Display a list of all contacts.

Add Contact: Add a new contact to the list.

Update Contact: Edit an existing contact's details.

Delete Contact: Remove a contact from the list.

# Prerequisites
Python 3.x: Ensure Python is installed on your system.

Flask: Install Flask by running:

pip install Flask

Run the Flask application:

python app.py

Open your browser and go to http://127.0.0.1:5000/ to access the Contacts Manager.

# Routes
Home (/)

Method: GET

Description: Displays the list of contacts and the form to add a new contact.

Add Contact (/add_contact)

Method: POST

Description: Adds a new contact with the details provided in the form.

Update Contact (/update_contact/<int:contact_id>)

Method: GET, POST

Description: Allows updating the details of a specific contact. The contact's details are pre-filled in the form. On form submission, updates the contact's details.

Delete Contact (/delete_contact/<int:contact_id>)

Method: GET

Description: Deletes a specific contact from the list.
