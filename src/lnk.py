def lnktsrs(jp, Lk):

    print len(Lk.keys())
    print jp
    import copy
    neffs={}
    nte={}
    ntlengthte={}
    ntlengtheff={}
    nlength={}
    mn=0
    for j in Lk.keys():
        qn=copy.deepcopy(j).split('s')
      #  print qn
        qnx=qn[0].split('g')
        qn2=qn[1].split('n')
        qnxx=qnx[0].split('p')
        strain=qn2[1]
        jmp=qnxx[1]
        gen=qnx[1].split('n')[1]
        #print qnx, qn2[1],qnxx[1]
        #print jmp,gen, strain
        #raw_input()
        if jp==int(jmp):
          #print("holalalalala")
          neffs[int(strain)]=Lk[j][3]
          nte[int(strain)]=Lk[j][1]
          ntlengthte[int(strain)]=Lk[j][0]
          ntlengtheff[int(strain)]=Lk[j][2]
          nlength[int(strain)]=Lk[j][4]
          mn+=1
    print mn
    ZN=len(neffs.keys())
    print ZN
    print("PHASE I")

    strain=[]
    neffsst=[]
    ntest=[]
    ltes=[]
    leffs=[]
    ltot=[]
    for i in range(ZN):
        if i in neffs.keys():
            neffsst.append(neffs[i])
            ntest.append(nte[i])
            strain.append(i)
            ltes.append(ntlengthte[i])
            leffs.append(ntlengtheff[i])
            ltot.append(nlength[i])
            #raw_input()
            #neffs.append(Lk[j][3])
            #nte.append
    LENSTATS=[]
    LENSTATS.append(strain)
    LENSTATS.append(neffsst)
    LENSTATS.append(ntest)
    LENSTATS.append(ltes)
    LENSTATS.append(leffs)
    LENSTATS.append(ltot)
    print len(LENSTATS[0])
    return LENSTATS
