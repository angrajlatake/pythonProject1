import random
import string
"""char= "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*" This is another option of using all the strings"""

password_len = int(input("how long do you want yor password to be : "))
password = int(input("How many passwords do you want to generate : "))
count = 0
s1 = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
while count != password :
    s = "".join(random.sample(s1,password_len))
    print("your password is :", s)
    count +=1
