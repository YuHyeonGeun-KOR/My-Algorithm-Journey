package d3;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class SWEA_D3_농작물수확하기 {
	public static void main(String[] args) throws Exception {

		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int test_case = 1; test_case <= T; test_case++) {
			int n = Integer.parseInt(br.readLine());
			String[][] board = new String[n][];
			for (int i = 0; i < board.length; i++) {
				board[i] = br.readLine().split("");
			}
			int result = 0;
			int x = n / 2;
			int end = n;
			int start = 0;
			int index = 0;
			while (true) {
				if(index > x) break;
				
				if (index == 0) {
					for (int i = start; i < end; i++) {
						result += Integer.parseInt(board[x][i]);
					}
				}else {
					for (int i = start; i <end; i++) {
						result += Integer.parseInt(board[x+index][i]);
						result += Integer.parseInt(board[x-index][i]);
					}
				}
				end -=1;
				start +=1;
				index +=1;
			}
			System.out.println("#" + test_case + " "+ result);
		}
	}
}
