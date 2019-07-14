#python3
#mencari PDF dan CDF dari suatu data untuk mengetahui bentuk distribusi
import numpy as np
import math
def pdfcdf(data):
	minn=min(data)
	maxx=max(data)
	k=math.floor(1+(3.3*math.log(len(data),10)))
	rentang=maxx-minn
	p=math.floor(rentang/k)
	int1=[]
	int2=[]
	kasli=0
	tmp=minn
	for i in range(k):
		int1.append(tmp)
		tmp=tmp+p
		int2.append(tmp)
		# print(tmp)
		kasli=kasli+1
		if (tmp == maxx):
			break
		else:
			tmp=tmp+1
	# print(kasli)
	##cari anggota kelompok
	anggota=[0]*kasli
	for i in range(kasli):
		for j in range(len(data)):
			if((data[j] >= int1[i]) and (data[j] <= int2[i])):
				anggota[i]=anggota[i]+1
			else:
				continue
	pdf=[0]*kasli
	cdf=[0]*kasli
	for i in range(len(anggota)):
		pdf[i]=anggota[i]/len(data)
		if(i==0):
			cdf[i]=pdf[i]
		else:
			cdf[i]=cdf[i-1]+pdf[i]

	##print hasil
	print("No  | interval | jml | 	pdf   | cdf 	|")
	for i in range(kasli):
		print(i,"  ",int1[i],"  ",int2[i],"",anggota[i],"	",pdf[i],"	",cdf[i])
	print("\nNilai min =",minn,"\nNilai max =",maxx,"\nNilai k =",kasli,
		"\nNilai interval =",p)
#impor data
data=np.loadtxt('data.csv',dtype='int')
pdfcdf(data)
