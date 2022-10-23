package BOJ;
import java.io.*;
import java.util.*;
public class BOJ_1976_여행가자 {
    
    static int N , M;
    static int[] p;
    static int[][] join;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        join = new int[N+1][N+1];

        for(int i =1 ; i<= N; i++){
            for (int j =1; j<= N; j++){
                join[i][j] = sc.nextInt();
            }

        }

        make();
        for  (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if(join[i][j]== 1){
                    union(i,j);
                }
            }
        }

        int[] input = new int[M];
        for (int i = 0; i < M; i++) {
            input[i] = sc.nextInt();
        }

      
        for (int i = 1; i < M; i++) {
            if(find(input[i]) != find(input[i-1])) {
                System.out.println("NO");
                return;
            }
        }

        System.out.println("YES");
    }

    //각각의 부모를 찾는다
    //만약 부모가 같으면 하나의 집합
    //부모가 다르면 작은쪽으로 맞춰준다.
    private static void union(int a, int b) {
        a = find(a);
        b = find(b);

        if(a == b) return;
        p[b] = a;
    }

    // 자기 자신이 부모면 자신을 리턴
    // 만약 다른 값이라면 부모를 끝까지 찾아 올라감
    // 내려오면서 부모로 초기화하면서 내려옴
    private static int find(int a) {
        if(p[a] ==a )return a;
        return p[a] = find(p[a]);
    }
    // 일단 자기자신을 부모로 설정
    public static void make(){
        p = new int[N+1];
        for(int i =1; i<=N; i++){
            p[i] = i;
        }
    }
}
