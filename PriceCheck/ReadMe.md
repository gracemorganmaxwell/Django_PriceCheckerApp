# PriceCheck Project

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Development Environment Setup](#development-environment-setup)
- [Running the Application](#running-the-application)
- [Admin Access](#admin-access)
- [Testing](#testing)
- [Deployment](#deployment)
- [License](#license)

## Overview

PriceCheck is a Django-based web application designed to help users compare prices of grocery products across different supermarket chains in New Zealand. The project aims to provide a user-friendly interface for customers to find the best deals and manage their shopping preferences. This project is based off and inspired by https://www.grocer.nz and is a price comparison site for New Zealand. Which takes data from the New Zealand grocer website and allows users to compare prices and products across different stores based on the users chosen product and preferred stores and their location. The data is scrapped from the grocer store websites. The project is still in development and is not yet fully functional. The target is to have a fully functional web application that allows users to compare prices and manage their shopping preferences in a user-friendly user interface and a safe and secure environment.

## Key Features

1. **Product Comparison**: Users can search and view products from various supermarkets, comparing prices and details.

2. **User Authentication**: The application supports user registration, login, and logout functionalities.

3. **Store Preferences**: Users can select and manage their preferred supermarket stores.

4. **Shopping Cart**: Authenticated users can add products to their cart and manage quantities.

5. **Favorite Products**: Users can mark products as favorites for quick access.

6. **Price History Tracking**: The application stores historical price data for products.

7. **Admin Interface**: A Django admin interface is available for managing products, stores, and user data.

8. **User Profiles**: Each user has a profile with additional information.

9. **Order Management**: The system supports creating and managing orders.

## Technology Stack

- **Backend**: Django (Python web framework)
- **Database**: MySQL
- **Frontend**: HTML, CSS (Tailwind CSS for styling)
- **JavaScript**: Used for dynamic frontend interactions
- **Authentication**: Django's built-in authentication system
- **Additional Libraries**:

  - django-tailwind for integrating Tailwind CSS
  - Pillow for image handling
  - python-dotenv for environment variable management

- Python (3.x recommended)
- pip (Python package manager)
- Django (Python web framework)
- MySQL (Database)
- HTML, CSS, JavaScript (Frontend)
- Django's built-in authentication system
- Pillow for image handling
- python-dotenv for environment variable management

## Project Structure

The PriceCheck project follows a typical Django structure:

- `PriceCheck/`: Main project directory
  - `settings.py`: Project settings and configuration
  - `urls.py`: Main URL routing
- `super/`: Main application directory
  - `models.py`: Database models (SupermarketChain, Store, Product, PriceHistory, Profile, UserStorePreference, FavoriteProduct, CartItem, Order, OrderItem)
  - `views.py`: View functions/classes for handling requests
  - `urls.py`: URL routing for the super app
  - `admin.py`: Admin interface configurations
  - `templates/`: HTML templates
  - `static/`: Static files (CSS, JavaScript, images)
- `mytheme/`: Tailwind CSS configuration
  - `static_src/`: Source files for Tailwind CSS
  - `static/`: Compiled Tailwind CSS output
- `manage.py`: Django's command-line utility for administrative tasks
- `requirements.txt`: List of project dependencies

## Key Functionalities

1. **Product Listing and Search**: Users can view a list of products, search by name, and filter by category and price.

2. **Store Preference Management**: Users can select their preferred stores, which are displayed on their dashboard.

3. **Shopping Cart**: Functionality to add, remove, and update quantities of products in the cart.

4. **User Dashboard**: Displays user's store preferences and favorite products.

5. **Price History Tracking**: Stores historical price data for products.

6. **User Profile Management**: Users can manage their profiles with additional information.

7. **Order Processing**: Users can create and manage orders.

8. **Supermarket Chain and Store Management**: Admin can manage supermarket chains and individual stores.

9. **Favorite Products**: Users can mark and manage their favorite products.

## Development and Deployment

- The project uses environment variables for sensitive information like database credentials.
- It includes configurations for both development and production environments.
- Static files are managed using Django's static file handling, with additional setup for Tailwind CSS.

## Future Enhancements

Based on the current structure, potential areas for enhancement could include:

1. Implementing a more robust search and filtering system.
2. Implementing a mobile app version for easier access on-the-go.

## Prerequisites

- Python (3.x recommended)
- pip (Python package manager)

## Development Environment Setup

1. Clone the repository:

   ```
   git clone https://github.com/gracemorganmaxwell/server_side_scripting_IT6006
   cd PriceCheck
   ```

2. Create a virtual environment:

   - Windows:
     ```
     python -m venv venv
     ```
   - macOS/Linux:
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

5. Set up environment variables:

   - Create a file named `.env` in the project root directory (same level as `manage.py`).
   - Add the following content to the `.env` file, replacing the values with your actual database information:
     ```
     DB_NAME=your_database_name
     DB_USER=your_database_user
     DB_PASSWORD=your_database_password
     DB_HOST=your_database_host
     DB_PORT=your_database_port
     ```
   - Add `.env` to your `.gitignore` file to prevent sensitive information from being committed.

6. Run database migrations:

   - Windows:
     ```
     python manage.py migrate
     ```
   - macOS/Linux:
     ```
     python3 manage.py migrate
     ```

7. Create a superuser:

   - Windows:
     ```
     python manage.py createsuperuser
     ```
   - macOS/Linux:
     ```
     python3 manage.py createsuperuser
     ```

8. Start the development server:

   - Windows:
     ```
     python manage.py runserver
     ```
   - macOS/Linux:
     ```
     python3 manage.py runserver
     ```

9. Access the application at `http://127.0.0.1:8000/`

## Admin Access

To access the Django admin interface:

1. Ensure the server is running
2. Visit `http://127.0.0.1:8000/admin/`
3. Log in with the superuser credentials created in step 7

## Deployment Notes

When deploying the application, ensure that you set the environment variables in your production environment.