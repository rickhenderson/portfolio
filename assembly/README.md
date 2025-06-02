# Learning & Using Assembly

Assembly is the cornerstone of binary reverse engineering, and it's fun too!

Except, it can be incredibly hard to learn.

I was exploring different ways of learning assembly because many reverse engineering tutorials jump right into debugging without much understanding of assembly language and I believe that puts analysts at a disadvantage. In addition, learning assembly can lead to exploit development if you want to expand your skill set.

I came up with a simple prompt for Claude.ai after struggling with trying to get started with the Paul Carter PC assembly book:

```
You are an educational professional. You have studied learning and curriculum design. How would you teach a person to program in assembly for the first time?
```

The response from Claude Sonnet 4 was clear, and used good instructional design principles by basing the lesson on familiar concepts.

Here is a link to the completed less using NASM. I was using Linux (Remnux) and NASM but it is not mentioned in the writeup.

* [x86 Assembly Addition Program with NASM](https://claude.ai/public/artifacts/a70d066c-24ab-45a4-b936-8e6cfd136b95)

I followed up with a prompt to include displaying the result on the screen because the initial program doesn't produce output.

```
Add as little code as possible to output the value of result to the console in linux
```

The resulting program allowed me to see how text was written to standard output, and a provided an interesting way to quickly convert numbers from 0-9 to their ASCII representation to make the output simpler!

Next, I wanted text output:

```
Write a simple assembly program to display text on the screen. The text should be: "You stand at the edge of a dark forest. There is a faint path to the north leading to  a warm glow, and a well-worn path leading to the east into the unseen forest."
```

I was very impressed that Claude commented on my writing:

---
This simple assembly program displays your atmospheric text on the screen. Here's how it works:
**Key elements:**

* `text db '...'` defines the string as a sequence of bytes
* The `10` at the end is the newline character (ASCII 10)
* `text_len equ $ - text - 1` calculates the string length automatically
* System call 4 (sys_write) outputs the text to stdout
* System call 1 (sys_exit) cleanly terminates the program

**To assemble and run:**

```bash
nasm -f elf32 textdisplay.asm -o textdisplay.o
ld -m elf_i386 textdisplay.o -o textdisplay
./textdisplay
```

The program will display your evocative forest scene text and exit. This demonstrates the fundamental pattern for text output in assembly - defining the string data, setting up the system call parameters, and invoking the kernel to handle the actual display.
Perfect for the beginning of a text adventure game written in assembly!

---

I worked with the code for a few minutes to write more than 1 line to the screen, then got Claude to produce a second basic lesson to include loops, so now I can create loops in assembly!

* [Lesson 2: x86 Assembly Looping Lesson - Multiple String Output](https://claude.ai/public/artifacts/e072b5a5-f397-41a4-b0b3-158085f8b18a)

An easy addition is given by Claude at the end of the lesson, but another addition would be to include the original paragraph describing the scenario. Another addition I'd like to make is using a function/loop to calculate the length of each string instead of storing it as a seperate varialble.
