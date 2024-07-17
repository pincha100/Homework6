my_dict = {"Алексей": 2002, "Ольга": 1956, "Владимир": 1997}
print(my_dict)
print(my_dict["Ольга"])
print(my_dict.get("Олег"))
my_dict.update({"Иван": 1990,
                "Дарья": 1999})
print(my_dict)
my_dict.pop("Иван")
print(my_dict)

my_set = {1,2,3,0,1,2, "String", True, False, (10,20)}
print(my_set)
my_set.add("some")
my_set.add(5)
print(my_set)
my_set.remove(3)
print(my_set)

