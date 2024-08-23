calls_ = 0


def count_calls():
    global calls_
    calls_ = calls_ + 1
    return


def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())

    print(tuple_)
    count_calls()
    return


def is_contains(string, list_to_search):
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()

    if string in list_to_search:
        print("True")
    else:
        print('False')

    count_calls()
    return


string_info("one")

string_info('toob')

is_contains('searCH', ['cambala', 'Search'])

print(calls_)
