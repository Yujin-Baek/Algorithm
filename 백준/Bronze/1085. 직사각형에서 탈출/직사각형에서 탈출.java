import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        int w = sc.nextInt();
        int h = sc.nextInt();
        
        int half1 = w/2;
        int half2 = h/2;
        
        int result1 = w - x;
        int result2 = h - y;
        
        if(half1<result1)
            result1 = x;
        
        if(half2<result2)
            result2 = y;
        
        if(result1<result2)
            System.out.println(result1);
        else
            System.out.println(result2);
        
        sc.close();
    }

}