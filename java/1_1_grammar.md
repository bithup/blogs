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

key word|description  
-------------|-----------
default      | switch语句中的默认分支  
native       | 表示方法用非java代码实现
synchronized | 表示同一时间只能由一个线程访问的代码块
volatile     | 标记字段可能会被多个线程同时访问，而不做同步
strictfp     | 浮点数比较使用严格的规则 
transient    | 修饰不要序列化的字段
assert       | 断言条件是否满足

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
- 变量声明为public static final时，变量名建议使用全大写

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
- boolean类型取决与使用情况和JVM具体实现，单个boolean值使用int表示，boolean数组中boolean用byte表示
- 大型稀疏矩阵使用byte数组更节约空间
- 数值包装类都继承值Number抽象类
- Java中char是Unicode编码，无宽窄字符之分
- 整数默认是int，尾部加L表示long，浮点数默认是double，尾部加f表示float
- 引用所占内存空间与系统位数有关，64位系统占8个字节
- 变量初始化与默认值：  
变量的初始化，类的属性，在创建对象时会默认初始化，但是在方法中定义的局部变量必须先初始化，再使用
> 问：short s1 = 1; s1 = s1 + 1;有什么错?  
      short s1 = 1; s1 += 1;有什么错?  
      short x = 1; y = 2; short z = x + y;有什么错？  
答：因为给short赋值时并没有像float那样使用f，明确指出类型；  
所以short s1 = 1; s1 += 1;这两个
表达式右边的 1 都会被当成int16；所有不会报错；
而s1 = s1 + 1右边的表达式计算的结果是int32的所以报错。
x + y表达式计算的值默认是int32，所以会出错。

### 字符串与数组
- 字符数组与字符串的区别
- 数组是一个对象，是哪个类的对象
- 底层结构
- 占用内存
- 一个中文字符在内存中占几个字节
- 引用类型的类型转换，强转

## Java运算符优先级和结合性

### 表格
 
priority|operator      |associative
--------|--------------|-----------
1       |() . []       |左到右
2       |! + - ~ ++ -- |右到左
3       |* / %         |左到右
4       |+ -           |左到右
5       |<< >> >>>     |左到右
6       |< <= > >= instanceof|左到右
7       |== !=         |左到右
8       |&             |左到右
9       |^             |左到右
10      |\|            |左到右
11      | &&           |左到右
12      | \|\|         |左到右
13      |?:            |右到左
14      |= += -= *= /= %= &= \|= ^= ~= <<= >>= >>>=|右到左

### 例子
```java
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
- 问：运算符为什么需要有优先级和结合性？  
答：如果所有的变量和常量的左边  
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


## Java流程控制语法
- for
- do while
- switch case
- assert
