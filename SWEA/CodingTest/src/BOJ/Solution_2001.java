package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution_2001 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int testcase = 1; testcase < T + 1; testcase++) {
			
			String[] input = br.readLine().split(" ");
			int n = Integer.parseInt(input[0]);
			int m = Integer.parseInt(input[1]);
			
			
			String[][] board = new String[n][];
			int result = 0;
 			for (int i = 0; i < n; i++) {
				board[i] = br.readLine().split(" ");
			}
			
			int[][] sumBoard = new int[n][n+1];
			
			for (int i = 0; i < n; i++) {
				for (int j = 1; j < n+1; j++) {
					sumBoard[i][j] = sumBoard[i][j-1] + Integer.parseInt(board[i][j-1]);
				}
			}
			
//			for (int i = 0; i < sumBoard.length; i++) {
//				System.out.println(Arrays.toString(sumBoard[i]));
//			}
			
			for (int i = 0; i < n-m+1; i++) { //4
				for (int j = 0; j < n-m+1; j++) {
//					System.out.printf("%d %d\n",sumBoard[i][j+m] - sumBoard[i][j] , sumBoard[i+1][j+m] -sumBoard[i+1][j]);
					int temp =0;
					for (int j2 = 0; j2 < m; j2++) {
						temp += sumBoard[i+j2][j+m] - sumBoard[i+j2][j];
					}
					result = Math.max(result , temp);
				}
			}
			System.out.println("#" + testcase + " " + result);
		}
		
	}
}
