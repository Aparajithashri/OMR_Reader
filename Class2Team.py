import random
from fpdf import FPDF
pdf=FPDF(format='A4')
pdf.add_page()
pdf.set_font("Arial",size=10)

f=open("Class2Team.csv","r")
boy=[[],[]]
girl=[[],[]]
lines=[]
output = [line.rstrip("\n") for line in f.readlines()]
for i in output:
	lines.append([j for j in i.split(',')])
for i in range(len(lines)):
	for j in lines[i]:
		if j=="Boy":
			if lines[i][2]=="IT":
				boy[1].append(lines[i])
			elif lines[i][2]=="CS":
				boy[0].append(lines[i])
		elif j=="Girl":
			if lines[i][2]=="IT":
				girl[1].append(lines[i])
			elif lines[i][2]=="CS":
				girl[0].append(lines[i])
team=[[],[],[],[],[]]
a=0

for i in range(50):
        s=random.choice(girl[0])
        team[a].append(s)
        girl[0].remove(s)
        s=random.choice(girl[1])
        team[a].append(s)
        girl[1].remove(s)
        s=random.choice(boy[0])
        team[a].append(s)
        boy[0].remove(s)
        s=random.choice(boy[1])
        team[a].append(s)
        boy[1].remove(s)
        a+=1
        if a==5:
                if len(boy[0])<5 or len(boy[1])<5 or len(girl[0])<5 or len(girl[1])<5:
                        break
                else:

                        a=0
m=0
for i in boy:
        for k in i:
                team[m].append(k)
                m+=1
                if m==5:
                        m=0
for i in girl:
        for l in i:
                team[m].append(l)
                m+=1
                if m==5:
                        m=0
                
tn=['Blue','Green','Pink','Yellow','White']
for i in team:
        i=i.sort(key=lambda x:x[1],reverse=True)
x=0
for i in team:
        pdf.multi_cell(0,4,('%s Team'%str(tn[x])))
        pdf.ln()
        for j in i:
                pdf.multi_cell(100,5,('%s,%s,%s'%(j[1],j[2],j[0])))
        pdf.ln()       
        x+=1
pdf.output("Class2Team.pdf")
