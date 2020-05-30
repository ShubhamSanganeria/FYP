import pandas as pd
import numpy as np
import random
x=[]
for i in range(100):

	temp=random.randrange(98,103)
	hum=random.randrange(58,85)
	if temp>100:
		bpm=random.randrange(110,140)
	else:
		if hum>70:
			bpm=random.randrange(110,140)
		else:
			bpm=random.randrange(60,100)

	
	x.append([temp,bpm,hum])

data=np.array(x)

my_data=pd.DataFrame(data,columns=['Body Temperature','BPM','Humidity'])

my_data.to_csv(r'C:\Users\PC\Desktop\FYP\result.csv',index=False,header=True)
print(my_data.head())