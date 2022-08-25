package swtest;


import java.util.*;
import java.io.*;
public class SWEA_2117_홍방범서비스 {
	static int[][] board;
	static int result;
	static int homecnt;
	static int n,m;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static int[][] visited;
	static Deque<int[]> dq = new ArrayDeque<>();
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int testcase = 1; testcase <= T; testcase++) {
			String[] input = br.readLine().split(" ");
			n= Integer.parseInt(input[0]);
			m= Integer.parseInt(input[1]);
			int k = m;
			board= new int[n][n];
			int breakcnt = 0;
			for (int i = 0; i < n; i++) {
				String[] temp = br.readLine().split(" ");
				for (int j = 0; j < temp.length; j++) {
					board[i][j] = Integer.parseInt(temp[j]);
					if(board[i][j] == 1) breakcnt +=1;
				}
				
			}
			
			result = Integer.MIN_VALUE;
			for (int l = 1; l < 2 * n; l++) {
				homecnt = Integer.MIN_VALUE;
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						homecnt = Math.max(homecnt, check(i,j,l));
						if(homecnt == breakcnt) break;
					}
				}
				if(homecnt * m - (l * l + (l - 1) * (l - 1)) >= 0) {
					result = Math.max(homecnt, result);
				} 
				
				
			}
			System.out.println("#" + testcase + " " + result);
			
		}
	}
	private static int check(int i, int j, int l) {
		dq.add(new int[] {i,j});
		visited = new int[n][n];
		visited[i][j] =1;
		int cnt = 0;
		if(board[i][j] == 1) cnt +=1; 
		while(dq.size()> 0){
			int[] now = dq.removeFirst();
			
			for (int d = 0; d < 4; d++) {
				int nx = now[0] + dx[d];
				int ny = now[1] + dy[d];
				
				if(nx >= 0 && nx <n && ny>=0 && ny < n && visited[nx][ny] == 0) {
					if(Math.abs(nx - i) + Math.abs(ny-j) < l) {
						dq.addLast(new int[] {nx, ny});
						visited[nx][ny] = 1;
						if(board[nx][ny] == 1) cnt +=1;
					}
				}
			}
		}
		dq.clear();
		return cnt;
	}
}
