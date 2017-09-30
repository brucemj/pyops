# -*- coding: UTF-8 -*-

import math
# http://www.pythontip.com/coding/code_oj_case/1
####### 1
a = 2
b = 3
print a + b
####### 2
L = [8,2,50,3]
# 冒泡排序
l_size = len(L) - 1
for i in range( l_size ):
    for j in range( 1, l_size - i ):
        if L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
print L
####### 3
a = 'xydz'
print a[::-1]
####### 4
a = {1:1,"a":2,3:3,"b":1}
#print ','.join( sorted(a.keys()) ) # 语法错误， string 和 int 无法 join
print  ','.join( sorted( map(str, a.keys()) ) )
####### 5
a = 'xyzwd'
print a[::2]
####### 6   100以内素数，空格分隔


####### 7   矩形面积，周长
a , b = 3 , 8
print(str(a * b) + ' ' + str(2 * (a + b)))
print("{} {}".format(a * b, 2 * (a + b)))
print(a * b, 2 * (a + b))
print("%s %s"%(a * b, 2 * (a + b)))

####### 8   列表L中位数 （若结果为小数，则保留一位小数）
    ## 对于升序L , 则当N为奇数时, L[(N-1)/2] ; 则当N为偶数时, ( L[(N)/2-1] + L[(N)/2] ) / 2
    ## [注] python2  5/2 = 2 ; python3 5/2=2.5  ; // 为整除
L=[0,1,2,3,4,5]
L.sort()
l_size = len(L)
n = l_size-1 >> 1 ## n = l_size-1 // 1
if l_size % 2 == 0:
    print ("%.1f" % (( L[n] + L[n+1] )/2.0) )
else:
    print L[n]

####### 9 最大公约数
a , b = 847 , 121
n , m = min(a,b) , 1
for i in range(1,n+1):
    if a%i==0 and b%i==0:
        m = i
print m
###  辗转相除啊
n = min([a,b])
m=max([a,b])
while n!=0:
    t = m%n
    m = n
    n = t
print m

####### 11 列表全乘，末尾0的个数
L = [2,8,3,50]

num2 = 0
num5 = 0
for i in L:
    while i % 2 ==0:
        num2 += 1
        i //= 2
    while i % 5 ==0:
        num5 += 1
        i //= 5
print(min(num2,num5))

####### 13 2进制1的个数
a = 9
num = 0
while a!=0:
    if a % 2 == 1:
       num += 1
    a = a//2
print num
a = 9
print sum( map(int , bin(a)[2:]) )

####### 14 print "Python之禅"
#import this
#print this.s

####### 15 大小写转换
print "aaAA123D".lower()

####### 16 人民币金额打印
a = -200023
num = [u'零', u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', '柒', u'捌', u'玖']
unit = [u'', u'拾', u'佰', u'仟', u'万', u'拾', u'佰', u'仟', u'亿', u'拾', u'佰', u'仟',u'万']

rmb , s = '' , str(abs(a))
u , iszero = len(s) , True
for n in range( len(s) ) :
    u = u - 1
    m = int(s[n])
    if m==0:
        #rmb = rmb  + unit[n]
        if iszero == False :
            rmb = rmb + ( '' if unit[u]==u'万' else num[m] )
            iszero = True
        rmb = rmb + ( unit[u] if unit[u]==u'万' else '' )
    else:
        iszero = False
        rmb = rmb + num[m] + unit[u]
print rmb
print (''+ rmb + u'圆') if a>=0 else (u'负'+ rmb + u'圆')

####### 167  一个萝卜一个坑 由于数值太大，最终结果和 1000000007 取模
n = 100
def f(n):
    L = [0, 0, 1, 2]
    if n >= 4 :
        for i in range(4 , n+1):
            t = (i-1) * ( L[i-1] + L[i-2] )
            L.append( t % 1000000007 )
    return L[n] # 每次append取模和 最后结果取模，对最终结果又没有影响 ？？？
print f(n)
####### 169  再谈数数II
a , b = 11 , 20000 # 那么0-9这10个数出现的次数分别是1,10,2,1,1,1,1,1,1,1
    # 考虑到 a b 之间数据规模问题, 不能直接用 range, 应该用迭代器之类
#allnum = ''.join( map(str, range(a,b+1)) )
#allnum_list = list(allnum)
#allnum_list.sort()
    #print sorted(allnum_list)

# 效率依然很低，而且空间消耗很大
L = [0] * 10
s = ""
while a<=b:
    s = s + str(a)
    a += 1
for i in range(10):
    print s.count(str(i))


