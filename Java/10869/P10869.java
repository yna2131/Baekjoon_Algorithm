import java.util.Scanner;

public class P10869 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int A = input.nextInt();
        int B = input.nextInt();

        System.out.println(A+B);
        System.out.println(A-B);
        System.out.println(A*B);
        System.out.println(A/B);
        System.out.println(A%B);

        input.close();
    }
}
