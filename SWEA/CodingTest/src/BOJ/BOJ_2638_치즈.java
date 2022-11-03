package BOJ;

import java.io.*;
import java.util.*;
public class BOJ_2638_치즈 {
	static int N , M;
	static int[][] board;
	static int[][] cboard;
	static int time = 0;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	static ArrayList<int[]> mList ;
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]);
		M = Integer.parseInt(input[1]);
		
		
		board = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			input = br.readLine().split(" ");
			for (int j = 0; j < input.length; j++) {
				board[i][j] = Integer.parseInt(input[j]);
			}
		}
		
		play();
		System.out.println(time);
	}
	private static void play() {
		
		while(true) {
			
			
			//바깥 처리 해주기
			makeOut();
			
			
			//녹일 애들 후보
			mList = new ArrayList<>();
			findStart();
			
			//녹일 애들이 있으면 확인
			if(mList.size()>0) {
				melt();	
				time +=1;
			}
			else {
				return;
			}
			// 되돌리기
			rollback();
			mList.clear();
		}
		
		
	}
	
	private static void rollback() {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				if(board[i][j] == 5) board[i][j] = 0;
			}
		}
	}
	private static void melt() {
		for (int i = 0; i < mList.size(); i++) {
			int cnt = 0 ;
			int[] now = mList.get(i);
			int x = now[0];
			int y = now[1];
			for (int d = 0; d <4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				
				if(nx>=0 && nx < N && ny >=0 && ny < M && board[nx][ny] == 5) {
					cnt +=1;
				}
				
			}
			if(cnt >= 2) {
				board[x][y] = 0; 
			}
		}
		
	}
	private static void findStart() {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				if(board[i][j] == 1) mList.add(new int[] {i,j});
			}
		}
	}
	private static void makeOut() {
		Deque<int[]> dq = new ArrayDeque<>();
		dq.add(new int[] {0,0});
		
		while(dq.size()>0) {
			int[] now = dq.removeFirst();
			int x = now[0];
			int y = now[1];
			
			for (int d = 0; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				
				if(nx>=0 && nx < N && ny >=0 && ny < M && board[nx][ny] == 0) {
					board[nx][ny] = 5;
					dq.add(new int[] {nx,ny});
				}
			}
		}
	}
	private static void showBoard() {
		for (int i = 0; i < board.length; i++) {
			System.out.println(Arrays.toString(board[i]));
		}
		System.out.println();
	}
}
