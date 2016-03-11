#reciever code
import sys
import random
import mod
g='0'
p=2**3217-1
x='0'
mgxy='0'
gy='0'
st=''
#x is secret key
def main():
    f=open("/home/varun/elgamal/fileb",'a+')
    f1=open("/home/varun/elgamal/filea","r+")
    fsrc=open('/home/varun/elgamal/sourcefile','r')
    readf(fsrc)
    gx=genkey(long(x),p)
    f1.seek(0,2)
    f1.write(str(p)+" "+g+" "+str(gx)+"#")
    if not f.read(1):
        sys.exit()
    f.seek(0,0)    
    read(f)    
    m=decrypt(long(x),long(gy),long(mgxy),long(g))
    msg='#'
    convstr(msg,m,f)
    
def readf(f):
    n=1
    global g,x
    while n<=2:
        char=f.read(1)
        if char=='#':
            break
        if char != ' ':
            if n==1:
               g = g+char
            elif n==2:
               x = x+char 
        else:
            n+=1               
     
def convstr(msg,m,f):
    v=m
    while m:
        stg(m%65)
        msg=st+msg
        m/=65
    f.write(msg)       
def stg(k):
    global st
    if k in range(0,9):
        st= chr(k+ord('0'))
    elif k in range(10,35):
        st= chr(k+55)
    elif k in range(36,61):
        st= chr(k-36+ord('a'))
    elif k==62:
        st= '.'
    elif k==63:
        st= ','
    elif k==64:
        st= ' '            
def read(f):
    global mgxy,gy
    n=1
    while n<=2:
        char=f.read(1)
        if char=='#':
            break
        if char != ' ':
            if n==1:
                mgxy=mgxy+char
            elif n==2:
                gy=gy+char 
        else:
            n+=1    
    
def genkey(x,p):    
    return mod.mod(long(g),x,p)
    #gx is public send gx and get gy
def decrypt(x,gy,mgxy,g):
    gxyinvrs = mod.mod(gy,(p-1-x),p)
    return (mgxy*gxyinvrs)%p         

if __name__ == '__main__':
  main()      
