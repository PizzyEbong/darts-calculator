"""
darts calculator to calculate scores in a simple darts match

"""
DartsScore1 = 0
print("""
enter (1) for 501
(2) for 301
(3) for 101
""")
playersChoice = int(input("Choose: "))
if playersChoice == 1:
    DartsScore1 = 501
    DartsScore2 = 501
    print(DartsScore1, + DartsScore2)
elif playersChoice == 2:
    DartsScore1 = 301
    DartsScore2 = 301
    print(DartsScore1, + DartsScore2)
elif playersChoice == 3:
    DartsScore1 = 101
    DartsScore2 = 101
    print(DartsScore1, + DartsScore2)
else:
    print("you have entered an invalid number")

while DartsScore1 != 0:
    plyerOneScore = int(input("Enter Player one Score: "))
    while plyerOneScore > 180:
        plyerOneScore = 0
        plyerOneScore = int(input("Enter Player one Score: "))
    plyerOneScore <= 180
    while plyerOneScore > DartsScore1:
        plyerOneScore = 0
        plyerOneScore = int(input("Enter Player one Score: "))
    DartsScore1 = DartsScore1 - plyerOneScore
    print("Playerone Score:", DartsScore1)

    while DartsScore2 != 0:
        plyerTwoScore = int(input("Enter Player Two Score: "))
        while plyerTwoScore > 180:
            plyerTwoScore > DartsScore2
            plyerTwoScore = 0
            plyerTwoScore = int(input("Enter Player Two Score: "))
        plyerTwoScore <= 180
        while plyerTwoScore > DartsScore2:
            plyerTwoScore = 0
            plyerTwoScore = int(input("Enter Player Two Score: "))
        DartsScore2 = DartsScore2 - plyerTwoScore
        print("Playertwo Score:", DartsScore2)
        break
    if DartsScore2 == 0:
        print("player two has won!!!!!")
        break


print("Congratulations You Have Won")


