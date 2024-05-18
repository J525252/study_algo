def d(n):
    dn = n
    n = str(n)
    for i in range(len(n)):
        dn += int(n[i])

    return str( dn )

dn_list = [str(i) for i in range(1, 10001)]
for n in range(1, 10000):
    dn = d(n)

    if( dn_list.count(dn) != 0 ):
        dn_list.remove(dn)

print( "\n".join(dn_list) )

