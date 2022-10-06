package BOJ;

import java.io.*;
import java.util.*;

public class BOJ_9205_맥주마시면서걸어가기 {
	
	static class Position {
		int x;
		int y;

		Position(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	static int[][] distance;
	static ArrayList<Position> p_list;
	static int N;
	static int[][] visited;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int testcase = 0; testcase < T; testcase++) {

			N = Integer.parseInt(br.readLine());
			p_list = new ArrayList<>();
			distance = new int[N + 2][N + 2];
			visited = new int[N+2][N+2];

			for (int i = 0; i < N + 2; i++) {
				String[] input = br.readLine().split(" ");
				p_list.add(new Position(Integer.parseInt(input[0]), Integer.parseInt(input[1])));
			}

			for (int i = 0; i < N + 2; i++) {
				for (int j = 0; j < N + 2; j++) {
					int d = Math.abs(p_list.get(i).x - p_list.get(j).x) + Math.abs(p_list.get(i).y - p_list.get(j).y);
					distance[i][j] = d;
				}
			}
			
			
			
			floid();
			
			if(distance[0][N+1] <= 1000) System.out.println("happy");
			else System.out.println("sad");
			
		}

	}

	public static void floid() {
		for (int k = 0; k < N + 2; k++) {
			for (int i = 0; i < N + 2; i++) {
				for (int j = 0; j < N + 2; j++) {
					if (distance[i][k]  <= 1000 && distance[k][j] <= 1000) {
						distance[i][j] = 1000;
					}
				}
			}
		}
	}
}
