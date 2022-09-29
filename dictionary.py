gameList = {"Red Dead Redemption": "RockStar",
            "Marvel Spider-Man": "Insomniac",
            "Marvel Snap": "Second Dinner",
            "DBZ Kakarot": "Bandai Namco"}
print("WE got the current Games")
#Other way to for-loop is for game in gameList := gameList[game]
for game, creator in gameList.items():
    print(game, "is made by", creator)