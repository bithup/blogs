# java interview

## 基础
- JDK、JRE、JVM的区别？
- 一个字节是多少bit（位），一KB中的B是Byte还是bit？
- 基本数据类型（几种）和包装类，byte/int/char/long各占多少字节，64位和32位jvm中int的长度是否相等？
- byte/char的取值范围，如果用超出变量取值范围的值给变量赋值会怎样？编译会报错吗？
- 两个对象hashcode相同，equals()比较的结果？
- 注解，元注解，注解是否可以修饰注解，如何自定义注解？
- 枚举是什么，有什么作用？和静态变量有什么区别？
- 类型推导
- 泛型

### 常用api，包名，类名

- Math.round();
- 字符串（常用方法）反转，截取，搜索，拼接
- 拼接大量的字符串怎么操作，多线程下用什么类？
- POI处理Excel，处理JSON的类库，处理XML的方式和类库及优缺点？

### 关键字和运算符

- final关键字的作用，String是否可变（为什么），final集合中的元素值是否可变？
- 权限
- 与或非，逻辑，按位，左移右移？
- 是否可以从一个static方法内部发出对非static方法的调用？
- Abstract/static/final 有哪几种组合？


## 面向对象编程

- 抽象类必须有抽象方法吗？
- 抽象类能用final修饰吗？
- 接口和抽象类的区别？
- 构造器Constructor是否可被override?
- 列举尽肯多的接口，以及他们的作用？
- 抽象类，内部类，匿名类，静态内部类，匿名内部类？
- new一个接口

## 集合

- Java容器有哪些？
- Collection和Collections的区别？
- 容器还实现哪些接口，比较，序列号，遍历
- List Set Map的区别？Map继承Collection接口吗？
- ArrayList和LinkedList的区别？LinkedList是单向还是双向链表？
- ArrayList和数组的区别
- HashMap/Hashtable/TreeMap，如何选择？
- HashMap实现原理
- Iterrator怎么使用？
- 怎么确保一个集合不被修改

## IO

- IO流分几种？字节流和字符流的区别？
- 字节数组和String相互转换？
- BIO、NIO、AIO
- File类常用方法，判断是否存在，是否是文件夹
- 以字节流、字符流、缓冲流读取文件

## 反射

- 什么是反射？
- 哪种设计模式用到反射？如何实现动态代理？

## 异常

- 常见异常，异常分类，哪些需要捕获，如何处理？
- throw和throws？
- final/finally/finalize区别？
- try-catch-finally中返回值的先后顺序

## 网络

## 多线程

- 并发和并行的区别？
- 线程和进程的区别？
- 守护线程是什么？
- 创建线程有哪些方式？
- run()和start()的区别？
- runnable和callable的区别？
- 线程有哪些状态，什么情况下会阻塞，如何唤醒
- sleep() 和 wait() 的区别？
- notify() 和 notifyAll()的区别？
- 创建线程池的方式？
- 线程池submit和execute方法的区别？
- 线程安全是什么？什么情况是线程不安全的？如何保证线程安全（加锁）？
- ++操作符是线程安全的吗？不是
- 什么是死锁？如何避免死锁？
- ThreadLocal使用场景？
- synchronized底层实现原理？
- synchronized\volatile\Lock之间的区别？
- atomic的原理？

## 设计模式

- 常见设计模式及实现？

## 算法

- 排序
- 递归
- 迭代
- 回归

## JVM

- jvm内存分配，分哪几块，存放什么数据？
- jvm中以什么编码存储字符串，一个字符占多少字节？
- class文件加载过程，classloader？
- GC是什么?为什么要有GC?GC算法 垃圾回收的优点和原理。并考虑2种回收机制。垃圾回收器可以马上回收内存吗？有什么办法主动通知虚拟机进行垃圾回收？

## 框架

### spring

- SpringMVC或Struts处理请求的流程
- spring的依赖注入有哪几种方式
- Spring AOP解决了什么问题？怎么实现的？aop与cglib，与asm的关系。
- 列举四个注解，并说明用法？

### ORM

- Hibernate和Ibatis这类ORM框架的区别？什么是ORM，解决的痛点是什么？

### 消息

- 几种推送模型的区别，long polling，websocket

### 微服务

- RPC的负载均衡、服务发现怎么做的

### web

- 如何实现跨域？