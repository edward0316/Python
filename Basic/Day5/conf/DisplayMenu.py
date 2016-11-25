import json

def display_shopping():
    s = "..\\db\\ShoppingMenu"
    try:
        f = open(s, 'r')
    except:
        print('The file does not exist.')
        exit()
    shoppingDic = json.load(f)
    #adding index in front of the dic's key
    tempList = []
    for i in shoppingDic.keys():
        tempList.append(i)
    #make sure the "Check purchase cart" option always appears at the last.
    shoppingDic["Check purchase cart"]= ""
    shoppingDic["Check out"] = ""
    shoppingDic["Delete item in cart"]= ""
    tempList.append("Check purchase cart")
    tempList.append("Delete item in cart")
    tempList.append("Check out")
    for i in tempList:
        print('%s. %s %s' % (tempList.index(i), i, shoppingDic[i]))
    return tempList


def dispaly_atm():
    s = "..\\db\\atmMenu"
    try:
        f = open(s, 'r')
    except:
        print('The file does not exist.')
        exit()
    atmDic = json.load(f)
    f.close()
    tempList = []
    for i in atmDic.keys():
        tempList.append(i)
    tempList.sort()
    for i in tempList:
        print("%s %s" % (i, atmDic[i]))
    return atmDic

def dispaly_root():
    s = "..\\db\\RootMenu"
    try:
        f = open(s, 'r')
    except:
        print('The file does not exist.')
        exit()
    rootList = json.load(f)
    f.close()
    for i in rootList:
        print("%s %s" % (rootList.index(i),i) )
    return rootList
#dispaly_atm()
#display_shopping()
#dispaly_root()

