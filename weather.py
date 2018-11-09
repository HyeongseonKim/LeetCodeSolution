from sources import daily, weekly

print("Daily forecast: ", daily.forecast())
print("Weekly forcast: ")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
