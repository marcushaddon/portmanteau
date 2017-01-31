import pronouncing
from model import db, Word
import re
from Class_Syllable_Helper import Syllable_Helper

class Portmanteau_Helper:
    def get_matches(self, string, page_size = 20, page = 1):
        # Pagination stuff
        start = page_size * (page - 1)
        stop = start  + page_size

        # Initialize a Word from the word we get so we can get its last phones
        word = Word(string)
        last_phones = word.last_phones

        search_pattern = self.choose_search_pattern(last_phones)
        print "SEARCH PATTERN " + search_pattern
        matches = pronouncing.search("^" + search_pattern)

        # See which of these have entries in our english dictionary
        filtered_matches = db.session.query(Word).distinct(Word.word).group_by(Word.word).filter(Word.word.in_(matches)).offset(start).limit(page_size).all() # need to do pagination HERE
        return { "overlapping_phones_regex": search_pattern, "matches": filtered_matches }

    def make_portmanteau(self, word1, word2_obj, overlapping_phones_regex):

        s = Syllable_Helper()
        # Eventually we will not be given over_lapping_phones, but over_lapping_phones_regex, and we'll have to derive the overlapping phones using the regex and the phones for the word
        # might be from word1 in some cases
        pronounciations = word2_obj.phones
        possible_pronounciation = 0
        possible_pronounciations = len(pronounciations)
        # print word2_obj.word + " HAS " + str(possible_pronounciations) + " pronunciations"
        pronounciation = pronounciations[possible_pronounciation]
        match = re.search(overlapping_phones_regex, pronounciation)

        while possible_pronounciation < possible_pronounciations and match == None:
            possible_pronounciation += 1
            pronounciation = word2_obj.phones[possible_pronounciation]
            match = re.search(overlapping_phones_regex, pronounciation)

        if match:
            overlapping_phones = match.group()
            letters_to_remove = s.map_letters_to_phones(word2_obj.word, overlapping_phones)

            # TODO: This is a stopgap solution (throws page size off!)
            if len(letters_to_remove) > 0:
                if (len(word2_obj.word) - len(letters_to_remove) < 4):
                    result = False
                else:
                    second_part = re.sub(letters_to_remove, "", word2_obj.word)
                    portmanteau = word1 + second_part

                    result = {
                    "portmanteau": portmanteau,
                    "word1": word1,
                    "word2": word2_obj.word
                    }
            else:
                result = False
        else:
            print "Why was " + pronunciation + " a match for " + over_lapping_phones_regex


        return result

    def choose_search_pattern(self, trailing_phones):
        s_helper = Syllable_Helper()
        phones_string = " ".join(trailing_phones) + " "
        print "INPUT: " + phones_string
        v_replace = re.sub(s_helper.v, 'v ', phones_string)
        pattern = re.sub(s_helper.c, 'c ', v_replace)

        print "PATTERN: " + pattern

        if pattern == 'c v c ':
            template = s_helper.c + '*' + s_helper.v + trailing_phones[-1]
        elif pattern == 'c v ':
            template = s_helper.c + trailing_phones[-1]
        elif pattern == 'v c c ':
            template = s_helper.v + trailing_phones[-2] + " " + trailing_phones[-1]
        else:
            template = trailing_phones[-1]

        #temp
        search_pattern = trailing_phones[-1]
        return template

    def get_portmanteaus(self, word, page_size=20, page=1):

        candidates = self.get_matches(word, page_size, page)
        portmantarray = []
        for candidate in candidates["matches"]:
            portmanteau = self.make_portmanteau(word, candidate, candidates["overlapping_phones_regex"])
            if portmanteau:
                portmantarray.append(portmanteau)
            else:
                print word + " failed"


        return portmantarray
