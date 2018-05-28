## Java关键字
### 分类	
- 基本类型：double、boolean、byte、float、long、char、int、short
- 类和接口：class、interface、extends、implements、new、instanceof、package、import、enum
- 访问权限：public、private、protected
- 异常处理：try、catch、finally、throw、throws
- 流程控制：do、while、if、else、for、continue、break、switch、case、default、return、assert  
- 类型修饰符：static、final、native、abstract、synchronized、volatile、strictfp、transient
- 引用：this、super、void
- 保留：goto、const

### 不常用
key word     |description
-------------|-----------
default      |switch语句中的默认分支  
native       |表示方法用非java代码实现
synchronized |表示同一时间只能由一个线程访问的代码块
volatile     |标记字段可能会被多个线程同时访问，而不做同步
strictfp     |浮点数比较使用严格的规则 
transient    |修饰不要序列化的字段
assert       |断言条件是否满足

### 小结
- 一共有50个关键字，其中const和goto没有使用
- 1.2版本增加strictfp，1.4版本增加asser，5.0版本增加enum
- null/true/false不在关键字列表中，但不能用作标识符
- default是与switch语句相关的关键字，那默认的权限修饰符与default有管吗
- sizeof不是Java关键字，怎么实现sizeof的功能
- Java中对null，void，true，false是如何处理的
- [Java SE官方文档](https://docs.oracle.com/javase/10/)
- [oracle官方tutorial关键字列表](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html)

## Java标识符
- 类名、接口名、方法名、变量名
- 只能包含字母、数字、下划线、$和￥组成，不能以数字开头，长度不限，区分大小写
- 一个类文件可以包含多个class，只有一个public class
- main函数的修饰符public static、返回值void、参数String[] args
- 变量名首字母大写和class首字母小写都是可以的，而且class首字母小写，创建对象时  
对象名和类名相同不会报错;但是Bean的属性名首字母大写，在生成构造函数以及setter  
和getter方法时会出错；

## Java数据类型

### 基本类型
type    |space   |range       |default
--------|--------|------------|---------
byte    |1       |-128~127    |0
short   |2       |-2^15~2^15-1|0
char    |2       |-2^15~2^15-1|'\u0000'
int     |4       |-2^31~2^31-1|0
float   |4       |3.4028235E38|0.0F
long    |8       |-2^63~2^63-1|0
double  |8       |IEEE754     |0.0D
boolean |not sure|true false  |false

### 基本类型隐式转换
- boolean类型不能转换
- 浮点数转换整数的方式是去掉小数点
- 字节数少的类型转字节数多的类型，自动转换
- byte/short/char与整数运算，默认隐式转换为int
- short与char如何转换
- long到float是自动转换吗
- [为什么是-128，而不是-127](https://www.cnblogs.com/ysj4428/p/6030771.html)
- Java浮点数结构
- Javalong型长度和系统位数的关系
- Java使用UTF16编码
> 问：short s1 = 1; s1 = s1 + 1;有什么错?  
      short s1 = 1; s1 += 1;有什么错?  
      short x = 1; y = 2; short z = x + y;有什么错？  
答：因为给short赋值时并没有像float那样使用f，明确指出类型；  
所以short s1 = 1; s1 += 1;这两个
表达式右边的 1 都会被当成int16；所有不会报错；
而s1 = s1 + 1右边的表达式计算的结果是int32的所以报错。
x + y表达式计算的值默认是int32，所以会出错。

### Java字符串与数组
- 字符数组与字符串的区别
- 数组是一个对象，是哪个类的对象
- 底层结构
- 占用内存
- 一个中文字符在内存中占几个字节
- 引用类型的类型转换，强转



变量的初始化，类的属性，在创建对象时会默认初始化，但是在方法中定义的局部变量必须先初始化，再使用







Java关键字、运算符、标识符命名、程序流程控制、数据类型及表示范围
