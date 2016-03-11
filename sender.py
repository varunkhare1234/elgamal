import random
import sys
import mod
p='0'
g='0'
gx='0'
def main():
    f=open("/home/varun/elgamal/filea",'r+')
    f2=open("/home/varun/elgamal/fileb",'r+')
    msg='#'
    char=f.read(1)
    while char !='#':
        msg=msg+char
        char=f.read(1)            
    m=evaluate(msg)
    #never use read, readline with next or for in clause bcause it readily shifts the cursor ahead for efficiency reasons giving vakue error
    if not f.read(1):                            #other part of code not run till now
        sys.exit()
    read(f)    
    y=random.randint(10**200,10**600)             #check bounds
    gy=keygen(long(g),long(p),y)
    emsg=encrypt (gy,long(p),long(gx),m,y)
    write(f2,emsg,gy)
    
def write(f2,emsg,gy):
    f2.write(str(emsg)+" "+str(gy)+"#")    
def read(f):
    n=1
    global p,g,gx
    while n<=3:
        char=f.read(1)
        if char=='#':
            break
        if char != ' ':
            if n==1:
                p = p+char
            elif n==2:
                g = g+char
            elif n==3:
                gx =gx+char 
        else:
            n+=1               
                  
def keygen(g,p,y):
    return mod.mod(g,y,p)
def encrypt(gy,p,gx,m,y):
    return (m*mod.mod(gx,y,p))%p    
def evaluate(msg):    
    i=0
    m=0
    g=0
    while(i<len(msg)-1):
        g=ord(msg[len(msg)-i-1])
        if g in range(ord('A'),ord('Z')):
            m=m+(g-ord('A')+10)*(65**i)
        elif g in range(ord('a'),ord('z')):
            m=m+(g-ord('a')+36)*(65**i)
        elif g in range(ord('0'),ord('9')):
            m+=(g-ord('0'))*(65**i)
        elif g ==ord('.'):
            m+=62*(65**i)
        elif g ==ord(','):
            m+=63*(65**i)
        elif g==ord(' '):
            m+=64*(65**i)         
        i=i+1
    return m  
    

if __name__ == '__main__':
  main()      
    
