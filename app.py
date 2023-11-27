from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample contacts list (replace this with a database in a real application)
contacts = [
    {'id': 1, 'name': 'John Doe', 'phone_number': '123-456-7890', 'email': 'john@example.com', 'address': '123 Main St'},
    {'id': 2, 'name': 'Jane Smith', 'phone_number': '987-654-3210', 'email': 'jane@example.com', 'address': '456 Oak Ave'},
    # Add more contacts as needed
]

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    address = request.form['address']

    # In a real application, you would add the contact to a database
    new_contact = {'id': len(contacts) + 1, 'name': name, 'phone_number': phone_number, 'email': email, 'address': address}
    contacts.append(new_contact)

    return redirect(url_for('index'))

@app.route('/update_contact/<int:contact_id>', methods=['GET', 'POST'])
def update_contact(contact_id):
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        address = request.form['address']

        for contact in contacts:
            if contact['id'] == contact_id:
                contact['name'] = name
                contact['phone_number'] = phone_number
                contact['email'] = email
                contact['address'] = address
                break

        return redirect(url_for('index'))
    else:
        contact_to_update = next((contact for contact in contacts if contact['id'] == contact_id), None)
        return render_template('update_contact.html', contact=contact_to_update)

@app.route('/delete_contact/<int:contact_id>')
def delete_contact(contact_id):
    global contacts
    contacts = [contact for contact in contacts if contact['id'] != contact_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
