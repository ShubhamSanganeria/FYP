import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('C:\\Users\\PC\\Desktop\\FYP\\result.csv')
x=[i for i in range(0,100)]


ax1=plt.subplot2grid((6,1),(0,0),rowspan=3,colspan=1,label='Humidity')
ax2=plt.subplot2grid((6,1),(3,0),rowspan=3,colspan=1,label='Heart Rate')

ax3=plt.subplot2grid((6,1),(3,0),rowspan=3,colspan=1,label='Body Temperature')


ax1.plot(data['Humidity'])
ax1.fill_between(x,data['Humidity'],70,alpha=0.3,facecolor='blue')
ax1.grid(True)


ax2.plot(data['BPM'])
ax2.fill_between(x,data['BPM'],90,alpha=0.3,facecolor='green')
ax2.grid(True)

ax3.plot(data['Body Temperature'])
ax3.fill_between(x,data['Body Temperature'],100,alpha=0.3,facecolor='red')
ax3.grid(True)

leg1=ax1.legend(loc=1,prop={'size':11})
leg1.get_frame().set_alpha(0.2)



leg2=ax2.legend(loc=1,prop={'size':11})
leg2.get_frame().set_alpha(0.2)


leg3=ax3.legend(loc=1,prop={'size':9})
leg3.get_frame().set_alpha(0.1)

plt.xlabel("Days")
plt.show()

