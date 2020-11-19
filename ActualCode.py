import googletrans
translator = googletrans.LANGUAGES

LaNG = {}
count= 0

for n in translator.items():
    if(n[0] == 'hi'):
        print(count)
    LaNG[n[1]] = n[0]
    count += 1

print(LaNG)