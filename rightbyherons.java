import java.util.Scanner;

class triangle
{
    public static void main(String args[]) 
    {
        Scanner myObj= new Scanner(System.in);
        double b,h,hy,s,ans;
        System.out.println("Enter base=");
        b=myObj.nextDouble();
        System.out.println("Enter height");
        h=myObj.nextDouble();
        hy=Math.sqrt(b*b+h*h);
        s=(b+h+hy)/2;
        ans=Math.sqrt(s*(s-b)*(s-h)*(s-hy));
        System.out.println(ans);
        myObj.close();
    }

}