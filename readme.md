# demoTest
接口自动化code

common：公共模块
    -baseAPI.py：基类，给其他业务层继承使用-

lib：基本业务层代码，继承baseAPI文件中class

conf：配置包 接口URL+method HOST：环境切换 logura：日志配置

data： 数据/用例 yml/excel 图片等

testCase： 测试用例套

outFiles： logs-日志文件夹 report：报告文件

docs：项目相关文档

utils：常规方法处理文件包--高可复用性

    - handle_data：处理加密数据或解密
    - handle_excel：处理excel
    - handle_loguru：封装日志
    - handle_path：路径处理 等等.......

pytest.ini：配置自定义mark标签
