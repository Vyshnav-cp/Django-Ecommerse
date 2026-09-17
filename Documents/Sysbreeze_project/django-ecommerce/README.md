# Django E-Commerce Store

A lightweight e-commerce website built with Django. The project demonstrates a clean Django application structure, built-in user authentication, protected pages, Product management through the admin site, and a responsive Bootstrap 5 interface.

## Features

- User registration with name, username, email, password, and password confirmation
- Duplicate username and email validation
- Login with username or email
- Django session-based authentication
- Protected home page for authenticated users
- Secure POST-based logout with CSRF protection
- Product model with name, description, price, image, and creation date
- Product management through Django admin
- Product search, date filtering, ordering, and pagination in admin
- Responsive Bootstrap 5 UI for desktop and mobile screens
- Friendly validation errors and empty product-state messaging
- SQLite database for simple local development

## Technologies Used

- Python 3.12+
- Django 6.1.1
- SQLite
- Bootstrap 5.3
- Pillow for product image support
- HTML and CSS

## Project Structure

```text
django-ecommerce/
├── ecommerce/
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Root URL configuration
│   ├── asgi.py              # ASGI entry point
│   └── wsgi.py              # WSGI entry point
├── store/
│   ├── migrations/
│   │   └── 0001_initial.py  # Product database migration
│   ├── templates/store/
│   │   ├── base.html        # Shared layout and navigation
│   │   ├── home.html        # Product listing page
│   │   ├── login.html       # Login page
│   │   └── register.html    # Registration page
│   ├── admin.py             # Product admin configuration
│   ├── forms.py             # Registration and login forms
│   ├── models.py            # Product model
│   ├── urls.py              # Store routes
│   ├── views.py             # Authentication and product views
│   └── tests.py             # Authentication and validation tests
├── manage.py
├── db.sqlite3               # Local SQLite database
└── README.md
```

## Installation

### 1. Clone or download the project

```bash
git clone <repository-url>
cd django-ecommerce
```

If the project is already downloaded, open a terminal in the directory containing `manage.py`.

### 2. Create a virtual environment

Linux and macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install django pillow
```

Pillow is required because the Product model uses Django's `ImageField`.

## Database Setup

Apply the built-in Django migrations and the Product migration:

```bash
python manage.py migrate
```

To verify that migrations are current:

```bash
python manage.py makemigrations --check --dry-run
```

## Create a Superuser

Create an administrator account for the Django admin site:

```bash
python manage.py createsuperuser
```

Follow the prompts for username, email, and password.

## Run the Development Server

```bash
python manage.py runserver
```

Open the application at:

- Website: <http://127.0.0.1:8000/>
- Admin site: <http://127.0.0.1:8000/admin/>

The local development settings use a development-only secret fallback. For non-development environments, set a secure secret key and disable debug mode:

```bash
export DJANGO_SECRET_KEY="replace-with-a-long-random-secret"
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS="your-domain.example.com"
```

## Admin Usage

1. Start the development server.
2. Open <http://127.0.0.1:8000/admin/>.
3. Sign in with the superuser account.
4. Open **Products** to add, edit, or delete products.
5. Product listings support name search, creation-date filtering, newest-first ordering, and pagination.

Product images are uploaded under the configured `products/` upload path.

## User Registration and Login Flow

1. Visit `/register/` to create an account.
2. Submit a name, username, email, password, and password confirmation.
3. Successful registration redirects to `/login/`.
4. Visit `/login/` and sign in using either the username or email address.
5. Successful authentication redirects to `/`.
6. The home page displays products from the database and requires authentication.
7. Logout is available in the shared navigation and uses a CSRF-protected POST request.
8. After logout, the user is redirected to `/login/`.

## Tests

Run the test suite with:

```bash
python manage.py test
```

The tests cover required-field validation, password confirmation, duplicate username and email checks, password hashing, username/email login, invalid credentials, protected home access, and logout behavior.

## Screenshots

_Add screenshots here before submitting the project._

Suggested screenshots:

- Registration page
- Login page
- Authenticated product listing page
- Django admin Product list
- Django admin Product form

## Future Improvements

- Add product categories and inventory tracking
- Add product detail pages
- Add a shopping cart and checkout flow
- Add order and payment processing
- Add customer profile and order history pages
- Store uploaded media with a production-ready storage service
- Add automated CI checks and deployment configuration
- Add pagination for larger product catalogs

## License

This project was created as a Django developer interview task and is intended for demonstration and evaluation purposes.
