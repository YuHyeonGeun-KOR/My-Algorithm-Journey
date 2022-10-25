package BOJ;

import java.io.*;
import java.util.*;

public class BOJ_1600_말이되고픈원숭이 {
	static int[] horseMovingDx = {-2,-1,-2,-1, 1, 2,1,2};
	static int[] horseMovingDy = {-1,-2, 1, 2,-2,-1,2,1};
	static int[] dx = {0,1,-1,0};
	static int[] dy = {1,0,0,-1};
	static int[][] board;
	static int K , W, H;
	static int[][][] visited;
	static int result;
	static class Monkey{
		int x;
		int y;
		int k;
		int time;
		public Monkey(int x , int y) {
			this.x = x;
			this.y = y;
			this.k = 0;
			this.time = 0;
		}
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		K = Integer.parseInt(br.readLine());
		
		String[] input = br.readLine().split(" ");
		
		W = Integer.parseInt(input[0]);
		H = Integer.parseInt(input[1]);
		result = Integer.MAX_VALUE;
		board = new int[H][W];
		
		for (int i = 0; i < H; i++) {
			input = br.readLine().split(" ");
			for (int j = 0; j < W; j++) {
				board[i][j] = Integer.parseInt(input[j]);
			}
		}
		visited = new int[K+1][H][W];
		play();
		
		if(result == Integer.MAX_VALUE) System.out.println(-1);
		else System.out.println(result);
		
	}
	private static void play() {
		Deque<Monkey> dq = new ArrayDeque<>();
		
		dq.add(new Monkey(0,0));
		visited[0][0][0] = 1;
		
		while(dq.size()>0) {
			Monkey m = dq.removeFirst();
			int x = m.x;
			int y = m.y;
			int k = m.k;
			int time = m.time;
			
			if(x == H-1 && y == W-1) {
				result = Math.min(result, time);
			}
			
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if(nx>=0 && nx < H && ny>=0 && ny < W) {
					if(board[nx][ny] != 1 && visited[k][nx][ny] == 0) {
						visited[k][nx][ny] = 1;
						Monkey temp = new Monkey(nx,ny);
						temp.k = k;
						temp.time = time + 1;
						dq.add(temp);
					}
				}
			}
			
			if(k < K) {
				for (int i = 0; i < 8; i++) {
					int nx = x + horseMovingDx[i];
					int ny = y + horseMovingDy[i];
					
					if(nx >= 0 && nx < H && ny >= 0 && ny < W) {
						if(board[nx][ny] != 1 && visited[k+1][nx][ny] == 0) {
							visited[k+1][nx][ny] = 1;
							Monkey temp = new Monkey(nx, ny);
							temp.k = k+1;
							temp.time = time +1;
							dq.add(temp);
						}
					}
				}
			}
			
			
			
		}
		
	}
}
