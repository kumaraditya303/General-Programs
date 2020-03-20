import java.util.Scanner;
class perfect {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = scan.nextInt();
        int c = 0;
        for (int i = 1; i < num; i++) {
            c += i;
        }
        if (c == num) {
            System.out.println(num + " is a Perfect Number.");
        }
        else{
            System.out.println(num+" is not a Prime Number.");
        }
        scan.close();
    }
}