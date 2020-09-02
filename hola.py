import numpy as np
import pandas as pd
print("")

dataflair_index =pd.date_range('1/1/2000', periods=8, freq="Y")
dataflair_index
dataflair_s1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
dataflair_df1 = pd.DataFrame(np.random.randn(8, 3), index=dataflair_index,columns=['A', 'B', 'C'])
#dataflair_wp1 = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],major_axis=pd.date_range('1/1/2000', periods=5),minor_axis=['A', 'B', 'C', 'D'])
dataflair = pd.Series(np.random.randn(1000))
dataflair.head()
dataflair.tail(3)
dataflair_df1[:2]
dataflair_df1.columns = [x.lower() for x in dataflair_df1.columns]
dataflair_df1
dataflair_s1.values
dataflair_df1.values
hola = 2+1
print("HOLA "+str(hola))
# victor.gonza.venv\lez@lasallistas.org.mx @vmgs
# //@vmgs

import PyPDF2 as pdf
pdfFileObj = open('c:\\a.pdf', 'rb')
pdfReader = pdf.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())