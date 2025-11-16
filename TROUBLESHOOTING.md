# Troubleshooting MySQLdb.OperationalError

## Common Causes & Solutions

### 1. MySQL Server Not Running
**Check if MySQL is running:**
```bash
# Windows
net start | findstr MySQL

# Or check services
services.msc
```

**Start MySQL:**
```bash
net start MySQL
```

### 2. Wrong Port Number
Your app uses port **3307** (non-standard). Check if MySQL is actually running on this port.

**Test connection:**
```bash
mysql -h localhost -P 3307 -u root -p
```

If this fails, your MySQL might be on the default port **3306**. Update `.env`:
```
DB_PORT=3306
```

### 3. Database Doesn't Exist
**Create the database:**
```bash
mysql -h localhost -P 3307 -u root -p < database_setup.sql
```

Or manually:
```sql
CREATE DATABASE IF NOT EXISTS contact_book;
USE contact_book;
-- Run the rest of database_setup.sql
```

### 4. Wrong Password
Verify your password in `.env` matches your MySQL root password.

### 5. MySQL Not Installed
If MySQL isn't installed, download from: https://dev.mysql.com/downloads/mysql/

## Quick Diagnostic

Run the app - it will now show detailed connection info:
```bash
python app.py
```

Look for the output showing which host/port/user it's trying to connect to.
