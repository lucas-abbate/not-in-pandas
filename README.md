# not-in-pandas

 Adds notin method to pandas.Series and pandas.DataFrame objects. Returns exactly the same as negating `isin`.

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install not-in-pandas.

```bash
pip install not-in-pandas

```

## Usage

```python
import pandas as pd
import not_in_pandas

# on Series
>>> s = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama', 'hippo'], name='animal')
>>> s.notin(['cow', 'lama'])

0    False
1    False
2    False
3     True
4    False
5     True
Name: animal, dtype: bool


# on DataFrame
>>> df = pd.DataFrame(
...   {
...    "animal_a": ["lama", "cow", "lama", "beetle", "lama"],
...    "animal_b": ["cow", "beetle", "cow", "hippo", "lama"]
...   }
... )

>>> df.notin(['cow', 'lama'])

   animal_a  animal_b
0     False     False
1     False      True
2     False     False
3      True      True
4     False     False
5      True      True
```

## Why this isn't already on Pandas?

Pandas core developers thought this method would be redundant, because you achieve the same results by negating a isin method `~Series.isin(['lama', 'cow'])`. And main files on the Pandas package are already huge and difficult to navigate, so I understand their reluctancy on adding more unnecessary stuff.

I personally think this method:

- Improves readability a lot, specially with nested conditions
- Keeps consistency with other `not` methods like `Series.notna` or `Series.notnull`
- Is consistent with raw Python logic `a not in b`
- Makes starting programmers less annoyed because they don't find a method they think should exist (and avoids a Google search), specially if they know that `.notna` already exists
- I use `.isin` a lot
