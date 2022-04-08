

import pandas as pd
import numpy as np


tables = pd.read_html('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')
print(tables)

df = pd.DataFrame(tables[0] , columns=['순위' , '선수명' , '팀명' , 'AVG'])
print(df)


