
def mod(a,b,c):
    if c==1:
        return 0
    md=1 
    while b>=0:
        if b==0:
            break
        if b%2:
           md = (md*(a%c))%c
        a= (a**2)%c
        b/=2               
    return md    
