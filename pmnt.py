from model import Word, db
import pronouncing
from Class_Syllable_Helper import Syllable_Helper
from Class_Portmanteau_Helper import Portmanteau_Helper
import csv

with open('end_patterns.csv', 'w') as csvfile:
    fieldnames = ['word', 'ending_pattern']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    p_helper = Portmanteau_Helper()

    word = Word('butt')
    phones = " ".join(word.last_phones)
    matches = pronouncing.search(phones)
    for match in matches:
        match_word = Word(match)
        last_phones = match_word.last_phones
        pattern = p_helper.choose_search_pattern(last_phones)
        writer.writerow({"word": match_word, "ending_pattern": pattern})
