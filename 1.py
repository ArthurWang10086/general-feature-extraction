# encoding: utf-8
#601	100200601	26963900601
# 2018-04-22 00:32:49:ShouTu	2017-12-06,2017-11-14	2018-04-06
# 2018-04-29:3,2018-04-26:26,2018-04-28:14	2018-04-29:3,2018-04-28:20,2018-04-26:29	None
# None	2018-04-21:3,2018-04-22:11,2018-04-26:5,2018-04-29:7

#
if __name__=='__main__':
    f = open('la_bi_joined.txt','r')
    data=f.read().split('\n')
    f.close()
    new_data=[]
    f=open('la_bi_actions.txt','w')
    for line in data:
        L = line.split('\t')
        if len(L)==10 or len(L)==12:
            print(len(L),':',L)
            L=L[:5]+['']+L[5:]

        Flag = False
        shoutuTimes = []
        chushiTimes =[]
        churnTimes = []
        tuijianTimes=[]
        extra =[]
        extra.append(L[0])
        extra.append(L[1])
        extra.append(L[2])
        actions = []
        for x in L[3].split(','):
            if x.split(':')[-1]=='ShouTu':
                shoutuTimes.append(x.split(' ')[0])

        shoutuTime = min(shoutuTimes) if len(shoutuTimes)>0 else '2019-01-01'

        for x in L[3].split(','):
            if x.split(':')[-1]=='ChuShi' and len(shoutuTimes)>0 and x.split(' ')[0]>=shoutuTime:
                chushiTimes.append(x.split(' ')[0])

        chushiTime = min(chushiTimes) if len(chushiTimes)>0 else '2019-01-01'

        for x in L[4].split(',')+L[5].split(','):
            if x>shoutuTime:
                churnTimes.append(x)

        if len(L)>11:
            for x in L[11].split(',')+L[12].split(','):
                if x>shoutuTime:
                    tuijianTimes.append(x.split(' ')[0])

        churnTime = min(churnTimes) if len(churnTimes)>0 else '2019-01-01'

        extra.append(shoutuTime)
        extra.append(chushiTime)



        #是否收徒
        if chushiTime==shoutuTime and len(chushiTimes)>0:
            #当天出师
            extra.append(-1)
        elif chushiTime>shoutuTime and len(chushiTimes) >0 and len(shoutuTimes)>0:
            #成功出师
            extra.append(1)
        elif len(shoutuTimes)>0:
            #收徒但没出师
            extra.append(0)
        else:
            break

        #是否流失
        if churnTime<chushiTime and len(churnTimes)>0 and len(chushiTimes)>0:
            extra.append(1)
        elif len(chushiTimes)<1 and len(churnTimes)>0:
            extra.append(1)
        else:
            extra.append(0)

        #是否推荐
        if shoutuTime in tuijianTimes:
            extra.append(1)
        else:
            extra.append(0)

        #actions
        for x in L[6].split(','):
            if len(x.split(':'))>1:
                actions.append(x.split(':')[0]+'\t'+'chat'+'\t'+x.split(':')[1])
        for x in L[7].split(','):
            if len(x.split(':'))>1:
                actions.append(x.split(':')[0]+'\t'+'chat_reverse'+'\t'+x.split(':')[1])
        for x in L[8].split(','):
            if len(x.split(':'))>1:
                actions.append(x.split(':')[0]+'\t'+'trade'+'\t'+x.split(':')[1])
        for x in L[9].split(','):
            if len(x.split(':'))>1:
                actions.append(x.split(':')[0]+'\t'+'trade_reverse'+'\t'+x.split(':')[1])
        for x in L[10].split(','):
            if len(x.split(':'))>1:
                actions.append(x.split(':')[0]+'\t'+'pve'+'\t'+x.split(':')[1])

        for action in actions:
            f.write('\t'.join([str(x) for x in extra])+'\t'+action+'\n')
    f.close()

