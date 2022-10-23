package BOJ;

import java.io.*;
import java.util.*;

public class BOJ_1956_운동 {
    static int V, E;
    static int[][] distance;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        V = sc.nextInt();
        E = sc.nextInt();
        distance = new int[V+1][V+1];
        for (int i = 0; i < V+1; i++) {
            Arrays.fill(distance[i], 9999999);
        }

        for (int i = 0; i < E; i++) {
            int left = sc.nextInt();
            int right = sc.nextInt();
            int cost = sc.nextInt();

            distance[left][right] = cost;

        }


        for (int k = 1; k <= V; k++) {
            for (int i = 1; i <= V; i++) {
                for (int j = 1; j <= V; j++) {
                    if(distance[i][k] + distance[k][j] < distance[i][j]){
                        distance[i][j] = distance[i][k] + distance[k][j];
                    }
                }
            }
        }

        int result = 9999999;
        for (int i = 1; i <= V; i++) {
            for (int j = 1; j <= V; j++) {
                if(i == j) result = Math.min(result , distance[i][j]);
                else if(distance[i][j] != 9999999 && distance[j][i] != 9999999){
                    result = Math.min(result , distance[i][j] + distance[j][i]);
                }
            }
        }

        if(result == 9999999) System.out.println(-1);
        else System.out.println(result);

    }
}
