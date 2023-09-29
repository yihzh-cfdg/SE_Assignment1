# PEP 8

## 缩进

采用4个空格进行缩进，空格是首选的缩进方法。

```python
# 与左括号对齐
foo = long_function_name(var_one, var_two,
                        var_three, var_four)

# 用更多的缩进来与其他行区分
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 挂行缩进应该再换一行
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```



## 每行不超过79个字符

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```



## 空行

1. 顶层函数和类的定义，前后用两个空行隔开。
2. 类里的方法定义用一个空行隔开。
3. 相关的功能组可以用额外的空行隔开。
4. 一堆相关的单行代码之间的空白行可以省略。
5. 在函数中使用空行来区分逻辑段。



## Imports导入

导入通常在分开的行，如：

```python
import os
import sys
```

导入总是位于文件的顶部，在模块注释和文档字符串之后，在模块的全局变量与常量之前。

导入应该按照以下顺序分组：
1. 标准库导入
2. 相关第三方库导入
3. 本地应用/库特定导入



## 表达式和语句中的空格

1. 各种右括号前不要加空格
2. 逗号、冒号、分号前不要加空格
3. 函数的左括号前不要加空格，如Func(1)
4. 序列的左括号前不要加空格，如list[2]
5. 操作符左右各加一个空格
6. 函数默认参数使用的赋值符左右省略空格



## 注释

块注释：在一段代码前增加的注释。在‘#’后加一空格。段落之间以只有‘#’的行间隔。

```python
# Description : Module config.
#
# Input : None
#
# Output : None
```



## 命名规范

1. 始终要将 self 作为实例方法的的第一个参数
2. 类名一般使用首字母大写
3. 如果函数的参数名和已有的关键词冲突，在最后加单一下划线
