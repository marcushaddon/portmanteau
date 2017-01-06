# ABOUT: A dictionary having for it's keys ARPAbet phonetic symbols, and for
# each key's value a regular expression that SHOULD match all letters or
# combinations of letters capable of producing the phoneme in the key.
# Regex's will match letter (combos) even when they are not nessecarily
# producing this phoneme, but that shouldn't be a problem for my purpose.

# NOTE: put 'ea' before 'e' in regex or it will just capture the 'e' in 'ea' and quit!
# NOTE: HOLY SHIT i might be able to search the prounouciaiton dictionary by
# phoneme to write huge tests for each one of these to make sure they work

phoneme_map = {
'AA': r"(a[hw]*)|o",
'AE': r"a",
'AH': r"[au]h*",
'AO': r"o|a",
'AW': r"ow",
'AY': r"ei|y|i",
'B': r"b",
'CH': r"ch",
'D': r"d",
'DH': r"th",
'EH': r"e",
'ER': r"[ieu]re*", # er|ir|ur|or ?
'EY': r"ay|e[iy]", #hmmm
'F': r"f",
'G': r"g",
'HH': r"h",
'IH': r"i|u|e",
'IY': r"ea|ie|e+|y|i", # hmmm
'JH': r"j|d*ge*",
'K': r"k|c",
'L': r"l",
'M': r"m",
'N': r"n",
'NG': r"ng",
'OW': r"ow*a*",
'OY': r"oy*i*",
'P': r"p+",
'R': r"r+",
'S': r"s+|c", #tricky
'SH': r"[sc]h", # hmm, z?
'T': r"t",
'TH': r"th",
'UH': r"oo|oul",
'UW': r"o[ou]|ew",
'V': r"v",
'W': r"wh*",
'Y': r"y",
'Z': r"z",
'ZH': r"s" # hmm
}

# output should be:
# [['mar', ['M', 'AA', 'R']], ['cus', ['K', 'AH', 'S']] ]

# def phones_to_syllables(syllable_array, phone_string, map):
    # initialize mapped_syllables nested array (each inner array containing [ 'syllable_string', [] ])

    # split phone_string into phones_array (or tuple?) and strip out accent numbers

    # last_assigned_phone_index = 0

    # for s in syllables_array
        # for p in phones_array[last_assigned_phone_index + 1 :]
            # if this phone's regex gets a result when searched (with case insensitive flag) against the current syllable
                # push this phone onto the second index (syllable_phones_array) of mapped_syllables[s]
                # last_assigned_phone_index++ (or maybe phones_array.indexof(phone)? )
            # else if the current index in mapped_syllables_array has no phones in its syllable_phones_array
                    # push this phone onto the previous index of mapped_syllables_array
                    # print error
            # else break loop (to move onto next syllable)

    # return mapped_syllables_array

syllables = ['mar', 'cus']
phones_array = ['M', 'AA', 'R', 'K', 'AH', 'S']
phones = [u'M AA1 R K AH0 S']


print phones_to_syllables(syllables, phones[0], phoneme_map)
