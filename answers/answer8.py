menfront=(jeans['FrontArea'][jeans['men'] == 1].mean())
menback=(jeans['BackArea'][jeans['men'] == 1].mean())
womenfront=(jeans['FrontArea'][jeans['women'] == 1].mean())
womenback=(jeans['BackArea'][jeans['women'] == 1].mean())

print('Avg men front pocket size is ' + str(menfront)) 
print('Avg men back pocket size is ' + str(menback)) 
print('Avg women front pocket size is ' + str(womenfront)) 
print('Avg women back pocket size is ' + str(womenback)) 
