
list_item = ["kola", 99, "ala", "dala" ]
list_item.append("sala") # remove / pop for last or index remove / insert for add list on anywere / extend for add 2 variable in one list 
list_item[3] = "xola"
#list_item.sort(reverse=True)         # clear for all remove / .reverse() for code list in reverse 
del list_item[0]
print(list_item[1:])
or_list = list_item.copy()
print(or_list)



c_tuple = tuple(or_list)
print(c_tuple)
tuples = ("ami", "tmi", 100, "tmi")
tuples += ("hello", )
print(tuples)  # del for delet full tuple
print(tuples * 2)
print(tuples[0])
print(tuples.count("tmi"))   # index for find index number
print(len(tuples))



set_item = {"lao", 22, "aao"}
set_item2 = {"fao", "aao"}
set_item.add("xao")    # remove / discard for also remove its advance not get error / clear for all remove
AA = set_item.symmetric_difference(set_item2)  # intersection() for show common value in both set / difference() for show defference in just one set 
print(AA)
set_item.update(set_item2) # union for add two set in one like update
print(set_item)




dictionary = {"al":44, "pl":77}
dictionary["cl"] = ("22")
dictionary.update({"bl":99, "pl":13})
del dictionary["cl"] 
print(dictionary.items())     # keys / values 
print(dictionary["pl"])
print(dictionary.get("bl"))

Nested_dictionary = {
    "D1":{
        "juki": 44,
        "nuki": 77,
        "muki": "puti"
    },
    "D2":{
        "luki": 90,
        "suki": "duki",
        "puki": 82
    },
    "D3":{
        "guki": 88,
        "auki": 12,
    }
}
print(Nested_dictionary)

dict1 = ("paja","jaja")
dict2 = ("maja",909)
print(dict.fromkeys(dict1, dict2))