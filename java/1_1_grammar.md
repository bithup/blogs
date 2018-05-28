## Java关键字
### 分类	
- 基本类型：double、boolean、byte、float、long、char、int、short
- 类和接口：class、interface、extends、implements、new、instanceof、package、import、enum
- 访问权限：public、private、protected
- 异常处理：try、catch、finally、throw、throws
- 流程控制：do、while、if、else、for、continue、break、switch、case、default、return
- 类型修饰符：static、final、native、abstract、synchronized、volatile、strictfp、transient
- 引用：this、super、void
- 保留：goto、const
- 其他：assert  

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









Java关键字、运算符、标识符命名、程序流程控制、数据类型及表示范围
