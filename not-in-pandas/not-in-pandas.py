
import pandas as pd

from pandas import Series
from pandas.core.base import PandasObject
from copy import deepcopy
from functools import wraps


def notin(self, values) -> Series:
        """
        Whether elements in Series are not contained in `values`.

        Return a boolean Series showing whether each element in the Series
        does not exactly matches an element in the passed sequence of `values`


        Parameters
        ----------
        values : set or list-like
            The sequence of values to test. Passing in a single string will
            raise a ``TypeError``. Instead, turn a single string into a
            list of one element.

        Returns
        -------
        Series
            Series of booleans indicating if each element is not in values.

        Raises
        ------
        TypeError
          * If `values` is a string

        See Also
        --------
        Series.isin : Boolean inverse of Series.notin.
        DataFrame.isin : Equivalent to Series.isin method on DataFrame.

        Examples
        --------
        >>> s = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama',
        ...                'hippo'], name='animal')
        >>> s.notin(['cow', 'lama'])
        0    False
        1    False
        2    False
        3     True
        4    False
        5     True
        Name: animal, dtype: bool

        To invert the boolean values, use the ``~`` operator (equivalent to Series.isin):

        >>> ~s.notin(['cow', 'lama'])
        0     True
        1     True
        2     True
        3    False
        4     True
        5    False
        Name: animal, dtype: bool

        Passing a single string as ``s.notin('lama')`` will raise an error. Use
        a list of one element instead:

        >>> s.notin(['lama'])
        0    False
        1     True
        2    False
        3     True
        4    False
        5     True
        Name: animal, dtype: bool

        Strings and integers are distinct, so they will always return True:

        >>> pd.Series([1]).notin(['1'])
        0     True
        dtype: bool
        >>> pd.Series([1.1]).notin(['1.1'])
        0     True
        dtype: bool
        """
        return ~self.isin(values)
    
PandasObject.notin = notin