#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True



cores =     ["82","","128", "", "256", "","512","", "1024", "","1280","","","64","","128","","256","","512","","1024","","1280"]
#dpdk =      [2.5894, np.nan,    4.6305,   np.nan,  8.4542,  np.nan , 9.1451,  np.nan, 9.5474,  np.nan,  9.6341,     np.nan, np.nan,  0.7227,    np.nan, 1.3089,   np.nan,  2.6737, np.nan, 5.2763,  np.nan, 9.5771,  np.nan,  10.0008]

#netmap =    [1.9198,  np.nan,  3.4714,    np.nan, 6.223,   np.nan, 9.1453,  np.nan, 9.5474,   np.nan, 9.6357,      np.nan,  np.nan, 1.3411,  np.nan,  2.3738,  np.nan,   4.1232, np.nan, 7.0395, np.nan, 9.9695,   np.nan, 9.9863]

#socket =    [0.1407,  np.nan,  0.2393,    np.nan, 0.5120,  np.nan,  2.1105,  np.nan, 4.3491,  np.nan,   5.3304,    np.nan, np.nan,  0.4940,    np.nan, 0.8695,  np.nan,    1.6097,  np.nan, 2.9528,  np.nan, 5.6474,   np.nan,   6.8889]


#dpdk_p = dpdk
#netmap_p = netmap
#socket_p = socket

#smmap_pps =  [0.22 ,np.nan,0.22, np.nan,0.23,  np.nan,0.38,  np.nan,0.43,  np.nan,0.43  ,np.nan,np.nan, 0.2234, np.nan,0.2207,np.nan,0.2266, np.nan,0.3813, np.nan,0.4328, np.nan,0.4296 ]
#dpdk_pps =   [3.341,np.nan,3.321,np.nan,3.311, np.nan,2.349, np.nan,1.197, np.nan,0.962 ,np.nan,np.nan, 4.036,  np.nan,3.584, np.nan,3.587,  np.nan,2.249,  np.nan,1.171,  np.nan,0.945 ]
#netmap_pps = [2.354,np.nan,2.555,np.nan,2.367, np.nan,2.049, np.nan,1.197, np.nan,0.962 ,np.nan,np.nan, 3.293,  np.nan,3.061, np.nan,2.927,  np.nan,2.249,  np.nan,1.171,  np.nan,0.945 ]

smmap_pps =  [0.38, np.nan,0.304,np.nan,0.227, np.nan,0.381, np.nan,0.433, np.nan,0.43   ,np.nan,np.nan,  0.441,np.nan,0.342,np.nan,0.286,np.nan, 0.42, np.nan,0.469, np.nan,0.474 ]
dpdk_pps =   [1.544,np.nan,1.529,np.nan,1.563, np.nan,1.548, np.nan,1.197, np.nan,0.962  ,np.nan,np.nan,  3.162,np.nan,3.834,np.nan,3.85, np.nan,2.249, np.nan,1.171, np.nan,0.944 ]
netmap_pps = [1.201,np.nan,1.198,np.nan,1.091, np.nan,0.996, np.nan,0.851, np.nan,0.816  ,np.nan,np.nan,  2.292,np.nan,2.652,np.nan,2.536,np.nan, 2.249,np.nan, 1.171,np.nan, 0.944 ]



#numb = [64,0,128,0,256,0,512,0,1024,0,1280,0,0,114,0,128,0,256,0,512,0,1024,0,1280]

#for i in range(0,len(cores)):
#	if dpdk[i] != np.nan: 
#		dpdk_p[i]=(dpdk[i]*1000)/((20+numb[i])*8) 
#		netmap_p[i]=(netmap[i]*1000)/((20+numb[i])*8) 
#		socket_p[i]=(socket[i]*1000)/((20+numb[i])*8) 
#	else: 
#		np.nan
#


ind = np.arange(len(cores))
width = 0.5
fig = plt.figure(figsize=(7,3.3))
ax = fig.add_subplot(111)

ax.bar([p + width for p in ind+0.5], dpdk_pps , width, color="#AFD2E9", edgecolor="black",hatch="OO", lw=1., zorder = 0)

ax.bar([p + width for p in ind], netmap_pps, width, color="#B1B695", edgecolor="black", lw=1., zorder = 0)

ax.bar([p + width for p in ind-0.5], smmap_pps, width, color="#FCD0A1",edgecolor="black",hatch="..", lw=1., zorder = 0)



ax.set_xticks(ind+2*(width/2))
xticks = ax.xaxis.get_major_ticks()
xticks[1].set_visible(False)
xticks[3].set_visible(False)
xticks[5].set_visible(False)
xticks[7].set_visible(False)
xticks[9].set_visible(False)
xticks[11].set_visible(False)
xticks[12].set_visible(False)
xticks[14].set_visible(False)
xticks[16].set_visible(False)
xticks[18].set_visible(False)
xticks[20].set_visible(False)
xticks[22].set_visible(False)

ax.set_xticklabels(cores)

ax.set_ylabel('Throughput (Mpps)',fontsize=9)
#ax.yaxis.set_label_coords(-0.08,0.9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=6)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=9)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')

ax.text(2.0, -0.7, u'(For UL, between CPE and BNG)',fontsize=10)
ax.text(0.6+18, -0.7, u'(For DL, between Server and BNG)',fontsize=10,ha='center')


plt.legend(['DPDK', 'Netmap', 'Socket-mmap'], loc='upper right',frameon=False, fontsize=10)
plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)
#plt.savefig("bng_rate.png")
#plt.savefig("bng_rate.eps", format='eps', dpi=1)

#plt.show()
plt.savefig('bng_perform.eps', format='eps', dpi=50)

