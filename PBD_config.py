from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@127.0.0.1:3306/pets_behavior_detect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init = SQLAlchemy(app)