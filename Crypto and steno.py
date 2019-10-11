# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:45:23 2019

@author: APPED
"""

import string
import itertools

def chunker(seq, size):
    it = iter(seq)
    while True:
       chunk = tuple(itertools.islice(it, size))
       if not chunk:
           return
       yield chunk


def prepare_input(dirty):
    """
    Prepare the plaintext by up-casing it
    and separating repeated letters with X's
    """
    
    dirty = ''.join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""
    
    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty)-1):
        clean += dirty[i]
        
        if dirty[i] == dirty[i+1]:
            clean += 'X'
    
    clean += dirty[-1]

    if len(clean) & 1:
        clean += 'X'

    return clean

def generate_table(key):


    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
 
    table = []

    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    for char in alphabet:
        if char not in table:
            table.append(char)

    return table

def encode(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""

   
    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1*5+(col1+1)%5]
            ciphertext += table[row2*5+(col2+1)%5]
        elif col1 == col2:
            ciphertext += table[((row1+1)%5)*5+col1]
            ciphertext += table[((row2+1)%5)*5+col2]
        else: # rectangle
            ciphertext += table[row1*5+col2]
            ciphertext += table[row2*5+col1]

    return ciphertext


def decode(ciphertext, key):
    table = generate_table(key)
    plaintext = ""

   
    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1*5+(col1-1)%5]
            plaintext += table[row2*5+(col2-1)%5]
        elif col1 == col2:
            plaintext += table[((row1-1)%5)*5+col1]
            plaintext += table[((row2-1)%5)*5+col2]
        else: # rectangle
            plaintext += table[row1*5+col2]
            plaintext += table[row2*5+col1]
    plaintext=plaintext.lower()
    return plaintext

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
key='tutorials'
enc=encode(plaintext,key)
print("Encrypted", enc)
stegnog(enc)
encrypted=desteg() 
print("Encryption",encrypted)
# printing result  
dec=decode(encrypted,key)
print("Original:",plaintext)
print("Decryption",dec)

