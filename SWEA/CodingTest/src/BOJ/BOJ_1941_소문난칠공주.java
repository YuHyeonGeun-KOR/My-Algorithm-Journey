package BOJ;

import java.io.*;
import java.util.*;

public class BOJ_1941_소문난칠공주 {
	static char[][] board = new char[5][5];
	static int[] dx = {0,1,-1,0};
	static int[] dy = {1,0,0,-1};
	static int result = 0;
	static List<Integer> clist = new ArrayList<>();
	static int[][] posi = new int[25][];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int i = 0; i < 5; i++) {
			String[] input = br.readLine().split("");
			for (int j = 0; j < 5; j++) {
				board[i][j] = input[j].charAt(0);
			}
		}
		int index = 0;
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				posi[index] = new int[] { i, j };
				index += 1;
			}
		}

		com(0);
		System.out.println(result);
	}

	private static void com(int index) {
		if (clist.size() == 7) {
			play();
			return;
		}

		for (int i = index; i < 25; i++) {
			clist.add(i);
			com(i + 1);
			clist.remove(clist.size() - 1);
		}
	}

	private static void play() {
		if (isOK()) {
			int slen = 0;
			int ylen = 0;
			for (int i = 0; i < 7; i++) {
				int x = posi[clist.get(i)][0];
				int y = posi[clist.get(i)][1];

				if (board[x][y] == 'Y')
					ylen += 1;
				if (board[x][y] == 'S')
					slen += 1;
			}

			if (ylen >= 4)
				return;
			if (slen >= 4)
				result += 1;
		}
	}

	private static boolean isOK() {
		int cnt = 0;
		int[][] t = new int[5][5];
		
		int x = 0;
		int y = 0;
		for (int i = 0; i < 7; i++) {
			x = posi[clist.get(i)][0];
			y = posi[clist.get(i)][1];	
			
			t[x][y] = 1;
		}
		
		Deque<int[]> dq = new ArrayDeque<>();
		
		dq.add(new int[] {x,y});
		
		while(dq.size()> 0) {
			int[] now = dq.removeFirst();
			
			int xx = now[0];
			int yy = now[1];
			
			for (int i = 0; i < 4; i++) {
				int nx = xx + dx[i];
				int ny = yy + dy[i];
				
				if(nx>=0 && nx < 5 && ny >=0 && ny < 5) {
					if(t[nx][ny] == 1) {
						t[nx][ny] +=1;
						cnt +=1;
						dq.add(new int[] {nx,ny});
					}
				}
			}
		}
		
		if(cnt == 7) return true;
		return false;
		
	}
}
