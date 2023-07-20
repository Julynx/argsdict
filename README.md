# argsdict
*Simple command-line argument parser.*
```python
$ python args.py John Smith --age=30 --married

from argsdict import args

arg = args(["name", "surname"])
>> {"name": "John",
    "surname": "Smith",
    "--age": "30",
    "--married": True}
```
