# Technology Stack

## Backend

- **Framework**: Flask 3.0.0 (Python web framework)
- **Database**: MySQL with flask-mysqldb 2.0.0 and mysqlclient 2.2.0
- **Configuration**: python-dotenv 1.0.0 for environment variable management

## Frontend

- Vanilla JavaScript (no frameworks)
- HTML5 with Jinja2 templating
- CSS3 with modern features (grid, flexbox, gradients)

## Database

- MySQL database named `contact_book`
- Single `contacts` table with fields: id, name, phone, email, created_at
- Port 3307 (non-standard, configurable via .env)

## Environment Configuration

All sensitive configuration is stored in `.env`:
- `SECRET_KEY`: Flask session secret
- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`: MySQL connection parameters

## Common Commands

### Setup
```bash
# Create virtual environment
python -m venv myvenv

# Activate virtual environment (Windows)
myvenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
mysql -h localhost -P 3307 -u root -p < database_setup.sql
```

### Running
```bash
# Run development server
python app.py

# Server runs on http://0.0.0.0:5000 with debug mode enabled
```

### Testing Database Connection
The app automatically tests the database connection on startup and prints diagnostic information to the console.
