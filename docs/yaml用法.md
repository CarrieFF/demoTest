yaml 使用场景：
    1- 做配置文件
    2- 做测试用例

配置文件：
    开发角度：
        1- 现成的第三方组件
            tomact----tomcat/conf/server.xml
            mysql----my.conf --端口，log，buffer 连接数等
            redis----redis.conf ---端口，连接池，内存模式
    测试角度：
        1- 性能测试---很多监控与项目配置文件会修改一些参数
        2- 自动化测试做配置文件 apiPath.yml
        3- 自动化测试用例
