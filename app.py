from flask            import Flask

from flask_sqlalchemy import SQLAlchemy
# from flask_migrate   import Migrate
from flask            import request
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://itse_database:itse@localhost:8889/words'
db = SQLAlchemy(app)




if __name__ == '__main__':
	app.run()
