# Technology Stack

## Backend

- **Framework**: Flask (Python web framework)
- **Database**: MySQL (accessed via flask-mysqldb)
- **ORM**: Direct SQL queries using MySQLdb cursors

## Frontend

- **Template Engine**: Jinja2 (Flask's default)
- **Styling**: Vanilla CSS with modern design patterns
- **JavaScript**: Vanilla JS for client-side interactions

## Database Configuration

- Host: localhost
- Port: 3307 (non-standard MySQL port)
- Database: contact_book
- Table: contacts (id, name, phone, email, created_at)

## Common Commands

### Running the Application

```bash
python app.py
```

The app runs on `http://0.0.0.0:5000` with debug mode enabled.

### Database Setup

```bash
mysql -u root -p < database_setup.sql
```

Or execute the SQL file through your MySQL client on port 3307.

## Dependencies

- Flask
- flask-mysqldb
- MySQLdb (mysqlclient)

## Environment Notes

- Uses Python virtual environment (myvenv/)
- Secret key should be changed in production (currently: 'your_secret_key_change_this')
- Database credentials are hardcoded in app.py (should use environment variables in production)
