# TaskFlow API

TaskFlow is a simple and robust RESTful API for task management, built with a modern Python technology stack. It serves as a practical demonstration of building a containerized, asynchronous web application.

The application allows authenticated users to create, view, update, and delete tasks. When a new task is created, a background notification is dispatched asynchronously, ensuring the API remains fast and responsive.

## Key Technologies

* **Backend:** Django, Django REST Framework
* **Asynchronous Tasks:** Celery
* **Message Broker:** RabbitMQ
* **Database:** PostgreSQL
* **Containerization:** Docker & Docker Compose

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You must have [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

### Installation

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/your-username/taskflow-project.git](https://github.com/your-username/taskflow-project.git)
    cd taskflow-project
    ```
    *(Replace the URL with your actual repository URL)*

2.  **Create an Environment File**
    The application uses an `.env` file to manage secret keys and database credentials. Create this file in the root of the project directory.

    ```sh
    # In the root 'taskflow-project' directory
    cp .env.example .env
    ```
    *(Note: You may need to create a `.env.example` file first, or simply create `.env` manually)*

    Your `.env` file should contain the following:
    ```env
    # Database Credentials
    POSTGRES_DB=taskflow
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    ```

3.  **Build and Launch the Containers**
    This single command will build the necessary Docker images and start all four services (web, worker, database, and message broker) in the background.

    ```sh
    docker-compose up --build -d
    ```
    *(The `-d` flag runs the containers in "detached" mode)*

4.  **Run Database Migrations**
    Once the containers are running, you need to set up the database tables.

    ```sh
    docker-compose exec web python manage.py migrate
    ```

5.  **Create a Superuser**
    To access the Django Admin and the secure API endpoints, you need an admin account.

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```
    Follow the prompts to create your username and password.

---

## Usage

Your multi-container application is now running.

* **API Endpoint:** `http://localhost:8000/api/tasks/`
* **Django Admin:** `http://localhost:8000/admin/`
* **RabbitMQ Management UI:** `http://localhost:15672` (Username: `guest`, Password: `guest`)

You can use the browsable API at `/api/tasks/` to create and manage tasks after logging in through the Django Admin.
