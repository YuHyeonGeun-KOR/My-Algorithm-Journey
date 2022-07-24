package d2;

import java.util.*;
import java.io.*;
public class Solution_14413 {
	public static void main(String[] args) throws Exception{
		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine()); 
		
		int[] dx = {0,0,1,-1};
		int[] dy = {1,-1,0,0};
		outer : for (int testcase = 1; testcase < T + 1; testcase++) {
			String[] input = br.readLine().split(" ");
			int n = Integer.parseInt(input[0]);
			int m = Integer.parseInt(input[1]);
			
			
			char[][]  board = new char[n][];
			
			for (int i = 0; i < n; i++) {
				board[i] = br.readLine().toCharArray();
			}
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if(board[i][j] == '#') {
						for (int d = 0; d < 4; d++) {
							int nx = i + dx[d];
							int ny = j + dy[d];
							
							if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
							else{
								if(board[nx][ny] == '#') {
									System.out.printf("#%d impossible\n" , testcase);
									continue outer;
								}
								else if(board[nx][ny] == '?') {
									board[nx][ny] = '.';
								}
							}
							
						}
					
					}else if(board[i][j] == '.') {
						for (int d = 0; d < 4; d++) {
							int nx = i + dx[d];
							int ny = j + dy[d];
							
							if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
							else{
								if(board[nx][ny] == '.') {
									System.out.printf("#%d impossible\n" , testcase);
									continue outer;
								}else if(board[nx][ny] == '?') {
									board[nx][ny] = '#';
								}
							}
							
						}
					
					}
					
				}
			}
			System.out.printf("#%d possible\n" , testcase);
		}
		
	}
}
