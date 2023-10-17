## Syntax Errors

These types of errors are ones where you run your code
and something breaks.

Relatively easy to fix.

## Semantic Errors

Semantic errors are much more challenging to fix

Semantic errors are when your code doesn't "mean" what you actually mean

```python
user_response = input("Do you like to eat food? ")

if user_response == "yes":
	print("You passed the human test.")
else:
	print("You must be some sort of robot.")
```

The problem with the above code is subtle. What I (Mr. Ubial) mean is that if the user answers with ANYTHING affirmative the code should go into the `"yes"` block.

One way to solve this problem is to use [[Strings#String Methods|String Methods]]. We can use `.lower()` to catch all permutations of capital letters.

```python
user_response = input("Do you like to eat food? ")

if user_response.lower() == "yes":
	print("You passed the human test.")
else:
	print("You must be some sort of robot.")
```