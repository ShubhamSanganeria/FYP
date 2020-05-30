import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('C:\\Users\\PC\\Desktop\\FYP\\result.csv')

ax1=plt.subplot2grid((6,1),(0,0),rowspan=2,colspan=1,label='Humidity')
ax2=plt.subplot2grid((6,1),(2,0),rowspan=2,colspan=1,label='Heart Rate')

ax3=plt.subplot2grid((6,1),(4,0),rowspan=2,colspan=1,label='Body Temperature')

x=[i for i in range(0,100)]


# ab_hum=[]

# for i in data['Humidity']:
# 	if i>70:
# 		ab_hum.append(i)


ax1.bar(x,data['Humidity'],label="Humidity")
leg=ax1.legend(loc=1,prop={'size':11})
leg.get_frame().set_alpha(0.3)


ax2.bar(x,data['BPM'],color='green',label="Heart Rate")
leg=ax2.legend(loc=1,prop={'size':11})
leg.get_frame().set_alpha(0.3)



ax3.bar(x,data['Body Temperature'],color='red',label="Body Temperature")
leg=ax3.legend(loc=1,prop={'size':9})
leg.get_frame().set_alpha(0.3)

plt.xlabel("Days")

plt.show()