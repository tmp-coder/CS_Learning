
这个任务就是检查 _start 开始的时候栈顶的所有值，


> 进入 xv6, gdb 调试
> 
> b *0x10000c (_start kernel start point)
> 
> x /24x $esp

![hw1-esp.png](./img/hw2-esp.png)

解释栈中的各个值，首先看 ```0x7d8d,0x7c4d```, 这显然是某个地址，先去 ```bootblock.asm``` 中找到这两个地址


```asm
 # Set up the stack pointer and call into C.
  movl    $start, %esp
    7c43:	bc 00 7c 00 00       	mov    $0x7c00,%esp
  call    bootmain
    7c48:	e8 ee 00 00 00       	call   7d3b <bootmain>

  # If bootmain returns (it shouldn't), trigger a Bochs
  # breakpoint if running under Bochs, then loop.
  movw    $0x8a00, %ax            # 0x8a00 -> port 0x8a00
    7c4d:	66 b8 00 8a          	mov    $0x8a00,%ax
 
```

这是栈建立的地方，也就是说栈顶在 **0x7c00**, **0x7c4d** 就是栈调用 bootmain 后的下面一条指令

继续看 bootmain

```asm

00007d3b <bootmain>:
{
    7d3b:	55                   	push   %ebp
    7d3c:	89 e5                	mov    %esp,%ebp
    7d3e:	57                   	push   %edi
    7d3f:	56                   	push   %esi
    7d40:	53                   	push   %ebx
    7d41:	83 ec 0c             	sub    $0xc,%esp
  readseg((uchar*)elf, 4096, 0);
    7d44:	6a 00                	push   $0x0
    7d46:	68 00 10 00 00       	push   $0x1000
    7d4b:	68 00 00 01 00       	push   $0x10000
```

栈建立好后压了很多 reg 值进去，就是那些 0

然后
我们在文件中搜索 7d8d,会发现是 ```entry``` 下面一条指令

```asm
//.bootblock.asm : line 322
entry();
    7d87:	ff 15 18 00 01 00    	call   *0x10018
    7d8d:	eb d5                	jmp    7d64 <bootmain+0x29>
```

所以整个栈的值解释如下



```
ox7c00 : 0x00007c4d # bootmain hou mian yitiao dizhi
       : 0x00000000 #
       :
       :
       :
       :
       :
       :
0x7bdc : 0x00007d8d # kernel hou de dizhi
```