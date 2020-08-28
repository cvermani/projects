import requests
import pandas as pd
import numpy as np
url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=ECON&course=101'

html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[0]
pos=0

con1 = df.iloc[:,0].values
con2 = df.iloc[:,2].values

flag = False
for item in con2:
	
	if  item == 'Web-Oriented Course':
		x = df.iloc[pos:pos+1, 0].values
		if x != 'Full' and x!='STT' and x!='Restricted' :
			
			flag = True
			break
	pos+=1
if flag==True:
	print('SPOT IS AVAILABLE')
else:
	print('no space yet :/')