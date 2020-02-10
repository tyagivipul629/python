def orangecap(d):
	d1={}
	for matchno,match in d.items():
		for playerno in match:
			d1[playerno]=0
	for matchno,match in d.items():
		for playerno in match:
			d1[playerno]=d1[playerno]+d[matchno][playerno]
	hscore=-1
	playername=-1
	for key in d1:
		if hscore<d1[key]:
			hscore=d1[key]
			playername=key
	return((playername,hscore))

print(orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
)