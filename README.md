# Meeting Rooms

## Installation 
first of all you have to install requirements by this code:
```bash
pip install -r requirements.txt
```
after that go to config directory and make a local_settings.py
and copy contents of Sample_local_settings.py in that file, and complete it.

### Config Settings

## Usage

### Account Usage App

### Company Usage App


### Room Usage App


### Notification Usage App


### Log Usage App


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









