#a weird set like, like struct in c
car = {
	"brand" : "Mercedes",
	"model" : "S450",
	"year" : 2021
}
print(car.get("model"))
# can change the Value
car["year"] = 2020
print(car.get("year"))
#can add Value
car["color"] = "black"
print(car.get("color"))
#delete Value using pop() method
car.pop("color")
#use clear to clear dictionary
car.clear()

