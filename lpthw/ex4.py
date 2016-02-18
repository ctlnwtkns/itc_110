#set the variable cars to equal the value 100
cars = 100
#set the variable space_in_car to equal the value 4
space_in_car = 4
#set the variable drivers to equal the value 30
drivers = 30
#set the variable passengers to equal the value 90
passengers = 90
#set the variable cars_not_driven to equal the difference between the values of variables cars and drivers
cars_not_driven = cars - drivers
#set the variable cars_driven to equal the value of the variable drivers
cars_driven = drivers
#set the variable carpool_capacity equal to the product of the variables cars_driven and space_in_car
carpool_capacity = cars_driven * space_in_car
#set the variable avg_passengers_per_car equal to the quotient of the variables passengers and cars_driven
avg_passengers_per_car = passengers / cars_driven

print "There are ", cars, " cars available."
print "There are only ", drivers, " drivers available."
print "There will be ", cars_not_driven, " empty cars today."
print "We can transport ", carpool_capacity, " people today."
print "We have ", passengers, " to carpool today."
print "We need to put about ", avg_passengers_per_car, " in each car."

#accidentally putting an extra underscore between car and pool in line 7 will generate a NameError.