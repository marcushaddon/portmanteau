from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script     import Manager
from flask_migrate    import Migrate, MigrateCommand
from flask            import request
# wrapper around hyphenate_word so everything doesnt break if we rewrite that later
from hyphenate        import hyphenate_word as word_to_syllables
import pronouncing
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://itse_database:itse@localhost:8889/words' # eventually make this be from shared config file
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class Word(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    word            = db.Column(db.String(30))
    wordtype        = db.Column(db.String(20))
    definition      = db.Column(db.String(2400))
    leading_phones  = db.Column(db.String(20))
    trailing_phones = db.Column(db.String(20))

    @property
    def syllables(self):
        return word_to_syllables(self.word)

    @property
    def leading_syllable(self):
        return self.syllables[0]

    @property
    def trailing_syllable(self):
        return self.syllables[-1]

    @property
    def first_phone(self):
        if self.leading_phones:
            return self.leading_phones
        else:
            phones = pronouncing.phones_for_word(self.leading_syllable)
        return phones

    @property
    def last_phone(self):
        if self.trailing_phones:
            phones = self.trailing_phones
        else:
            # To be replaced with method to actually get it
            phones = pronouncing.phones_for_word(self.trailing_syllable)
        return phones

    def __init__(self, word = "", wordtype = "", definition = ""):
        self.word       = word
        self.wordtype   = wordtype
        self.definition = definition

    def __repr__(self):
        return self.word + ": " + self.definition



if __name__ == '__main__':
	manager.run()
