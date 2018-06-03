import re
import urllib.request

city=input("Enter a City: ")
url="https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
#print(data1)
m=re.search('span class="phrase"',data1)
start=m.start()
end=m.start()+100
Newstring=data1[start:end]
#print(Newstring)
humidity=data1[start+20:start+30]
temp=data1[start+32:start+44]
date=data1[start+51:end-33]
date1=data1[end-31:end-25]
date2=data1[end-18:end-3]
print("Weather: "+str(humidity)+" "+str(temp)+" "+str(date)+" "+str(date1)+" "+str(date2))




