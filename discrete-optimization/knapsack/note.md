
# java 代码的坑

1. solverJava.py 运行java文件 如果显示 ```can not load or find main class``` 应该是需要在环境变量 classpath 中添加 ```.;``` 即当前目录，这个具体可以参见[爆栈答案](https://stackoverflow.com/questions/18093928/what-does-could-not-find-or-load-main-class-mean)
2. 我在```solverJava.py``` 中加了```os.system("javac .\Solver.java")``` 这行代码，使得`.java` 文件每次都能都被重新编译

3. 重构了 solver 方法，提供一个接口 使得不同的算法只需要提供 solve方法即可

# knapsack 问题算法

## dp

这个方法很简单，以前学过

$dp[k][j] = \max \{dp[k][j-1],values[j] + dp[k-weights[j]][j-1]\}$

但是要注意，因为要求出 `taken[i]` 即第 $i$ 个单元是否 $taken$ 故用一维数组无法求出答案
