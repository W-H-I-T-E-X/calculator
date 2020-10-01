import os
red='\033[1;31m'
rset='\033[0m'
print (red+"             _    ____   ___")
print ("            / \  |  _ \ / _ *")
print ("           / _ \ | |_) | | | |")
print ("          / ___ \|  _ <| |_| |")
print ("         /_/   \_\_| \_ \___/ "+rset)
print ("--------------------------------------------")
print ("                     |")
print ("                     |")
print ("                     |")
print ("                     |")
print ("                     |")
print ("   [1].CALCULATE     |    [2].EXIT")
print ("       -----------   |   -----------")
print ("            |        |        |")
print ("            |        |        |")
print ("            |--------|--------|")



a = int(input())
if a==2:
    exit()
if a==1:
    c = float(input("ENTER YOUR FIRST NUMBER = "))
    print (" ")
    d = float(input("ENTER YOUR SECOUND NUMBER = "))
    print (" ")

print ("                   ____________")
print ("                 /             \ ")
print ("                /               \ ")
print ("               |                 |")
print ("               | [1] ADDITION    |")
print ("               | [2] SUBTRACTION |")
print ("               | [3] DEVISION    |")
print ("               | [4] MULTYPLY    |")
print ("                \               /")
print ("                 \_____________/")

e = int(input())
if e==1:
    sum=c+d
    print ("your answear is = ",(sum))
    os.system("python cal.py")
    sleep=2.0
if e==2:
    sus=c-d
    print ("your answear is = ",(sus))
    os.system("python cal.py")
if e==3:
    sud=c/d
    print ("your answear is = ",(sud))
    os.system("python cal.py")
if e==4:
    sul=c*d
    print ("your answear is = ",(sul))

    os.system("python cal.py")

