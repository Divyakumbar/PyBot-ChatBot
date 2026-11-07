print("="*20,"WELCOME TO PYBOT","="*20)
u_name=input("May I know your name: ")
print("Hello ",u_name)
u_details={}
while True:
 u_i=input("YOU: ")
 if u_i.lower()=="hello":
    print("PYBOT: Hi ",u_name)
 elif u_i.lower()=="how are you":
    print("PYBOT: I am fine",u_name,"What's about you??")
 elif u_i.lower()=="what is your name?":
    print("PYBOT: I am PyBot,a Chatbot which is built to communicate with people ")
 elif u_i.lower()=="bye":
    print("PYBOT: Bye ",u_name,"Take care!!")
    break
 else:
    print("PYBOT: I didn't understand your words.Can you repeat it for me")
u_details["fav_food"]=input("PYBOT: What's your fav food?")
u_details["fav_color"]=input("PYBOT: What's your fav color?")
u_i=input("YOU: ")
if u_i=="what is my fav food":
   print(u_details["fav_food"])
elif u_i=="what is my fav color":
   print(u_details["fav_color"])

