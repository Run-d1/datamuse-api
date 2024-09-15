import requests


def get_like_sound(word):
    baseurl = 'https://api.datamuse.com/words'
    param = {}
    param['sl'] = word
    param['max'] = "7"
    resp = requests.get(baseurl, params=param)
    words = resp.json()
    return [d['word'] for d in words]


# print(get_like_sound("read"))


def main():
    print("This program is designed to provide you with words that might sound similar or even have the same pronunciation!")
    wrd = input('Enter a word, then press "Enter": ')
    print("\nwords that sound like", wrd, "are:- ")
    print(get_like_sound(wrd))


main()
