import pandas as pd
import re
from openpyxl.workbook import Workbook

file = "chat.txt"

mobile_list=[]
with open(file) as f:
	for line in f:
		text=line
		phoneNumRegex = re.compile(r'[789]\d{9}',re.VERBOSE)
		for groups in phoneNumRegex.findall(text):
			#print(groups)
			mobile_list.append(groups)
df=pd.DataFrame()
n=len(mobile_list)
df['Phone No']=mobile_list[0:(n+1)]
df.to_excel("r2.xlsx",index=False)
