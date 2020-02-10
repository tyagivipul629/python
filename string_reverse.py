def reverse(str):
	k=""
	for i in str:
		k=i+k
	if k==str:
		return True
	else:
		return False
str=input("Enter the string:")
if reverse(str):
	print("String is palindrome")
else:
	print("String is not palindrome")