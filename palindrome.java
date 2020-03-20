import java.util.*;

class palindrome {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number:");
        int num = scan.nextInt();
        int a=num;
        int r = 0;
        int temp = 0;
        while (num > 0) {
            temp = num % 10;
            r = r * 10 + temp;
            num /= 10;
        }
        if (r == a)
            System.out.println("Palindrome");
        else
            System.out.println("Not Palindrome");
        scan.close();

    }
}