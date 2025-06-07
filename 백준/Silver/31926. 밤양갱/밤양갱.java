import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long N = Long.parseLong(st.nextToken());
        long result = 8;
        int cnt = 1;
        while (cnt < N) {
            cnt *= 2;
            result += 1;
        }
        if (cnt == N) {
            System.out.println(result+2);
        } else if (cnt > N) {
            System.out.println(result+1);
        }
    }
}