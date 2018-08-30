from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import time
from functools import reduce
from collections import Counter

#i=Image.open('images/numbers/y0.5.png')
#iar=np.asarray(i)

#plot.imshow(iar)
#print (iar)
#plot.show()
def createExample():
    numberArrayExample = open('numArEx.txt','a')
    numbersWehave = range(0,10)
    versionsWehave = range(1,10)

    for eachNum in numbersWehave:
        for eachVer in versionsWehave:
            imageFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei =Image.open(imageFilePath)
            eiar= np.array(ei)
            eiar1 = str(eiar.tolist())
 
            lineTowrite = str(eachNum)+'::'+eiar1+'\n'
            numberArrayExample.write(lineTowrite)
    
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            #print (eachPix)
            #time.sleep(5)
            #avgNum = reduce(lambda x , y: x+y, eachPix[:3])/len(eachPix[:3])
            avgNum = sum(eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
    
    
    #balance = reduce(lambda x, y: x+y, balanceAr)/len(balanceAr)
    balance = sum(balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if sum(eachPix[:3])/len(eachPix[:3]) > balance:
                eachPix[0]=255
                eachPix[1]=255
                eachPix[2]=255
                eachPix[3]=255
            else:
            
                eachPix[0]=0
                eachPix[1]=0
                eachPix[2]=0
                eachPix[3]=255
                  
            
    return newAr
def whatNumberIsThis(filepath):
    matchedAr = []
    loadExamples = open('numArEx.txt','r').read()
    loadExamples = loadExamples.split('\n')

    i=Image.open(filepath)
    iar= np.array(i)
    iarl=iar.tolist()
    
 
    inQuestion = str(iarl)

    for eachExample in loadExamples:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixInQuestion = inQuestion.split('],')
            eachPixEx = currentAr.split('],')
            x=0
            while x<len(eachPixEx):
                if eachPixEx[x]==eachPixInQuestion[x]:
                    matchedAr.append(int(currentNum))
                x=x+1
    print (matchedAr)
    x=Counter(matchedAr)
    print (x)
            
            

whatNumberIsThis('images/test.png') 

i = Image.open('images/numbers/0.1.png');
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png');
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png');
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png');
iar4 = np.array(i4)

'''threshold(iar3)
threshold(iar4)
threshold(iar2)

fig = plot.figure()
ax1 = plot.subplot2grid((8,6),(0,0), rowspan = 3, colspan = 3)
ax2 = plot.subplot2grid((8,6),(4,0), rowspan = 3, colspan = 3)
ax3 = plot.subplot2grid((8,6),(0,3), rowspan = 3, colspan = 3)
ax4 = plot.subplot2grid((8,6),(4,3), rowspan = 3, colspan = 3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plot.show()
'''
