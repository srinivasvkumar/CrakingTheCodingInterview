
def strreplace(str):
    le = len(str)
    newar = []
    for ch in str:
        if ch == ' ':
            newar.append('%20')
        else:
            newar.append(ch)
    return newar


# def urlify(string, length):
#     '''function replaces single spaces with %20 and removes trailing spaces'''
#     new_index = len(string)
#     string1 = ""

#     for i in reversed(range(length)):
#         if string[i] == ' ':
#             # Replace spaces
#             string1[new_index - 3:new_index] = '%20'
#             new_index -= 3
#         else:
#             # Move characters
#             string1[new_index - 1] = string[i]
#             new_index -= 1

#     return string1


length = 24
test_string = 'much ado about nothing      '

st = ''.join(strreplace(
    "every human is a good person, there are a billion such people     "))
print("replacing empty space", st)


# print("replace by index",  urlify(test_string, length))
