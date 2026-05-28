import math
import secrets

global pqlist
global e,N,d
pqlist=[]
e=65537
N=0
d=0

MorseNum={
    "A":12,
    "B":2111,
    "C":2121,
    "D":211,
    "E":1,
    "F":1121,
    "G":221,
    "H":1111,
    "I":11,
    "J":1222,
    "K":212,
    "L":1211,
    "M":22,
    "N":21,
    "O":222,
    "P":1221,
    "Q":2212,
    "R":121,
    "S":111,
    "T":2,
    "U":112,
    "V":1112,
    "W":122,
    "X":2112,
    "Y":2122,
    "Z":2211,

    "1":12222,
    "2":11222,
    "3":11122,
    "4":11112,
    "5":11111,
    "6":21111,
    "7":22111,
    "8":22211,
    "9":22221,
    "0":22222,

    "?":112211,
    ".":121212,
    ",":221122,
    "-":211112,
    ":":222111,
    "/":21121
}

def random():
    n=secrets.randbits(512)|1
    n=n*2310+1
    return n
def Miller():#Miller–Rabin
    while 1:
        n=random()
        d=n-1
        s=0
        while d%2 == 0:
            d//=2
            s+=1
        ok = True
        for a in [2,3,5,7,11,13,17]:
            x=pow(a,d,n)
            if x in (1,n-1):
                continue
            for _ in range(s-1):
                x=pow(x,2,n)
                if x == n-1:
                    break
            else:
                ok = False
                break
        if ok:
            return n


def Prime():
    global e,N,d
    p=Miller()
    while 1:
        q=Miller()
        N=p*q
        phi=(p-1)*(q-1)
        if math.gcd(e,phi)==1:
            d=pow(e,-1,phi)
            if (e*d)%phi == 1:
                break
def RSA(mode):
    if mode == 0:
        text=input("数字 >>")
        M=pow(int(text),e,N)
        print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print()
        print("暗号化 >>",M)
    elif mode == 1:
        code=input("暗号 >>")
        C=pow(int(code),d,N)
        print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print()
        print("復号化 >>",C)
    return

def Pollard():#Pollard’s Rho
    Prun=1
    while Prun:
        inprun=1
        while inprun:
            n=input("nを入力, exit:終了 >>")
            print(n)
            c2=input("決定？(y/n) >>")
            if c2=="y":
                inprun=0
        if n=="exit":
            break
        else:
            n=int(n)
        a=1
        value=[2,2]
        while a == 1:
            value[0]=(value[0]**2+1)%n
            value[1]=(value[1]**2+1)%n
            value[1]=(value[1]**2+1)%n
            a=math.gcd(abs(value[0]-value[1]),n)
        if a == n:
            print("失敗")
        else:
            print(a,n//a)
def Morse():
    while 1:
        inprun=1
        while inprun:
            mode=input("1:変換, 2:復号, exit:終了 >>")
            c2=input("決定？(y/n) >>")
            if mode not in ("1","2","exit"):
                print("不正")
            elif c2=="y":
                inprun=0
        if mode == "1":
            inprun=1
            while inprun:
                code=input("codeを入力 >>")
                print(code)
                c2=input("決定？(y/n) >>")
                if c2=="y":
                    inprun=0
            print()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print()

            a=0
            l=len(code)
            s=str(code)
            for i in range(l):
                a+=int(s[-i-1])*3**i
            print("十進法 >>",a)
        elif mode == "2":
            inprun=1
            while inprun:
                n=input("数字を入力, exit:終了 >>")
                print(n)
                c2=input("決定？(y/n) >>")
                if c2=="y":
                    inprun=0
                    n=int(n)
            print()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print()

            check=1
            keta=0
            a=""
            while check < n:
                check*=3
                keta+=1
            for i in range(keta+1):
                if 2*check<=n:
                    a=a+"2"
                    n-=2*check
                elif check<=n:
                    a=a+"1"
                    n-=check
                else:
                    a=a+"0"
                check//=3
            print("三進法 >>",int(a))
        elif mode == "exit":
            break
        print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print()

def Morse2():
    while 1:
        inprun=1
        while inprun:
            mode=input("1:変換, 2:復号, exit:終了 >>")
            c2=input("決定？(y/n) >>")
            if mode not in ("1","2","exit"):
                print("不正")
            elif c2=="y":
                inprun=0
        if mode=="1":
            inprun=1
            while inprun:
                text=input("文字を入力 >>")
                print(text)
                c2=input("決定？(y/n) >>")
                if c2=="y":
                    inprun=0
            text=text.upper()
            print()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print()

            a="0"
            for i in range(len(text)):
                a+=str(MorseNum[text[i]])+"0"
            print(a)
            print()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print()
        elif mode=="2":
            inprun=1
            while inprun:
                code=input("コードを入力 >>")
                print(code)
                c2=input("決定？(y/n) >>")
                if c2=="y":
                    inprun=0
            print()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print()
            code=code.split('0')
            s=""
            for i in code:
                for k,v in MorseNum.items():
                    if i == str(v):
                        s+=str(k)
                        break
                else:
                    s+=" "
            print(s.lower())
            print()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print()

        elif mode=="exit":
            break



address={
    "me":{
        "N":1,#自分の公開鍵を書く
        "e":65537#ここは共通の方がいい
    },
    "2":{
        "N":1,#人の公開鍵をここにメモしておく
        "e":65537
    }
}




def main():
    global e,N,d
    run=1
    d=1#自分の秘密鍵を書く。
    name="Non"
    while run:
        print("送信先設定:",name)
        print("秘密鍵:",d)
        print("公開鍵",N)
        print("公開鍵2",e)
        print()
        print("mode 0:初期化, 02:送信先設定 1:暗号化, 2:素因数分解, 3:素数生成, 4:復号, 5:モールス十進, 6:モールス三進")
        c=input("exit:終了 >>")
        if c=="0":
            d=int(input("d >>"))
            N=int(input("N >>"))
            e=int(input("e >>"))
        elif c=="02":
            inprun=1
            while inprun:
                mode=input("1:手打ち, 2:アドレス, exit:終了 >>")
                c2=input("決定？(y/n) >>")
                if mode not in ("1","2","exit"):
                    print("不正")
                elif c2=="y":
                    inprun=0
            if mode=="1":
                N=int(input("N >>"))
                e=int(input("e >>"))
                name="Non"
            if mode=="2":
                print(address.keys())
                inprun=1
                while inprun:
                    ad=input("アドレス >>")
                    c2=input("決定？(y/n) >>")
                    if ad not in (address):
                        print("不正")
                    elif c2=="y":
                        inprun=0
                N=int(address[ad]["N"])
                e=int(address[ad]["e"])
                name=ad

        elif c=="1":
            RSA(0)
        elif c=="2":
            Pollard()
        elif c=="3":
            Prime()
        elif c=="4":
            RSA(1)
        elif c=="5":
            Morse()
        elif c=="6":
            Morse2()



        elif c=="exit":
            c2=input("終了しますか？(y/n) >>")
            if c2=="y":
                run=0
        else:
            print("不明")
        print()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print()




if __name__=="__main__":
    main()
