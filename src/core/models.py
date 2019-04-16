from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# Shared db module for todo and user models.
db = SQLAlchemy()