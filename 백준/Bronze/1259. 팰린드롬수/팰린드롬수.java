import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while(true) {
            int n = sc.nextInt();
            if(n==0) {
                break;
            } else {
                String n2 = String.valueOf(n);
                
                int index = n2.length()/2-1;
                
                if(n2.length()%2==1) {
                    int index2 = n2.length()/2+1;
                    
                    String s1 = n2.substring(0, index+1);
                    StringBuilder sb = new StringBuilder(n2.substring(index2));
                    String s2 = sb.reverse().toString();
                    
                    if(s1.equals(s2))
                        System.out.println("yes");
                    else
                        System.out.println("no");
                } else {
                    String s1 = n2.substring(0, index+1);
                    StringBuilder sb = new StringBuilder(n2.substring(index+1));
                    String s2 = sb.reverse().toString();
                    
                    if(s1.equals(s2))
                        System.out.println("yes");
                    else
                        System.out.println("no");
                }
            }
        }
        sc.close();
    }
}