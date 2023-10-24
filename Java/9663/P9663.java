import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class P9663 {
    
    static int[] arr;
    static int N;
    static int depth = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String string = bufferedReader.readLine();

        N = Integer.parseInt(string);
        arr = new int[N];

        nQueen(0);
        System.out.println(depth);
    }

    private static void nQueen(int depth) {
        if (depth == N) {
            P9663.depth++;
            return;
        }
        
        for (int i = 0; i < N; i++) {
            arr[depth] = i;
            if (isPossible(depth)) {
                nQueen(depth + 1);
            }
        }
    }

    private static boolean isPossible(int column) {
        for (int i = 0; i < column; i++) {
            if (arr[i] == arr[column]) {
                return false;
            }
            else if (Math.abs(column - i) == Math.abs(arr[column] - arr[i])) {
                return false;
            }
        }
        return true;
    }
}
