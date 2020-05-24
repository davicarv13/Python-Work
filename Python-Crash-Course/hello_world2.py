dinner_invitations = ["David Bowie", "Prince", "Madonna"]
print("Dear " + dinner_invitations[0] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[1] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[2] +", would you like to come to dinner with me?\n")

print("------------------------------------------------\n")

guest = "Prince"

dinner_invitations.remove(guest)
print(guest + " could not make it to my dinner\n")

new_guest = "Taylor Swift"
dinner_invitations.insert(1, new_guest)

print("Dear " + dinner_invitations[0] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[1] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[2] +", would you like to come to dinner with me?\n")

print("------------------------------------------------\n")

dinner_invitations.insert(0, "Mariah Carey")
dinner_invitations.insert(3, "Cher")
dinner_invitations.append("Kylie Minogue")

print("Dear " + dinner_invitations[0] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[1] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[2] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[3] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[4] +", would you like to come to dinner with me?\n")
print("Dear " + dinner_invitations[5] +", would you like to come to dinner with me?\n")

print("------------------------------------------------\n")

print("Dear " + dinner_invitations.pop() +", I'm so sorry but i can't bring you to my dinner anymore\n")
print("Dear " + dinner_invitations.pop() +", I'm so sorry but i can't bring you to my dinner anymore\n")
print("Dear " + dinner_invitations.pop() +", I'm so sorry but i can't bring you to my dinner anymore\n")
print("Dear " + dinner_invitations.pop() +", I'm so sorry but i can't bring you to my dinner anymore\n")

print("------------------------------------------------\n")

print("Dear " + dinner_invitations[0] +", you're still invited to my dinner\n")
print("Dear " + dinner_invitations[1] +", you're still invited to my dinner\n")



print("------------------------------------------------\n")

del dinner_invitations[1]
del dinner_invitations[0]

print("Final list: " + str(dinner_invitations))