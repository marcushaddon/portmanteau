from model import db
from model import Word
from sqlalchemy import func

word = "Dog"

def update_word(word):
    if word.leading_phones == None:
        sylls = ','.join(word.first_phones)
        word.leading_phones = sylls
        result = db.session.commit()


# latest = db.session.query(func.min(Word.id)).filter(Word.leading_phones==None).first()[0]
# last = latest + 10000

def update_words(words):
    total = len(words)
    print "Updating " + str(total) + " records."
    for i in range(0, total):
        if i % 100 == 0:
            print "Progress: {0} of {1}".format(i, total)
        update_word(words[i])

def update_all_words():
    alphabet = 'E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
    for letter in alphabet:
        all_words = Word.query.filter(Word.word.like(letter+'%')).all()
        print "NOW ON LETTER " + letter
        update_words(all_words)

# all_words = Word.query.filter(Word.id.between(latest, last)).all()
# all_words = Word.query.filter(Word.word.like('E%')).all()
# update_words(all_words)


update_all_words()
