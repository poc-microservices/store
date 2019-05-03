import os

from core import app

# Load user, and todo module to the application
import health
import store
import channel

if __name__ == '__main__':
    app.run()