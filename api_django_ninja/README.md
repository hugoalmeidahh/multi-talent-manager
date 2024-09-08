# API DJANGO WITH DJANGO-NINJA

This project using django with django-ninja.

## TALENT MANAGEMENT

## EXTRA TIPS : ❤️ by Saymon
- create an api.py file in the project with the main configurations;
- create an api.py in each app and do not use the view.
- create a functions file to reuse functions that can be used between views, apis and models.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- **Python 3.10+**
- **PostgreSQL**
- **Docker** (if you choose to run the project with Docker)

## Installation without Docker

### Step 1: Clone the repository

```bash
git clone https://github.com/hugoalmeidahh/talent-manager.git
cd talent-manager
```

### Step 2: Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Step 3: Install the dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure the database
You need to create a PostgreSQL database and configure the credentials in the settings.py file. Here is an example configuration in settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 5: Apply migrations
```bash
python manage.py migrate
```

### Step 6: Run the development server
```bash
python manage.py runserver
```
Now you can access the API at http://localhost:8000.

### Step 7: Access Swagger (API Documentation)
Once the server is running, you can access the automatically generated documentation at http://localhost:8000/swagger/ to test the endpoints.

## Running the project with Docker
If you prefer to run the project using Docker, follow the steps below:

### Step 1: Install Docker
Make sure Docker is installed. If not, follow the installation instructions.

### Step 2: Create the .env file
Create a .env file in the project root with the following variables:

```bash
POSTGRES_DB=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_database_password
DJANGO_SECRET_KEY=your_django_secret_key
```

### Step 3: Build the Docker image
In the project root, run the following command to build the Docker image:

```bash
docker-compose build
```

### Step 4: Run the containers
```bash
docker-compose up
```
This will start Django and a PostgreSQL container. The API will be accessible at http://localhost:8000 and Swagger at http://localhost:8000/swagger/.

### Step 5: Run migrations inside the container
If this is your first time running the project, apply the migrations:

```bash
docker-compose exec web python manage.py migrate
Running Tests
To run tests, use the following command:
```
```bash
python manage.py test
```
If you're using Docker, run it inside the container:

```bash
docker-compose exec web python manage.py test
Contribution
Contributions are welcome! Feel free to open issues and submit pull requests.
```

## License
This project is licensed under the MIT License.

### Explanation

- **Installation without Docker**: This section explains how to manually install the project, including setting up the virtual environment, installing dependencies, and configuring the database.
- **Running with Docker**: This part explains how to use Docker to run the project, leveraging `docker-compose` to manage containers, and setting up the database configuration.
- **Tests**: Provides instructions on how to run the tests both locally and inside the Docker container.


## API DOCS
Access the API:
- Visit `http://localhost:8000/api/docs` for the Swagger documentation.

## 🦸&nbsp; About Author
Hello, I'm Hugo Almeida, I'm a fullstack architect and mobile++. 
I am passionate about technology, programming, processes and planning. 
I united all these passions in one profession. 

If you have questions, suggestions and criticism are very welcome. Follow my contacts.
If you like, _don't forget to send stars for this project._

👤 **Hugo Almeida (Hugão Dev)**

* Twitter: [@hugaodev](https://twitter.com/hugaodev)
* Github: [@hugoalmeidahh](https://github.com/hugoalmeidahh)
* LinkedIn: [@hugoalmeidahh](https://linkedin.com/in/hugoalmeidahh)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ for you!_

## License
This project is licensed under the MIT License.