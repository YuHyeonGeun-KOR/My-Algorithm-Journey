package BOJ;

import java.util.*;
import java.io.*;
public class BOJ_1149_RGB거리 {
	public static void main(String[] args) throws Exception {
		BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int cost[][] = new int[N+1][3];
        int input[][] = new int[N+1][3];
        
		for(int i = 1; i <= N; i++) {
            String[] temp = br.readLine().split(" ");
			for(int j = 0; j < 3; j++) {
            	input[i][j] = Integer.parseInt(temp[j]);
            }
		}
		for(int i = 1; i <= N; i++) {
			cost[i][0]  = Math.min(cost[i-1][1], cost[i-1][2]) +input[i][0];
			cost[i][1]  = Math.min(cost[i-1][0], cost[i-1][2]) +input[i][1];
			cost[i][2]  = Math.min(cost[i-1][0], cost[i-1][1]) +input[i][2];
		}
		
		System.out.println(Math.min(cost[N][0], Math.min(cost[N][1], cost[N][2])));
		
	}
 }