def isEven(page):
    if page % 2 ==0:
        return True
    else:
        return False

p = int(input("please type in the page number: "))

if isEven(p) ==True:
    print(p)
else:
    print("&60s%d"%("",p))

              
