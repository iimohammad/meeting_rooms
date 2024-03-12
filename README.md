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
```bash
py manage.py test
```
### Check Coverage Tests

```bash
pip install coverage
```

```bash
coverage run --source='.' manage.py test
```

```bash
coverage report
```

```bash
coverage html
```









