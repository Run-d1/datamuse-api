import requests


def get_spelled_like(word):
    baseurl = 'https://api.datamuse.com/words'
    param = {}
    param['sp'] = word
    param['max'] = "10"
    resp = requests.get(baseurl, params=param)
    words = resp.json()
    return [d['word'] for d in words]


# print(get_spelled_like("octepus"))


def main():
    print("This program is developed to help you find the word you're looking for, ")
    print("especially when you know how it sounds but not how it is spelled :) \n")
    wrd = input('Enter the word, then press "Enter": ')
    print("\nwords that are spelled similarly to", wrd, "are:- ")
    print(get_spelled_like(wrd))


main()
