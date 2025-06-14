def process_string(s):
    vowels = "aeiouAEIOU"
    vowel_str = ""
    consonant_str = ""

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_str += char
            else:
                consonant_str += char

    return (vowel_str, len(vowel_str), consonant_str)
