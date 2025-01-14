# 1、栈和堆
'''
    1、栈区（stack）：编译器自动分配释放，存放函数的参数值，局部变量的值等，其操作方式类似于数据结构的栈。
    2、堆区（heap）：一般是由程序员分配释放，若程序员不释放的话，程序结束时可能由OS回
'''

# 2、栈和堆申请方式
'''
    1、栈（stack）：由系统自动分配
    2、堆（heap）： 需要程序员自己编写
'''

# 3、栈和堆的效率
'''
    1、栈：栈由系统自动分配，速度快，但是程序员无法控制。
    2、堆：堆是有程序员自己分配，速度较慢，容易产生碎片，不过用起来方便。
'''

# 4、栈和堆的储存
'''
    1、栈：在函数调用时，第一个进栈的是主函数中函数调用后的下一条指令的地址
    2、堆：一般是在堆的头部用一个字节存放堆的大小，具体内容由程序员安排。
'''

'''
    总结：其实说的简单点就是：栈是由系统分配的内存地址（也可以理解为常量），堆就是程序员自己手写的字符串（也可以理解为变量量）
'''