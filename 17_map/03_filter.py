print()
print(">>>Filter")
print()

print("1- Filtrar de: 1,2,3,5 los que son pares")
numbers1 = [1,2,3,4,5]
new_numbers1 = list(filter(lambda x : x%2 == 0, numbers1))
print(numbers1)
print(new_numbers1)
print()


print("2- Filtrar de: un arreglo de dicc")
matches = [
            {
                "home_team": "Bolivia",
                "away_team" : "Uruguay",
                "home_team_score": 3,
                "away_team_score": 1,
                "home_team_result": "Win"
                
            },
            {
                "home_team": "Brasil",
                "away_team" : "Mexico",
                "home_team_score": 1,
                "away_team_score": 1,
                "home_team_result": "Draw"
                
            },
            {
                "home_team": "Ecuador",
                "away_team" : "Venezuela",
                "home_team_score": 5,
                "away_team_score": 0,
                "home_team_result": "Win"
                
            },
        ]
print("***Longitud: ", len(matches))
print(matches)
new_list = list(filter(lambda item : item["home_team_result"] == "Win", matches))
print("***Longitud new_list: ", len(new_list))
print(new_list)
print()
