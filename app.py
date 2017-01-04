from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script     import Manager
from flask_migrate    import Migrate, MigrateCommand
from flask            import request
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://itse_database:itse@localhost:8889/words'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)




if __name__ == '__main__':
	app.run()
