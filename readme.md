#作业-1

 1. 程序功能介绍
 2. readme
 3. 流程图
 4. 代码

## 1.程序功能介绍
登录程序：输入用户名，用户名不在被锁定用户名单中则输入密码，如用户名和密码正确则登录成功，否则输入3次错误用户名或者密码，则添加进被锁定用户无法登录。
###2.readme
用户名密码需要提前写入文件夹user_info.txt，被锁定用户也可以提前写入锁定文件夹lock_info.txt。格式都为alex：123，也可以打开这个文件查看格式！
###3.流程图
```flow
flow
st=>start: 开始
op=>operation: 输入用户名
cond=>condition: 判断是否被锁定
op2=>operation: 输入密码
cond2=>condition: 判断用户名密码是否匹配
op3=>operation: 重新输入密码
cond3=>condition: 输入次数为3次后锁定
e=>end: 退出！
e2=>end: 登录成功！
e3=>end: 被锁定退出！
st->op->cond
cond(yes)->e
cond(no)->op2
op2->cond2
cond2(yes)->e2
cond2(no)->op3
op3->cond3
cond3(yes)->e3
```
###代码
```python
import sys

f=open('user_info.txt','r') # 把用户文件打开转换成字典
user_info=f.read()
user_lis=user_info.split('#')
user_dic={}
for item in user_lis:
    item_lis=item.split(':')
    user_dic[item_lis[0]]=item_lis[1]

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

```

