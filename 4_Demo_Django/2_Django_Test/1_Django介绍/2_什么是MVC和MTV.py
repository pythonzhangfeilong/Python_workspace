##### 1、MVC:
'''
    全名Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件工程典范，
    用业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，
    不需要重新编写业务逻辑。
'''
# 说的简单点：
'''
    一种代码和文件的组织和管理形式！不要被缩写吓到了，这其实就是把代码分散到不同的文件中，把不同类型的文件又放到不同目录下的
    一种做法，然后取了个高大上的名字。当然，它带来的好处有很多，比如前后端分离，松耦合等等，在使用中慢慢体会就会逐渐明白
'''

# MVC分别的意思
'''
    模型(model)：定义数据库相关的内容，一般放在models.py文件中。
    
    视图(view)：定义HTML等静态网页文件相关，也就是那些HTML、CSS、JS等前端的东西。
    
    控制器(controller)：定义业务逻辑相关，就是你的主要代码。
'''

##### 2、MTV
'''
    Django觉得MVC的字面意思很别扭，不太符合它的理念，就给它改了一下。view不再是HTML相关，而是主业务逻辑V了，相当于控制器。
    HTML被放在Templates中，称作模板T，于是MVC就变成了MTV。这其实就是一个文字游戏，和MVC本质上是一样的，换了个名字和叫法而已，
    换汤不换药。
'''

# MTV分别的含义
'''
    M:Model(数据库)                有的也叫模型，其实就是写数据库的东西，一般是models.py
    T:Templates(前端的HTML)        Templates在建立好Django是一个文件夹，把前端的东西放在这个里面
    V:View(主逻辑)                 在MVC中vews中放的是前端的内容，在MTV中就是放的主逻辑
'''










