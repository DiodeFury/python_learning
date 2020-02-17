# customer = {
#     "name": "john smith",
#     "age": 30 ,
#     "is_verifide":True
# }
# print (customer.get("name"))  #用get是为了当关键值不存在时不报错，而是显示none
# print (customer.get("Name"))
# print (customer.get("birthday",'1999 10 29'))
# customer["name"] = "laidong"
# print (customer.get("name"))
# pratice1
phone = input("phone:")
digits_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!")+" " #当数字不存在时，用感叹号“！”替代了“none”
print(output)
#pratice2 
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "😩"
}
output = ""
for word in words:
    output += emojis.get(word,word)+ " "
print (output)