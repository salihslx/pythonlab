import java.util.Scanner;

public class average {

    public static void main(String[] args) {
        
         System.out.println("enter the three numebrs");

         Scanner input = new Scanner(System.in);

         int num1 = input.nextInt();
         int num2 = input.nextInt();
         int num3 = input.nextInt();

         int sum = num1 + num2 + num3;
         int avg = sum/3;

         System.out.println("average of the number = " +avg);

         input.close();
    }
    
}
