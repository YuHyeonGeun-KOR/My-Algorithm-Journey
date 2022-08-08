package d3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class SWEA_D3_농작물수확하기2 {
	public static void main(String[] args) throws Exception {

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			int n = sc.nextInt();
			int ans = 0;
			int[][] farm = new int[n][n];
			for (int i = 0; i < n; i++) {
				char[] data = sc.next().toCharArray();
				for (int j = 0; j <n; j++) {
					farm[i][j] = data[j] - '0';
				}
			}
			int center = n/2;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if(Math.abs(center - i) + Math.abs(center - j) <= center) {
						ans += farm[i][j];
					}
				}
			}
			System.out.println("#" + T + " " + ans);
		}
	}
}
