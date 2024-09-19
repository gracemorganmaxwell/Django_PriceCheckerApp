# PriceCheck Project

## Environment Setup

This project uses environment variables to manage sensitive information like database credentials. Follow these steps to set up your environment:

1. Create a file named `.env` in the project root directory (same level as `manage.py`).

2. Add the following content to the `.env` file, replacing the values with your actual database information (which is in the Teams group chat):

   ```
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=your_database_host
   DB_PORT=your_database_port
   ```

3. Make sure to add `.env` to your `.gitignore` file to prevent sensitive information from being committed to version control.

4. Install the required packages by running:
- Windows:
   ```
   pip install -r requirements.txt
   ```
- macOS/Linux:
   ```
   pip3 install -r requirements.txt
   ```

5. When deploying the application, ensure that you set these environment variables in your production environment.

## Running the Project

[Add instructions on how to run the project here]

## Additional Notes

[Any other relevant information about the project]

## Getting Started

Follow these steps to set up and run the PriceCheck project locally.

### Prerequisites

- Python (3.x recommended)
- pip (Python package manager)

### Setup

1. Either Clone the repository or fetch / pull the latest changes:
   ```
   git clone https://github.com/gracemorganmaxwell/server_side_scripting_IT6006
   ```
1.1 Navigate into the project directory:
   ```
   cd PriceCheck
   ```

2. Create a virtual environment:
-Windows:
   ```
   python -m venv venv
   ```
-macOS/Linux:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install required packages:
   - Windows:
   ```
   pip install -r requirements.txt
   ```
   - macOS/Linux:
   ```
   pip3 install -r requirements.txt
   ```

5. Run database migrations:
   - Windows:
   ```
   python manage.py migrate
   ```
   - macOS/Linux:
   ```
   python3 manage.py migrate
   ```

6. Create a superuser:
   - Windows:
   ```
   python manage.py createsuperuser
   ```
   - macOS/Linux:
   ```
   python3 manage.py createsuperuser
   ```

7. Start the development server:
   - Windows:
   ```
   python manage.py runserver
   ```
   - macOS/Linux:
   ```
   python3 manage.py runserver
   ```

8. Access the application at `http://127.0.0.1:8000/`

### Admin Access

To access the Django admin interface:
1. Ensure the server is running
2. Visit `http://127.0.0.1:8000/admin/`
3. Log in with the superuser credentials created in step 6
