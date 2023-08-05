import pywhatkit 

phone_number = input("enter phone number: ")
pywhatkit.sendwhatmsg(phone_number, "Esta mensagem foi automaticamente enviada via programa 👍 ", 13, 3)
#+55xxxxxxxxx
#pywhatkit.sendwhatmsg(phone_number, "Esta mensagem foi automaticamente enviada via programa 👍 ", 13, 3, 15, True) # 15 -> tempo para rodar código, True -> fecha aba

# Group 
group_id = input("Enter group id: ")
pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 'hora', 'minuto')

