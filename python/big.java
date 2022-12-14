import java.util.Scanner;
public class big {

    public static void main(String[] args) {
        System.out.println("enter the 3 numbers");
        Scanner input = new Scanner(System.in);

        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();

        if(a>b){

            if(a>c){
                System.out.println( a +" is biggest");
            }
            else{
                System.out.println( c +" is biggest");
            }

        }
        else if(b>a){

            if(b>c){
                System.out.println( b +" is biggest");
            }
            else{
                System.out.println( c +" is biggest");
            }

        }



        }
    }
    

