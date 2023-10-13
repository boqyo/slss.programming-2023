## Search - A Practical ExampleWe can implement a basic type of search algorithm using loops, one is called [linear search]([https://en.wikipedia.org/wiki/Linear_search](https://en.wikipedia.org/wiki/Linear_search)).It goes something like this:```pseudocodeish  
for <item> in <list>:  
if <item> == <item you want to find>:  
<do something with the item>  

```Here's a practical example. Let's say that we're looking to see if Jasmine Soto is in the list. We can do this:```python  
names = ['Elizabeth Singleton', 'Raymond Mitchell', 'Steven Murphy', 'Daniel Terry', 'Glenn Fisher', 'Jasmine Soto', 'Deborah Hicks', 'Beverly Ryan', 'Jason Smith', 'Jason Washington']for name in names:  
if name == "Jasmine Soto":  
print("We found her!")
## Iterating *n* Number of TimesWe can iterate/loop for any number of times.  
Repeating as many times as we want  
In Python, we do it in a strange way.  

for i in range(<positive integer>):  
<code block>  
e.g. 
# print out "Mr. Ubial is pretty cool" 20 times
for _ in range(20):
print("Mr. Ubial is pretty cool") 
Recall that in the other way of looping (for `item` in `list`). That `item` points at the current item in the list.In this way of looping, that `item` thing shows us how many times we've looped since the beginning.For example, we can do something like this
# Repeat something 5 times and we want to keep track of
# of how many iterations we've completedfor i in range(5):  
print(i)  

Simply put, `i` is a counter. It counts how many times we're looping.