import java.util.*;
import java.io.*;

class Solution {
	static int fcnt;
	static int fsum;
	static List<int[]> core = new ArrayList<>();
	static List<int[]> clist = new ArrayList<>();
	static boolean[] visited;
	static int[] corex;
	static int[] corey;
	static int[][] board;
	static int[][] copyBoard;
	static int N;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		for (int testcase = 1; testcase <= T; testcase++) {

			N = Integer.parseInt(br.readLine());
			board = new int[N][N];
			for (int i = 0; i < N; i++) {
				String[] temp = br.readLine().split(" ");
				for (int j = 0; j < temp.length; j++) {
					board[i][j] = Integer.parseInt(temp[j]);
					if (board[i][j] == 1 && i != 0 && i != N - 1 && j != 0 && j != N - 1) {
						core.add(new int[] { i, j });
					}
				}
			}

			visited = new boolean[core.size()];
			fcnt = Integer.MIN_VALUE;
			fsum = Integer.MAX_VALUE;
			corex = new int[core.size()];
			corey = new int[core.size()];
			for (int i = 1; i <= core.size(); i++) {
				per(0,i);
			}
			if(fsum == Integer.MAX_VALUE)fsum=0;
			System.out.println("#" + testcase + " " + fsum);
			core.clear();
			clist.clear();
		}

	}

	private static void per(int index,int size) {
		if (clist.size() == size) {
			check(0,board, 0, 0);
			return;
		}

		for (int i = index; i < core.size(); i++) {
			clist.add(core.get(i));
			per(i + 1 , size);
			clist.remove(clist.size()-1);
		}
	}

	private static void check(int cnt, int[][] board, int index, int sum) {
		if (index == clist.size()) {
			if (cnt > fcnt) {
				fcnt = cnt;
				fsum = sum;
			} else if (cnt == fcnt) {
				if (fsum >= sum)
					fsum = sum;
			}
			return;
		}
		int x = clist.get(index)[0];
		int y = clist.get(index)[1];
		int tempsum = sum;
		for (int i = 0; i < 4; i++) {
			int c = 0;
			int nx = x;
			int ny = y;
			copyBoard = copy(board);
			while (true) {
				nx += dx[i];
				ny += dy[i];
				if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
					break;
				}
				// 전선 끝까지 연결 했다면
				if (nx == N - 1 || ny == N - 1 || nx == 0 || ny == 0) {
					if (copyBoard[nx][ny] == 0) {
						copyBoard[nx][ny] = 2;
						check(cnt + 1, copyBoard, index + 1, tempsum + c + 1);
						break;
					} else
						break;
				} else {
					if (copyBoard[nx][ny] != 0)
						break;
					c += 1;
					copyBoard[nx][ny] = 2;
				}
			}
		}
	}

	private static int[][] copy(int[][] board) {
		int[][] temp = new int[N][];
		for (int i = 0; i < N; i++) {
			temp[i] = Arrays.copyOf(board[i], N);
		}
		return temp;
	}
}