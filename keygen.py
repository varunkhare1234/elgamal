#keygenerator
import random
import sys
def main():
    g=random.randint(10**500,10**800)
    x=random.randint(10**500,10**800)
    f=open("/home/varun/elgamal/sourcefile",'w+')
    f.write(str(g)+" "+str(x)+"#")
    
if __name__ == '__main__':
  main()     
    
