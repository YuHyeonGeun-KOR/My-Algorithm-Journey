package BOJ;

import java.io.*;
import java.util.*;

/*
 * 7 9 7 30 2 7 9 25
 * 
 * 7 9 7 30 
 * 
 * [7 2] [9 1 ] [30 1]
 * 
 * */
public class BOJ_2531_회전초밥 {
	static int N, D, K, C;
	static int start, end;
	static int[] board;
	static int result = Integer.MIN_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]);
		D = Integer.parseInt(input[1]);
		K = Integer.parseInt(input[2]);
		C = Integer.parseInt(input[3]);

		board = new int[N+K];
		for (int i = 0; i < N; i++) {
			board[i] = Integer.parseInt(br.readLine());
		}
		for (int i = N; i < N+K; i++) {
			board[i] = board[i-N];
		}
		end = start + K -1;
		check();
		System.out.println(result);

	}

	private static void check() {
		while (true) {
			if (end == N+K)
				break;

			Set<Integer> set = new HashSet<>();
			for (int i = start; i <= end; i++) {
				set.add(board[i]);
			}

			if (!set.contains(C)) {
				result = Math.max(result, set.size() + 1);
			} else {
				result = Math.max(result, set.size());
			}

			start += 1;
			end += 1;
		}
	}
}
