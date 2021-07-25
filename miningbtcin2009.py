import hashlib, time, random

ok='0000000000000000000000000000000000000000000000000000000000000000'
hexg='9999999999999999999999999999999999999999999999999999999999999999'
print('To mine BTC you will need to find a SHA256 hash starting with 19 zeroes to get 6.25BTC ($215k, July 2021)\nIn 2009, only 8 zeroes were needed to mine a block and get 50BTC ($1.7m, July 2021)\n')
print("However, this doesn't mean that it's easy. This program is made to mimick how much it would take to mine a single block in 2009.")
input('\nPress ENTER to start.\n')
end=1
totaltime=0
while hexg[0:8]!=ok[0:8]: # replace 'hexg[0:8]!=ok[0:8]' with True to keep without an end
    cont=0
    start=time.time()
    while hexg[0:end]!=ok[0:end]:
        hexg=(hashlib.sha256(hex(cont+random.randint(0,1000000)).encode())).hexdigest()
        cont+=1
    endt=time.time()
    tempo=endt-start

    totaltime+=tempo
    print('It took',cont+1,'tries','(',round(tempo,2),'s )','to get the first',end,'numbers right.\nGenerated:',hexg,'\n')
    t=3
    while t!=0:
        print('Trying',end+1,'zeroes in:',t,'s   -   Total time spent:',round(totaltime,2),'s')
        time.sleep(1)
        t-=1
    print('\n')
    end+=1
