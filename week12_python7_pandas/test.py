ID_ctr={}

for Line in IN:
    Line.strip('\n')
    if re.search("^@(\w+)", Line):
        M=re.search("^@(\w+)", Line)
        ID = M.group(1)
        #print(ID)
        if ID in ID_ctr:
            ID_ctr[ID] = ID_ctr.get(ID) + 1
        else:
            ID_ctr[ID] = 1
        print(ID, ID_ctr[ID])
