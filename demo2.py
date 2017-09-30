# -*- coding: UTF-8 -*-
import time , datetime
import math
#http://www.pythontip.com/coding/code_oj_case/17
####### 17  给你两个正整数a,b,  输出它们公约数的个数。

def time_txt():
    # return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

a , b  = 24 , 36
g , num = 1 , 0
while  g <= min(a,b): # 这里可以先求最大公约数，减少遍历次数
    if a%g==0 and b%g==0:
        num += 1
    g += 1
print num

print sum([1 if a%x==0 and b%x==0 else 0 for x in range(1,min(a,b)+1)])  # 一行代码

####### 18  给你两个正整数a,b,  输出它们公约数的个数。
### 我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。今天我们反其道而行之，
# 给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。输出这两个数，
# 小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
# 注：所给数据都有解，不用考虑无解的情况。
a ,b = 3 , 60 # 则输出：12 15


####### 19
# 抓不住爱情的我 总是眼睁睁看它溜走 ...现在来练习一下发现爱的能力，
# 给你一个字符串a,如果其中包含"LOVE"（love不区分大小写)则输出LOVE，否则输出SINGLE。
# 例如：a = "OurWorldIsFullOfLOVE"
# 则输出：LOVE
a = "OurWorldIsFullOfLOVE"
if 'love' in a.lower():
    print 'LOVE'
else:
    print 'SINGLE'

####### 20
# 给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。
# 这里将字母表的z和a相连，如果超过了z就回到了a。
# 例如a="cagy", b=3,
# 则输出 ：fdjb
a , b ="cagy" , 3
def ch20(l):
    return chr( ord(l)+b if ord(l)+b <=  ord('z') else ord(l)+b-ord('z')+ord('a')-1 )
print ''.join( map( ch20  , list(a)) )
print(''.join([chr(97+(ord(a[i])-97+b)%26) for i in range(len(a))]))  # 列表推倒

####### 21 回文子串
# 给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
# 回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".
a , n = 'abcddd' , 3
l , r = len(a) , False
for i in range(l-n+1):
    if a[i:i+n]==a[i+n-1:i-1:-1]:
        r = True
        break
print 'YES' if r else 'NO'


######## 24
# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
# 棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
# 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。

# 方法一 bsf  http://www.pythontip.com/coding/report_detail/1930/
def way1(n,m):
    '''
    python的二维数组
    '''
    dx = [1,2,2,1,-1,-2,-2,-1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    def bfs(n,m):
        vis = [ ([0]*(m+1))  for i in range(n+1)]
        q = [(0,0,0)]
        vis[0][0] = 1
        setp = 0xFFFFFFF
        while q:
            temp = q.pop(0)
            if temp[0] == n and temp[1] == m:
                if temp[2] < setp:
                    setp = temp[2]
            for x,y in zip(dx,dy):
                curx = temp[0] + x
                cury = temp[1] + y
                if curx>n or cury>m or curx<0 or cury<0 or vis[curx][cury]:
                    continue
                vis[curx][cury] = 1
                curstep = temp[2] + 1
                q.append((curx,cury,curstep))
        return -1 if setp == 0xFFFFFFF else setp
    print(bfs(n,m))

# 方法二 直接计算  http://www.pythontip.com/coding/report_detail/1789/
def way2(n,m):
    def calc(n,m):
        a=min(n,m)
        b=max(n,m)
        if a==1 and b!=2:
            print (-1)
        elif (a+b)%3==0:
            print ((a+b)//3)
        elif (a+b)%3==1:
            print ((a+b)//3+3)
        else:
            print ((a+b)//3+2)
    calc(n,m)

#  方法三 向量求和 http://www.pythontip.com/coding/report_detail/218/
def way3(n,m):
    steps=[]
    Flag=False
    for i in range(-1,max(m/2,n)+1):
        for j in range(-1,max(m,n/2)+1):
            for k in range(-1,2):
                for l in range(-1,2):
                    a1,a2,a3,a4=i,j,k,l
                    if m==1:
                        a1,a4=0,0
                    if n==1:
                        a2,a3=0,0
                    if 2*a1+a2-a3-2*a4==m and a1+2*a2+2*a3+a4==n and a1+a2>0:
                        steps.append(abs(a1)+abs(a2)+abs(a3)+abs(a4))
                        Flag=True
    if Flag:
        steps.sort()
        print steps[0]
    else:
        print '-1'

# 方法四 终点=向量的和，这个容易理解 http://www.pythontip.com/coding/report_detail/571/
# 该方法 4个 for 循环，效率严重低下，慎运行
def way4(n, m):
    n, m = min(n, m), max(n, m)
    if n < 2:  # 只有一列的情况
        if m / 2.0 % 2 == 1:
            print m / 2
        else:
            print -1
    else:  # 两列或以上
        def Lv_mul(Lv, Ln, n=4):  # n个向量与n个数对应相乘，返回n个向量
            def v_mul(v, k):  # 一个向量与一个数相乘，返回一个向量
                return [i * k for i in v]

            return [v_mul(Lv[i], Ln[i]) for i in range(n)]

        def Lv_sum(L):  # 多个向量相加，返回一个向量
            def v_add(v1, v2):  # 两个向量相加，返回一个向量
                return [v1[i] + v2[i] for i in range(len(v1))]

            return reduce(v_add, L)

        a = [[-1, 2], [1, 2], [2, 1], [2, -1]]  # 四个向量
        S = []  # 可能性集合
        for k0 in range(-m, m):
            for k1 in range(-m, m):
                for k2 in range(-m, m):
                    for k3 in range(-m, m):
                        k = [k0, k1, k2, k3]  # 四个向量的步数（带正负）
                        if Lv_sum(Lv_mul(a, k)) == [n, m]:  # 如果能走到终点
                            S.append(map(abs, k))  # 记录每个向量的步数（去掉正负）
        print reduce(min, map(sum, S))  # 打印最少的步数

n , m =300, 360

for w in ['way1', 'way2', 'way3', 'way4']:
    t1 = time_txt()
    eval(w)(n,m)
    t2 = time_txt()
    print w , t1 , ' ==== ' , t2



