import java.util.Scanner;


public class calculator {
    public static void main(String[] args) {


        System.out.println("enter the two numbers");

        Scanner input = new Scanner(System.in);

         int num1 = input.nextInt();

         int num2 = input.nextInt();
         
       
         System.out.println("enter the operator");

         
        
         int ope = input.nextInt();


        if( ope == 1 ){

            int c = num1 + num2 ;
            System.out.println("sum is ="+ c);
        }
        else if(ope == 2){

            int c = num1 - num2 ;
            System.out.println("sub is ="+ c);
        }
         else if(ope == 3 ){

            int c = num1 * num2 ;
            System.out.println("mup is ="+ c);
        }
         else if(ope == 4){

            int c = num1 / num2 ;
            System.out.println("dev is ="+ c);
        }
        else{

            System.out.println("operator id not exist");
        }

     
       
      input.close();
     

        
    }

    
}
