# FastAPI Boilerplate with `.env` Configuration

This is a FastAPI boilerplate project with environment variable support using `.env` and `python-dotenv`. It is configured for easy development and debugging in PyCharm, using Uvicorn as the ASGI server.

## Features

- FastAPI application setup.
- Environment variable management using `.env` files.
- Pre-configured `.gitignore` to exclude sensitive files and common build artifacts.
- PyCharm run/debug configuration for streamlined development.
- Auto-reloading server with `uvicorn`.
- Dependency management with `requirements.txt`.

## Repository

You can find the project on GitHub: [FastAPI Boilerplate](https://github.com/Senpaixyz/fastapi-boilterplate.git)

## Prerequisites

- Python 3.7+
- [PyCharm IDE](https://www.jetbrains.com/pycharm/) (optional but recommended).
- FastAPI and Uvicorn installed in your project environment.

## Installation

1. Clone the repository and navigate into the project directory:

    ```bash
    git clone https://github.com/Senpaixyz/fastapi-boilterplate.git
    cd fastapi-boilterplate
    ```

2. Create and activate a virtual environment:

    ```bash
    # On macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # On Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. Install the dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project:

    ```bash
    touch .env
    ```

    Add your environment variables to the `.env` file, for example:

    ```env
    DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
    SECRET_KEY=mysecretkey
    DEBUG=True
    ```

## Running the Application

To run the FastAPI application, follow these steps:

### Running from the Terminal

1. Use `uvicorn` to start the FastAPI application with auto-reload enabled:

    ```bash
    uvicorn main:app --reload
    ```

2. Open a browser and navigate to `http://127.0.0.1:8000` to see the running application.

3. You can also visit the interactive API documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.

### Running in PyCharm

1. Open the project in PyCharm.

2. Set up the run/debug configuration:
   - Go to **Run > Edit Configurations**.
   - Click the **+** icon to add a new configuration.
   - Choose `Python` as the configuration type.
   - In the **Module name** field, enter `uvicorn`.
   - In the **Parameters** field, add:

     ```bash
     main:app --reload
     ```

   - Make sure the working directory is set to the root of your project.
   - Add environment variables by loading from the `.env` file:
     - In the **Environment variables** section, click the folder icon.
     - Select the `.env` file from your project root.
   - Save the configuration.

3. Run or Debug the application from PyCharm using the **Run** or **Debug** buttons.

## Accessing Environment Variables

In your FastAPI application, you can access environment variables using `os.getenv()`:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Example of accessing an environment variable
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
debug_mode = os.getenv("DEBUG")
