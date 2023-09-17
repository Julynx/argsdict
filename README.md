# argsdict
*Simple command-line argument parser.*
```
$ python example.py John Smith --age=30 --married
```
> example.py
```python
from argsdict import args

dictionary = args(['name', 'surname'])
```
> dictionary
```json
{
  "name": "John",
  "surname": "Smith",
  "--age": "30",
  "--married": true
}
```
