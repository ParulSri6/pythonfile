def sum_of_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum


def count_vowels(s):
    vowels = set('aeiou')
    count_vowels = 0
    for char in s.lower():
        if char in vowels:
            count_vowels += 1
    return count_vowels


def reverse_string(s):
    return s[::-1]


def replace_consonants(s):
    input_string = ""
    vowels = set('aeiouAEIOU')
    for char in s:
        if char.isalpha() and char.lower() not in vowels:
            input_string += "*"
        else:
            input_string += char
    return input_string


def find_maximum(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[:n]


def pig_latin(s):
    words = s.split()
    vowels = "aeiouAEIOU"
    translated_words = []

    for word in words:
        if word[0] in vowels:
            translated_words.append(word + "way")
        else:
            translated_words.append(word[1:] + word[0] + "ay")

    return ' '.join(translated_words)


def number_replacer(numbers, old, new):
    replaced_list = []
    for num in numbers:
        if num == old:
            replaced_list.append(new)
        else:
            replaced_list.append(num)
    return replaced_list


def fizzpop(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzPop")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Pop")
        else:
            result.append(str(i))
    return result


# Bonus functions
def caesar_encode(s, k):
    encoded = []
    for char in s:
        if char.isalpha():
            shift = k % 26
            base = ord('A') if char.isupper() else ord('a')
            encoded.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            encoded.append(char)
    return ''.join(encoded)


def caesar_decode(s, k):
    decoded = []
    for char in s:
        if char.isalpha():
            shift = -k % 26  # Negate k to reverse the encoding shift
            base = ord('A') if char.isupper() else ord('a')
            decoded.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            decoded.append(char)
    return ''.join(decoded)


if __name__ == '__main__':
    sum_of_even_numbers([1, 2, 3, 4, 5])
    count_vowels("hello world")
    reverse_string("hello")
    replace_consonants("hello")
    find_maximum([1, 2, 3, 4, 5])
    merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
    fibonacci(10)
    pig_latin("hello world")
    number_replacer([1, 2, 3, 2, 4], 2, 5)
    fizzpop(5)
    caesar_encode("hello", 3)
    caesar_decode("khoor", 3)
