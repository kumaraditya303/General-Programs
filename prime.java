import java.util.*;


class prime {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int i = 0;
        int c = 0;
        for (i = 2; i < a; i++) {
            if (a % i == 0) {
                c = c + 1;
            }
        }
        if (c == 0) {
            System.out.println("Prime");
        }
        else{
            System.out.println("Composite");
        }
        sc.close();
    }
}