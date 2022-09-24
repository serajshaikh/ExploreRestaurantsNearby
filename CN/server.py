import socket
#Saeser cypher Encreption
def sesEnc(text,s):
    result=''
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            result+=chr((ord(char)+s-65)%26+65)
        else:
            result+=chr((ord(char)+s-97)%26+97)
    return result


#Saesar cypher Encreption
def sesDec(text,s):
    result=''
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            result+=chr((ord(char)-s-64)%26+64)
        else:
            result+=chr((ord(char)-s-96)%26+96)
    return result

s=socket.socket()
s.bind((socket.gethostname(),12345))
s.listen(1024)
while True:
    k1,a1=s.accept()
    print(f"receve message: {a1}")

    msg=k1.recv(20)
    msg=msg.decode()

    key=int(k1.recv(20))

    op=int(k1.recv(20))
    if op==1:
        res = sesEnc(msg,key)
        k1.send(res.encode())
    else:
        res=sesDec(msg, key)
        k1.send(res.encode())
    
    k1.close()



# ////////////////////////vergenecipher
""" 
import socket
def generateKey(text, key):
    key=list(key)
    if(len(key)==len(text)):
        return ("".join(key))
    else:
        for i in range(len(text)-len(key)):
            key.append(key[i%len(key)])
    return ("".join(key))


def vergEnc(text, key):
    result=[]
    for i in range(len(text)):
        result.append(chr(((ord(text[i])+ord(key[i]))%26)+65))
    return ("".join(result))


def vergDec(text, key):
    result=[]
    for i in range(len(text)):
        result.append(chr((ord(text[i])-ord(key[i])+26)%26+65))
    return ("" .join(result))


s=socket.socket()
s.bind((socket.gethostname(),12345))
s.listen(1024)
while True:
    k,a=s.accept()
    print(f"CONNECTED TO {a}")

    msg=k.recv(1024).decode()

    key=k.recv(1024).decode()

    option=k.recv(1024)

    if option==1:
        key=generateKey(msg,key)
        key=key.upper()
        res=vergEnc(msg.upper(),key)
        k.send(res.encode())
    else:
        key=generateKey(msg,key)
        key=key.upper()
        res=vergDec(msg.upper(),key)
        k.send(res.encode())

    k.close()
 """


# ////////////Rail Fains cypher//////////
""" 
def railEnc(text,key):
    rail=[['\n' for i in range(len(text))] for j in range(len(key))]
    down=False
    row, col=0,0
    for i in range(len(text)):
        if row==0 or row ==len(key)-1:
            down=not down
        rail[row][col]=text[i]
        col+=1
        if down:
            row+=1
        else:
            row-=1

    res=""
    for i in range(len(key)):
        for j in range(len(text)):
            if rail[i][j]!='\n':
                res+=rail[i][j]
    return res

def railDec(text, key):
    rail=[['\n' for i in range(len(text))] for j in range(len(key))]
    down=False
    row, col=0,0
    for i in range(len(text)):
        if row==0 or row ==len(key)-1:
            down=not down
        rail[row][col]='*'
        col+=1
        if down:
            row+=1
        else:
            row-=1
    k=0
    for i in range(len(key)):
        for j in range(len(text)):
            if rail[i][j]=='*':
                rail[i][j]=text[k]
                k+=1
    res=""
    down=False
    row, col=0,0
    for i in range(len(text)):
        if row==0 or row ==len(key)-1:
            down=not down
        res+=rail[row][col]
        col+=1
        if down:
            row+=1
        else:
            row-=1
    return res

text=input("Enter Text: ")
key=input("Enter Key: ")
res1=railEnc(text,key)
res2=railDec(res1,key)
print(res1)
print(res2)
 """


#  ////////////////playfair cypher////////////////
""" 
# plain text ko sudhar rahe hai
def diagraph(txt):
    for i in range(0,len(txt)+1,2):
        if i<len(txt)-1:
            if txt[i]==txt[i+1]:
                txt=txt[:i+1]+'Z'+txt[i+1:]
        if len(txt)%2!=0:
            txt+='Z'
    return txt

def keygeneratar(key):
    keymatrix=[[0 for i in range(5)] for j in range(5)]
    arraylist=[]
    for i in range(len(key)):
        k=key[i]
        if k=='J':
            k='I'
        if i not in arraylist:
            arraylist.append(key[i])

    for i in range(65,91):
        k=chr(i)
        if k=='J':
            k='I'
        if k not in arraylist:
            arraylist.append(k)

    for i in range(5):
        for j in range(5):
            keymatrix[i][j]=arraylist[5*i+j]
    return keymatrix

def indexLocator(char, keymatrix):
    if char=='J':
        char='I'
    poslist=[]
    for i in range(5):
        for j in range(5):
            if keymatrix[i][j]==char:
                poslist.append(i)
                poslist.append(j)
                break;

    # print(poslist)
    return poslist

# indexLocator(c)

def playEnc(text, key):
    text=diagraph(text)
    reslist=[]
    matrix=keygeneratar(key)
    print('Matrix is:')
    for i in range(5):
        for j in range(5):
            print(matrix[i][j], end=" ")
        print()

    for i in range(0,len(text),2):
        n1=indexLocator(text[i], matrix)
        n2=indexLocator(text[i+1], matrix)
        print(f"{n1},{n2}")
        if n1[1]==n2[1]:
            r1=(n1[0]+1)%5
            c1=n1[1]
            r2=(n2[0]+1)%5
            c2=n2[1]
            reslist.append(matrix[r1][c1])
            reslist.append(matrix[r2][c2])
        elif n1[0]==n2[0]:
            r1=(n1[1]+1)%5
            c1=n1[0]
            r2=(n2[1]+1)%5
            c2=n2[0]
            reslist.append(matrix[c1][r1])
            reslist.append(matrix[c2][r2])
        else:
            reslist.append(matrix[n1[0]][n2[1]])
            reslist.append(matrix[n2[0]][n1[1]])
    return ("".join(reslist))

text=input("Enter plain: ").replace(" ","").upper()
key=input("Enter key: ").replace(" ","").upper()

print(playEnc(text, key))

 """
""" 
#  //////////////COLUMINAR CIPHER////////////////
import math
def encryptMessage(msg,key):
    k_index=0
    msglen=float(len(msg))
    msglist=list(msg)
    keylist=sorted(list(key))
    col=len(key)
    row=int(math.ceil(msglen/col))
    fill=int(row*col-msglen)
    for i in range(fill):
        msglist.append("_")
    # print(msglist)
    matrix=[['_'for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            matrix[i][j]=msglist[col*i+j]
    # print(matrix)
    res=""
    for i in range(col):
        keyIndex=key.index(keylist[k_index])
        for j in range(row):
            res+=matrix[j][keyIndex]
        k_index+=1
    # print(res)
    return res

def decryptMessage(msg, key):
    k_index=0
    msglen=float(len(msg))
    msglist=list(msg)
    klis=sorted(list(key))
    col=len(key)
    row=int(math.ceil(msglen/col))
    matrix=[['None' for i in range(col)] for j in range(row)]
    k=0
    for i in range(col):
        index_curr=key.index(klis[k_index])
        for j in range(row):
            matrix[j][index_curr]=msglist[k]
            k+=1
        k_index+=1
    
    res=''
    for i in range(row):
        for j in range(col):
            if matrix[i][j]!='_':
                res+=matrix[i][j]
    return res;


msg=input("Enter PlainText: ")
key=input("Enter Key: ")

cipher = encryptMessage(msg,key)
print("Encrypted Message: {}".format(cipher))

print("Decryped Message: {}".format(decryptMessage(cipher, key)))
 """