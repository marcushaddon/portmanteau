from app import db

# db.Model.metadata.reflect(db.engine)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(30))
    wordtype = db.Column(db.String(20))
    definition = db.Column(db.String(2400))

    def __init__(self, word = "", wordtype = "", definition = ""):
        self.word = word
        self.wordtype = wordtype
        self.definition = definiition

    def __repr__(self):
        return self.word + ": " + self.definition
