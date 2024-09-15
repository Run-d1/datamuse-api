import requests


def get_sounds_alike(word):
    baseurl = 'https://api.datamuse.com/words'
    param = {}
    param['rel_hom'] = word
    param['max'] = "10"
    resp = requests.get(baseurl, params=param)
    words = resp.json()
    return [d['word'] for d in words]


# print(get_sounds_alike('red'))
# print(get_sounds_alike("read"))

# ['read', 'redd', 'reade']
# ['red', 'reed', 'reid', 'redd', 'reade', 'ried', 'wrede', 'riede']


def main():
    print("This program is designed to provide you with words that might sound similar or even have the same "
          "pronunciation!")
    wrd = input('Enter a word, then press "Enter": ')
    print("\nwords that sound like", wrd, "are:- ")
    print(get_sounds_alike(wrd))


main()
