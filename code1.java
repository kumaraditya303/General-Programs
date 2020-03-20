import java.util.*;

class table {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        for (int i = 1; i <= 10; i++) {
            System.out.println(a + " x " + i + " = " + (i * a));
        }
        scanner.close();
    }
}