from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
import string as st


class CreateData:
    def __init__(self):
        self.EQUAL_MAX = 1
        self.SIZE = 'size'
        self.size = 100
        self.COLUMNS_COUNT = 'col'
        self.DEFAULT_COLUMNS_COUNT = 1
        
        self.DATE = 'date'
        self.MIN_DATE = 'min_date'
        self.MAX_DATE = 'max_date'
        self.date_now = datetime.now().date()
        self.date_year_ago = self.date_now - relativedelta(years=1)
        
        self.BOOLEAN = 'bool'
        
        self.INT = 'int'
        self.MIN_INT = 'min_int'
        self.MAX_INT = 'max_int'
        self.DEFAULT_INT = [1, 10]
        
        self.FLOAT = 'float'
        self.MIN_FLOAT = 'min_float'
        self.MAX_FLOAT = 'max_float'
        self.DEFAULT_FLOAT = [1, 10]
        
        self.STR = 'str'
        self.MIN_STR = 'min_str'
        self.MAX_STR = 'max_str'
        self.DIGITS = 'dgts'  # digits
        self.PUNCUATION = 'pctn'  # punctuation marks
        self.DEFAULT_STR = [1, 10]
        
        self.functions = {
            self.DATE : self.date_type,
            self.BOOLEAN : self.boolean_type,
            self.INT : self.int_type,
            self.FLOAT : self.float_type,
            self.STR : self.str_type,
        }

    def date_type(self, params:dict = {}) -> np.ndarray:
        min_date = params[self.MIN_DATE] if self.MIN_DATE in params else self.date_year_ago
        max_date = params[self.MAX_DATE] if self.MAX_DATE in params else self.date_now
        
        return np.random.choice(pd.date_range(min_date, max_date), self.size)
    
    def boolean_type(self, params:dict = {}) -> np.ndarray:
        func = np.vectorize(lambda t: True if t else False)
        
        return func(np.random.choice([1,0], self.size))
    
    def int_type(self, params:dict = {}) -> np.ndarray:
        min_int = params[self.MIN_INT] if self.MIN_INT in params else self.DEFAULT_INT[0]
        max_int = params[self.MAX_INT] if self.MAX_INT in params else self.DEFAULT_INT[1]
        
        return np.random.randint(min_int, max_int + self.EQUAL_MAX, self.size)
    
    def float_type(self, params:dict = {}) -> np.ndarray:
        min_float = params[self.MIN_FLOAT] if self.MIN_FLOAT in params else self.DEFAULT_FLOAT[0]
        max_float = params[self.MAX_FLOAT] if self.MAX_FLOAT in params else self.DEFAULT_FLOAT[1]
        
        return np.random.uniform(min_float, max_float, self.size)
    
    def str_type(self, params:dict = {}) -> list:
        min_str = params[self.MIN_STR] if self.MIN_STR in params else self.DEFAULT_STR[0]
        max_str = params[self.MAX_STR] if self.MAX_STR in params else self.DEFAULT_STR[1]
        digits = params[self.DIGITS] if self.DIGITS in params else None
        punctuation = params[self.PUNCUATION] if self.PUNCUATION in params else None
        
        letters = st.ascii_letters
        
        if digits:
            letters += st.digits
            
        if punctuation:
            letters += st.punctuation

        return [''.join(np.random.choice(list(letters), np.random.randint(min_str, max_str + self.EQUAL_MAX))) for _ in range(self.size)]

    def gnrt(self, params:dict = None, easy:bool = False) -> pd.DataFrame:
        self.size = params[self.SIZE]
        df = pd.DataFrame()
        
        for func in self.functions.keys():
            if easy:
                df[func] = self.functions[func]()
                
            else:
                if self.COLUMNS_COUNT in params[func] and params[func][self.COLUMNS_COUNT] > 0:
                    for column in range(params[func][self.COLUMNS_COUNT]):
                        df[func + str(column)] = self.functions[func](params[func])
        
        return df
    
    def get_params(self):
        params = {
            self.SIZE: self.size,
            f'{self.DATE}':{
                f'{self.COLUMNS_COUNT}':self.DEFAULT_COLUMNS_COUNT,
                f'{self.MIN_DATE}':f'{self.date_year_ago}',
                f'{self.MAX_DATE}':f'{self.date_now}',
            },
            f'{self.BOOLEAN}':{
                f'{self.COLUMNS_COUNT}':self.DEFAULT_COLUMNS_COUNT,
            },
            f'{self.INT}':{
                f'{self.COLUMNS_COUNT}':self.DEFAULT_COLUMNS_COUNT,
                f'{self.MIN_INT}':self.DEFAULT_INT[0],
                f'{self.MAX_INT}':self.DEFAULT_INT[1],
            },
            f'{self.FLOAT}':{
                f'{self.COLUMNS_COUNT}':self.DEFAULT_COLUMNS_COUNT,
                f'{self.MIN_FLOAT}':self.DEFAULT_FLOAT[0],
                f'{self.MAX_FLOAT}':self.DEFAULT_FLOAT[1],
            },
            f'{self.STR}':{
                f'{self.COLUMNS_COUNT}':self.DEFAULT_COLUMNS_COUNT,
                f'{self.MIN_STR}':self.DEFAULT_STR[0],
                f'{self.MAX_STR}':self.DEFAULT_STR[1],
                f'{self.DIGITS}':False,
                f'{self.PUNCUATION}':False,

            }
        }
        return params
