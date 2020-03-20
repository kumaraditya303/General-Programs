import java.util.Scanner;

class number
{
    public static void main(String args[])
    {
        Scanner myObj =new Scanner(System.in);
        System.out.print("Enter the number =");
        int num;
        num=myObj.nextInt();
        if(num>=0)
        {
            System.out.println("Positive number");
        }
        else
        {
            System.out.println("Negative number");
        }
        myObj.close();
    }
}