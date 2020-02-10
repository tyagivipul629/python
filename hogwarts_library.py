ls_books={}
ls_borrower=[]
ls_checkout=[]
ls_issued=[]
def add_to_list():
	str1=input()
	if str1=='Books':
		str1=input()
		while str1!='Borrowers':
			ls=str1.split('~')
			ls_books[ls[0]]=ls[1]
			str1=input()
	if str1=='Borrowers':
		str1=input()
		while str1!='Checkouts':
			ls=str1.split('~')
			ls_borrower.append(ls)
			str1=input()
	if str1=='Checkouts':
		str1=input()
		while str1!='EndOfInput':
			ls=str1.split('~')
			ls_checkout.append(ls)
			str1=input()
def issue_details():
	for i in ls_checkout:
		for j in ls_borrower:
			if i[0]==j[0]:
				st=ls_books[i[1]]
				ls_issued.append([i[2].strip('\n'),j[1].strip('\n'),i[1],st.strip('\n')])
	ls_issued.sort()
def print_details():
	for i in ls_issued:
		print(i[0],i[1],i[2],i[3],sep='~')
add_to_list()
issue_details()
print_details()
