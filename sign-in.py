#用户信息字典
import sys

f=open('user_info.txt','r') # 把用户文件打开转换成字典
user_info=f.read()
user_lis=user_info.split('#')
user_dic={}
for item in user_lis:
    item_lis=item.split(':')
    user_dic[item_lis[0]]=item_lis[1]
# user_dic[0]=123
# print(user_dic)


count=0
username=input("用户名输入：")
if username in user_dic: # 判断用户是否在字典里
    l=open('lock_info.txt','r') # 把被锁定用户文件打开转化成字典
    lock=l.read()
    l.close()
    lock_lis = lock.split('#')
    lock_dic = {}
    for items in lock_lis:
        items_lis = items.split(':')
        lock_dic[items_lis[0]] = items_lis[1]
    if username in lock_dic: # 判断用户是否在字典里
        print("被锁定") #在文件中就输出“被锁定”然后退出，不在的文件中，则输入密码
        #退出
        sys.exit('被锁定请联系管理员')
    else:
        while count<3:
            password = input("密码：") # 输入密码
            if password == user_dic[username]: # 用户名和密码正确匹配则登录
                print("登陆成功，欢迎%s!" % username)
                sys.exit()
            else:
                count+=1 # 不然count加1，继续输入密码
                if count==3: # 输入密码次数为3，则吧用户和用户密码写入锁定用户文件中格式为（#alex:123）
                    l=open('lock_info.txt','a')
                    l.write("#%s:%s"%(username,user_dic[username]))
                    print("%s用户被锁定。。。"%username)
                    sys.exit()
                else:print("密码错误！请重新输入。还有%s机会！"% (3-count))
else:
    print("用户名不存在")
