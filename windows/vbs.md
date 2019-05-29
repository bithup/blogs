## 变量

- 命名规则，
- 类型variant
- 声明：Dim、Public、private
- 数组：使用（），例demos(2)声明长度为3的数组

## 子程序

- 以Sub和End Sub开头和结尾
- 可以带参数，没有返回值

## 函数程序

- 以Function和End Function开头和结尾
- 可以有参数，有返回值

## 条件判断

- If ... Then
- ElseIf ... Then
- Else ...
- End If

## 循环

- For...Next ： 运行一段代码指定的次数

```vb
For i = 0 To 5

Next
```

- For Each...Next ： 针对集合中的每个项目或者数组中的每个元素来运行某段代码

```vb
Dim demos(2)
For Each x In demos

Next
```

- Do...Loop ： 运行循环，当条件为 true 或者直到条件为 true 时

```vb
Do While i>10
some code
Loop

Do
some code
Loop While i>10

Do Until i=10
some code
Loop

Do
some code
Loop Until i=10

Do Until i=10
i=i-1
If i<10 Then Exit Do
Loop
```

## 常用对象

- ADODB.Stream
- InternetExplorer.Application
- Msxml2.XMLHTTP
- Scripting.Dictionary
- Scripting.FileSystemObject
- Shell.Application
- WScript.Shell

## 正则

## 字符串

- 字符串拼接

```vb
Dim str, i
str = abc
i = 4
str = str&i
msgbox str
```

- 时间函数year() month()
- Mid()
- 