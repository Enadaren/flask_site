import os
import confuse

app_dir=os.path.abspath(os.path.dirname(__file__))
os.environ['MYAPPDIR']=app_dir
appConfig = confuse.Configuration('MYAPPDIR')

class Config:
   SECRET_KEY="secretkey"
   WORKER_KEY="workerkey"
 # LANGUAGES = ['en', 'by']
   SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://alisa:alisa@localhost/recipes_db'
   SQLALCHEMY_TRACK_MODIFICATIONS=False
    