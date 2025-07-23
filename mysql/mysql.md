# MySQL安装教程

[MySQL安装教程（详细版）_mysql安装教程8.0.36-CSDN博客](https://blog.csdn.net/m0_71422677/article/details/136007088)

# MySQL导入数据库

1. 先在目标数据库建好表结构（和导入的表的结构一样），会创建表对应的idb文件

   ```
   create table 表名(
   	id varchar(32) not null comment '主键id',
   	name varchar(32) comment '姓名',
   	......,
   	primary key (id)	
   )
   ```

2. 删除表空间（删除创建的idb文件）（可以手动删除，但是有些时候会弹出文件已打开，无法删除，此时就可以用这个命令删除）

   ```
   ALTER TABLE 表名 DISCARD TABLESPACE;
   ```

3. 将导入的表（idb文件）

4. 文件授权：导入表空间

   ```
   alter table 表名 import tablespace;
   ```

5. 如果表中有属性`AUTO_INCREMENT`的字段（如id之类的），那么需要更新`AUTO_INCREMENT` 计数器。

   ```
   ALTER TABLE 表名 AUTO_INCREMENT = 当前最大id的值 + 1;
   
   查询当前表的最大id
   SELECT MAX(id) FROM {table_name}
   ```
   
   ```
   更新脚本：
   import mysql.connector
   # 数据库连接配置
   config = {
       'user': 'root',
       'password': 'admin',
       'host': '127.0.0.1',
       'database': 'flask_app',
   }
   
   # 连接到 MySQL 数据库
   conn = mysql.connector.connect(**config)
   cursor = conn.cursor(dictionary=True)
   
   # 查询所有表的最大id
   cursor.execute("""
       SELECT table_name 
       FROM information_schema.columns 
       WHERE table_schema = %s AND column_name = 'id'
   """, (config['database'],))
   
   # 获取所有包含 'id' 列的表
   tables = cursor.fetchall()
   
   # 打印查询结果以检查返回的数据结构
   print(tables)
   
   # 对每个表进行操作
   for table in tables:
       print(table)  # 打印每个表的内容，以便调试
       table_name = table.get('TABLE_NAME')  # 使用 .get() 来避免 KeyError
   
       # 查询表的最大 id
       cursor.execute(f"SELECT MAX(id) AS max_id FROM {table_name}")
       max_id_result = cursor.fetchone()
       max_id = max_id_result['max_id'] if max_id_result['max_id'] is not None else 0
       # 更新 AUTO_INCREMENT
       new_auto_increment = max_id + 1
       print(f"Updating {table_name} AUTO_INCREMENT to {new_auto_increment}")
   
       # 执行 ALTER TABLE 语句
       cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = %s", (new_auto_increment,))
   
   # 提交更改并关闭连接
   conn.commit()
   cursor.close()
   conn.close()
   
   print("AUTO_INCREMENT values updated successfully.")
   ```

# 数据库

1. 创建数据库：`create database 数据库名称;`
2. 查询有哪些数据库：`show databases;`
3. 进入某个数据库：`use 数据库名称;`

# 表

1. 在数据库中创建表（表中字段id、用户名、密码）： `create table users(id tinyint, username varchar(20), password char(32));`
2. 查看数据库中所有表：`show tables;`
3. 表中插入字段值：`insert into users values (1,'11', '11');`
4. 查询表中所有字段：`select * from 表名`
5. 查询表中所有的字段名：`show columns from 表名`
6. `DELETE` 语句用于从表中删除满足特定条件的行。如果你确定要删除整行数据，可以使用：`DELETE FROM 表名 WHERE 条件;`。例如：`DELETE FROM users WHERE username = '44';`
7. 更新表中数据`UPDATE 表名 SET 字段名 =  WHERE 条件;`
8. 删除表：`DROP TABLE table_name;`

