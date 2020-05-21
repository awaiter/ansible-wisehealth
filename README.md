# ansible-wisehealth
Moving bricks for life.

自动化升级开发（本升级只限于公司内部）
基于Ansible + Python

内容：
1. 基于原先的升级脚本进行修改，要有升级日志
其中日志包含
    1、项目任务（洞察力fm、wisehealth_fm、BMS项目、clcs...）
    2、升级类型（热升级、冷升级（**））
    3、触发时间--升级时间
    4、结束时间
    5、升级结果（Success | Failed）
        Success：返回
    4、升级类型（前端、后端、数据库）
    4、升级主机名称（ansible server）
    5、升级主机名称（linux: hostname）
    6、升级主机ip
    7、
2. 将多个升级脚本进行合并，不同项提取生成配置文件


系统升级注意事项
1. 停止服务

2. 备份线上代码，backup “application/**.date”

3. 删除线上代码

4. 上传线上代码

5. 启动服务

6. 检查服务