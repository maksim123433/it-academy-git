def translation(s : str):
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
    result = 0
    interval = 0
    for char_index in range(len(s) - 1):
        if roman_to_int[s[char_index]] >= roman_to_int[s[char_index + 1]]:
            result += roman_to_int[s[char_index]] - interval
            interval = 0
        else:
            interval += roman_to_int[s[char_index]]
    result += roman_to_int[s[-1]] - interval
    return result
s = 'MMMMMMMMCMXLIX'
print(translation(s))
