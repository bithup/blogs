### Java简介与发布历史

###### 时间轴
- Java之父：James Gosling
- 最初设计目的是为机顶盒这种嵌入式设备，为了平台无关性，使用虚机器码，语言开发阶段将设计目的扩展到万维网应用。
- 1994年Java 1.0a提供下载
- 1995年正式公开发布，诞生
- 1996年初，Java 1.0版正式发布
- 1997.02.18，JDK1.1发布
- 2000.05.08，JDK1.3发表
- 2000.05.29，JDK1.4发布
- 2004.09.30，Java SE 5.0
- 2005.06，Java SE 6.0发布
- 2006.11.13，sun开始开源Java SE 6终版
- 2009年，sun被oracle收购
- 2011.07，Oracle发布Java SE 7
- 2014.03，Oracle发布Java SE 8
- 2017， Java SE 9
- 2017， Java SE 10

######Java官方组织
- [JCP官网](https://jcp.org/en/home/index)
- [OpenJDK](http://openjdk.java.net/)

###### Java版本与新特性
Java 1.0
- JDBC
- 内部类
- Java Bean
- Remote Method Invocation
- 反射

Java 1.2
- 集合框架
- 字符串常量
- Just In Time编译器
- Swing，Java 2D类库

Java 1.3
- 声音API
- jar文件索引

Java 1.4
- XML处理
- 打印
- Logging API
- JDBC 3.0
- 断言
- Preferences API
- 链式异常处理
- IPv6
- 正则
- Image I/O

Java SE 5.0
- 泛型
- 增强for循环
- 自动装箱和拆箱
- 类型安全的枚举
- 可变参数
- 静态引入
- 注解
- Instrumentation

Java SE 6
- 支持脚本语言
- JDBC 4.0 API
- Java Compiler API
- 可插拔注解

Java SE 7
- switch字符串
- 泛型对象类型推断
- catch多个异常
- 动态语言支持
- try-with-resources
- NIO.2
- 数值用二进制字符串表示
- 

Java SE 8
- lambda
- 改进日期与时间API
- Functional接口
- 接口默认方法和静态方法
- 方法引用


###  Java关键字

###### 简单分类
- 类型
- 流程控制

###### 不常用关键字

关键字 | 描述
------|-------
assert | 断言条件是否满足
continue | 不执行循环体剩余部分
default | switch语句中的默认分支
do-while | 循环语句，循环体至少会执行一次
final | 表示定义常量
finally | 无论有没有异常发生都执行代码
goto | 用于流程控制
instanceof | 测试一个对象是否是某个类的实例
native | 表示方法用非java代码实现
strictfp | 浮点数比较使用严格的规则
synchronized | 表示同一时间只能由一个线程访问的代码块
throws | 抛出多个异常
transient | 修饰不要序列化的字段
volatile | 标记字段可能会被多个线程同时访问，而不做同步

###### 小结
- 一共有50个关键字，其中const和goto没有使用
- null/true/false不在关键字列表中，但不能用作标识符
- 分几类
- default是与switch语句相关的关键字，那默认的权限修饰符与default有管吗
- sizeof不是Java关键字，怎么实现sizeof的功能
- [参考博客](https://www.cnblogs.com/AloneZ/p/java1.html)
- [Java SE官方文档](https://docs.oracle.com/javase/10/)
- [oracle官方tutorial关键字列表](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html)


### Java命名规范
- 什么叫标识符
- 只能包含字母、数字、下划线和$组成
- 不能以数字开头，长度不限，区分大小写
- 包名和系统文件夹的命名规则
- 类文件不使用pakage指定包路径会怎样
- 一个类文件包含多个class
- main函数的写法，必须带参数吗
- 变量名首字母大写会怎样
- class首字母小写会怎样

Java命名规范中，实体类属性名以小写字母开头，但并没有说不能以大写字母开头  
手动编写实体类时，将属性companyName的首字母大写  
使用IDE自动生成构造函数  
```
public Custom(long id, String companyName, String telephone) {
    this.id = id;
    CompanyName = companyName;
    this.telephone = telephone;
}
```
构造函数中CompanyName前没有this  
原因是只有首字母大写  
如果遇到首字母需要大写的情况，因该将前两个字母都大写  
例如：private String IDCard;  
这样生成构造函数时不会出错  
```
public Custom(long id, String companyName, String IDCard) {
    this.id = id;
    CompanyName = companyName;
    this.IDCard = IDCard;
}
```
另外，属性名前两个字母不能一个大写一个小写，要么同时大写，要么同时小写  
例如：iDCard，IdCard都是非法的

### Java数据类型

###### 基本类型
类型|占用字节|数值表示范围|默认值
----|----|----|----
byte|1|-128~127| |
short|2| | |
char|2| | |
int|4| | |
float|4| | |
long|8| | |
double|8| | |
boolean|不定| | |

###### 基本类型隐式转换
- boolean类型不能转换
- 浮点数转换整数的方式是去掉小数点
- 字节数少的类型转字节数多的类型，自动转换
- byte/short/char与整数运算，默认隐式转换为int
- short与char如何转换
- long到float是自动转换吗

###### 引用类型
```
//父类
Class Car{
    int price;
}
//子类
Class Benz extends Car{
    String color;
}
//实例指具有某种数据结构的内存区域
//new操作符执行的功能是，申请分配内存空间，并返回引用
//一般创建对象
Benz benz = new Benz();

//多态，父类引用指向子类示例
//编译器如何编译这段代码
//类型是给人看的，机器里只有类型所占内存的区别
//代码运行时内存变化：函数栈执行到这一步，需要将一个引用压栈，先实例化父类，再实例化子类，
//将子类内存区域设置为不可访问，将返回引用压栈；
Car car = new Benz();

//子类引用能否指向父类实例，下面例子运行时会报错，申请的内存空间，无法覆盖声明的内存空间
Benz benz = (Benz)new Car();

//先将一个父类引用指向子类实例，然后将这个父类引用赋值给一个子类引用
Car car = new Benz();
//此处的强转是将子类示例不可访问的空间解锁
Benz benz = (Benz)car;

//Map(String, Object)存取值时发生的类型转换
//mybatis中使用map为SQL传参数时，传入String类型能自动转换成Long或int

//不相关的类型之间，不管所占内存的大小，不能转换
```
[子类实例创建过程](http://www.cnblogs.com/chenyangyao/p/5296807.html)
思考：子类与父类之间的转换，类型转换发生在编译阶段还是运行阶段

###### 数组和其他引用类型的差异

###### Java字符串
- 底层结构
- 占用内存
- 一个中文字符在内存中占几个字节

###### 变量，常量的声明，定义，初始化
- 什么情况可以不初始化

###### 面试题
> 题：short s1 = 1; s1 = s1 + 1;有什么错?  
short s1 = 1; s1 += 1;有什么错?  
short x = 1; y = 2; short z = x + y;有什么错？  
答：因为给short赋值时并没有像float那样使用f，明确指出类型；  
所以short s1 = 1; s1 += 1;这两个
表达式右边的 1 都会被当成int16；所有不会报错；
而s1 = s1 + 1右边的表达式计算的结果是int32的所以报错。
x + y表达式计算的值默认是int32，所以会出错。

###### 小结
- boolean类型取决与使用情况和JVM具体实现，单个boolean值使用int表示，boolean数组中boolean用byte表示
- [表示范围](https://www.cnblogs.com/ysj4428/p/6030771.html)
- 大型稀疏矩阵使用byte数组更节约空间
- 数值包装类都继承值Number抽象类
- Java中char是Unicode编码，无宽窄字符之分
- 整数默认是int，尾部加L表示long，浮点数默认是double，尾部加f表示float
- 引用所占内存空间与系统位数有关，64位系统占8个字节

### Java运算符优先级和结合性

- 问：运算符为什么需要有优先级和结合性？答：如果所有的变量和常量的左边  
或右只有一个运算符，就不需要优先级；如果一个变量的左右都有运算符，就需  
要使用优先级判断先执行那个表达式。如果一个变量被两个表达式共享，而且变  
量左右的运算符优先级相同，就需要使用优先级判断先执行那个表达式。
- 考虑结合性是在相邻的两个运算符优先级相同的情况下
- 大多数运算符结合性都是自左向右；括号，点号，四则运算，  
关系运算（等于，大于小于等），逻辑与，逻辑或
- 逻辑与会短路，按位与不会短路，Java中使用逻辑与，如果左边  
表达式为false，则不会计算右边表达式；如果使用按位与，两边表达式都要计算。
- c语言中没用bool值，Java语言中有。Java中按位与运算两边的表达式计算的值是数值型还是bool型。
- 结合性自右向左：赋值运算符，常见的单目运算符，逻辑非，按位取反，条件运算符
```
public class Demo {
    public static void main(String[] args){
      int i = 0;
      int j = i++;
      int k = --i;
      
      int i = 0;
      int j = i++ + ++i;
      int k = --i + i--;
      
      int i = 0;
      int k = ++i--;
      
      /*自增与自减运算符还遵循以下规律：
         1. 可以用于整数类型byte、short、int、long，浮点类型float、double，以及字符串类型char。
         2. 在Java5.0及以上版本中，它们可以用于基本类型对应的包装器类
            Byte、Short、Integer、Long、Float、Double、Character。
         3. 它们的运算结果的类型与被运算的变量的类型相同。*/
      
      //赋值运算符
      
      int a=0;
      a+=a-=a=9;
      
      //连续赋值，=向右结合，自右向左，所以下面表达式等价于a = (b = c)
      //结合可简单理解为给表达式加上（），自右向左就是加括号或执行的顺序；
      int a=b=c;
      
      
      //条件运算符
      int x = 3;  
      int y = 2;  
      int z = x > y ? 100 : ++y > 2 ? 20 : 30; 
    }
}
```

### 流程控制语法


