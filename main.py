# For managing tables properly
import pandas as pd
from pandas import DataFrame

# For saving strings as CSV
import pdfkit

test = pd.read_csv('test.CSV', sep=',')

print(test)

test_string = None
for index, row in test.iterrows():
    print(row)
    if test_string is None:
        test_string = row['Body']
    else:
        test_string = test_string + '\n\n\n\n' + row['Body']

pdfkit.from_string(test_string, 'out.pdf')
