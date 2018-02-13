# bsetools

Helps to get bse quotes from bseindia.com. 

```python
from bsetools import bsetools

obj = bsetools()
print(obj.get_quote('Infosys'))

#[1] 1103.80

```

In case if wrong stock names are given which does not match it returns the message accordingly.

```python 

obj = bsetools()
print(obj.get_quote("acdfssklmkfv"))

#No relevant share price found for acdfssklmkfv

```



