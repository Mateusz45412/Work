line_sn = 0
# kenetration = ((line_sn-3)*1700) + ((line_sn-(line_sn-3)) * 500)

cabel1= ((line_sn-1)//3)+1
cabel2= line_sn-cabel1

kenetration = (cabel1*1700)+(cabel2*500)


print(kenetration)
