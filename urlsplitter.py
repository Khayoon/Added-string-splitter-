def count_strings_between_plus(input_string):
    count = 0
    if '+' in input_string:
        parts = input_string.split('+')
        count = len(parts) - 1
    return count

#  input
string = " "

count = count_strings_between_pluses(string)

print(f"'{string}' has {count} strings.")
