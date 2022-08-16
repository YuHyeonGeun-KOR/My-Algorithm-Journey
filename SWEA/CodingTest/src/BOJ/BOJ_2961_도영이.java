package BOJ;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ_2961_도영이 {
	static int result = Integer.MAX_VALUE;
	static List<int[]> list = new ArrayList<>();
	static int[][] input; 
	public static void com(int idx , int len) {
		if(list.size() == len) {
			check();
			return;
		}
		
		for (int i = idx; i < input.length; i++) {
			list.add(input[i]);
			com(i + 1 ,len);
			list.remove(list.size() - 1);
		}
		
	}
	
	public static void check() {
		int sin = list.get(0)[0];
		int sseun = list.get(0)[1];
		
		for (int i = 1; i < list.size(); i++) {
			sin *= list.get(i)[0]; 
			sseun += list.get(i)[1]; 
		}
		
		if(result > Math.abs(sin - sseun)) result = Math.abs(sin - sseun);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n= sc.nextInt();
		input = new int[n][2];
		
		for (int i = 0; i < n; i++) {
			input[i][0] = sc.nextInt();
			input[i][1] = sc.nextInt();
		}
		
		for (int i = 1; i < n+1; i++) {
			com(0,i);
			list.clear();
		}
		System.out.println(result);
	}
}
