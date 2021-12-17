from datetime import datetime

import locale  #Türkçe yazdırmak için.
locale.setlocale(locale.LC_ALL,"")

şu_an = datetime.now()

saniye = datetime.timestamp(şu_an) #şuanki zamanı saniye cinsinden yazdırdık.
print(saniye)

şu_an2 = datetime.fromtimestamp(saniye) #saniyeyi tarihe çeviriyor
print(şu_an2)

şu_an3 =datetime.fromtimestamp(0)
print(şu_an3)

tarih = datetime(2000,10,27)
şu_an4 = datetime.now()
fark = şu_an4 - tarih
print(fark)

#print(datetime.strftime(şu_an,"%Y %B %A"))
#print(datetime.strftime(şu_an,"%Y")) #yıl
#print(datetime.strftime(şu_an,"%B")) #ay
#print(datetime.strftime(şu_an,"%D")) #tarih
#print(datetime.ctime(şu_an)) #anlaşılan bir gösterim.
#print(şu_an.year)
#print(şu_an.month)
#print(şu_an.hour)