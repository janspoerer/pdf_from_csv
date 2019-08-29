# For managing tables properly
import pandas as pd
from pandas import DataFrame

# For saving strings as CSV
import pdfkit

# Reading data
test = pd.read_csv('test.CSV', sep=',')

# Adjusting the format
test_string = """
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
"""
for index, row in test.iterrows():
        test_string += row['Body'] + '<br><br><br>'

test_string += """
</body>
</html>
"""

# Creating an intermediary HTML file
generated_html = open("generated_html.html", "w")
generated_html.write(test_string)
generated_html.close()

# Generating the PDF
pdfkit.from_file('generated_html.html', 'out.pdf')

