# my first python challenge 
Birth =input("Please enter year of birth: ")
Year = int(Birth)
Age = 2019 - Year
if Age < 18:
    print("you are a minor")
elif Age >= 18 and Age <= 36:
    print("you are a youth")
else:
    print("you are an elder")
