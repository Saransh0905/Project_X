import pandas as pd

data=pd.read_csv("C:/Users/DELL/Desktop/data_main.csv")
columns=data.columns
functioncolumn=data.iloc[:,-1]
funcol=[]
for i in range(len(functioncolumn)):
    functioncolumn[i]=str(functioncolumn[i])
    funcol.append(functioncolumn[i].split(','))
    funcol[i]=sorted(funcol[i])


clas=[]
for i in range(len(funcol)):
    new=[]
    for j in range(len(funcol[i])):
        if funcol[i][j][:7].lower()=='metallo':
            new.append('Metal')
        if funcol[i][j][:8].lower()=='cysteine':
            new.append('Cysteine')
        if funcol[i][j][:8].lower()=='aspartic':
            new.append('Aspartic')
        if funcol[i][j][:8].lower()=='glutamic':
            new.append('Glumatic')
        if funcol[i][j][:6].lower()=='serine':
            new.append('Serine')
        if funcol[i][j][:9].lower()=='threonine':
            new.append('Threonine')
    new=list(set(new))
    clas.append(new)
print(clas)