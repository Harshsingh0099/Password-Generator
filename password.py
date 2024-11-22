import random as rd
import string as st
length = int(input("enter the length of password : "))
lower = st.ascii_lowercase
upper = st.ascii_uppercase
num = st.digits
symbols = st.punctuation
all = lower + upper + num + symbols
temp = rd.sample(all,length)
password = "".join(temp)
print(password)

