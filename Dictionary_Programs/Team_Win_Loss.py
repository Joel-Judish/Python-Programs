teams={}
w=[]
l=[]

while True:
    team_name=input("Enter the Team Name:")
    wins=int(input("Enter the number of wins:"))
    losses=int(input("Enter the number of losses:"))
    teams[team_name]=[wins,losses]
    if(input("Do you want to continue,Enter (y/n)")=='n'):
        break;

print("The Teams are:")
for key in teams:
    print(key)
for key in teams:
    w.append(teams[key][0])
    l.append(teams[key][1])
maxw=max(w)
maxl=max(l)

for key in teams:
    if(teams[key][0]==maxw):
        print("Team with maximum wins is ",key)
    if(teams[key][1]==maxl):
        print("Team with maximum losses is ",key)
wpteam=input("Enter the team name to find the win percentage :")
if(wpteam in teams):
    percentage=(teams[wpteam][0]/(teams[wpteam][0]+teams[wpteam][1]))*100
print("Win percentage of team ",wpteam,"is ",percentage)



