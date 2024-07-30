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
    merge_dicts = {**dict1, **dict2}
    merge_dicts.update(dict2)
    return merge_dicts

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def pig_latin(s):
    pig_latin = []
    for word in s.split():
        if word[0].lower() in 'aeiou':
            pig_latin.append(word + 'way')
        else:
            pig_latin.append(word[1:] + word[0] + 'ay')
    return ' '.join(pig_latin)

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
    result = ""
    for char in s:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            rotated_char = chr((ord(char) - base + k) % 26 + base)
            result += rotated_char
        else:
            result += char
    return result


def caesar_decode(s, k):
    return caesar_encode(s, -k)


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
    caesar_encode("hello")
    caesar_decode("khoor")