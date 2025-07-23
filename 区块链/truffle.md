# truffle init

1. 初始化项目

2. 修改生成的truffle-config.js文件，使之和环境匹配

   ```
   module.exports = {
     networks: {
       // Ganache 本地开发网络配置
       development: {
         host: "127.0.0.1",     // Ganache 本地主机地址
         port: 7545,            // Ganache 默认端口
         network_id: "*",       // 匹配任意网络 ID
         gas: 1000000,         // Gas 限制，确保足够
         gasPrice: 20000000000, // Gas 价格，设置为 20 gwei
       },
     },
   
     // Mocha 配置
     mocha: {
       timeout: 100000, // 单位为毫秒，避免测试超时
     },
   
     // Solidity 编译器配置
     compilers: {
       solc: {
         version: "0.8.21",    // 与合约所用的 Solidity 版本一致
         settings: {
           optimizer: {
             enabled: true,   // 开启优化器
             runs: 200,       // 优化运行次数
           },
           evmVersion: "istanbul", // 与 Ganache 默认兼容的 EVM 版本
         },
       },
     },
   
     // 数据库设置（可选）
     db: {
       enabled: false, // 禁用 Truffle DB
     },
   };
   
   ```

# truffle compile

编译contracts中的智能合约文件

# truffle migrate

运行migrations中的js迁移脚本，将智能合约迁移到区块链上

## 迁移脚本

### artifacts.require()

在迁移开始时，我们通过 `artifacts.require（）`方法告诉 Truffle 我们想要与哪些合约进行交互。 这个方法类似于Node的`require`，但在我们的例子中，它特别返回了一个合约抽象contract abstraction，我们可以在其余的部署脚本中使用它。 指定的名称应与该源文件中的**合约定义的名称**相匹配。 不传递源文件的文件名，因为文件可以包含多个合约。

```
solidity智能合约:
contract Coin {
  // ...
}

js迁移脚本:
const Coin = artifacts.require("Coin");
```

### deployer.deploy(contract, args…, options)

部署合约可以通过使用指定`合约对象`和`可选的合约构造函数的参数`来进行合约部署。对于单个合约很有用，DApp只存在此合约的一个实例。 它将在部署之后设置合约地址（即`Contract.address` 将等于新部署的地址），并且它将覆盖任何先前存储的地址。

```
// 部署没有构造函数的合约
deployer.deploy(A);

//  部署合约 并使用一些参数传递给合约的构造函数。
deployer.deploy(A, arg1, arg2, ...);

// 如果合约部署过，不会覆盖
deployer.deploy(A, {overwrite: false});

// 设置gasLimit 和部署合约的账号
deployer.deploy(A, {gas: 4612388, from: "0x...."});

// 部署多个合约，一些包含参数，另一些没有。
// 这比编写三个`deployer.deploy（）`语句更快，因为部署者可以作为单个批处理请求执行部署。
deployer.deploy([
  [A, arg1, arg2, ...],
  B,
  [C, arg1]
]);

// 外部依赖示例:
//对于此示例，我们的依赖在部署到线上网络时提供了一个地址，但是没有为测试和开发等任何其他网络提供地址。
//当我们部署到线上网络时，我们希望它使用该地址，但在测试和开发中，我们需要部署自己的版本。 我们可以简单地使用`overwrite`键来代替编写一堆条件。

deployer.deploy(SomeDependency, {overwrite: false});
```

# 实例

## 智能合约

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Coin{
    address hoster;
    mapping(address=>uint) private balances; //防止非法访问
    event Deal(address from, address to, uint amount);
    event Send(address to, uint amount);
    
    constructor(uint initialsuppuly) {
        balances[msg.sender] = initialsuppuly;
    }

    function deal(address receiver, uint account) public{
        require(balances[msg.sender]>=account && balances[receiver] + account <= type(uint).max); //防止溢出
        balances[receiver] += account;
        balances[msg.sender] -= account;
        emit Deal(msg.sender, receiver, account);  
    }
        
    function get(address site) public view returns(uint){
        require((msg.sender == hoster) || (site == msg.sender));
        return balances[site];
    } 
}
```

## 迁移脚本

```
// migrations/2_coin_migration.js
const Coin = artifacts.require("Coin");

module.exports = function(deployer) {
  // 设置初始供应量，例如 1000 个代币
  const initialSupply = 500;

  // 部署 Coin 合约，并传递初始供应量作为构造函数参数
  deployer.deploy(Coin, initialSupply);
};

```

## 调用的python脚本

```
# app.py
import json
from web3 import Web3, HTTPProvider

# Truffle 开发区块链地址
blockchain_address = 'http://127.0.0.1:7545'
# 创建与区块链交互的客户端实例
web3 = Web3(HTTPProvider(blockchain_address))
# 获取所有可用账户
accounts = web3.eth.accounts
print(accounts)

# 编译后的合约 JSON 文件路径
compiled_contract_path = 'build/contracts/Coin.json'
# 部署的合约地址（见 `migrate` 命令输出中的 `contract address`）
deployed_contract_address = '0x0686A0ccaBF9AFd900C01946d118e8D8343c3c30'

# 打开编译后的合约 JSON 文件
with open(compiled_contract_path, encoding="utf-8") as file:
    contract_json = json.load(file)  # 加载合约信息为 JSON
    contract_abi = contract_json['abi']  # 获取合约的 ABI - 调用其函数时必需

# 获取已部署合约的引用
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

#  调用合约函数（这不会持久化到区块链）
#  获取合约部署者的余额
web3.eth.defaultAccount = accounts[1]
balance = contract.functions.get(accounts[1]).call()

# 打印返回的消息
print(balance)

receiver_address = accounts[1]  # 接收者地址
amount = 100  # 转账金额

contract.functions.deal(receiver_address, amount).transact({'from': accounts[0]})

web3.eth.defaultAccount = accounts[1]
balance = contract.functions.get(accounts[1]).call()

# 打印返回的消息
print(balance)

```
