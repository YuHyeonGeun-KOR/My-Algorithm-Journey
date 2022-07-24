package d2;

import java.util.*;
import java.io.*;
public class Solution_2005 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		for (int test_case = 1; test_case < T+1; test_case++) {
			int N = Integer.parseInt(br.readLine());
			int[][] result = new int[N][N];
			result[0][0] = 1;
			for (int i = 1; i < N; i++) {
				for (int j = 0; j < i+1; j++) {
					if(j == 0 ||  j == i) {
						result[i][j] = 1;
					}
					else {
						result[i][j] = result[i-1][j-1] + result[i-1][j]; 
					}
				}
			}
			System.out.printf("#%d %n" , test_case);
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < i+1; j++) {
					System.out.print(result[i][j]);
					System.out.print(" ");
				}
				System.out.println();
			}
			
			
		}
	}
}
