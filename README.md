# Project Name

Tajir is a website where users can post their items for sale or buy items from other users. The word "Tajir" has two meanings in Arabic: "sell" and "seller". By adding "al"(in arabic of course) to the word, it represents a platform that facilitates buying and selling productsn online in Morocco.

## Project Structure

- `backend`: Contains the backend code.
  - `api`: Contains the API code.
  - `backend`: Contains the project settings.
  - `manage.py`: Django management script.
  - `requirements.txt`: List of project dependencies.

## Usage

### Welcome Home Page

To access the home page, navigate to:
    - http://localhost:8000/

### Manage Users

To view a list of users use the following URL:
    - http://localhost:8000/api/users/

### User Posts

To view posts created by a specific user, use the following URL pattern:
    - http://localhost:8000/api/users/<user_id>/posts/
    - Replace `<user_id>` with the ID of the user whose posts you want to view.

### Manage Posts

To view a list of posts or create a new post, use the following URL:
    - http://localhost:8000/api/posts/


### Post Detail, Update, Delete
To view details of a specific post, update it, or delete it, use the following URL pattern:
    - http://localhost:8000/api/posts/<post_id>/
    - Replace `<post_id>` with the ID of the post you want to interact with.

### Register, Login, Logout
To register/create user use the following URL:
    -  http://localhost:8000/api/auth/register/
To login:
    - http://localhost:8000/api/auth/login/

Curl Request Example
You can use curl to make HTTP requests to interact with the API.

To get posts associated with a specific user (replace <user_id> with the ID of the user):
curl http://localhost:8000/users/<user_id>/posts/