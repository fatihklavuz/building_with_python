import time


strl=10
for i in range(strl):
    print(" "*(strl -i)+"*"*(2*i+1))
    time.sleep(1)
for i in range(strl):
    time.sleep(1)
    print("---"*7) 
    print("|_|"*7)
print("|_|"*2,"   |   ", "|_|"*2)
print("|_|"*2," o | o ", "|_|"*2)
print("|_|"*2,"   |   ", "|_|"*2)
print("|_|"*3,"_", "|_|"*3)
