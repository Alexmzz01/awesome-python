#validare user input
#username no more than 12 char
#user not contain spaces
# user not contain digits

user_input = input("digite username : ")
result = len(user_input)
print(f"{result} caratteri in {user_input}")
result_count_char = ("ok rientra nei 12 carartteri" if result <= 12 else "nok")
print(result_count_char)
result_spazio = user_input.count(" ")
print(f"{result_spazio} spazi nell username {user_input}")
if result_spazio >= 1:
    print(f"{result_spazio} e presente uno spazio")
    spazio_replace = user_input.replace(" ", "")
    print(f"{spazio_replace} ora e normalizzato")

numeri_in_username = user_input.isdigit()
print(numeri_in_username)
numeri_in_username = ("ok" if numeri_in_username == False else "nok")
print(numeri_in_username)


