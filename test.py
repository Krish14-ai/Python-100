vowels = ['a','e','i','o','u'] 
str = input("Enter a string : ")
count = 0   
count = sum(1 for char in str.lower() if char in vowels)
print("Number of vowels in the string is : ", count)