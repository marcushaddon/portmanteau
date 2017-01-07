# portmanteau
My first Flask app. It will make portmaneaus.

I have a MySQL English dictionary with words, parts of speech, and definitions.
I have a pronunciation library with a Python interface.
I have a library that does an ok (for now) job of splitting words into syllables.

I've added a column to to the MySQL database to store the pronounciation (probably
a comma seperated list of the phonemes) of the first syllable of each word. When
a user submits a word, I'll find the pronunciation of the last syllable of that
word, and then query the database for words whos first syllable's pronounciation
overlaps, and then generate all the portmanteaus.

Very much in progress. One day maybe I can use the NLTK to mash up the definitions
of each of the words to provide definitions for all the portmaneaus.
