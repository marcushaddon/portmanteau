# ABOUT: A dictionary having for it's keys ARPAbet phonetic symbols, and for
# each key's value a regular expression that SHOULD match all letters or
# combinations of letters capable of producing the phoneme in the key.
# Regex's will match letter (combos) even when they are not nessecarily
# producing this phoneme, but that shouldn't be a problem for my purpose.

# NOTE: put 'ea' before 'e' in regex or it will just capture the 'e' in 'ea' and quit? maybe?
# NOTE: HOLY SHIT i might be able to search the prounouciaiton dictionary by
# phoneme to write huge tests for each one of these to make sure they work

# NOTE: Current trouble spots: the last syllable in words where syllables are
# divided between double consonants ('ly' in silly, 'py' in happy), only get
# mapped to the phoneme for the vowel, since the phoneme for the consonant is
# mapped to the first consonant in the previous syllable


import re
class Syllable_Helper:

    phoneme_map = {
    'AA': r"(a[hw]*)|o",
    'AE': r"a",
    'AH': r"[auo+ei]h*|ou", #r"[au]h*"
    'AO': r"oa*|a", #oa*
    'AW': r"[ao][wu]",
    'AY': r"ei|y|i",
    'B': r"[bp]",
    'CH': r"c+h*|t",
    'D': r"d",
    'DH': r"th",
    'EH': r"[ea]",
    'ER': r"h*[iaoeu]r+e*",
    'EY': r"ay|e[iy]|a", #hmmm
    'F': r"f|[gp]h",
    'G': r"[gx]",
    'HH': r"w*h",
    'IH': r"[iuey]",
    'IY': r"ea|ie|e+|y|i", # hmmm
    'JH': r"j|d|d*ge*",
    'K': r"[kcxq]",
    'L': r"l",
    'M': r"m",
    'N': r"ne*",
    'NG': r"ng*",
    'OW': r"ow*a*|e[(au)w]",
    'OY': r"oy*i*",
    'P': r"p+",
    'R': r"r+e*",
    'S': r"s+e*|c|x", #tricky
    'SH': r"[sc]h|[tc]i|x|s+", # hmm, z?
    'T': r"t+|ed",
    'TH': r"th",
    'UH': r"o[ou]*|o*ul*",
    'UW': r"o*[ou]+|ew", # o[ou]|ew
    'V': r"v",
    'W': r"u|q|wh*|o",
    'Y': r"[yu]",
    'Z': r"[zsx]",
    'ZH': r"s|ge*" # hmm
    }

    syllable_regex = r"(([A-Z]+\s)+([A-Z]+[0-2]\s)([A-Z]+\s)(?!([A-Z]+[0-2]\s)))|(([A-Z]+\s)+([A-Z]+[0-2]\s))|(([A-Z]+[0-2]\s)([A-Z]+\s))"

# output should be:
# [['mar', ['M', 'AA', 'R']], ['cus', ['K', 'AH', 'S']] ]

    # Map phones to broken syllables
    def phones_to_syllables(self, syllables_array, phones_string):
        # print "----------NEW TEST---------"

        # initialize mapped_syllables nested array (each inner array containing [ 'syllable_string', [] ])
        mapped_syllables_array = map(lambda syllable: [syllable, []], syllables_array)

        # split phone_string into phones_array (or tuple?)
        phones_array = phones_string.split(" ")

        # and strip out accent numbers
        # phones_array = map(lambda string: re.sub(r"\d", "", string), phones_array)
        phone_bookmark = 0

        # loop through syllables array
        for syllable_index in range(0, len(syllables_array)):
            syllable = syllables_array[syllable_index]
            # print "Current syllable: " + syllable

            # loop through phones array starting after last assigned phone
            for phone_index in range(phone_bookmark, len(phones_array)):
                phone = phones_array[phone_index]
                # print "Current phone: " + phone

                # see if this phone's regex gets a result when searched (with case insensitive flag) against the current syllable
                pattern = self.phoneme_map[re.sub(r"\d", "", phone)]
                match = re.search(pattern, syllable)
                if match:

                    # push this phone onto the second index (syllable_phones_array) of mapped_syllables[s]
                    mapped_syllables_array[syllable_index][1].append(phone)

                    # remove the matched bit so we wont match against it again NOT SURE ABOUT THIS
                    # print("Found match for {0} in {1}".format(phone, syllable))
                    syllable = syllable[match.end():]
                    phone_bookmark = phone_index + 1 # (or maybe++? )

                # else if this phone doesnt match this syllable and the current index in mapped_syllables_array has no phones in its syllable_phones_array
                elif len(mapped_syllables_array[syllable_index][1]) == 0:

                    # push this phone onto the previous index of mapped_syllables_array
                    mapped_syllables_array[syllable_index - 1][1].append(phone)
                    phone_bookmark = phone_index + 1

                    # print error
                    # print("Could not find match in {0} for {1}, mapping to previous syllable for now.".format(syllable, phone, syllables_array[syllable_index - 1]))

                # else break loop (to move onto next syllable without updating phone_bookmark so we will keep going with this phone)
                else:
                    # print("Couldn't find match for {0} in {1}, moving on...".format(phone, syllable))
                    break;


        return mapped_syllables_array

    # Extract letter group from word that corresponds to a group of phones
    def map_letters_to_phones(self, word, phones_string):
        master_pattern = r""
        phones_array = phones_string.split(" ")
        for phone in phones_array:
            pattern = self.phoneme_map[re.sub(r"\d", "", phone)]
            master_pattern += "(" + pattern + ")"

        match = re.search(master_pattern, word, re.IGNORECASE)
        if match:
            return match.group()
        else:
            print "Why was " + word + " a match for " + phones_string
            return ""

    def split_phones_into_syllables(self, phones_string):
        phones_string += " "
        phones_syllables_array = []

        while len(phones_string) > 0:
            syllable_match = re.search(self.syllable_regex, phones_string)
            if syllable_match:
                syllable = syllable_match.group()
                phones_syllables_array.append(syllable.rstrip())
                phones_string = phones_string.replace(syllable, "")
            else:
                # TEMPORARY
                print "SYLLABLE HELPER OUT OF IDEAS"
                phones_syllables_array[-1] += phones_string.rstrip()
                phones_string = ""

        return phones_syllables_array
