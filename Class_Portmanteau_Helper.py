import pronouncing
from model import db, Word
import re
from Class_Syllable_Helper import Syllable_Helper

class Portmanteau_Helper:
    def get_matches(self, string, page_size = 20, page = 1):
        # Initialize a Word from the word we get so we can get its last phones
        word = Word(string)
        last_phones = word.last_phones

        # Pagination stuff
        start = page_size * page
        stop = start  + page_size

        # Format phones for pronouncing
        # Evenutally this will be a dynamically selected regex
        search_string = " ".join(last_phones)
        matches = pronouncing.search("^" + search_string)

        # See which of these have entries in our english dictionary
        filtered_matches = db.session.query(Word).distinct(Word.word).group_by(Word.word).filter(Word.word.in_(matches)).all() # need to do pagination HERE
        return { "overlapping_phones": search_string, "matches": filtered_matches }

    def make_portmanteau(self, word1, word2_obj, overlapping_phones):
        s = Syllable_Helper()
        # Eventually we will not be given over_lapping_phones, but over_lapping_phones_regex, and we'll have to derive the overlapping phones using the regex and the phones for the word
        # might be from word1 in some cases
        letters_to_remove = s.syllable_from_phones(word2_obj.word, overlapping_phones)

        second_part = re.sub(letters_to_remove, "", word2_obj.word)
        portmanteau = word1 + second_part

        result = {
        "portmanteau": portmanteau,
        "word1": word1,
        "word2": word2_obj.word
        }

        return result

    def get_portmanteaus(self, word):
        candidates = self.get_matches(word)
        portmantarray = []
        for candidate in candidates["matches"]:
            portmanteau = self.make_portmanteau(word, candidate, candidates["overlapping_phones"])
            portmantarray.append(portmanteau)

        return portmantarray
