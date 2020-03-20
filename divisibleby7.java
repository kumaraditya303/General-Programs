import java.util.Scanner;
class divisibleby7
{
    public static void main(String args[])
    {
        Scanner myObj= new Scanner(System.in);
        int num;
        num=myObj.nextInt();
        if(num%7==0)
        {
            System.out.println("Divisible");
        }
        else
        {
            System.out.println("Indivisible");
        }
        myObj.close();
    }
}