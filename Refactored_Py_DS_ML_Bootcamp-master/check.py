def check(pas):
    if len(pas) <8:
        raise Exception("too short")
    print('password is strong')

try:
    ari=input("enter password")
    check(ari)
except Exception as e:
    print(e)
    
    
    