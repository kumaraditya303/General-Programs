import java.util.Scanner;

class end7
{
    public static void main (String args[]) {
        Scanner myObj=new Scanner(System.in);
        int num;
        int r;
        num=myObj.nextInt();
        r=num%10;
        if (r==7){
            System.out.println("End with 7");
        }           
        else
        {
            System.out.println("Not end with 7 ");
        }
        myObj.close();
        
    }
}