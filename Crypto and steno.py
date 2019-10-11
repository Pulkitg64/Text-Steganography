
def stegnog(text):
    
    res = ''.join(format(i, 'b') for i in bytearray(text, encoding ='utf-8'))
    print(res)
    print("The string after binary conversion : " + (res)) 
    print(res[3])
    
    length = len(res)
    print(length)
    
    count = 0
    while (count < length):     
        if(res[count]=='0'):
            print("ZERO")
        else:
            print("ONE")
        count=count+1
        
    file1 = open("test.txt","r") 
    file2 = open("Steg.txt","w+") 
    
    count = 0
    while True:
    # read line
        data = file1.readline()
        if(count<length):   
            if(res[count]=='1'):       
                data=data[0].lower() + data[1:] 
        file2.write(data)
        count=count+1
        if not data:
            break
    
def desteg():
    
     crypto =''
     file2 = open("Steg.txt","r") 
     while True:
        data = file2.readline()
        if not data:
            break
        if(data[0].isupper()):
            crypto=crypto+'0'
        else:
            crypto=crypto+'1'
      
        
        
     print("Encrypted Code Bits:") 
     print(crypto)
     lengthcr = len(crypto)
     print(lengthcr)
     
     first=''
     for i in range(0, lengthcr,7):
         num=0
         
         num=num+int(crypto[i+0])*64
         if(i+1<lengthcr):
             num=num+int(crypto[i+1])*32
         if(i+2<lengthcr):
             num=num+int(crypto[i+2])*16
         if(i+3<lengthcr):
             num=num+int(crypto[i+3])*8
         if(i+4<lengthcr):
             num=num+int(crypto[i+4])*4
         if(i+5<lengthcr):
             num=num+int(crypto[i+5])*2
         if(i+6<lengthcr):
             num=num+int(crypto[i+6])*1
         if(num>64):
             charac = chr(num)
             first=first+charac
         if(num==0):
             break;
        
     print(first)   
     return first

plaintext='IRONMAN'

stegnog(plaintext)
decrypted=desteg() 
print("Message After Uncovering File: ",decrypted)


