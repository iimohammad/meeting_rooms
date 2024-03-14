# Meeting Room Reservation System
The Meeting Room Reservation System is a Django web application that allows users to reserve meeting rooms for sessions. Users can view available meeting rooms, book a room for a specific date and time, and manage their reservations.
## Features

- User Authentication: Users can create accounts, login, and logout.
- View Available Rooms: Users can view a list of available meeting rooms.
- Reserve Room: Users can reserve a meeting room for a specific date and time.
- Manage Reservations: Users can view and cancel their existing reservations.

## Setup
To run the Meeting Room Reservation System locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/iimohammad/meeting-room.git
```
Navigate to the project directory:
```bash
cd meeting-room-reservation
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Apply database migrations:
```bash
python manage.py migrate
```
Create a superuser account (for accessing the admin interface):
```bash
python manage.py createsuperuser
```
Run the development server:
```bash
python manage.py runserver
```
The application will be accessible at `http://localhost:8000.`


after that go to config directory and make a local_settings.py
and copy contents of Sample_local_settings.py in that file, and complete it.

### Config Settings

## Usage
- Navigate to the application URL in your web browser.
- Register for a new account or log in with an existing account.
- View the list of available meeting rooms.
- Select a room, date, and time for your reservation.
- Confirm your reservation.
- To cancel a reservation, navigate to your profile page and select the reservation to cancel.

## Admin Interface
The admin interface can be accessed at `http://localhost:8000/admin`. You can log in with the superuser account created during setup. From the admin interface, you can manage users, meeting rooms, and reservations.

## Technologies Used
- Django
- HTML/CSS
- JavaScript (optional, for frontend interactivity)
- SQLite (default database)

## How to Test Project 

### Load Prepared Data
```bash
python manage.py loaddata
```

### Test 
To run the tests for the project, execute the following command:
```bash
py manage.py test
```
### Check Coverage Tests
To check the test coverage, you need to install the coverage tool. If you haven't installed it yet, you can do so using pip:
```bash
pip install coverage
```
Once installed, you can run the tests with coverage and generate coverage reports.
Run the tests with coverage:
```bash
coverage run --source='.' manage.py test
```
Generate a coverage report:
```bash
coverage report
```
This command will display the coverage report in the terminal, showing which parts of the code are covered by the tests.
Optionally, you can generate an HTML report for a more detailed view:
```bash
coverage html
```

## Contributors
- Mohammad Baharlou
- Masih Shafiei
- Amirhosein Farahani
- Amirabas Afrasiabi
- Peyman Shojaei

## Mentor 
Seyed MohammadAli Golestani

## License
This project is licensed under the MIT License.








