from bs4 import BeautifulSoup
from urllib.request import urlopen
my_address="http://www.lsfx.pudong-edu.sh.cn/infoweb/"
html_page=urlopen(my_address)
html_text = html_page.read().decode('gbk')
my_soup=BeautifulSoup(html_text)
print(my_soup.get_text())
#print(html_text)

import os
my_path="D:\swiss"
file_names_list=os.listdir(my_path)
for file_name in file_names_list:
    print(file_name)

from random import randint
print(randint(0,10))
score=[('zbx',88,90,91),('wax',98,89,90),('zty',78,89,97)]
score=sorted(score,key=lambda d:d[3],reverse=True)
print(score)

myfile=open("hello.txt","w")
myfile.writelines("this is hello")
myfile.close()

#score=sorted(score.items(),key=lambda d:d[1],reverse=True)
#input_string=input("what's your name?")
#print("my name is:",input_string)

def mysqr(number):
    sqr_num=number**2
    return sqr_num

print(mysqr(4))

for n in range(1,5):
    print("n=",n)
print("end loop")


                   
