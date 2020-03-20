import java.util.Scanner;

class digitprime {
     public static void main(String args[]) {
          Scanner scan = new Scanner(System.in);
          System.out.print("Enter a number: ");
          int num = scan.nextInt();
          int c = 0;
          while (num > 0) {
               int l = num % 10;
               for (int i = 2; i < l; i++) {
                    if (l % i == 0) {
                         c++;
                    }
               }
               if (c == 0) {
                    System.out.println(l + " is a prime number");
                    c = 0;
               } else {
                    System.out.println(l + " is a not prime number");
                    c = 0;
               }
               num /= 10;
          }
          scan.close();
     }
}