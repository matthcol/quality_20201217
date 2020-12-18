import locale
import functools
import pandas as pd
import pytest

# wrong for fr: assert 'été' < 'étuve'
# wright for fr: assert locale.strcoll('été', 'étuve') < 0
# wrong for es: assert locale.strcoll('mano', 'mañana') < 0
# whright for es: assert locale.strcoll('mañana', 'martes') < 0

@pytest.fixture(params=[
    ('fr-FR',
     ['étage', 'étuve', 'été', 'embouteillage', 'vélo' ],
     ['embouteillage','étage', 'été', 'étuve','vélo' ]), 
    ('es-ES', ['mano', 'mañana', 'madre', 'martes'],
             [ 'madre','mano', 'mañana', 'martes'])])
def diacritiqueArgs(request):
    """
    1st param: locale
    2nd param: words to sort in this locale
    3rd param: expected sorted list
    """
    return request.param
    
def test_text_diacritique(diacritiqueArgs):
    # 1. given : args
    codeLocale, givenWords, expectedSortedwords = diacritiqueArgs
    locale.setlocale(locale.LC_ALL, codeLocale)    
    # 2. when
    givenWords.sort(key=functools.cmp_to_key(
        locale.strcoll))
    # 3. then
    assert givenWords == expectedSortedwords

    
def test_load_texte_utf8():
    #filename = 'data_utf8.csv'
    filename = 'data_latin1.csv'
    #encoding = 'UTF-8'
    encoding = 'ISO-8859-1'
    expectedVilles = [ 'Toulouse','Créteil', 'Mareuil-sur-Aÿ'] 
    # when
    data = pd.read_csv(filename, encoding=encoding, sep=';')
    # then
    assert list(data.ville) == expectedVilles
    
    
    
    
    
    
    
    
    
    
    