import java.util.Scanner;


class su {
    
    public static void main(String[] args) {
        
        System.out.println("enter the two number");

        Scanner input = new Scanner(System.in);
        int num1 = input.nextInt();
       
         int num2 = input.nextInt();


         int sum  = num1 + num2 ;

        System.out .println("sum of the two numbers ="+sum);
    }
}
