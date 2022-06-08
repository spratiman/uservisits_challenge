# UserVisitChallenge
Northbridge Financial Corporation Tech Challenge

## Pre-requisites
1. Python 3.x
2. Pip
3. Git
4. virtualenv

## Project Setup

1. Git clone https://github.com/spratiman/uservisits_challenge.git
2. cd uservisits_challenge
3. virtualenv venv
4. source venv/bin/activate
5. cd northbridge_app
6. pip install -r requirements.txt
7. python manage.py migrate
8. python populate_dummy_data.py
9. python manage.py runserver

## Test Suite
1. pytest

## API
Following APIs are provided to view the dummy data and can be accessed via https://127.0.0.1:8000/api/v1

### GET /users/
Returns list of users with their name, email and is_active status

### GET /policies/
Returns list of policies with the user email, hash_id, start_date and state
### GET /pages/
Returns list of pages with their name

### GET /visits/
Returns list of visits with their created (visited) date, policy hash_id, page name

## Notice Dummy Data
This can be found in populate_dummy_data.py
This is also loaded as part of the setup process

## Future Improvements - If I had more time
1. Add Authentication to secure API calls
2. Add pytest for API and user report views
and consequently not create duplicate Match
3. Add an Admin Page
4. Add visualize the user visits with the help of charts