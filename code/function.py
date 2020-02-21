#1简单的函数创建
# def greet_user(first_name,last_name):
#     print (f'hello!{first_name} {last_name}')
#     print ("welcome aboard")


# print("start")
# greet_user("john","smith")
# print("finish")

#2调用返回值的函数
def square(number):
    return number*number #把return去掉最后输出none

print(square(3))

#3把之前emoji做成一个函数
def change_emoji(message):
    words = message.split(' ')
    emojis = {
        ":)": "😁",
        ":(": "😩"
    }
    output = ""
    for word in words:
        output += emojis.get(word,word)+ " "
    return output


message = input(">")
print (change_emoji(message))

