from model import Word, db
import pronouncing
from Class_Syllable_Helper import Syllable_Helper
import csv

helper = Syllable_Helper()
phones = helper.phoneme_map

def test_phones():
    for phone, pattern in phones.iteritems():
        test_phone(phone, pattern)

def test_phone(phone, pattern):
    print "Now testing " + phone
    phones_result = pronouncing.search(phone + '[0-2]*')
    filtered_results = db.session.query(Word).distinct(Word.word).group_by(Word.word).filter(Word.word.in_(phones_result)).all()
    total = len(filtered_results)
    total_failed = 0
    with open('phone_mapping_test_results/' + phone + '.csv', 'w') as csvfile:
        fieldnames = ['phone', 'word string', 'phones_array', 'total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for result in filtered_results:
            word = result.word
            mapped_letters = helper.map_letters_to_phones(word, phone)
            if len(mapped_letters) < 1:
                total_failed += 1
                writer.writerow({'phone': phone, 'word string': word, 'phones_array': result.phones})

        writer.writerow({'phone': 'success:', 'word string': total_failed, 'phones_array': 'out of', 'total': str(total)})

phone = 'AA'
test_phones()
