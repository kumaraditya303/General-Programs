import java.util.*;
import java.math.*;
import java.lang.*;

class oddeven {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number = \t");
        int a = sc.nextInt();
        if (a % 2 == 0) {
            System.out.println("Even");
        } else {
            System.out.println("Odd");
        }
        sc.close();
    }
}
