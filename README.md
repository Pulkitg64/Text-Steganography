# Text-Steganography
The code is using text steganography to hide the message in a text file which is a poem in our case.

## Coversion of Plaintext Message into binary Format
The message to be hidden is converted to binary format on the basis of their ASCII values

 `res = ''.join(format(i, 'b') for i in bytearray(text, encoding ='utf-8'))`
  `print("The string after binary conversion : " + (res))`

## Opening Text File and creating a Empty Steg File

	file1 = open("test.txt","r") 
    file2 = open("Steg.txt","w+") 
## Conversion of Text File to Steg File

We read our file line by line and bits of message bit by bit
+ If current bit is zero, then first letter of line is converted to lowercase
+ If current bit is one, then first letter of the line is converted to uppercase

	```
  count = 0
  while True:
    data = file1.readline()
    if(count<length):
      if(res[count]=='1'):
        data=data[0].lower() + data[1:] 
        file2.write(data)
        count=count+1
        if not data:
            break

