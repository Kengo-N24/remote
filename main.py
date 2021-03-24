import url_get
import paramiko

url = url_get.yturl()

f = open('output.txt','w')
f.write(url)
f.close()
