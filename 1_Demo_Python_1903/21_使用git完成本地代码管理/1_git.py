'''
神奇带闪电网站：https://learngitbranching.js.org/
21.1  版本控制介绍以及常用的版本控制工具
版本控制是指对软件开发过程中各种程序代码、配置文件及说明文档等文件变更的管理，是软件配置管理的核心思想之一。
编写一个成熟可用的程序是一个工作量很大的工程，并非我们一次性就可以搞定的工作，所以在开发过程当中需要：
1、	多人协作
随着对程序体验的需求的提高，一个程序需求的编程知识和模块也在增多，这种情况下让一个程序员同时掌握多门技术是不好实现的：
1、掌握的难度大，开发的成本高（比如：一个大牛的工资）
2、开发效率高，一个人开发的效率是不行的
所以，我们在工作当中大部分讲究的是协作开发，我们以项目需求的技术模块进行团队的组合。
比如，开发一个web项目：如果要招聘一个web大牛，前端、后端、运维服务器都很牛的大牛，薪资高先不说，人也不好找啊。并且一个大牛的开发效率和开发压力也很大。所以我们会形成一个开发的团队，找前端开发工程师，后端开发工程师，运维工程师，数据库工程师来完成这个光荣而又艰巨的任务。
2、	版本迭代
就好像一个美术家要完成一件作品，并不是一蹴而就的，好多时候是经历过多次修改的过程，我们编程也是一样的，当然这个修改要有原则，并不是推倒重来的过程（当然前期无药可救的不算），而是有简单的一个完整的框架开始，然后不断优化升级的过程，这个过程就是版本迭代。
那在这个过程当中，我们需要对代码进行管理，比如：提交、检出、回溯历史、冲突解决、多人协作。那这些需求也就衍生出了我们要学习使用的版本控制工具。
各个公司由于开发的需求和其他因素用到的版本控制工具不都相同，这里我们介绍几种使用较多的版本控制工具。
cvs：  是一个C/S系统,是一个常用的代码版本控制软件。主要在开源软件管理中使用。
多个开发人员通过一个中心版本控制系统来记录文件版本，从而达到保证文件同步的目的。是一种很古老的版本控制工具了，但是是很典型的集中式版本控制工具
SVN： 是一个开放源代码的版本控制系统，相较于RCS、CVS，它采用了分支管理系统，它的设计目标就是取代CVS。可以说是集中式版本控制的集大成者。
Git：   是一个开源的分布式版本控制系统，可以有效、高速的处理从很小到非常大的项目版本管理。是一种分布式的版本控制工具
GitHub：gitHub是一个面向开源及私有软件项目的托管平台,因为只支持git 作为唯一的版本库格式进行托管,故名gitHub。
上面介绍了我们常用的四种版本控制软件，但是也要给大家解释两个概念：
分布式版本控制：分布式的版本控制就是每个人都可以创建一个独立的代码仓库用于管理，各种版本控制的操作都可以在本地完成。每个人修改的代码都可以推送合并到另外一个代码仓库中。
集中式版本控制：只有一个中央控制，所有的开发人员都必须依赖于这个代码仓库。每次版本控的操作也必须链接到服务器才能完成。
所以很多公司喜欢用集中式的版本控制是为了更好的控制代码。如果个人开发，就可以选择Git这种分布式的。并不存在那个更加好或者其他的。
21.2  版本控制工具-GIT
gitHub是一个面向开源及私有软件项目的托管平台,因为只支持git 作为唯一的版本库格式进行托管,故名gitHub。
'''