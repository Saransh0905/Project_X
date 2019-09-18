import pandas as pd

objects = []

with open("./data/uniprot-taenia+solium+protease.fasta",'r') as f:
    lines = f.readlines()

    for i in range(len(lines)):
        if(lines[i][0] == '>'):
            tp, url, info = lines[i].split("|")
            s = ''
            j = i+1
            while j < len(lines):
                if(lines[j][0] != '>'):
                    s += lines[j][:-1]
                    j += 1
                else:
                    break
            objects.append([url,"https://www.uniprot.org/uniprot/"+url,False,s])
            i = j        
            
df = pd.DataFrame(objects)
df.columns = ["Name","url","PresentInTSP","info"]
df.to_csv("d.csv",index=False)

objects = []

with open("./data/T.solium_proteases_280.txt",'r') as f:
    lines = f.readlines()

    for i in range(len(lines)):
        if(lines[i][0] == '>'):
            nm = list(lines[i].split("-"))[0]
            s = ''
            j = i+1
            while j < len(lines):
                if(lines[j][0] != '>' or len(lines[j]) == 0 or lines[j] == '\n'):
                    s += lines[j][:-1]
                    j += 1
                else:
                    break
            objects.append([nm[1:],s])
            i = j 

df = pd.DataFrame(objects)
df.columns = ['name','info']
df.to_csv("tsp.csv",index=False)
