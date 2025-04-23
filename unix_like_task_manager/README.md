#  Unix-like Task Manager API

Unix-like Task Manager is a simple and easy-to-use task management system inspired by Unix. It helps individuals and teams create, organize, and track tasks with useful details like category, schedule, and more.
The project is built using **FastAPI** for the backend, **PostgreSQL** for the database, and **SQLAlchemy** to handle database operations. The code is neatly organized using routers, models, schemas, and CRUD functions. It also follows good coding practices like using a .env file for settings and keeping the code modular and clean.

##  Project Structure

unix_like_task_manager/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   └── task_model.py
│   ├── schemas/
│   │   └── task_schema.py
│   ├── db/
│   │   ├── session.py
│   │   └── base.py
│   ├── crud/
│   │   └── task_crud.py
│   ├── api/
│   │   └── task_routes.py
│   ├── core/
│   │   └── config.py
│
├── .env
├── requirements.txt
└── README.md

##  Features

-  Create new tasks
-  Read all tasks or by ID
-  Update task details
-  Delete task by ID
-  Delete all tasks 
-  Full Swagger docs at `/docs`
- `.env` support for secure config handling

##  Tech Stack

- **FastAPI** – Fast web framework for APIs
- **SQLAlchemy** – ORM for DB communication
- **PostgreSQL** – Relational DB
- **Pydantic** – Data validation & serialization
- **dotenv** – Manage environment variables


## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/unix_like_task_manager.git
cd unix_like_task_manager
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Linux/macOS
venv\Scripts\activate          # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env` File

Update the `.env` file with your DB credentials:

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=unix_task_db
DATABASE_USER=User_Name
DATABASE_PASSWORD=Your_Password
DATABASE_URL=postgresql://postgres:Password@localhost:5432/unix_task_db
```

### 5. Create the Database

Database can create it using:

```sql
CREATE DATABASE unix_task_db;
```
(unix_task_db: eg for database name)

##  Run the Project

```bash
uvicorn app.main:app --reload 

```

- Visit API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative Docs (ReDoc): [http://localhost:8000/redoc](http://localhost:8000/redoc)


##  API Endpoints Summary

| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| POST   | `/tasks`           | Create a new task       |
| GET    | `/tasks`           | Get all tasks           |
| GET    | `/tasks/{id}`      | Get task by ID          |
| PUT    | `/tasks/{id}`      | Update a task by ID     |
| DELETE | `/tasks/{id}`      | Delete a task by ID     |
| DELETE | `/tasks`           | Delete **all** tasks    |

## Create DATABASE
---> To create a new PostgreSQL database using pgAdmin

✅ Using SQL Command in pgAdmin
1.Open pgAdmin and log in with your credentials.
2.In the Query Editor window that opens, paste the following SQL command:
```sql
## CREATE DATABASE unix_task_db;
```
(unix_task_db: eg for database name)
---> Configure your .env file
DATABASE_URL=postgresql://postgres:Password@localhost:5432/databaseName
(Replace postgres with your PostgreSQL username,Replace Password with your PostgreSQL password,Replace localhost with the host if you're using a different server,5432 is the default port for PostgreSQL, so you can leave it as is unless you have a custom port,Replace your DB Name)
----> you can switch to the newly created database using:
```sql
## \c unix_task_db
```
This command will connect to unix_task_db and let you start working with it.

