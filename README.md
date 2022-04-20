# URLSearchParams
The URLSearchParams interface defines utility methods to work with the query string of a URL.

## URLSearchParams().getAll()
The getAll() method of the URLSearchParams interface returns all parameter as an array. 

### Syntax

```py
URLSearchParams().getAll()
```

### Examples

```py
from URLSearchParams import URLSearchParams

src = URLSearchParams("https://www.google.com?q=python")
print(src.getAll())

>>> ['q=python']
```

## URLSearchParams().get()
The get() method of the URLSearchParams interface returns the first value associated to the given search parameter. 

### Syntax
```py
URLSearchParams(url).get(name)
```

### Examples

```py
from URLSearchParams import URLSearchParams

src = URLSearchParams("https://www.google.com?q=python")
print(src.get("q"))

>>> 'python'
```

## URLSearchParams().append()
The append() method of the URLSearchParams interface appends a specified key/value pair as a new search parameter.

### Syntax
```py
URLSearchParams(url).append({name : value})
```

### Examples

```py
from URLSearchParams import URLSearchParams

src = URLSearchParams("https://www.google.com?q=python")
print(src.append({"lang" : "en"}))

>>> 'https://www.google.com?q=python&lang=en'
```

## License
- [The Unlicense](https://unlicense.org/)