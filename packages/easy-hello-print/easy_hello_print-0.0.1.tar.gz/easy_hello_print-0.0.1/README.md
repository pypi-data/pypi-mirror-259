这是个有趣的包，
输入语言，就能返回对应hello world的写法
比如：
ch=Choose()
ch.choose="c"
ch.print_data()

result:
#include<stdio.h>
    int main(void) {
        printf("Hello World!
");
        return 0;
}

ch=Choose()
ch.choose="java"
ch.print_data()

result:
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
