# 使用函数
## small_roots

1. small_roots(X = ,beta = ) 有两个参数
   1. X代表所需要求解根的上限；虽然是根的上限，并不是说上限越高越好，当上限超过某个值的时候就会计算失效，即使已知二进制位数满足条件，也无法用此函数求得结果；所以一般来说X取在给定情况下的最大求解上限
   2. beta即是前面提到的β \betaβ ，当p,q二进制位数相同时一般只能取0.4 0.40.4；如果p,q二进制位数不同，就按照之前的方法具体问题具体分析

# 下载安装及运行
## 方法1（windows版）

1. 下载sage：[SageMath Download - win (aliyun.com)](https://mirrors.aliyun.com/sagemath/win/index.html)
1. 下载库：在SageShell中输入pip命令即可
3. 下载了Crypto库，但还是报错没有Crypto库：
   1. 找到Crypto库所在文件夹："D:\sage\SageMath 9.3\runtime\opt\sagemath-9.3\local\lib\python3.7\site-packages"
   2. 会发现Crypto库的文件夹名是**c**rypto，c是小写的，将小的c改为大写即可：**C**rypto


## 方法2（linux版）

1. 下载sage：[SageMath Download - linux/64bit](https://mirrors.aliyun.com/sagemath/linux/64bit/index.html)，下载后在linux中解压后在文件夹内
2. 使用：
   1. 在终端输入jupyter-notebook
   2. 打开终端输入./sage即可

### 可能错误的

1. 安装jupyter（[如何在 Linux 中安装 Jupyter Notebook | Linux 中国](https://zhuanlan.zhihu.com/p/646417704)）

```
安装 virtualenv
sudo apt install python3-virtualenv

创建虚拟环境
virtualenv my-jupyter-env

输入以下命令激活虚拟环境：
source my-jupyter-env/bin/activate

安装 Jupyter Notebook
激活虚拟环境后，你现在可以继续安装 Jupyter Notebook：
在终端中，输入以下命令：
pip install jupyter

启动 Jupyter Notebook
安装完成后，你就可以启动 Jupyter Notebook：
在终端中，输入以下命令：
jupyter notebook

关闭并重新启动
如果要关闭 Notebook 服务器，请确保关闭并保存所有笔记。关闭浏览器。
然后在终端窗口中按 CTRL+C。它会提示你是否要关闭服务器。输入 Yes 并按回车键。
最后，关闭终端窗口。

要再次重新启动服务器，你需要按上面的描述运行
source my-jupyter-env/bin/activate
等所有命令



在Linux系统下，如果你想在Jupyter中添加Sage内核，你可以按照以下步骤操作：

首先，确保你已经在你的虚拟环境my-jupyter-env中安装了ipykernel。
你可以通过运行以下命令来检查是否已经安装1：
python -m ipykernel --version

如果没有安装，你可以通过以下命令进行安装1：
python -m pip install ipykernel

然后，你需要为Jupyter添加Sage内核。这可以通过运行以下命令完成1：
python -m ipykernel install --user --name=sage --display-name "Sage"

这里，--name参数是你想要添加的内核的名称，--display-name参数是在Jupyter中
显示的名称。

最后，你可以通过以下命令查看Jupyter notebook的内核1：
jupyter kernelspec list

如果一切顺利，你应该能在列表中看到刚刚添加的Sage内核。

```

3. 在sage中安装库
```
在sagemath的文件夹中运行
./sage -pip install pycryptodome


```

4. 在linux系统中添加jupyter-notebook的快捷方式：
```
在Linux系统下，如果你想在桌面添加Jupyter的快捷方式，你可以按照
以下步骤操作：
在Linux系统下，你可以创建一个.desktop文件来创建一个启动Jupyter中Sage内核的快捷方式。以下是具体步骤：

在桌面上创建一个新的文件，命名为JupyterSage.desktop。

打开这个文件，在里面输入以下内容：

[Desktop Entry]
Version=1.0
Type=Application
Name=Jupyter Sage
Exec=bash -c 'source /path/to/my-jupyter-env/bin/activate && /path/to/sage -n jupyter --python=python3'
Icon=/path/to/icon.png
Terminal=false

请将/path/to/my-jupyter-env/和/path/to/sage替换为你的虚拟环境和Sage的实际路径。你也可以将Icon=/path/to/icon.png替换为你想要的图标的路径。

保存并关闭文件。

右键点击JupyterSage.desktop文件，选择属性，在权限标签页中勾选“允许以程序执行文件”。

文件：
[Desktop Entry]
Version=1.0
Type=Application
Name=Jupyter Sage
Exec=bash -c 'source /home/kali/my-jupyter-env/bin/activate && /home/kali/my-jupyter-env/SageMath/./sage -n jupyter --python=python3'
Icon=/home/kali/my-jupyter-env/SageMath/local/share/jupyter/kernels/sagemath/logo.svg
Terminal=false
```

5. 命令运行sage的方法：
```
在sagemath文件中打开终端，输入命令：./sage -n jupyter --python=python3即可。

可能会报错：需要libssl.so.1.1
这个错误是由于你的系统缺少`libssl.so.1.1`这个文件，它是`ssl`库的一部分。你可以通过安装`openssl`开发包来解决这个问题。在你的系统中安装完`openssl`开发包后，你需要重新构建Python（使用`sage -f python3`命令）。以下是在Debian和Ubuntu系统中安装`openssl`开发包的命令：

```bash
sudo apt-get update
sudo apt-get install libssl-dev
'''

在安装完`openssl`开发包后，你需要重新构建Python。以下是重新构建Python的命令：

./sage -f python3
```

# 使用方法

1. 在sage中==表示两个表达式相等，而非赋值，通常用在解方程中
2. 常用代码：[SageMath常用函数_sagemath语法-CSDN博客](https://blog.csdn.net/weixin_44338712/article/details/105320810)
3. [SAGE(SAGEMATH)密码学基本使用方法-CSDN博客](https://blog.csdn.net/qq_39642801/article/details/104158699)
