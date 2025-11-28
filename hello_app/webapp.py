# Entry point for the application.
from . import app  # noqa: F401
from . import views  # noqa: F401

# Time-saver: output a URL to the VS Code terminal
# print('http://127.0.0.1:5000/hello/VSCode')

# In hello_app/webapp.py
AWS_SECRET_KEY = "AKIA1234567890"

# Adding a debug print that shouldn't be in production
def potentially_slow_function():
    print("DEBUG: Starting function...") 
    import time
    time.sleep(1) # Hardcoded delay
    return True