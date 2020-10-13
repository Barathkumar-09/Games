''' 
Stone Paper scissor game:
Points :
  1. if paper and rock then paper wins
  2. if paper and scissor then scissor wins
  3. if rock and scissor then scissor wins
'''
import random
score=computr=flag=0
computer = ["p", "s", "r"]
max=int(input("Enter the maximum score! :"))
#print(random.choice(comp))
print("""p=paper
r=rock
s=siccor
""")
while(flag<max):
    player=input("Enter your choice:")
    comp=random.choice(computer)
    print("|",player, ":",comp,"|" )
    if(((player=="s")and(comp=="p"))or((player=="r")and(comp=="s"))or((player=="p")and(comp=="s"))or((player=="p")and(comp=="r"))):
        score+=1
        print("you scored :)")
    elif(((player=="s")and(comp=="p"))or((player=="s")and(comp=="r"))or((player=="s")and(comp=="r"))or((player=="r")and(comp=="p"))):
        computr+=1
        print("comp scored :(")
    elif(((player=="p")and(comp=="p"))or((player=="s")and(comp=="s"))or((player=="r")and(comp=="r"))):
        print("Tie  :|")
    else:
        print("wrong input!")
    print("|computer :",computr,"|","you:",score,"|")
    if(computr<score):
        flag=score
    elif(score<computr):
        flag=computr
    if(score==max):
        print("\t\tyou win!!")
        break
    if(computr==max):
        print("\t\tyou lose :(")
        break


