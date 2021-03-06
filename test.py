import re
import pronouncing
from Class_Syllable_Helper import Syllable_Helper
# (c+vc(?!v))|(c+v)|(vc) basic pattern, need to detect dipthongs

v = r"([A-Z]+[0-2]\s)"
c = r"([A-Z]+\s)"

# syllable_regex = r"(([A-Z]+\s)+([A-Z]+[0-2]\s)([A-Z]+\s)(?!([A-Z]+[0-2]\s)))|(([A-Z]+\s)+([A-Z]+[0-2]\s))|(([A-Z]+[0-2]\s)([A-Z]+\s))"
cvc = r"(([A-Z]+\s)+([A-Z]+[0-2]\s)+([A-Z]+\s)(?!([A-Z]+[0-2]\s)))"
cv = r"(([A-Z]+\s)+([A-Z]+[0-2]\s))(?!([A-Z]+[0-2]\s))"
vc = r"(([A-Z]+[0-2]\s)([A-Z]+\s))"
cvvc = r"(?P<dipthong>([A-Z]+\s)*([A-Z]+[0-2]\s){2}([A-Z]+\s))"

syllable_regex = cvvc + "|" + cvc + "|" + cv + "|" + vc


def split_phones_into_syllables(phones_string):
    phones_string += " "
    print "PHONES STRING: " + phones_string
    phones_syllables_array = []

    while len(phones_string) > 0:
        syllable_match = re.search(syllable_regex, phones_string)
        if syllable_match:
            if syllable_match.group("dipthong"):
                print "FOUND A DIPTHONG: " + syllable_match.group("dipthong")
                dipthong = syllable_match.group("dipthong")
                middle = re.search(v, dipthong).end()
                first = dipthong[:middle].rstrip()
                second = dipthong[middle:].rstrip()
                phones_syllables_array.extend([first, second])
                phones_string = phones_string.replace(dipthong, "")
            else:
                print "FOUND A NORMAL SYLLABLE: " + syllable_match.group()
                syllable = syllable_match.group()
                phones_syllables_array.append(syllable.rstrip())
                phones_string = phones_string.replace(syllable, "")
        else:
            print "COULDNT FIND SYLLABLE" + str(syllable_match)
            print phones_string
    return phones_syllables_array

word = "demagogue"
phones = pronouncing.phones_for_word(word)[0]
phones_syllables = split_phones_into_syllables(phones)
print phones_syllables

letter_syllable_array = []

helper = Syllable_Helper()
for i in range(0, len(phones_syllables)):
    letter_syllable = helper.map_letters_to_phones(word, phones_syllables[i])
    letter_syllable_array.append(letter_syllable)

print letter_syllable_array
