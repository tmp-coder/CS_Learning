
这是课件3,关于GDB内容的整理,一些常用指令: ```c,si,n,b```就不说了

- finish runs code until the current function returns.
- advance \<location> runs code until the instruction pointer gets to the specied location.
- Modify breakpoints using delete, disable, enable.
- break \<location> if \<condition> sets a breakpoint at the specied location, but only breaks if the condition is satised. 
- cond <number> <condition> adds a condition on an existing breakpoint.
- watch \<expression> will stop execution whenever the expression's value changes.
- watch -l \<address> will stop execution whenever the contents of the specied memory address change.
- info frame prints the current stack frame.
- list <location> prints the source code of the function at the specied location.
- backtrace might be useful as you work on lab 1!

更多内容可见 help
or [gdb_slides.pdf](../lec/gdb_slides.pdf)

