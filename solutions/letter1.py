letter = '010 001 000 000 101 00 0111 10001 0110 00 000 01 1 0 0100 1001 10001 101 01 011' \
         ' 0 010 00 10 10001 011 10001 010 111 11 01 10 0 10001 100 011 01 10001 101 01' \
         ' 0110 00 1 01 10 01 10001 111 0110 00 000 01 0100 10001 0110 010 00 1110 00 10' \
         ' 001 10001 0110 111 10001 101 111 1 111 010 111 0111 10001 0110 111 110 00 1000' \
         ' 0100 01 10001 00100 101 000 0110 0 100 00 1010 00 0101 000000 10001 11 10 0' \
         ' 10001 001 100 01 0100 111 000 1001 10001 111 1 0100 111 0001 00 1 1001 10001' \
         ' 101 111 0 100001 101 01 101 00 0 10001 000 1000 0 010 0 0001 0 10 00 0101' \
         ' 10001 00 10001 1010 0 10 10 1011 0 10001 1000 001 11 01 110 00 10001 011' \
         ' 10001 1000 01 10 101 0 000000 10001 000 0 0111 1110 01 000 10001 1 01 11' \
         ' 10001 100 111 0100 0001 10 01 10001 111 101 01 1100 01 1 1001 000 0101' \
         ' 10001 0000 111 010 111 1111 01 0101 10001 000 001 11 11 01 10001 00 1100' \
         ' 10001 1100 01 10001 10 01 101 111 0110 0100 0 10 00 0111 10001 0110 111 10001' \
         ' 0110 010 111 1010 0 10 1 01 11 000000 10001 0101 10001 010 0 1111 00 0100 010101' \
         ' 10001 1110 1 111 10001 1 111 1 10001 0110 1011 1 0100 00 011 1011 0111 10001 001' \
         ' 11 010101 10001 101 111 1 111 010 1011 0111 10001 000 11 111 0001 0 1 10001 111' \
         ' 1 110 01 100 01 1 1001 10001 00100 1 001 10001 1 01 0111 10 001 10001 00 10001' \
         ' 010 01 000 1111 00 0010 010 111 011 01 1 1001 10001 0110 111 000 0100 01 10 00' \
         ' 0 10001 11 111 0001 0 1 10001 1100 01 1000 010 01 1 1001 10001 000 111 100 0 010' \
         ' 0001 00 11 111 0 10001 000 0 0111 0010 01 10001 000 0 1000 0 10001 011 10001' \
         ' 101 01 1110 0 000 1 011 0 10001 011 111 1100 10 01 110 010 01 0001 100 0 10 00' \
         ' 0101 000000 10001 000 0100 0 100 001 0111 10001 00 10 000 1 010 001 101 1010' \
         ' 00 0101 11 10001 011 10001 000 0100 0 100 001 0011 1101 0 11 10001 0110 00' \
         ' 000 1001 11 0 000000 10001 010 111 1000 0 010 1 10001 0010 01 0100 101 111 10' \
         ' 10001 000 101 111 1 1'

letlet=letter.split()

alphabet = '''
А ·−
Б −···
В ·−−
Г −−·
Д −··
Е ·
Ж ···−
З −−··
И ··
Й ·−−−
К −·−
Л ·−··
М −−
Н −·
О −−−
П ·−−·
Р ·−·
С ···
Т −
У ··−
Ф ··−·
Х ····
Ц −·−·
Ч −−−·
Ш −−−−
Щ −−·−
Ъ −−·−−
Ы −·−−
Ь −··−
Э ··−··
Ю ··−−
Я ·−·−
'''

abc=alphabet.split('\n')
n=len(abc)
m=2
qqq = [[''] * m for i in range(n-2)]
for i in range(len(abc)-2):
    ss = abc[i+1].split()

#·−·−
    cc=ss[1].replace('·','0').replace('−','1')
    ll=ss[0]
    qqq[i][0]= cc
    qqq[i][1]= ll

res=''    
for i in range(len(letlet)):
    for j in range(len(qqq)):
        if letlet[i]==qqq[j][0]:
            res=res+qqq[j][1]
            
print(res)    
