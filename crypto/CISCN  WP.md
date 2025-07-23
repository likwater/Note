# 2023
## SM2

1. 仔细阅读文档，按照文档中的要求进行操作，先生成公私钥对（用网址[https://const.net.cn/tool/sm2/genkey/](https://const.net.cn/tool/sm2/genkey/)），输入命令行，得到
```
私钥A  92B14610F8DEBCE61D5DA123E7817D94D6925BF66E39A39D8FA39F0CB3FBCEBF
公钥A  20F0DD108E3C83ACF3D09C63F530F25DE4285038ABB3EC10F2EB69CF84A49DF2F89C1A095A6C55D602E97A1AAAD42B75D08F22E4D2CB73866554F5304B24F40B
公钥B（明文）"publicKey": "046fd1df43b8d49b3b3a922bc7ffd15c86a7f2773f3a397f61dea47d869eb65979f8f68d5b592ea478d03ca8c8610a1fc381b08b8def17741b974b9815cfd5c632",
私钥B（密文）"privateKey": "67b17ed330c61caf2d9229407d21d6de97713516316b6d54f8fd94352efdbecd",
随机数c(密文)"randomString": "ec3c9c54291b80e1dacda3f99ac42c18194a2a9df3972d9f57584a2b0a2cbb166c75fc77597e6f5a4edf0a91d725d446bc32b918695b492565e3ca7b36a5c53ca85453b3c63456d1fee29e04a97d79716da7155eb01052a9d7357c889d6f6d86e5d7de774a2a02473f0945a026f59e52",
```

2. 用sm2和sm4（[https://const.net.cn/tool/sm2/sm2-decrypt/](https://const.net.cn/tool/sm2/sm2-decrypt/)；[https://const.net.cn/tool/sm4/sm4-ecb-decrypt/](https://const.net.cn/tool/sm4/sm4-ecb-decrypt/)）在线解密网站，按文档中的要求进行解密
3. 最后得到正确的D的明文：
```
curl -d "name=%E5%88%98%E9%95%87%E7%8E%AE&school=%E6%B5%B7%E5%8D%97%E5%A4%A7%E5%AD%A6&phone=18990663161" http://123.56.244.196:20043/api/login

 "id": ”41161566-7538-4551-a417-7d653c08d12d"

curl -d "id=41161566-7538-4551-a417-7d653c08d12d&publicKey=20F0DD108E3C83ACF3D09C63F530F25DE4285038ABB3EC10F2EB69CF84A49DF2F89C1A095A6C55D602E97A1AAAD42B75D08F22E4D2CB73866554F5304B24F40B" http://123.56.244.196:20043/api/allkey

私钥A  92B14610F8DEBCE61D5DA123E7817D94D6925BF66E39A39D8FA39F0CB3FBCEBF
公钥A  20F0DD108E3C83ACF3D09C63F530F25DE4285038ABB3EC10F2EB69CF84A49DF2F89C1A095A6C55D602E97A1AAAD42B75D08F22E4D2CB73866554F5304B24F40B
公钥B（明文）"publicKey": "046fd1df43b8d49b3b3a922bc7ffd15c86a7f2773f3a397f61dea47d869eb65979f8f68d5b592ea478d03ca8c8610a1fc381b08b8def17741b974b9815cfd5c632",
私钥B（密文）"privateKey": "67b17ed330c61caf2d9229407d21d6de97713516316b6d54f8fd94352efdbecd",
随机数c(密文)"randomString": "ec3c9c54291b80e1dacda3f99ac42c18194a2a9df3972d9f57584a2b0a2cbb166c75fc77597e6f5a4edf0a91d725d446bc32b918695b492565e3ca7b36a5c53ca85453b3c63456d1fee29e04a97d79716da7155eb01052a9d7357c889d6f6d86e5d7de774a2a02473f0945a026f59e52",

curl -d "id=41161566-7538-4551-a417-7d653c08d12d" http://123.56.244.196:20043/api/quantum
密钥D(密文)"quantumString": "af938591d55923cef0f458a11648324be23dd0a4ffe92085489a07c4ae544d8e489372dc1896924609c1b1411c5a4da46cf3bffc40c0d087cf4faa8a4dba59e874dbf7b2563bb3261a9f1a48d2e5bb2a54c78e044cf3043f54fa825d1f7956930c408a963ac59231b6675487b8941b9b"

curl -d "id=41161566-7538-4551-a417-7d653c08d12d&quantumString=4b3a23518f239acfd77bbb2480bdcdf4" http://123.56.244.196:20043/api/check

c明文：F4 8B BF 61 0F 39 F4 64 15 23 57 89 AA 5E 8E E1 
私钥B明文：90 D9 8D B9 05 E7 37 C5 CA F8 9C 8B 45 0B D8 80 3F 53 9C 76 F5 96 BC 2D 81 BA 48 47 BA F7 05 5A 
D ： 4B3A23518F239ACFD77BBB2480BDCDF4  4b3a23518f239acfd77bbb2480bdcdf4

curl -d "id=41161566-7538-4551-a417-7d653c08d12d" http://123.56.244.196:20043/api/search


```

4. 将D的明文发送过去，可以得到最终的flag，提交即可
## sign in passwd:

1. 题目
```
j2rXjx8yjd=YRZWyTIuwRdbyQdbqR3R9iZmsScutj2iqj3/tidj1jd=D
GHI3KLMNJOPQRSTUb%3DcdefghijklmnopWXYZ%2F12%2B406789VaqrstuvwxyzABCDEF5
```

2. 看见有%，且%后面的两个字母像是16进制，可以考虑是这部分是url编码，解码后得到
```
GHI3KLMNJOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF5
```

3. 发现这是一个长为65的字符串，包含连续字符A-Z、a-z、0-9、+、/、=，因此猜测这是一个base64密码表，这是一个字母对应表，对应规则：（有时可能是64个，没有那个等号），再将还原后的字符串进行base64解码
```
GHI3KLMNJOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF(5)
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/(=)
```

4. 脚本
```
import base64
import urllib.parse
# This is your custom Base64 alphabet
custom_alphabet = 'GHI3KLMNJOPQRSTUb%3DcdefghijklmnopWXYZ%2F12%2B406789VaqrstuvwxyzABCDEF5'
# Decode the URL-encoded characters in the custom alphabet
custom_alphabet = urllib.parse.unquote(custom_alphabet)
# This is the standard Base64 alphabet
standard_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
# Create a translation table that maps characters from the custom alphabet to the standard alphabet
translation_table = str.maketrans(custom_alphabet, standard_alphabet)
# This is the encoded string
encoded_string = 'j2rXjx8yjd=YRZWyTIuwRdbyQdbqR3R9iZmsScutj2iqj3/tidj1jd=D'
# Translate the encoded string using the translation table
translated_string = encoded_string.translate(translation_table)
print(translated_string)
# Decode the translated string using standard Base64
decoded_string = base64.b64decode(translated_string).decode('utf-8')
print(decoded_string)

```

5. 还可用网站解码base64：
   1. [https://ctf.mzy0.com/CyberChef3/#recipe=From_Base64%EF%BC%88Base64%E8%BD%AC%E6%8D%A2%EF%BC%89('GHI3KLMNJOPQRSTUb%3DcdefghijklmnopWXYZ/12%2B406789VaqrstuvwxyzABCDEF5',true)&input=ajJyWGp4OHlqZD1ZUlpXeVRJdXdSZGJ5UWRicVIzUjlpWm1zU2N1dGoyaXFqMy90aWRqMWpkPUQzMQ](https://ctf.mzy0.com/CyberChef3/#recipe=From_Base64%EF%BC%88Base64%E8%BD%AC%E6%8D%A2%EF%BC%89('GHI3KLMNJOPQRSTUb%3DcdefghijklmnopWXYZ/12%2B406789VaqrstuvwxyzABCDEF5',true)&input=ajJyWGp4OHlqZD1ZUlpXeVRJdXdSZGJ5UWRicVIzUjlpWm1zU2N1dGoyaXFqMy90aWRqMWpkPUQzMQ)
   2. alphabet中填对应规则的字母串
```
GHI3KLMNJOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF5
```
再直接输入徐解密的密文即可解密
## 可信度量：

1. 和去年一样，今年同样是将flag还是直接存在了靶机中。估计出题人可信计算水平很高，但是不太了解Linux系统的权限和命令。直接grep搜索一下：
```
grep -r "flag{" /
```
2. 末尾得到搜索到的文件结果，直接cat即可得到Flag。

## badkey:

1. 题目：给的是交互式环境，找到满足条件的x，p，q，即可得到flag。x的长度只有4，可以通过枚举，找到正确的x
```
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from hashlib import sha256
import random, os, signal, string

def proof_of_work():
    random.seed(os.urandom(8))
    proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    print('Give me XXXX: ')
    x = input()
    if len(x) != 4 or sha256(x.encode()+proof[4:].encode()).hexdigest() != _hexdigest:
        print('Wrong PoW')
        return False
    return True

if not proof_of_work():
    exit(1)
    
signal.alarm(10)
print("Give me a bad RSA keypair.")

try:
    p = int(input('p = '))
    q = int(input('q = '))
    assert p > 0
    assert q > 0
    assert p != q
    assert p.bit_length() == 512
    assert q.bit_length() == 512
    assert isPrime(p)
    assert isPrime(q)
    n = p * q
    e = 65537
    assert p % e != 1
    assert q % e != 1
    d = inverse(e, (p-1)*(q-1))
except:
    print("Invalid params")
    exit(2)

try:
    key = RSA.construct([n,e,d,p,q])
    print("This is not a bad RSA keypair.")
    exit(3)
except KeyboardInterrupt:
    print("Hacker detected.")
    exit(4)
except ValueError:
    print("How could this happen?")
    from secret import flag
    print(flag)

```

2. 考源码审计（）：有题知按要求正常生成的n、d、e、p、q，要不符合python函数RSA.construct([n,e,d,p,q])，进入construct函数的源码查看，发现只能是n和d不互质才能满足题上条件。![image-20240714161425482](./图片/CISCN  WP.assets/image-20240714161425482-1721656469206-1.png)
   1. 因为只有当d=a*p，n=p*q才能满足d和n不互质，所以得到a∗p∗e=k∗(p−1)∗(q−1)+1  =>  p∗[(q−1)∗k−a∗e]=(q−1)∗k−1                       =>p=[(q−1)∗k−1]/[(q−1)∗k−a∗e]。因为p为整数，所以(q−1)∗k−a∗e是(q−1)∗k−1的因子   
   2. 当k>e时，phi*k>phi*e,由phi*k=a∗p∗e-1=d*e-1>phi*e => d>phi,因为rsa中d<phi，与之相矛盾，所以不成立。
   3. 所以只考虑k<e时的情况，设p大于q，所以 (q−1)∗k−a∗e是小因子，令A=q-1，则a∗p∗e=k∗(p−1)∗(q−1)+1等价于a∗p∗e=k∗(p−1)∗A+1，                                    同时除p, 得a*e=k*(p-1)*A/p，变形后得 A*k-a*e=k*A/p-1，
   4. 因为p>q，所以A/p=(q-1)/p<1 =>A*k/p<k<e => A*k-a*e=k*A/p-1<e
   5. 所以(q−1)∗a−k∗e<e =>令(q−1)∗a=k*e+b,则[(q−1)∗a]%e=b，所以(q−1)∗a−k∗e=b=[(q−1)∗a]%e，b!=0 => p=[(q−1)∗a−1]/[(q−1)∗a]%e]
```
e = 65537
while True:
    q = getPrime(512)
    for k in range(e):
        x = (q-1)*k
        x %= e
        if x == 0:
            continue
        if ((q-1)*k-1) % x == 0:
            p = ((q-1)*k-1)//x
            if isPrime(p) and p.bit_length()==512:
                print(p,q)
                break
```

3. construct函数的源码查看：
   1. 按ctrl键，点击construct函数，但进去后会发现源码不对，看不到有效信息，是个pyi文件，因此我们需要进入此代码所存放的文件夹中去寻找真正的函数源代码。
   2. 在cunstruct函数的pyi文件中，点击右键，找到“打开与”，点击“文件路径”即可知道此代码在文件中的位置![image-20240714161444406](./图片/CISCN  WP.assets/image-20240714161444406-1721656475153-3.png)
   3. 得到这个，再双击点击，即可打开此代码所在的文件夹                                          <img src="D:/笔记/图片/CISCN  WP.assets/image-20240714161501653.png" alt="image-20240714161501653" style="zoom:80%;" />
   4. 再在该文件夹中找到名为rsa的py文件，在此源码中找到名为construct的自定义函数，这时找到的函数源码才是真正的源码
4. 函数的源码查看：
   1. 按ctrl键，点击需查看的函数，进去后观察源码是否正确，如果看不到有效信息，是个pyi文件或其他文件
   2. 此时我们需要进入此代码所存放的文件夹中去寻找真正的函数源代码。
   3. 在此函数的pyi文件或其他文件中，点击右键，找到“打开与”，点击“文件路径”即可知道此代码在文件中的位置
   4. 得到这个，再双击点击此文件名，即可打开此代码所在的文件夹，然后在其中找与该函数库名相同的文件，有可能时py文件，也可能是c文件，如果都没找到，就一次点开看，最终找到有效文件，再在其中找与该函数名相同的自定义函数即可

# 2024

## OvO

1. 题目：

   ```python
   from Crypto.Util.number import *
   from secret import flag
   
   nbits = 512
   p = getPrime(nbits)
   q = getPrime(nbits)
   n = p * q
   phi = (p-1) * (q-1)
   while True:
       kk = getPrime(128)
       rr = kk + 2
       e = 65537 + kk * p + rr * ((p+1) * (q+1)) + 1
       if gcd(e, phi) == 1:
           break
   m = bytes_to_long(flag)
   c = pow(m, e, n)
   
   e = e >> 200 << 200
   print(f'n = {n}')
   print(f'e = {e}')
   print(f'c = {c}')
   
   """
   n = 111922722351752356094117957341697336848130397712588425954225300832977768690114834703654895285440684751636198779555891692340301590396539921700125219784729325979197290342352480495970455903120265334661588516182848933843212275742914269686197484648288073599387074325226321407600351615258973610780463417788580083967
   e = 37059679294843322451875129178470872595128216054082068877693632035071251762179299783152435312052608685562859680569924924133175684413544051218945466380415013172416093939670064185752780945383069447693745538721548393982857225386614608359109463927663728739248286686902750649766277564516226052064304547032760477638585302695605907950461140971727150383104
   c = 14999622534973796113769052025256345914577762432817016713135991450161695032250733213228587506601968633155119211807176051329626895125610484405486794783282214597165875393081405999090879096563311452831794796859427268724737377560053552626220191435015101496941337770496898383092414492348672126813183368337602023823
   """
   
   ```

2. 求解推导：
   $$
   e=65537+kp+(k+2)(p+1)(q+1)+1=(k+2)n+(2k+2)p+(k+2)q+(k+65540) \\
   ⇒e//n=k+2+(2k+2)p//n+(k+2)q//n+(k+65540)//n=k+2 \\
   因为题目中最终给出的是e',e'=e >> 200 << 200,所以\Delta e =e-e'，且\Delta e 的最大是200位\\
   因为n是1024位，所以n远远大于\Delta e，所以e'//n = (e-\Delta e)=e//n-\Delta e // n=k+2，k=e'//n−2\\
   令e中已知的项都为a，即a=(k+2)n+k+65540 \\
   e=(2k+2)p+(k+2)q+a \\
   ep=(2k+2)p^2+(k+2)n+ap \\
   目前是e的低200位未知，等式又已知,所以解出来的p也是高位基本准确，低200位未知 \\
   那么具体解法可以参考d的高位攻击，很快便能出结果的
   $$

3. 代码

   ```sage
   from Crypto.Util.number import *
   
   def get_full_p(p_high, n, bits):
       PR.<x> = PolynomialRing(Zmod(n))    
       f = x + p_high
       f = f.monic()
       roots = f.small_roots(X=2^(bits + 10), beta=0.4)  
       if roots:
           x0 = roots[0]
           p = gcd(x0 + p_high, n)
           return ZZ(p)
   
   n = ...
   e = ...
   c = ...
   
   k = e // n - 2
   a = 65537 + (k + 2) * n + (k + 2) + 1
   P.<x> = PolynomialRing(RealField(1024))
   f = e * x - ((2 * k + 2) * x ^ 2 + (k + 2) * n + a * x)
   res = f.roots()
   
   if res:
       for y in res:
           p_high = int(y[0])
           p = get_full_p(p_high, n, 200)
           if p:
               print(p)   
   ```

   ```python
   from Crypto.Util.number import *
   n = ...
   e = ...
   c = ...
   k = e // n - 2
   p = 9915449532466780441980882114644132757469503045317741049786571327753160105973102603393585703801838713884852201325856459312958617061522496169870935934745091
   q = n // p
   e = 65537 + k * p + (k + 2) * ((p+1) * (q+1)) + 1
   phi = (p - 1) * (q - 1)
   d = gmpy2.invert(e,phi)
   print(long_to_bytes(gmpy2.powmod(c,d,n)))
   ```


## chechin

1. 题目

   ```python
   from Crypto.Util.number import *
   from secret import flag
   
   p = getPrime(512)
   q = getPrime(512)
   n = p*q
   x = 2021*p+1120*q
   h = (inverse(x,n)+x)%n
   e = 65537
   c = pow(bytes_to_long(flag), e, n)
   
   print('n =', n)
   print('c =', c)
   print('h =', h)
   print('p0 =', p >> 490)
   
   # n = 124592923216765837982528839202733339713655242872717311800329884147642320435241014134533341888832955643881019336863843062120984698416851559736918389766033534214383285754683751490292848191235308958825702189602212123282858416891155764271492033289942894367802529296453904254165606918649570613530838932164490341793
   # c = 119279592136391518960778700178474826421062018379899342254406783670889432182616590099071219538938202395671695005539485982613862823970622126945808954842683496637377151180225469409261800869161467402364879561554585345399947589618235872378329510108345004513054262809629917083343715270605155751457391599728436117833
   # h = 115812446451372389307840774747986196103012628652193338630796109042038320397499948364970459686079508388755154855414919871257982157430015224489195284512204803276307238226421244647463550637321174259849701618681565567468929295822889537962306471780258801529979716298619553323655541002084406217484482271693997457806
   # p0 = 4055618
   
   ```

2. 题目分析

3. 代码

## ez_rsa

1. 题目

   ```python
   from Crypto.Util.number import *
   from Crypto.PublicKey import RSA
   import random
   from secret import flag
   
   m = bytes_to_long(flag)
   key = RSA.generate(1000)
   passphrase = str(random.randint(0,999999)).zfill(6).encode()
   output = key.export_key(passphrase=passphrase).split(b'\n')
   for i in range(7, 15):
       output[i] = b'*' * 64
   with open("priv.pem", 'wb') as f:
       for line in output:
           f.write(line + b'\n')
   with open("enc.txt", 'w') as f:
       f.write(str(key._encrypt(m)))
   ```

   ```
   enc.txt: 
   55149764057291700808946379593274733093556529902852874590948688362865310469901900909075397929997623185589518643636792828743516623112272635512151466304164301360740002369759704802706396320622342771513106879732891498365431042081036698760861996177532930798842690295051476263556258192509634233232717503575429327989
   
   priv.pem:
   -----BEGIN RSA PRIVATE KEY-----
   Proc-Type: 4,ENCRYPTED
   DEK-Info: DES-EDE3-CBC,435BF84C562FE793
   
   9phAgeyjnJYZ6lgLYflgduBQjdX+V/Ph/fO8QB2ZubhBVOFJMHbwHbtgBaN3eGlh
   WiEFEdQWoOFvpip0whr4r7aGOhavWhIfRjiqfQVcKZx4/f02W4pcWVYo9/p3otdD
   ig+kofIR9Ky8o9vQk7H1eESNMdq3PPmvd7KTE98ZPqtIIrjbSsJ9XRL+gr5a91gH
   ****************************************************************
   ****************************************************************
   ****************************************************************
   ****************************************************************
   ****************************************************************
   ****************************************************************
   ****************************************************************
   ****************************************************************
   hQds7ZdA9yv+yKUYv2e4de8RxX356wYq7r8paBHPXisOkGIVEBYNviMSIbgelkSI
   jLQka+ZmC2YOgY/DgGJ82JmFG8mmYCcSooGL4ytVUY9dZa1khfhceg==
   -----END RSA PRIVATE KEY-----
   
   ```

2. 题目分析

3. 代码
