s = input()
ls_alnum=[]
ls_alphabetic=[]
ls_digit=[]
ls_lowercase=[]
ls_uppercase=[]
for i in s:
    ls_alnum.append(i.isalnum())
    ls_alphabetic.append(i.isalpha())
    ls_digit.append(i.isdigit())
    ls_lowercase.append(i.isdigit())
    ls_uppercase.append(i.isupper())
print(any(ls_alnum))
print(any(ls_alphabetic))
print(any(ls_digit))
print(any(ls_lowercase))
print(any(ls_uppercase))