#!/usr/bin/env python3

ft_list = ["hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi"}

ft_list[1] = "World"
# ft_tuple = ("Hello", "Switzerland")
ft_tuple_modif = list(ft_tuple)
ft_tuple_modif[1] = "Switzerland"
ft_tuple = tuple(ft_tuple_modif)
ft_set.remove("tutu!")
ft_set.add("Lausanne")
ft_dict["Hello"] = "42Lausanne"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)