from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script     import Manager
from flask_migrate    import Migrate, MigrateCommand
from flask            import request
import json
from Class_Portmanteau_Helper import Portmanteau_Helper

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://itse_database:itse@localhost:8889/words'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@app.route('/api/<word>/candidates')
def get_candidates(word):
	helper = Portmanteau_Helper()
	candidates = helper.get_matches(word)
	return str(candidates["matches"])

@app.route('/api/<word>/portmanteaus')
def get_portmanteaus(word):
	page_size = request.args.get('page_size') or 20
	page = request.args.get('page') or 1
	helper = Portmanteau_Helper()
	portmanteaus = helper.get_portmanteaus(word, int(page_size), int(page))
	return json.dumps(portmanteaus)

if __name__ == '__main__':
	app.run()
