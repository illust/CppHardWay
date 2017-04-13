## auto和decltype区别主要有如下三个方面：
***第一***，auto类型说明符用编译器计算变量的初始值来推断其类型，而decltype虽然也会让编译器分析表达式并得到它的类型，但是不实际计算表达式的值。
例如：
```
int a = 3,b = 4;
decltype(a = b) d = a;
```
赋值是会产生引用的一类典型表达式，引用的类型就是左值的类型，因此编译器分析a = b;得到int&类型并且不会执行赋值操作，得到d的值为3。

***第二***，编译器推断出来的auto类型有时候和初始值的类型并不完全一样，编译器会适当的改变结果类型时期更符合初始化规则。例如，auto一般会忽略掉顶层const，而把底层const保留下来。与之相反，decltype会保留变量的顶层const。
例如：
```
const int ci = 0,&cj = ci;
auto cr = ci;
decltype(ci) x = 0;  //x has type const int
decltype(cj) y = x;  //y has type const int& and is bound to x
decltype(cj) z;      //error:z is a reference and must be initialized
```
cr的类型就是int;x的类型是const int，y,z的类型都是const int&，因此都需要初始化，所以z的声明是错误的。

***第三***，与auto不同，decltype的结果类型与表达式形式密切相关，如果变量名加上了一对括号，则得到的类型与不加括号时会有不同。如果decltype使用的是一个不加括号的变量，则得到的结果就是该变量的类型；如果给变量加上了一层或多层括号，则编译器将推断得到引用类型。
例如：
```
int a = 3;
decltype(a) c1 = a;
decltype((a)) c2 = a;
```
a的类型是int，因此c1也是int型；c2的类型由decltype根据表达式(a)推导出为int&型。
