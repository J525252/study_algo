s = input()
diff_chr = ord("A") - ord("a") # A = 65, a = 97

new_s = ""
for si in s:
    if( 'a' <= si <= 'z'):
        new_s += chr(ord(si) + diff_chr)
    elif( 'A' <= si <= 'Z'):
        new_s += chr(ord(si) - diff_chr)

print(new_s)
