## PyNotes

### Iterables

Ex: Lists, strings, tuples, sets, dictionaries
- Ordered sequences (lists, strings, tuples) can be indexed and sliced with [] and [n:m]
  - ex: `my_list[0]` or `my_list[0:2]`
- Dicts support indexing with keys
  - ex: `my_dict['key']`

#### Comprehension
```python
# Lists: 
[expression for item in iterable if condition]
# Sets:
{expression for item in iterable if condition}
# Dicts:
{key_expression: value_expression for item in iterable if condition}
{key_expression: value_expression for key, value in iterable if condition}

```