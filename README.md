# ansible-wisehealth
Moving bricks for life.

## 说明
* 基于公司内部系统升级进行开发
* 代码获取基于ftpserver, 未来目标基于gitlab-ci
* 基于Ansible + Python2.x/3
* 定时任务（暂不支持）
* 邮件/微信升级通知（开发中）
* Web配置（计划开发中）
* 对接playbook（计划开发中）

## 执行
在ansible主机上执行"ansible"目录中"main.py"

## 1. 基本架构
为了满足线上开发、生产环境的需要，须要保证整个升级业务正常，不容出错。

1. 停止服务
2. 备份线上代码
3. 删除线上代码
4. 上传线上代码
5. 启动服务
6. 检查服务（独立出来，可作为监控使用）

## 2. 配置文件
配置文件形如“.ini/cfg”形式，从本地ansible中获取主机名

## 3. 日志构成
内容：
1. 基于原先的升级脚本进行修改，要有升级日志
其中日志包含：
1. 项目任务（洞察力fm、wisehealth_fm、BMS项目、clcs...）
2. 升级类型（热升级、冷升级（**））
3. 触发时间--升级时间
4. 结束时间
5. 升级结果（Success | Failed）
6. 升级类型（前端、后端、数据库）
7. 升级主机名称（ansible server）
8. 升级主机名称（linux: hostname）
以任务为主

2. 将多个升级脚本进行合并，不同项提取生成配置文件

## 4. 使用说明
1. 在Ansible主机中将```/etc/ansible/hosts```配置文件拷贝至项目中。