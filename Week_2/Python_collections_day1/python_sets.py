#Code-Along - Sets
#Sets are data collections, but the key difference is that they are UNORDERED
# Syntax name = {}

car_parts = {"wheels", "doors", "engine"}

print(car_parts)

#Sets can be appended
car_parts.add("windows")
print(car_parts)

#can remove items from sets
car_parts.discard("doors")
print(car_parts)

#Frozen sets
frozen_set = ([1,3,5,26])
print(frozen_set)
#frozen sets do not change their order. they are like tupls (immutable)