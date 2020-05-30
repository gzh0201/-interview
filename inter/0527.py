# 操作系统

# 1 select,poll和epoll

# 其实所有的I/O都是轮询的方法,只不过实现的层面不同罢了.

# 这个问题可能有点深入了,但相信能回答出这个问题是对I/O多路复用有很好的了解了.其中tornado使用的就是epoll的.

# selec,poll和epoll区别总结

# 基本上select有3个缺点:

# 连接数受限
# 查找配对速度慢
# 数据由内核拷贝到用户态
# poll改善了第一个缺点

# epoll改了三个缺点.

# 2 调度算法

# 先来先服务(FCFS, First Come First Serve)
# 短作业优先(SJF, Shortest Job First)
# 最高优先权调度(Priority Scheduling)
# 时间片轮转(RR, Round Robin)
# 多级反馈队列调度(multilevel feedback queue scheduling)
# 常见的调度算法总结:http://www.jianshu.com/p/6edf8174c1eb

# 实时调度算法:

# 最早截至时间优先 EDF
# 最低松弛度优先 LLF

# 3 死锁

# 原因:

# 竞争资源
# 程序推进顺序不当
# 必要条件:

# 互斥条件
# 请求和保持条件
# 不剥夺条件
# 环路等待条件
# 处理死锁基本方法:

# 预防死锁(摒弃除1以外的条件)
# 避免死锁(银行家算法)
# 检测死锁(资源分配图)
# 解除死锁
# 剥夺资源
# 撤销进程


# 4 程序编译与链接


# Bulid过程可以分解为4个步骤:预处理(Prepressing), 编译(Compilation)、汇编(Assembly)、链接(Linking)

# 以c语言为例:

# 1 预处理

# 预编译过程主要处理那些源文件中的以“#”开始的预编译指令，主要处理规则有：

# 将所有的“#define”删除，并展开所用的宏定义
# 处理所有条件预编译指令，比如“#if”、“#ifdef”、 “#elif”、“#endif”
# 处理“#include”预编译指令，将被包含的文件插入到该编译指令的位置，注：此过程是递归进行的
# 删除所有注释
# 添加行号和文件名标识，以便于编译时编译器产生调试用的行号信息以及用于编译时产生编译错误或警告时可显示行号
# 保留所有的#pragma编译器指令。