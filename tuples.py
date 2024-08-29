# tupples with cities and population
cities = (
    ("athens", 664046),
    ("thessaloniki", 315196),
    ("patras", 167446),
    ("hrakleio", 140730),
    ("larissa", 144651)
)

# calculate the mean value
total_population = 0

for city in cities:
    total_population += city[1]
    average_population = total_population / len(cities)
print(total_population)
print(average_population)