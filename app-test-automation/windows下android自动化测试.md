## 环境搭建

- 安装JDK
- 安装Android SDK
- 安装python及相关依赖库
- 安装Nodejs  
- 安装appium，appium-doctor，使用npm安装或者安装appium desktop，

环境变量|值|
----|----|
JAVA_HOME| JDK或JRE安装目录
PAHT| %JAVA_HOME%bin
ANDROID_HOME| Android SDK安装目录
PATH| %ANDROID_HOME%tools
PATH| %ANDROID_HOME%platform-tools
PATH| %ANDROID_HOME%build-tools\“version”

## 测试连接Android手机并获取app信息
- Android手机进入开发者模式，使用数据线连接电脑，并开启USB调试模式
- 使用adb devices查看是否连接成功
- 使用SDK中build-tools目录下aapt工具查看appPackage和appActivity，格式：aapt dump badging xxx.apk
- 没有apk文件时，查询appPackage和appActivity，打开要查看的app，然后：adb shell dumpsys window windows | grep -E 'mFocusedApp'  ；以/隔开的就是要查询的。
- 或者adb shell dumpsys activity | finstr 'mFocusedActivity' ;windows下用findstr，Linux下用grep
- appium使用Android SDK tools目录下**uiautomatorviewer.bat**工具识别控件

## desired caps参数
能力|值|描述|
----|----|----|
platformName|android|
deviceName|udid|
appPackage|com.xxx.xxx|
appActivity|com.xxx.activity|
noSign|true|
noReset|true|
unicodeKeyboard|true|
resetKeyboard|true|
chromeOptions|{'androidProcess': 'com.tencent.mm:tools'}|
url| |
newCommandTimeout|120|
udid|设备唯一标识符|
其他参数参考：[caps.md](https://github.com/appium/appium/blob/master/docs/cn/writing-running-appium/caps.md)

- ‘autoLaunch‘:‘false‘   #appium是否要自动启动或安装APP，默认为ture
- ‘newCommandTimeout‘:‘60‘  #设置未接受到新命令的超时时间，默认60s，说明：如果60s内没有接收到新命令，appium会自动断开，如果我需要很长时间做driver之外的操作，可设置延长接收新命令的超时时间
- ‘unicodeKeyboard‘:True,
- ‘resetKeyboard‘:True  
- ‘noReset‘:‘false‘  #在会话前是否重置APP状态，默认是false

## Python测试脚本
```python
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '7.x.x'
desired_caps['udid'] = ''
desired_caps['appPackage'] = ''
desired_caps['appActivity'] = ''
desired_caps['newCommandTimeout'] = ''

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
element = driver.find_element_by_id('xxxxx')
element.click()
element.send_keys('abcdefg')
```

## python依赖库及

python库|描述|
----|----|
setuptools|abc
Appium-Python-Client| 
selinum|
urllib3|

## Appium运行原理
测试脚本发送JSONwire protocol http消息到appium server；appium server转换HTTP消息为相应指令，发送到Android设备上的bootstrap.jar；bootstrap.jar驱动uiautomation执行命令；bootstrap.jar继承了uiautomation中的testcase类。

```flow
st=>start: start
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
```
