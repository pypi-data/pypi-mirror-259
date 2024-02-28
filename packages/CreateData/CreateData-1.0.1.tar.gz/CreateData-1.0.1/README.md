
# CreateData
[![PyPI - Version](https://img.shields.io/pypi/v/CreateData?style=flat-square&logo=PyPI&logoColor=white)](https://pypi.org/project/CreateData/)

When you need to come up with a test dataset quickly.
## Python
```python
pip install CreateData
```
and you need to install:
```python
pip install pandas numpy python-dateutil
```
## Fast and easy data generation N-row
```python
import CreateData.create_data as cd

cd.EasyData().gnrt({'size':1000}, easy=True)
```  
  
**Output example:**
| id|    date    |  bool |int|   float  |   str    |
| - |:----------:|:-----:| -:| --------:| -------- |
| 0 | 2023-07-17 | False | 6 | 5.776716 | ITYELsf  |
| 1 | 2024-01-01 | True  | 8 | 6.385161 | kvGhRr   |
| 2 | 2023-04-01 | False | 3 | 3.418855 | Ur       |
| 3 | 2023-11-06 | True  | 8 | 5.984482 | PZqwSJaO |
| 4 | 2023-07-16 | False | 1 | 4.696562 | yvye     |


## Need more columns and their customizations?
```python
params = cd.EasyData().get_params()
```
Output:  

*{'size': 100,
 'date': {'col': 1, 'min_date': '2023-02-27', 'max_date': '2024-02-27'},
 'bool': {'col': 1},
 'int': {'col': 1, 'min_int': 1, 'max_int': 10},
 'float': {'col': 1, 'min_float': 1, 'max_float': 10},
 'str': {'col': 1, 'min_str': 1, 'max_str': 10, 'dgts': False, 'pctn': False}}*

small clarification:  
max_date <- now()  
min_date <- max_date - 1 year  

## Edit the dictionary and pass it to the function
```python
cd.EasyData().gnrt(params)
```