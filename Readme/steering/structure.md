# Project Structure

```
contact-book/
├── app.py                    # Main Flask application with routes
├── database_setup.sql        # Database schema and sample data
├── myvenv/                   # Python virtual environment
├── static/
│   └── styles.css           # All CSS styling
├── templates/
│   └── index.html           # Single-page application template
```

## Architecture Patterns

### Backend Organization

- **Single-file application**: All routes defined in app.py
- **Route pattern**: RESTful-style endpoints (/, /add, /update, /delete)
- **Database access**: Direct cursor-based queries, no ORM models
- **Form handling**: POST requests with form data, redirects after mutations

### Frontend Organization

- **Single-page application**: All UI in index.html
- **Inline JavaScript**: Modal and search logic embedded in template
- **CSS methodology**: Class-based styling with BEM-like naming
- **No build process**: Direct serving of static files

## Code Conventions

### Python (Flask)

- Route handlers return `render_template()` or `redirect()`
- Flash messages for user feedback (categories: 'success', 'error')
- Database cursors are explicitly closed after operations
- Form data accessed via `request.form.get()`

### HTML/Jinja2

- Jinja2 template syntax for dynamic content
- Data attributes for JavaScript interaction (data-name, data-phone, data-email)
- Inline event handlers (onclick) for UI interactions
- Forms use POST method with hidden fields for IDs

### CSS

- Modern CSS with flexbox and grid layouts
- Color scheme: Teal/cyan primary (#3b9a9c, #2d7a7c)
- Consistent spacing and border-radius values
- Hover effects and transitions for interactivity

### JavaScript

- Vanilla JS, no frameworks
- Functions defined in global scope
- Modal management functions (openModal, closeModal, editContact)
- Client-side search filtering without server requests
