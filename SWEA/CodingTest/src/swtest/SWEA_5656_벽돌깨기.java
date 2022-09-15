package swtest;

import java.io.*;
import java.util.*;

public class SWEA_5656_벽돌깨기 {
	static int N, W, H;
	static int[][] board;
	static int[] dx = { 0, -1, 0, 1 };
	static int[] dy = { 1, 0, -1, 0 };
	static List<Integer> c_list = new ArrayList<>();
	static Deque<int[]> dq = new ArrayDeque<>();

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int testcase = 1; testcase <= T; testcase++) {
			String[] input = br.readLine().split(" ");

			N = Integer.parseInt(input[0]);
			W = Integer.parseInt(input[1]);
			H = Integer.parseInt(input[2]);

			board = new int[H][W];

			for (int i = 0; i < H; i++) {
				String[] temp = br.readLine().split(" ");
				for (int j = 0; j < W; j++) {
					board[i][j] = Integer.parseInt(temp[j]);
				}
			}

//			com();
			play();
		}

	}

	private static void com() {
		if (c_list.size() == N) {
			play();
			System.out.println(Arrays.toString(c_list.toArray()));
			return;
		}

		for (int i = 0; i < W; i++) {
			c_list.add(i);
			com();
			c_list.remove(c_list.size() - 1);
		}
	}

	private static void play() {
		// TODO Auto-generated method stub
		int[][] cboard = copy();
		int[][] visited = new int[H][W];
		c_list.add(1);
		for (int i = 0; i < c_list.size(); i++) {
			int[] start = find(c_list.get(i), cboard);
			if (start[0] == -1)
				continue;
			dq.add(new int[] {1,2,1});
			
			while (dq.size() > 0) {

				int[] now = dq.removeFirst();
				int x = now[0];
				int y = now[1];
				int b = now[2];
				visited[x][y] = 1;
				if (b == 1) {
					cboard[x][y] = 0;
					continue;
				}

				for (int k = 0; k < 4; k++) {
					int nx = 0;
					int ny = 0;
					for (int d = 0; d < cboard[x][y]; d++) {
						nx = x + dx[k]*d;
						ny = y + dy[k]*d;
						if(nx >=0 && nx < H && ny>=0 && ny < W && visited[nx][ny] ==0 && cboard[nx][ny] > 0) {
							visited[nx][nx] = 1;
							dq.add(new int[] {nx,ny,cboard[nx][ny]});
							cboard[nx][ny] = 0;
						} 
					}
				}
			}
			
			c_list.add(1);
			for (int[] j : cboard) {
				System.out.println(Arrays.toString(j));
			}
			System.out.println();
			
		}
	}

	private static int[] find(int w, int[][] cboard) {
		for (int i = 0; i < H; i++) {
			if (cboard[i][w] != 0)
				return new int[] { i, w , cboard[i][w] };
		}
		return new int[] { -1, -1 };
	}

	private static int[][] copy() {
		int[][] c = new int[H][];
		for (int i = 0; i < H; i++) {
			c[i] = Arrays.copyOf(board[i], W);
		}
		return c;
	}
}
