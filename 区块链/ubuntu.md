# ubuntu

1. 安装ubuntu虚拟机：[https://blog.csdn.net/qq_45657288/article/details/116084337](https://blog.csdn.net/qq_45657288/article/details/116084337)
2. [https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/installation.html](https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/installation.html)（kali的话对应的是ubuntu系统的命令）
3. [Ubuntu系统中安装升级卸载nodejs和npm_ubuntu 卸载npm还能查到版本-CSDN博客](https://blog.csdn.net/qq_36938617/article/details/95309493)
4. 更新npm和node：
    1. 先通过npm下载n，再通过n更新node，即可（更新完node会发现npm已自动更新）

```plain
//查看npm是否全局安装了n模块
sudo npm ls n -g         
//全局安装n模板
sudo npm install n -g          
//列出当前n模块中管理的node版本
sudo n ls   
//切换指定需要使用的node版本（若n模块中没有该版本，自动进行安装）
n <version>  
//查询当前最新的node稳定版本
n --lts           
//安装或激活最新的弄得稳定版本
n lts    
（//重置路径的hash
hash -r
//终端提醒新版node下载位置更换，需使用hash -r重置
）

//卸载npm全局安装的n模块
sudo npm uninstall n -g      
```

    2. 更新npm和nodejs时，可以先将老版的npm和nodejs都删了，再在ubuntu中直接从官网下载最新的node，再将其添加到系统路径即可（但不知为何sudo无法调用）

```python
#删除npm和nodejs
sudo apt-get remove npm
sudo apt-get remove nodejs

node官网：https://nodejs.org
下载下来的最新版的node压缩包中就包含了nodejs（node）和npm
用归档管理器将其解压到桌面，重命名为nodejs
#将桌面的解压后的nodejs文件夹移动到/usr/local/目录下
sudo mv ~/桌面/nodejs /usr/local/
#接下来，将nodejs添加到系统路径中。您可以使用以下命令将nodejs添加到系统路径
#这个只能临时将此路径添加到系统路径，关闭这个终端后就会失效
export PATH=$PATH:/path/to/nodejs/bin
#请将/path/to/nodejs替换为nodejs的安装路径。
export PATH=$PATH:/usr/local/nodejs/bin

#这个可以将路径永久添加为系统路径
#这将在您的主目录下的.bashrc文件中添加一行，
#将/usr/local/nodejs/bin路径添加到环境变量PATH中。
echo 'export PATH=$PATH:/usr/local/nodejs/bin' >> ~/.bashrc
#输入以下命令以使更改生效：
source ~/.bashrc
```

5. 常用命令：

```python

#使主机中复制的内容能粘贴到虚拟机
#解决系统显示页面不全，属于缩小状态。
#通过安装VMware Tools并重启解决：
sudo apt-get update
sudo apt-get install open-vm-tools-desktop

#命令的作用是将 pipx 的可执行文件路径添加到 PATH 环境变量中，
#以便您可以在终端中直接运行 pipx 命令。
#如果您在终端中运行 pipx 命令时遇到“command not found”错误，
#那么您可以尝试运行 python3 -m pipx ensurepath 命令来解决这个问题。
#这个命令会将 pipx 的可执行文件路径添加到 PATH 环境变量中，
#以便您可以在终端中直接运行 pipx 命令。
python3 -m pipx ensurepath 

清理掉自动安装的并且不需要软件包（安装完一个软件包后立刻使用才有用）
命令：
sudo apt autoremove         //清理掉不需要软件包

//系统没有安装pip
sudo apt-get install python3-pip

//在当前目录下新建文件
touch deploy.py

```



