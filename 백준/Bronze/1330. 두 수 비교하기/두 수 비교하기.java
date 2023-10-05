import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int a,b;
        
        Scanner sc = new Scanner(System.in);
        
        a = sc.nextInt();
        b = sc.nextInt();
        
        if(a>b) {
            System.out.println('>');
        }else if(a==b) {
            System.out.println("==");
        }else {
            System.out.println('<');
        }
        sc.close();
        //if조건문 쓸 때 {} 안 써도 되는 이유?
        //모두 지워봐도 에러 발생하지 않음
        
    }

}