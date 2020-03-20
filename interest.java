import java.util.Scanner;
class MyClass{
    public static void main(String args[]){
        Scanner myObj =new Scanner(System.in);
        int p;
        double r;
        int t;
        double si;
        double amt;
        System.out.print("Enter Principal =\t");
        p=myObj.nextInt();
        System.out.print("Enter Rate% =\t");
        r=myObj.nextDouble();
        System.out.print("Enter Time =\t");
        t=myObj.nextInt();
        myObj.close();
        si=p*r*t/100;
        amt=si+p;
        System.out.println("Simple Interest ="+si);
        System.out.println("Amount ="+amt);
    }
}