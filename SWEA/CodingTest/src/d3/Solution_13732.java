package d3;
import java.util.*;
import java.io.*;
public class Solution_13732 {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		outer : for (int testcase = 1; testcase < T+1; testcase++) {
			int n = Integer.parseInt(br.readLine());
			
			String[][] board = new String[n][];
			
			for (int i = 0; i < n; i++) {
				board[i] = br.readLine().split("");
			}
			
			
			int min_x = Integer.MAX_VALUE , min_y = Integer.MAX_VALUE  , max_x = Integer.MIN_VALUE  , max_y = Integer.MIN_VALUE;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if(board[i][j].equals("#")) {
						min_x = Math.min(min_x, i);
						min_y = Math.min(min_y, j);
						max_x = Math.max(max_x, i);
						max_y = Math.max(max_y, j);
						
					}
				}
			}
			if(max_y - min_y  != max_x - min_x) {
				System.out.printf("#%d no\n" , testcase);
				continue outer;
			}
			for (int i = min_x; i < max_x+1; i++) {
				for (int j = min_y; j < max_y+1; j++) {
					if (!board[i][j].equals("#")) {
						System.out.printf("#%d no\n" , testcase);
						continue outer;
					}
				}
			}
			
			System.out.printf("#%d yes\n" , testcase);
			
			
			
			
			
		}
	}
}
