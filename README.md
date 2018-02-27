# bsetools

Helps to get bse quotes from bseindia.com. Available on PyPI now at : https://pypi.python.org/pypi/bsetools/ 


# Instalation

```
pip install bsetools
```

# Python 2.7+

```python
from bsetools import bsetools

obj = bsetools()
print(obj.get_quote('Infosys'))

#[1] 1103.80

```

# Python 3.5+ 

```python
from bsetools import bsetools

obj = bsetools.bsetools()
print(obj.get_quote('Infosys'))

#[1] 1103.80

```

In case if wrong stock names are given which does not match it returns the message accordingly.

```python 

print(obj.get_quote("acdfssklmkfv"))

#No relevant share price found for acdfssklmkfv

```



