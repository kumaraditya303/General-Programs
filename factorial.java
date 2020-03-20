
import java.util.*;
class ci
{
    public static void main(String args[])
    {
        Scanner obj=new Scanner(System.in);
        System.out.print("Enter a number = ");
        int a=obj.nextInt();
        long fact=1;
        int i=1;
        for(i=1;i<=a;i++)
        {
            fact*=i;
        }
        System.out.print("Factorial = "+fact);
        obj.close();

}
}