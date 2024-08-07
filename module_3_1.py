calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string = tuple([len(string), string.upper(), string.lower()])
    return string


def is_contains(string, list_to_search):
    count_calls()
    string_up = str(string.upper())  # Для исключения влияния регистра при поиске совпадений
    list_to_search_up = [i.upper() for i in list_to_search]  # Для исключения влияния регистра при поиске совпадений
    return string_up in list_to_search_up


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
