"""
message = input("How are you today? Enter your response here or Q to quit: ")
for i in message:
    if message == "Q":
        print("End")
    elif message =="q":
        print("End")
        Stop 
    elif message== "I am feeling great":
        print (f"{message}")
        print ("End")
    else: 
        print(f"{message}"+"Enter your reponse here or Q to quite")
          
"""
"""

message = input("How are you today? Enter your response here or Q to quit: ")
while message != "Q" or "q" or "I am feeling great":
      print(f"{message}"+"Enter your reponse here or Q to quite")
          


condition1=False
message = input("How are you today? Enter your response here or Q to quit: ")
if message == "q" or message == "Q" or message == "I am feeling great":
    condition1=True
while condition1 == False:
    print(f"{message}")
    message = input("How are you today? Enter your response here or Q to quit: ")
    if message =="q" or message == "Q" or message == "I am feeling great":
        condition1=True
print ("End")
"""


message = input("How are you today? Enter your response here or Q to quit: ")
while message !="q" or message != "Q" or message != "I am feeling great":
    print(f"{message}")
print ("end")
'''
    message = input("How are you today? Enter your response here or Q to quit: ")  
print ("End")        

  
          
