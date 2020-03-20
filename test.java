class check {

     public static void main(String args[]) {
          int x = 10;
          int y = x++ + ++x * 2 + x++;
          System.out.println(x);
          System.out.println(y);
     }
}
