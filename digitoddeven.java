import java.util.Scanner;

class digitoddeven {
     public static void main(String args[]) {
          Scanner scan = new Scanner(System.in);
          System.out.print("Enter a number: ");
          int num = scan.nextInt();
          while (num > 0) {
               int c = num % 10;
               if (c % 2 == 0) {
                    System.out.println(c + " is a even number");

               } else {
                    System.out.println(c + " is a not odd number");
               }

               num /= 10;
          }
          scan.close();
     }

}
