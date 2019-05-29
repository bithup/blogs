## 常用adb命令
adb命令使用-s 参数加设备号指定设备（只连接单个设备情况下，忽略）
adb version
adb kill-server/start-server
adb pull/push  电脑和手机直接传输文件
adb install apk文件路径
adb shell pm list package 列出已安装包名
adb uninstall  包名 
使用exit 退出adb shell
adb shell wm size 获取屏幕分辨率
adb install : 包含两步，adb push 和adb shell pm install
adb shell pm clear <pkname> 清楚缓存
adb shell dumpsys package <pkname> 查看应用详细信息

## adb shell
adb shell am 命令
adb shell am start -n com.android.settings/com.android.settings.Settings
这个命令是Android系统的设置界面， 斜杆前的是包名，后面的是activity名
获取包名和activity名的方法有两种：
使用aapt命令和 apk文件获取package和launch_activity
或
adb shell dumpsys window windows | findstr Current

切换输入法
adb shell ime list -s 查看安装输入法
adb shell ime set io.appium.settings/.UnicodeIME

模拟输入(只能输入ASCII)
adb shell input text ""
引号中是要输入的内容，特殊字符要使用\转义
 
点击屏幕坐标
adb shell input tap 100 100
滑动屏幕
adb shell  input swipe 1000 1000 100 1000

返回, 4 表示返回上一级
adb shell input keyevent 4
其他keycode可搜索Android Keycode

发送鼠标事件Touch
adb shell sendevent/getevent 
模拟滑动轨迹

输入中文
切换AdbIME输入法
然后
adb shell am broadcast -a ADB_INPUT_TEXT
 --es msg '中文'
