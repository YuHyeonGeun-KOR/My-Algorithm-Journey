package d3;

import java.util.Scanner;

public class SWEA_D3_SpotMart {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int testcase = 1; testcase <= T; testcase++) {
			int result = 0;

			int n = sc.nextInt();
			int m = sc.nextInt();
			
			int[] list = new int[n];
			for (int i = 0; i < n; i++) {
				list[i] = sc.nextInt();
			}
			
			int max = 0;
			int sum = 0;
			
			
			for (int i = 0; i < list.length-1; i++) {
				for (int j = i+1; j < list.length; j++) {
					sum = list[i] + list[j];
					if(sum <= m && sum > max) {
						max = sum;
					}
				}
			}
			
			if(max == 0)result = -1;
			else result = max;
			
			System.out.println("#" + testcase + " " + result);
			
		}
	}
}
