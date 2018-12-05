这是 programing language part A 的一个简单回顾


# 思考

这门课程可以说非常棒，给了我很多在程序语言上的洞见，可以说是让我重新理解了编程，重新理解了程序语言，不过可能关于整个 程序语言(programing language,PL)的研究, 在工业界真正的用武之地是很少的，或者说不如真正的应用计算机科学(系统,机器学习,etc)来的那么直接。不过我却认为里面有很多迷人的哲学式的美感。这是我第一次用函数式语言，我被他的间接，以及逻辑上的清晰感给折服了。所有计算都是用函数解决的，可以说是非常接近于数学逻辑了。不过真要入这个程序语言的坑，可能还得稍后一些，彼时的我需要的更多的还是一些工业界的东西。(:( ,不然就要饿肚子了)。扯了这么多，感觉是在为不继续学习 Part B，找借口...

# 知识回顾

## wk1

wk1 主要是讲一些 ML的基本用法和概念:

- variable binding
- function binding
- List
- immutable
  
但是最为主要的还是在最后的一节:,作者点出了程序语言的几个重要特征(不要忘了，这门课程的目的是叫我们如何学习所有程序语言)

- **Syntax**: How do you write the various parts of the language?
- **Semantics**: What do the various language features mean? For example, how are expressions evaluated?
- **Idioms**: What are the common approaches to using the language features to express computations?
- **Libraries**: What has already been written for you? How do you do things you could not do without
library support (like access les)?
- **Tools**: What is available for manipulating programs in the language (compilers, read-eval-print loops,
debuggers, ...)

其实学习语言最主要的是掌握语言的 特性，也就是第三点 (**idoms**),这很切合我的想法，所以我上了第一周后就信心满满的继续学了起来

然后后面就是围绕ML的语言特性展开了，重点在于**函数式编程**

wk1 编程作业没什么好说的

## wk2

wk2 的核心在于: **datatype**.

围绕这个展开了如下几个点:

- pattern match
- polymorphic datatype
- tail recursion

作业就是让你全部用pattern match 而不是用 ```hd,tail,#```之类的内置函数

作业编程作业就会发现**pattern match** 和tail recursion 实在是太好用了

**tail recursion** 应该是一个比较通用的概念，不仅仅是函数式里面才有的。因为从他的设计来说，非函数式也可以设计成这样。至于 **pattern match** 我确实在其他语言里没有使用过

**remark:** 我对这些东西仅在理解是什么，怎么用的阶段，以及有什么好处的阶段，至于更深的地方，他的设计哲学在哪里，我变不清楚了。

## wk3

wk3 可以说是整个函数式语言的核心了。

- fun as arguments and returned value
- lexical scope
- closures
- currying
- map,filter,fold
- Combining function

总之有了这些的 idiom 之后的特性是 : 代码更短，逻辑更强，语法糖更多

当然我从不认为语言糖是语言的核心，**其实个人认为语法糖在语言设计中最无足轻重** 但是上面的那些特性，都是语言基于数学逻辑的自然表达，就算没有诱人的语法糖,那些特性也是必须有的。

这周的作业难度要大一些，同时也更简洁一些，用了函数式语法后会发现作业表述起来非常简单。

这周作业剩下最后一个 challenge 没有做，这个challenge是叫你去实现一个type-checker 系统.其他均为满分

## wk4

感觉我wk4 挺boring 的，就是将信息隐藏和表示不变性，这个其实我在 [MIT 6.031 software construction](http://mit.edu/6.031) 中看过，所以了解的比较清楚，就没认真学这章了，

最后还好通过了 :)

# 以后的路

学了这个以后准备把: Part B,Part C 学了，然后以后可能要深入了解一下程序语言，

**programing language 还是很有意思的**
