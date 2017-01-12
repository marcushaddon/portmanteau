import pronouncing
from model import db, Word

class Portmanteau_Helper:
    def get_matches(self, string, page_size = 20, page = 1):
        # Initialize a Word from the word we get so we can get its last phones
        word = Word(string)
        last_phones = word.last_phones

        # Pagination stuff
        start = page_size * page
        stop = start  + page_size

        # Format phones for pronouncing
        search_string = "^" + " ".join(last_phones)
        matches = pronouncing.search(search_string)

        # See which of these have entries in our english dictionary
        filtered_matches = db.session.query(Word).distinct(Word.word).group_by(Word.word).filter(Word.word.in_(matches)).all() # need to do pagination HERE
        return filtered_matches
