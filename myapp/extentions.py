from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

babel=Babel()
migrate=Migrate()
db=SQLAlchemy()