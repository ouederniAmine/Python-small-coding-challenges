inp=str(input("Give me your name: "))
hey=inp.lower()
num=0
voyelle=""
position=""

for i in range(len(hey)):
    if hey[i]=="a" or hey[i]=="e" or hey[i]=="i" or hey[i]=="y" or hey[i]=="o" or hey[i]=="u" and hey[i]!= " " :
        num = num +1
        position = position+ str(i)
        voyelle = voyelle + hey[i]
    else: continue

print("Dans ce mot il y a " , num , "voyelle.")
for i in range(num):
    print("Voyelle num " ,int(position[i] )+ 1, " est " , voyelle[i] )

