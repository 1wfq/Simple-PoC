漏洞描述
本脚本用于验证SpringBlade框架中/api/blade-system/menu/list接口存在的SQL注入漏洞。该漏洞允许攻击者通过未参数化的输入执行任意SQL命令。

漏洞详情
受影响接口: /api/blade-system/menu/list

漏洞类型: SQL注入

使用方法
单个目标测试
bash
python springblade_sqli.py -u http://目标网站
批量扫描
bash
python springblade_sqli.py -f urls.txt
参数	说明
-u	测试单个URL
-f	从文件读取多个URL测试
-h	显示帮助信息
环境要求
Python 3.x
Requests库(pip install requests)

免责声明
本工具仅限授权安全测试使用。未经授权对系统进行测试属于违法行为。
