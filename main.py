import requests
from bs4 import BeautifulSoup
op=open('info1.txt','r')
op.readline()
urls=[]
for i in range(11678):
    urls.append(op.readline().replace('\n',''))
op.close()
op=open('data.txt','a')
j=0
for i in range(1135,len(urls)):
    ip=urls[i]
    try:
        r=requests.get(ip) 
        soup=BeautifulSoup(r.content,'html.parser')
        temp=soup.findAll('p')[0]
        op.write(temp.text)
        op.write('___'*10)
        j+=1
        print "Done with"+str(j)+"case(s)"
    except:
        pass


    
