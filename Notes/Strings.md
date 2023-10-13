Strings are a [[Type]] of data

# [Format Strings](https://github.com/teacherubial/slss-programming-2023-24/blob/main/Notes/Strings.md#format-strings)

If we want to evaluate inside of a string, we use _f-strings_.  
To create an f-string, we put an `f` before the open quote

```python
fave_food = input("What's your favourite food? ")

print(f"Ooooooo, {fave_food} sounds good!")
```

# [String Methods](https://github.com/teacherubial/slss-programming-2023-24/blob/main/Notes/Strings.md#string-methods)

[[Methods]] are functions that we can use on [[Objects]].

String methods allow us to modify strings.

Say for example, we want to make all the characters of a string lowercase.

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())
```

We can use string methods to help solve [[Errors#Semantic Errors|semantic errors]].

## [`.lower()`](https://github.com/teacherubial/slss-programming-2023-24/blob/main/Notes/Strings.md#lower)

The `.lower()` method takes a string and converts all uppercase characters to lowercase.

## [`.upper()`](https://github.com/teacherubial/slss-programming-2023-24/blob/main/Notes/Strings.md#upper)

The `.upper()` method uppercases all the letters.

## [`.strip(chars)`](https://github.com/teacherubial/slss-programming-2023-24/blob/main/Notes/Strings.md#stripchars)

The `.strip()` method **removes** characters from both the beginning and the end of the string.

```python
user_feeling = input("How are you feeling today? ")

# "good!" "good." "Good!" "good!!!!!!!!!!!!!"
if user_feeling.lower().strip("!.,") == "good":
	print("That's great!")
```

## [`.split(str) -> List`](https://github.com/teacherubial/slss-programming-2023-24/blob/main/Notes/Strings.md#splitstr---list)

The `.split()` method splits a string into a [[List|list]], separating the string based on the characters you give it.

```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_str.split(" ")
```