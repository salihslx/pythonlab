 import java.util.Scanner;
public class autonumber {


    public static void main(String[] args) {

        System.out.println("enter the number");

        Scanner input = new Scanner(System.in);
         int n = input.nextInt();

         System.out.println(" ");

        

        int i = 0;
        int j = 0;

        
           if( n>100){

            System.out.println("limit is not exist"); 
           }
           else{

            for(i=0; i<n; i=i+1){
                System.out.print(i);
                System.out.print(" , ");
            }
            System.out.println("  ");

             while(j<n){
 
                j = j+2;
                System.out.print(j);
                System.out.print(" ");                                               

    
            }

            System.out.println("limit is exist");
           }                     
    }
    
}
