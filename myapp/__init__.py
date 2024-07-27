from flask import Flask,request,session,current_app
from flask_uploads import UploadSet,configure_uploads, IMAGES, patch_request_class
from flask_babel import lazy_gettext as _l
from config import Config
from myapp.extentions import db, migrate
import os

app=Flask(__name__)
app.config.from_object(Config)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['UPLOADED_IMAGES_DEST']=os.path.join(basedir,"static")
print(basedir)
db.init_app(app)
migrate.init_app(app,db)
images=UploadSet('images',IMAGES)
configure_uploads(app,images)
patch_request_class(app)
