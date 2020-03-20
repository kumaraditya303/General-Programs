import java.util.Scanner;

class digitalsum 
{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number = ");
        String a = scanner.nextLine();
        int length = a.length();
        int num = Integer.parseInt(a);
        int temp = 0;
        int sum = 0;
        for (int i = 1; i <= length; i++) {
            temp = num % 10;
            num -= temp;
            num /= 10;
            sum += temp;
            temp = 0;
        }
        System.out.println("Sum of digits = " + sum);
        scanner.close();
    }
}