import requests


def get_similar_meaning(word):
    baseurl = 'https://api.datamuse.com/words'
    param = {}
    param['ml'] = word
    param['max'] = "15"
    resp = requests.get(baseurl, params=param)
    words = resp.json()
    return [d['word'] for d in words]


# print(get_similar_meaning("Bright"))


def main():
    print("This program is designed to help you find words with similar meanings.")
    wrd = input('Enter the word, then press "Enter": ')
    print("\nwords with a meaning similar to", wrd, "are:- ")
    print(get_similar_meaning(wrd))


main()
