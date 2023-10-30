import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class P1008 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String string = bufferedReader.readLine();
        StringTokenizer stringTokenizer = new StringTokenizer(string, " ");

        double a = Double.parseDouble(stringTokenizer.nextToken());
        double b = Double.parseDouble(stringTokenizer.nextToken());

        System.out.println(a / b);
    }
}
