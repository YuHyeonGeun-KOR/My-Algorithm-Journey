package BOJ;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class BOJ_N과M3 {
	static List<Integer> arr = new ArrayList<>();
	
	static int[] visited;
	static int n;
	static int m;
	public static StringBuilder sb = new StringBuilder();
	public static void com() {
		if (arr.size() == m) {

			for (int i = 0; i < m; i++) {
				sb.append(arr.get(i)).append(' ');
			}
			sb.append('\n');
			return;
		}

		for (int i = 1; i < n + 1; i++) {
			
				arr.add(i);
				com();
				arr.remove(arr.size() - 1);
			
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();
		com();
		System.out.println(sb);
	}
}
