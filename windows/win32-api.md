## 字符编码

### ASCII和UNICODE

```c
//ANSI编码
char c = 'A';
char * p = "hello";
char a[] = "hello";
//宽字符在WCHAR.h中定义
//typedef unsigned short wchar_t
wchar_t c = 'A';
wchar_t * p = L"hello";
wchar_t a[] = L"hello";
//字符串函数的两个版本
strlen();
wcslen();
//兼容两种字符集
TCHAR c = 'A';
PTCHAR p = TEXT("hello");
```

### 控件

创建控件就是创建不同类型的窗口
