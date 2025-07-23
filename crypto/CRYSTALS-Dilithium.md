# 参考文献

1. 论文：[CRYSTALS-Dilithium Algorithm Specifications and Supporting Documentation (Version 3.1)]([CRYSTALS-Dilithium (pq-crystals.org)](https://pq-crystals.org/dilithium/data/dilithium-specification-round3-20210208.pdf))
2. https://mp.weixin.qq.com/s/A_4PwpCL0p3M1Z4D6lcTsQ

# 困难问题

1. MSIS
1. SelfTargetMSIS
1. MLWE

#  数学符号

1.  **`:=`** 表示**定义（define as）**，用于明确表达某个符号或表达式的定义。

   1. **形式化意义**：**`:=`** 的左侧是要被定义的符号，右侧是该符号的具体定义。

   2. **区别于等号（`=`）**：普通等号 `=` 表示等值或相等，而 **`:=`** 强调这是一个新的定义或约定。
   3. 示例：$f(x) := x^2 + 1$表示$f(x)$被定义为$x^2 + 1$。

# 算法中调用的函数

1. $Power2Round_q(r, d)$:
   1. $r := r \mod^+ q$
   2. $r_0 := r \mod 2^d$
   3. $return\left( \frac{(r - r_0)}{2^d}, r_0 \right)$

2. $MakeHint_q(z, r, \alpha)$ 
   1. $r_1 := \text{HighBits}_q(r, \alpha)$
   2. $v_1 := \text{HighBits}_q(r + z, \alpha)$ 
   3. $return[r_1 \neq v_1]$

3. $UseHint_q(h, r, \alpha)$ 
   1. $m := \frac{(q - 1)}{\alpha}$
   2. $(r_1, r_0) := \text{Decompose}_q(r, \alpha)$
   3. $If\{h = 1 \quad and \quad r_0 > 0\} \quad return \quad (r_1 + 1) \mod^+ m$ 
   4. $If\{h = 1 \quad and \quad r_0 \leq 0\} \quad return \quad (r_1 - 1) \mod^+ m$ 
   5. $return \quad r_1$

4. $Decompose_q(r, \alpha)$}
   1. $r := r \mod^+ q$
   2. $r_0 := r \mod^{\pm} \alpha$ 
   3. $If\{r - r_0 = q - 1\}$
      1. $r_1 := 0; r_0 := r_0 - 1$ 

   4. $Else  \quad r_1 := \frac{r - r_0}{\alpha}$(相当于$r_1 = \lfloor \frac{r}{\alpha} \rfloor$)
   5. $return (r_1, r_0)$

5. $HighBits_q(r, \alpha)$
   1. $(r_1, r_0) := \text{Decompose}_q(r, \alpha)$
   2. $return \quad r_1$

6. $LowBits_q(r, \alpha)$
   1. $(r_1, r_0) := \text{Decompose}_q(r, \alpha)$
   2. $return \quad r_0$

7. $SampleInBall$(从签名中的压缩表示$ \tilde{c}$ 中还原出完整的多项式 $c$):

   1. $\tilde{c}$ 是 $c$ 的压缩形式，作为签名的一部分被发送。$c$ 是一个稀疏多项式，属于一个有限域（模 $q$的环），其系数仅为 −1、0、+1，并且满足固定的汉明重量（非零系数的个数是固定的）。$\tilde{c}$ 是一种编码，仅记录了 $c$中非零系数的位置和符号。函数 $SampleInBall$ 是从压缩的 $\tilde{c}$中重新构造稀疏多项式 $c$。
   2. 稀疏多项式$ c$的性质：$c$ 是一个 n次多项式（即维度为 n的向量）。其中有$ \tau$个系数是非零值（−1 或 +1），其他的系数是 0。$\tau$是协议中预先定义的固定参数。

   1. 压缩表示 $\tilde{c}$ ：$\tilde{c}$  记录了 $\tau$个非零值的位置信息以及它们的符号。一般使用一个紧凑的二进制编码格式表示，具体编码方式会因实现而异。
   2. 重构过程（SampleInBall）：根据 $\tilde{c}$ 中的编码信息，确定 $\tau$个非零值的位置。读取这些位置的符号（−1 或 +1）。构造一个多项式 $c$，其系数根据以上信息设置为 −1、+1，其他位置的系数置为 0。

# 引理

## 引理1

假设 $q$和 $\alpha$是正整数，满足 $q>2\alpha$，$q\equiv1 \pmod {\alpha}$且$\alpha$为偶数。设 $r $和$ z$是 $R_{q}$中的元素向量，其中 $\|z\|_{\infty}\leq\frac{\alpha}{2}$，并且 $h$，$h'$是比特向量。那么$ HighBits$，$MakeHint_{q}$和 $UseHint_{q}$算法满足以下性质。

### 性质1

$UseHint_{q}(MakeHint_{q}(z,r,\alpha),r,\alpha)=HighBits_{q}(r + z,\alpha)$

### 性质2

令$ v_{1}=UseHint_{q}(h,r,\alpha)$，则$ \left\|r - v_{1}\cdot\alpha\right\|_{\infty}\leq\alpha + 1$。此外，如果 $h$中 1的个数是 $\omega$，那么在以 $q$为模的中心约简后，$r - v_{1}\cdot\alpha$除了至多 $\omega$个系数外，其余系数的绝对值至多为$ \frac{\alpha}{2}$。 

### 性质3

对于任意的$ h$，$h'$，如果 $UseHint_{q}(h,r,\alpha)=UseHint_{q}(h',r,\alpha)$，那么 h = h'

### 引理1的扩展

由引理1可以推出：$2\gamma_2 \cdot UseHint_q(h,Az-ct_1 \cdot2^d,2\gamma_2)=Az-ct_1 \cdot 2^d$，其中$\|u\|_\infty \leq 2\gamma_2+1$。证明如下：

1. $\gamma_2 = \lceil \frac{q}{2^{d+1}} \rceil$；令$r=Az-ct_1 \cdot 2^d$
2. 由引理1的性质1：$UseHint_q(MakeHint_q(z, r, \alpha), r, \alpha) = HighBits_q(r + z, \alpha)$可知当我们取$z=u$和$\alpha=2 \gamma_2$且$\|u\|_\infty \leq 2\gamma_2+1$时可以得到：$UseHint_q(MakeHint_q(u, r, 2 \gamma_2), r, 2 \gamma_2) = HighBits_q(r + u, 2 \gamma_2)$
3. 将$r=Az-ct_1 \cdot 2^d$带入可以得到：$UseHint_q(MakeHint_q(u, Az - ct_1 \cdot 2^d, 2\gamma_2), Az - ct_1 \cdot 2^d, 2\gamma_2) = HighBits_q(Az - ct_1 \cdot 2^d + u, 2\gamma_2)$
4. 由引理1性质1，我们知道：$UseHint_q(h, Az - ct_1 \cdot 2^d, 2\gamma_2) = HighBits_q(Az - ct_1 \cdot 2^d, 2\gamma_2)$，其中$h$是我们通过$MakeHint$生成的提示信息
5. 由$HighBits_q$知$\alpha \cdot HighBits_q(x,\alpha) \approx x $，所以$2\gamma_2 \cdot HighBits_q(Az - ct_1 \cdot 2^d + u, 2\gamma_2) \approx Az - ct_1 \cdot 2^d + u$
6. 4同时乘$2\gamma_2$并将5带入4中可以得到：$2\gamma_2 \cdot UseHint_q(h,Az-ct_1 \cdot2^d,2\gamma_2)=Az-ct_1 \cdot 2^d + u$

## 引理2

如果$\|s\|_\infty \leq \beta$且$\|LowBits_q(r,\alpha)\|_\infty < \frac{\alpha}{2}-\beta$，则$HighBits_q(r, \alpha) = HighBits_q(r + s, \alpha)$

## 引理3

当满足$(r_1, r_0) = Decompose_q(r, \alpha), (w_1, w_0) = Decompose_q(r + s, \alpha), \|s\|_\infty \leq \beta$时，有：$\|s + r_0\|_\infty < \frac{\alpha}{2} - \beta \iff w_1 = r_1 \land \|w_0\|_\infty < \frac{\alpha}{2} - \beta$

# 公开参数

1. XOF算法，原文采用了SHAKE256, 也可以换成其他的
2. 多项式环：$R_q = \mathbb{Z}_q[X]/(X^{256} + 1)$，这里$q = 2 ^{23} - 2 ^{13} + 1 = 8380417$。环中的元素是模$q$的多项式，且每个多项式的最高次数为 255
3. $l \times k$: 公开的矩阵的大小，本文演示代码采用$4 \times 4$的矩阵，其他大小可以参考原始公开的文档
4. $d$: $t$丢弃的bit的长度
5. $\eta$: 私钥的系数的范围
6. $\gamma_1$: $y$的系数的范围
7. $\gamma_2$: low-order 的裁剪范围

# 密钥生成算法

1. 生成一个种子

   1. $\zeta \leftarrow \{0,1\}^{256}$，首先生成一个256bit的随机值，这个随机值呢，其实是不参与后面的交换过程的，只是为了生成后面的随机种子（$\rho, \rho', K$）
   2. 采用的伪随机数算法采用基于哈希的伪随机数生成算法SHAKE-256或AES算法（理论上是可以换的），利用$H$函数分别生成$(\rho, \rho', K) \in \{0,1\}^{256} \times \{0,1\}^{512} \times \{0,1\}^{256} := H(\zeta)$。即通过伪随机数生成算法将初始随机值$\zeta$通过哈希函数$H$转换为三个伪随机值$\rho、 \rho'、 K$
      1. $\rho \in \{0,1\}^{256}$是用于生成随机矩阵$A$的种子
      2. $\rho'  \in \{0,1\}^{512}$和$K  \in \{0,1\}^{256}$在后续用于私钥和公钥的生成

2. 通过这三个初始值可以用来生成密钥

   1. 生成随机矩阵$A$：$A \in \mathbb{R}^{k \times l}_q := \text{ExpandA}(\rho)$，其中$A$ 是一个$ k×l$ 矩阵，元素属于有限域 $\mathbb{R}_q$。（这一步可以通过NTT算法优化加速）
      1. 使用种子派生矩阵的原因：如果直接传输一个矩阵 $A$，它的传输数据量会非常庞大，特别是在密钥生成、签名或加密等步骤中，矩阵的大小可能会达到数百字节甚至更大。如果一个矩阵的大小非常大，这会在传输、存储和计算效率上带来显著的开销。而种子派生矩阵可以只传输256比特的种子，传输内容就极大的减小了。
      2. 派生矩阵的过程：为了减小传输内容的大小，算法采用了 种子$\rho$来派生出一个矩阵$A$。虽然种子本身只有 256 位（32 字节），但通过派生过程，可以从这个种子中获得一个非常大的矩阵或其他多项式结构
      3. 为什么通过派生可以减小传输内容：通过使用一个较小的种子值，并通过算法生成矩阵 $A$，可以保持信息的完整性，同时显著减小需要传输的数据量。种子只是一个固定长度的值（例如 256 位），而矩阵本身可能有成千上万的位数，但通过数学操作（如伪随机生成），可以从一个较小的种子生成矩阵，且接收方可以根据相同的算法来复原该矩阵。
   2. 计算私钥
      1. ：$(s_1, s_2) \in S_\eta^{\ell} \times S_\eta^k := \text{ExpandS}(\rho')$
         1. 这里$S_\eta$表示系数范围在$\eta$之内，这里私钥是一个系数较小的值。
         2. $\ell$和 $k$是参数，决定了 $s_1, s_2$的维度。
         3. $\text{ExpandS}(\rho')$表示通过种子 $\rho'$ 和某种伪随机生成算法扩展得到这些值。
      2. $t := A s_1 + s_2$
      3. $(t_1, t_0) := \text{Power2Round}_q(t, d)$，$\text{Power2Round}_q$是一个特殊的分解函数，将$t$分解为两个部分$t_1$和$t_0$，其中$t_1$是高位部分，$t_0$是低位部分。
      4. 计算一个值$\text{tr} \in \{0,1\}^{256} := H(\rho \| t_1)$。这里，其实在签名的时候，再来计算也可以，就是私钥里面也放一下$t_1$就好了。
      5. 得到对应的私钥$\text{sk} = (\rho, K, \text{tr}, s_1, s_2, t_0)$
   3. 计算公钥：$\text{pk} = (\rho, t_1)$（这里的$t_1$即前面计算私钥时的$t_1$）。公钥$\text{pk}$仅包含种子$\rho$和分解后的高位部分$t_1$，体积小且便于传输。
   4. 流程：
      1. 生成一个随机种子，通过种子生成3个分别为256和512为的随机值
      2. 通过256位随机值生成派生矩阵A
      3. 通过扩展算法计算一个512位的随机值得到私钥的一部分，再以此计算出t，并保存t的低位作为私钥的一部分，对t的高位做处理后同样作为私钥的一部分
      4. 将前面生成随机矩阵A的256位随机值和t的高位作为公钥
   


# 签名算法

1. 首先根据$\rho$来恢复矩阵$A$：$\mathbf{A} \in \mathbb{R}^{k \times l}_q := \text{ExpandA}(\rho)$
2. 计算一个hash值：$\mu \in \{0, 1\}^{512} := H(tr \parallel M)$，消息$M$
3. 生成一个随机值$\rho'$，这里可以采用$H$派生$\rho' \in \{0, 1\}^{512} := H(K \parallel \mu)$，也可以随机取值$\rho' \in \{0, 1\}^{512}$（和生成密钥中的$\rho'$有区别）
4. 初始化变量：计数器$\kappa=0$
5. 进入循环，判断条件：$(z, h) :=\perp$
   1. 随机生成y的值：$y \in S_{\gamma_1}^{l} := \text{ExpandMask}(\rho', \kappa)$，其中$y$的系数范围是通过$\gamma_1$来决定的
   2. 计算：$w := A y$
   3. 读取$w$的高位：$w_1 := \text{HighBits}_{\gamma_2}(w, 2\gamma_2)$
   4. 计算一个倍数值，并将其转换成一个多项式：$\tilde{c} \in \{0,1\}^{256} := H(\mu \| w_1)，c \in B_{\tau} := \text{SampleInBall}(\tilde{c})$
   5. 计算：$z := y + c s_1，r_0 := \text{LowBits}_{\gamma_2}(w - c s_2, 2\gamma_2)$
   6. 这里需要判断$z$和$r_0$的范数，是否在范围之内。当$||z||_{\infty} \geq \gamma_1 - \beta \quad or \quad ||r_0||_{\infty} \geq \gamma_2 - \beta$时，$(z, h) :=\perp$并跳转到5.8
   7. 当$z$和$r_0$的范数不满足5.6中的条件时，计算$h$的值，$h := \text{MakeHint}_{q}(-c t_0, w - c s_2 + c t_0, 2\gamma_2) $
      1. 当$||c t_0||_{\infty} \geq \gamma_2 $或$h$的汉明重量大于$w$时，$(z, h) :=\perp$并跳转到5.8
      2. 当不满足上面5.7.1的条件时，$k=k+1，\sigma = (\tilde{c}, z, h)$并**退出循环**（**此时满足的条件：**$||z||_{\infty} < \gamma_1 - \beta$ 、$||r_0||_{\infty} < \gamma_2 - \beta$、$||c t_0||_{\infty} < \gamma_2$ 以及 $h$的汉明重量小于$w$），返回$\sigma = (\tilde{c}, z, h)$作为最终签名内容
   8. $k=k+1$，并跳转到5.1符合判断条件后继续循环。
      1. 在这里$k$的作用主要是用来控制循环的次数，它并不直接影响签名的计算方式。计数器的步长变化主要影响的是算法的执行效率，而不是安全性。实现者可以根据实际情况调整步长，所以在一些关于CRYSTALS-Dilithium算法讲解的网页中步长可能不是1而是其他数值（如$\ell$等）
6. 签名结果：$\sigma = (\tilde{c}, z, h)$
7. 流程：
   1.  通过私钥中的的值恢复随机矩阵A
   2. 计算消息的hash值
   3. 进入循环计算，直到找到符合条件的值

# 验签算法

1. 首先，判断$h、z$的范围（$\|z\|_\infty<\gamma_1-\beta$并且$h$的汉明重量小于$w$），是不是合理，不合理，直接返回验签失败
2. 首先根据$\rho$来恢复矩阵$\mathbf{A}$：$\mathbf{A} \in \mathbb{R}^{k \times l}_q := \text{ExpandA}(\rho)$
3. 计算$\mu$的值，这里和私钥计算的值是一样的$\mu \in \{0, 1\}^{512} := H(tr \parallel M)$
4. 恢复$c$的值，得到一个多项式$c:=SampleInBall(\tilde{c})$
5. 计算$w_1' := \text{UseHint}_q(h, \mathbf{A}z - ct_1 \cdot 2^d, 2\gamma_2)$
6. 验签$\tilde{c} = H(\mu \| w_1')$，计算$\tilde{c}$和传输过来的是否一致，如果一致，验签成功，否则，验签失败。
7. 流程：
   1. 通过公钥中值恢复随机矩阵$\mathbf{A}$
   2. 计算消息的hash值
   3. 计算对比值是否正确



# 签名原理（正确性证明）

1. 签名时：$w_1= \text{HighBits}_{\gamma_2}(w, 2\gamma_2),\tilde{c}= H(\mu \| w_1)$
2. 验签时：$w_1' := UseHint_q(h, \mathbf{A}z - ct_1 \cdot 2^d, 2\gamma_2)，\tilde{c} = H(\mu \| w_1')$，计算$\tilde{c}$和传输过来的是否一致，如果一致，验签成功，否则，验签失败。
3. 所以只用证明$w_1 = w_1'$即可完成正确性证明

## 正确性证明

1. 令$h := \text{MakeHint}_{q}(-c t_0, w - c s_2 + c t_0, 2\gamma_2) $，$z=-ct_0, r=w-cs_2+ct_0，\alpha = 2\gamma_2$带入**引理1**$UseHint_{q}(MakeHint_{q}(z,r,\alpha),r,\alpha)=HighBits_{q}(r + z,\alpha)$，其中满足$\|z\|_\infty \leq \frac{\alpha}{2}$即$\|ct_0\|_\infty <\gamma_2$所以有$UseHint_q(h,w-cs_2+ct_0,2\gamma_2) = HighBits_q(w-cs_2,2\gamma_2)$
2. 因为$w=\mathbf{A}y$ and $t=\mathbf{A}s_1+s_2$，所以$w - cs_2 = \mathbf{A}y-cs_2=\mathbf{A}(z-cs_1)-cs_2=\mathbf{A}z-ct$
3. 因为$(t_1, t_0) := \text{Power2Round}_q(t, d)$，所以有$ct = c(t_1 \cdot 2^d + t_0)=ct_1 \cdot 2^d + ct_0$。所以$w-cs_2 + ct_0 = \mathbf{A}z-ct + ct_0 = \mathbf{A}z - ct_1 \cdot 2^d$，所以有$UseHint_q(h,w-cs_2+ct_0,2\gamma_2) = UseHint_q(h,\mathbf{A}z - ct_1 \cdot 2^d,2\gamma_2)=HighBits_q(w-cs_2,2\gamma_2) $
4. 因为$\|cs_2\|_\infty \leq \beta$且$\|LowBits_q(w-cs_2,2\gamma_2)\|_\infty < \gamma_2-\beta$，所以由**引理2**得$HighBits_q(w-cs_2,2\gamma_2) = HighBits_q(w-cs_2+cs_2,2\gamma_2)=HighBits_q(w,2\gamma_2)=w_1$
5. 所以$w_1' = UseHint_q(h, \mathbf{A}z - ct_1 \cdot 2^d, 2\gamma_2)=HighBits_q(w,2\gamma_2)=w_1$，证毕

# 形式化安全分析（安全规约）

遵循 **挑战者-攻击者模型** 和 **随机预言模型（ROM）**，并规约到相关的数学困难问题（如 MLWE 、SelfTargetMSIS和 MSIS）。

## **1. 密钥恢复（Key Recovery）的形式化安全分析**

### **安全目标**

攻击者不能从公钥 $(A,t)$中恢复私钥$ (s_1, s_2)$。

### **攻击模型**

攻击者$\mathcal{A}$被赋予如下能力：

- 知道公钥$ t = \mathbf{A} \cdot s_1 + s_2$；
- 知道系统参数$\mathbf{A}$和签名算法的实现；
- 攻击目标是从 $(\mathbf{A}, t)$中恢复$s_1, s_2$。

### **安全性定义**

1. CRYSTALS-Dilithium 的密钥恢复安全性规约到 **模块化学习同余问题（MLWE）**。

2. **MLWE 问题：**给定$ \mathbf{A} \in R_q^{m \times k}$和 $t \in R_q^m$，区分以下两种分布：
1. $t = \mathbf{A} \cdot s_1 + s_2$，其中 $s_1, s_2$ 是从高斯分布中独立采样的短向量；
   
1. $t$是从均匀分布中随机生成的。

如果攻击者能够破解密钥恢复问题，则可以有效地区分上述两种分布。

### **形式化证明**

1. **挑战设置：**
   挑战者 $\mathcal{C} $初始化系统参数：
   - 生成 $\mathbf{A}$ 和 $t$，满足 $t = \mathbf{A} \cdot s_1 + s_2$，其中$s_1, s_2$是短向量。
   - 将$(\mathbf{A}, t)$提供给攻击者 $\mathcal{A}$。
2. **攻击者能力：**
   $\mathcal{A}$接收$(\mathbf{A}, t)$并尝试恢复$s_1, s_2$
3. **规约到 MLWE：**如果攻击者$\mathcal{A}$能够成功恢复私钥$sk$，那么说明攻击者$\mathcal{A}$能够识别出$t$是从均匀分布中随机生成的还是$t = \mathbf{A} \cdot s_1 + s_2$（其中$s_1$,$s_2$是从高斯分布中独立采样的短向量）并从$t = \mathbf{A} \cdot s_1 + s_2$中成功恢复$s_1$,$s_2$，这证明攻击者$\mathcal{A}$能够高效破解MLWE问题，与MLWE问题的计算困难性假设矛盾，所以证明定理1。同时因为MLWE问题的困难性，公钥$pk=(A,t)$中的$t$和从均匀分布中随机生成的$t$没有区别。
4. **归谬证明：**
   假设存在一个攻击者能够破解密钥恢复问题，则他能够高效破解 MLWE 问题。这与 MLWE 的计算困难性假设矛盾。

### **结论**

密钥恢复的安全性直接规约到 MLWE 的困难性。

------

## **2. 新消息伪造（UF-CMA）的形式化安全分析**

### **安全目标**

攻击者不能在选定消息攻击（CMA）模型下伪造未签名消息$M'$的有效签名$\sigma'$。

由文献[1]中6.2.1的论证可知，对于零知识确定性签名方案，如果攻击者能够利用量子访问哈希函数$H$和经典访问签名Oracle的能力在UF-CMA模型下伪造一个新的消息签名，那么实际上可以通过构造一个不需要访问签名Oracle的攻击者在UF-NMA模型下完成伪造新的消息签名。因此，基于CRYSTALS-Dilithium签名算法的数学特性以及文献[1]提出的归约方法以及确定性签名方案的特性，可以通过模拟签名Oracle的行为实现从UF-CMA到UF-NMA的安全性归约。所以当证明CRYSTALS-Dilithium签名算法在UF-NMA模型下是安全的，即可推出其在UF-CMA模型下的安全性。下面证明CRYSTALS-Dilithium签名算法在UF-NMA模型下的安全性：

[1]CRYSTALS-Dilithium Algorithm Specifications and Supporting Documentation(Version 3.1)

### **攻击模型**

1. 攻击者$ \mathcal{A} $被赋予如下能力：
   1. 查询公钥接口
   2. **伪造目标** ：输出一个未签名消息$ M' $和有效签名 $\sigma' = (z', h', c')$
2. 攻击者的目标是生成一个有效签名，使得验证者认为签名有效，且消息 $M'$没有在之前的签名查询中请求过。

### **安全性定义**

1. CRYSTALS-Dilithium 的新消息伪造安全性规约到 **自目标模块化短整数解问题（SelfTargetMSIS）**。
2. **SelfTargetMSIS 问题：**给定矩阵$ A $和哈希函数$ H$，找到一个向量 $y = [z, c, u]$，满足：$[I \ | \mathbf{A}] \cdot y = t'$,其中 $\|y\|_\infty \leq \gamma$，且 $t'$满足签名验证公式的约束。

### **形式化证明**

1. **挑战设置：**
   1. 初始化：挑战者 $\mathcal{C}$执行以下步骤：
      1. 随机生成系统参数，包括公钥矩阵$\mathbf{A}$、私钥$(s_1, s_2)$，以及哈希函数 $H$
      2. 计算公钥$(\mathbf{A}, t=As_1+s_2)$
      3. 向攻击者$\mathcal{A}$提供公钥$(\mathbf{A},t)$

   2. 签名验证公式可化简为： $H(\mu\|UseHint(h, \mathbf{A}z - ct_1 \cdot 2^d, 2\gamma_2)) = c$，其中：
      1. $\mu$是消息$M$的消息摘要：$\mu =Hash(Hash(\rho ||{{t}_{high}})||M)$
      2. $h$是生成的提示信息
      3. $t_1$是公钥$t$的高位部分
2. 公钥查询接口
   1. 将攻击者查询的公钥提供给攻击者
3. **攻击者伪造签名的条件**
   1. 攻击者$ \mathcal{A} $成功伪造签名$ \sigma' = (z', h', c') $的条件是：
      1. 签名验证公式成立：$H(\mu' \| UseHint_q(h', \mathbf{A}z' - c't_1 \cdot 2^d, 2\gamma_2)) = c'$
      2. 消息$ M' $没有在签名查询中被请求过。
4. **将伪造的签名规约到 SelfTargetMSIS：**
   1. 由引理1可以得到：$2\gamma_2 \cdot UseHint_q(h,\mathbf{A}z-ct_1 \cdot2^d,2\gamma_2)=\mathbf{A}z-ct_1 \cdot 2^d +u=>UseHint_q(h,\mathbf{A}z-ct_1 \cdot2^d,2\gamma_2)=\frac{1}{2\gamma_2}\cdot(\mathbf{A}z-ct_1 \cdot 2^d + u)$
   2. 我们令$t=t_1 \cdot 2^d+ t_0$，其中$\|t_0\|_\infty\leq2^{d-1}$。可以得到：$\mathbf{A}z - ct_{1} \cdot 2^{d} + u = \mathbf{A}z - c(t - t_{0}) + u = \mathbf{A}z - ct + (ct_{0} + u) = \mathbf{A}z - ct + u'$
   3. 我们可以得到$u'$最坏情况下的上限$\|u'\|_{\infty} \leq \|ct_{0}\|_{\infty} + \|u\|_{\infty} \leq \|c\|_{1} \cdot \|t_{0}\|_{\infty} + \|u\|_{\infty} \leq \tau \cdot 2^{d - 1} + 2\gamma_{2} + 1$
   4. 因此敌手$\mathcal{A}$如果能够成功伪造签名信息$ \sigma' = (z', h', c') $，就能找到$z',c',u',M$满足$\|z’\|_{\infty}<\gamma_{1}-\beta,\|c’\|_{\infty}=1,\|u'\|_{\infty}\leq\tau\cdot2^{d - 1}+2\gamma_{2}+1$, $H(\mu' \| UseHint_q(h', \mathbf{A}z' - c't_1 \cdot 2^d, 2\gamma_2)) = c'$,以及 $h$的汉明重量小于$w$）由此可以得到：$H(\mu\|UseHint_q(h', \mathbf{A}z' - c't_1 \cdot 2^d, 2\gamma_2)) = H\left(\mu \left\|\frac{1}{2\gamma_{2}}\cdot\left[\mathbf{A}|t|I_{k}\right]\cdot\left[\begin{array}{c}z’\\c'\\u'\end{array}\right]\right.\right)=c$
   5. 为了简化公式，我们定义函数$H'$满足$H(\mu \|x)=H'(\mu\|2\gamma_2x)$，得到：$H'\left(\mu \left\|\left[\mathbf{A}|t|I_{k}\right]\cdot\left[\begin{array}{c}z'\\c'\\u'\end{array}\right]\right.\right)=c$
   6. 令$t'= \mathbf{A}z'-c't+u'$，则有$\left[\mathbf{A}|t|I_{k}\right]\cdot\left[\begin{array}{c}z'\\c'\\u'\end{array}\right]=t'$，即存在一个短向量$y' = \left[\begin{array}{c}z'\\c'\\u'\end{array}\right]$，满足：$[I \ | \mathbf{A}] \cdot y' = t'$，其中 $\|y'\|_\infty \leq \gamma$。
   7. 这正是 **SelfTargetMSIS 问题** 的定义：在给定矩阵$[I ∣A] $和目标值 $t'$的情况下，找到一个短向量 $y = \left[\begin{array}{c}z'\\c'\\u'\end{array}\right]$，满足：$[I \ | \mathbf{A}] \cdot y = t'$，其中 $\|y\|_\infty \leq \gamma$。
5. **归谬证明：**如果攻击者$ \mathcal{A}$ 能够在选定消息攻击（CMA）模型下伪造签名，则：他能够有效找到一个 $y = [z', c', u']$，满足 SelfTargetMSIS 问题的定义。那么他就能够破解 SelfTargetMSIS 问题。这与 SelfTargetMSIS 的困难性假设矛盾。

### **结论**

新消息伪造的安全性规约到 SelfTargetMSIS 的困难性。

------

## **3. 强不可伪造性（SUF-CMA）的形式化安全分析**

### **安全目标**

攻击者不能在选定消息攻击（CMA）模型下伪造任何签名消息$M$的有效签名$\sigma'$。

### **攻击模型**

基于上面新消息伪造的证明，只用证明：无法基于$\sigma$构造出新的有效签名$\sigma'$

- 攻击者$ \mathcal{A} $被赋予如下能力：
  1. 查询公钥接口
  2. 查询签名接口，获得$\sigma = (z, h, c)$
  3. **伪造目标** ：
     1. 输出一个消息$ M $和有效签名 $\sigma' = (z', h', c)$
     2. 消息$ M $的签名$\sigma'$之前没有被查询过，即使是查询过消息$ M $的签名，只要构造的有效签名$\sigma'$并不是查询到的而是构造出来的

### **安全性定义**

1. CRYSTALS-Dilithium 的强不可伪造性规约到 **模块化短整数解问题（MSIS）**。
2. **MSIS 问题：**给定矩阵 $\mathbf{A}$，找到非零短向量$y$，满足：$[I | \mathbf{A}] \cdot y = 0$，且$ \|y\|_\infty \leq \gamma$

### **形式化证明**

1. **挑战设置：**
   挑战者$\mathcal{C} $初始化：

   - 系统参数 $\mathbf{A}$、签名公式 $\sigma = (z, h, c)$

2. **攻击者能力：**
   $\mathcal{A}$能够查询公钥和签名并且能只改变签名中的$(z,h)$，并尝试找到 $\sigma \neq \sigma'$，满足：

   $H(\mu\|UseHint_q(h', \mathbf{A}z' - ct_1 \cdot 2^d, 2\gamma_2))=H(\mu\|UseHint(h, \mathbf{A}z - ct_1 \cdot 2^d, 2\gamma_2))=c$

3. **规约到 MSIS：**

   1. 如果 $\mathcal{A}$成功伪造出签名$\sigma'$签名，则$UseHint_q(h, \mathbf{A}z - ct_1 \cdot 2^d, 2\gamma_2) = UseHint_q(h', \mathbf{A}z' - ct_1 \cdot 2^d, 2\gamma_2)$
   2. 所以$\frac{1}{2\gamma_2}\cdot(\mathbf{A}z-ct_1 \cdot 2^d + u)=\frac{1}{2\gamma_2}\cdot(\mathbf{A}z'-ct_1 \cdot 2^d + u)$，两式相减得到：$ \mathbf{A} \cdot (z - z') + u = 0$, 令 $y = \left[\begin{array}{c}z-z'\\u\end{array}\right]$，则可以变形为$[I | \mathbf{A}] \cdot y = 0$，其中$y$是一个短向量，满足 MSIS 的定义。

4. **归谬证明：**
   如果$ \mathcal{A} $能够生成有效签名$\sigma'$，则能够通过这个算法找到有效的短向量$y$，满足 MSIS 问题定义。那么他就能够破解 MSIS 问题。这与MSIS 的困难性假设矛盾。

### **结论**

强不可伪造性的安全性规约到 MSIS 的困难性。

------

## **总结**

CRYSTALS-Dilithium 的安全性分析如下：

1. **密钥恢复**规约到 **MLWE**；
2. **新消息伪造**规约到 **SelfTargetMSIS**；
3. **强不可伪造性**规约到 **MSIS**。

最终安全界限为：

$Adv_{SUF-CMA} \leq Adv_{MLWE} + Adv_{SelfTargetMSIS} + Adv_{MSIS} + \text{negligible terms}$

