from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script     import Manager
from flask_migrate    import Migrate, MigrateCommand
from flask            import request
# wrapper around hyphenate_word so everything doesnt break if we rewrite that later
from hyphenate        import hyphenate_word as word_to_syllables
from Class_Syllable_Helper import Syllable_Helper
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
        return word_to_syllables(self.word.lower())

    @property
    def leading_syllable(self):
        return self.syllables[0]

    @property
    def trailing_syllable(self):
        return self.syllables[-1]

    @property
    def first_phones(self):
        first_phones = []
        if self.leading_phones:
            first_phones = self.leading_phones
        else:
            phones = pronouncing.phones_for_word(self.word.lower())
            if len(phones) > 0:
                helper = Syllable_Helper()
                phones_result = helper.phones_to_syllables(self.syllables, phones[0])
                if phones_result:
                    first_phones = phones_result[0][1]
        return first_phones

    @property
    def last_phones(self):
        last_phones = []
        if self.trailing_phones:
            last_phones = self.trailing_phones
        else:
            # To be replaced with method to actually get it
            phones = pronouncing.phones_for_word(self.word.lower())
            if len(phones) > 0:
                helper = Syllable_Helper()
                phones_result = helper.phones_to_syllables(self.syllables, phones[0])
                if phones_result:
                    last_phones = phones_result[-1][1]
        return last_phones

    def __init__(self, word = "", wordtype = "", definition = ""):
        self.word       = word
        self.wordtype   = wordtype
        self.definition = definition

    def __repr__(self):
        return self.word + ": " + self.definition



if __name__ == '__main__':
	manager.run()
