# Project Structure

## Directory Layout

```
/
├── app.py                    # Main Flask application with routes and DB logic
├── requirements.txt          # Python dependencies
├── database_setup.sql        # MySQL schema and sample data
├── .env                      # Environment variables (not in git)
├── .gitignore               # Git exclusions
├── TROUBLESHOOTING.md       # Database connection troubleshooting guide
├── templates/               # Jinja2 HTML templates
│   └── index.html          # Main contact list page with modal
├── static/                  # Static assets
│   └── styles.css          # Application styles
└── myvenv/                  # Python virtual environment (not in git)
```

## Code Organization

### app.py
- Flask app initialization and configuration
- MySQL connection setup with flask-mysqldb
- Database connection testing function
- Five routes: index (GET), add (POST), update (POST), delete (POST)
- All routes redirect to index after POST operations
- Flash messages for user feedback

### templates/index.html
- Single-page application structure
- Contact cards rendered server-side via Jinja2
- Modal dialog for add/edit operations
- Client-side JavaScript for search and modal management
- Inline JavaScript (no separate JS files)

### static/styles.css
- Modern CSS with custom properties could be added
- Responsive grid layout for contact cards
- Modal styling with overlay
- Consistent color scheme: teal (#3b9a9c, #2d7a7c)
- Mobile-friendly with responsive design

## Conventions

- All database operations use parameterized queries to prevent SQL injection
- Flash messages use categories: 'success' and 'error'
- Forms use POST method with redirects (POST-Redirect-GET pattern)
- Contact cards store data attributes for JavaScript access
- Modal reuses same form for both add and edit operations
