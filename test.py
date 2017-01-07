from Class_Syllable_Helper import Syllable_Helper
import pronouncing as p
import hyphenate as h

myguy = Syllable_Helper()

def test_word(word):
    phones = p.phones_for_word(word)
    if len(phones) < 1:
        print "Couldnt get phones for: " + word
        return
    phone_string = phones[0]
    syllables = h.hyphenate_word(word)
    if not syllables:
        print "Couldnt get syllables for: " + word
        return
    result = myguy.phones_to_syllables(syllables, phone_string)
    print "RESULT FOR >>" + word + "<<"
    for piece in result:
        print piece[0] + ": " + ' - '.join(piece[1])

word_list = [
'dog',
'pizza',
'airplane',
'cricket',
'Silly', # might need to handle split between double consonants
'bumper'
]

def run_test(word_list):
    for word in word_list:
        test_word(word)





run_test(word_list)
