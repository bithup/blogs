1.查找DOM节点（元素）
 - 通过id属性查找：var x=document.getElementById("intro");
 - 通过标签名查找：var x=x.getElementsByTagName("p");
 - 通过name属性查找：var x=x.getElementsByName("intro");
 - 通过class属性查找：var x=x.getElementByClassName("intro");
 
2.改变元素内容
 - document.write()
 - document.getElementById(id).innerHTML
 - document.getElementById(id).attribute  //attribute用具体属性代替，如：src,name等；

3.改变元素样式
 - document.getElementById(id).style.property
 - style.property有哪些:color/visibility

4.节点事件属性
 - onclick/onload/onunload/onchange/onmouseover/onmouseout/onmousedown/onmouseup
 - document.getElementById("myBtn").onclick
 - [HTML DOM Event](http://www.w3school.com.cn/jsref/dom_obj_event.asp)
 - <a href="http://www.w3school.com.cn/jsref/dom_obj_event.asp" target="_blank">HTML DOM Event</a>
 
5.document对象
 - HTML DOM Document:document，
 - 对象集合：all[],forms[],images[],links[],anchors[],applets;
 - 对象属性：body,cookie,domain,title,referrer,URL,lastModified;
 - 对象方法：close(),getElementByXXX(),open(),write(),writeln();
 
6.element对象
 - 获取element对象
 - 属性和方法：参考[w3school](http://www.w3school.com.cn/jsref/dom_obj_all.asp)

7.Attribute对象
 - attr：节点属性
 - nodemap：属性节点无序集合
 
8.event对象
 - 属性：元素的事件属性
 - JavaScript对象events，与DOM对象event的关系
 
 9.浏览器对象
  - window：包含下面几个对象或对象的只读引用
  - navigator：可以获取浏览器和系统信息
  - screen：屏幕信息
  - history：历史信息
  - location：当前URL
 
 
