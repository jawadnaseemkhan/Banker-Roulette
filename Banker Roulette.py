import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

len_names = len(names)  
banker_roulette = random.randint(0, len_names-1)
#print(names[banker_roulette])
payee = names[banker_roulette]
print(f"{payee} is going to buy the meal today!")