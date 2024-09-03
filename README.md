
# Carpentry Project

This project is a carpentry application that utilizes both frontend and backend technologies.

## Frontend (frontend_carpi)

This folder contains the frontend code developed with Vue.js and Vite.

### Recommended IDE Setup

For the best development experience, it is recommended to use [VSCode](https://code.visualstudio.com/) with the [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) extension (and disable Vetur).

### Customize configuration

For customizing the frontend configuration, please refer to the [Vite Configuration Reference](https://vitejs.dev/config/).

### Project Setup

To set up the frontend project, run the following command:

```sh
npm install
```

#### Compile and Hot-Reload for Development

To compile and enable hot-reloading for development, run the following command:

```sh
npm run dev
```

#### Compile and Minify for Production

To compile and minify the frontend code for production, run the following command:

```sh
npm run build
```

#### Run Unit Tests with [Vitest](https://vitest.dev/)

To run unit tests using [Vitest](https://vitest.dev/), execute the following command:

```sh
npm run test:unit
```

#### Lint with [ESLint](https://eslint.org/)

To lint the frontend code using [ESLint](https://eslint.org/), run the following command:

```sh
npm run lint
```

## Backend (backend_carpi)

This folder contains the backend code developed with Django.

### Django Documentation

For detailed documentation on working with Django, please refer to the [Django documentation](https://docs.djangoproject.com/).

### Installation

To install Django, you can use pip:

```sh
pip install django
```

### Creating a Django Project

To create a new Django project, run the following command:

```sh
django-admin startproject project_name
```

Replace `project_name` with the desired name for your project.

### Running the Development Server

To start the development server, navigate to the project directory and run the following command:

```sh
python manage.py runserver
```

This will start the server at `http://localhost:8000/`.

### Creating Django Apps

To create a new Django app within your project, run the following command:

```sh
python manage.py startapp app_name
```

Replace `app_name` with the desired name for your app.

### Database Configuration

Django supports multiple databases. You can configure the database settings in the `settings.py` file of your project.

### Migrations

Django provides a built-in migration system to manage database schema changes. To create and apply migrations, use the following commands:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Django Admin

Django provides an admin interface for managing your application's data. To create a superuser account, run the following command:

```sh
python manage.py createsuperuser
```

You can then access the admin interface at `http://localhost:8000/admin/`.

