package swtest;

import java.util.Arrays;
import java.util.Scanner;

public class SWEA_5653_줄기세포배양2 {
	static class cell {
		int time, lifePower;
		boolean flag;

		public cell(int time, int lifePower) {
			super();
			this.time = time;
			this.lifePower = lifePower;
			this.flag = false;
		}

	}

	static cell[][] cBoard;
	static cell[][] copyBoard;
	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { 1, -1, 0, 0 };
	static int len = 375;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		StringBuilder sb = new StringBuilder();
		for (int testcase = 1; testcase < T + 1; testcase++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			int k = sc.nextInt();
			cBoard = new cell[len][len];
			copyBoard = new cell[len][len];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					int l = sc.nextInt();
					if (l != 0) {
						cBoard[i + len / 2][j + len / 2] = new cell(0, l);
						copyBoard[i + len / 2][j + len / 2] = new cell(0, l);
					}
				}
			}
			for (int i = 0; i < k + 1; i++) {
				for (int x = 0; x < len; x++) {
					for (int y = 0; y < len; y++) {
						if (cBoard[x][y] != null) {
							if (cBoard[x][y].time <= cBoard[x][y].lifePower *2)cBoard[x][y].time += 1;
							if (cBoard[x][y].time == cBoard[x][y].lifePower + 1) {
								for (int d = 0; d < 4; d++) {
									int nx = x + dx[d];
									int ny = y + dy[d];

									if (copyBoard[nx][ny] == null) {
										copyBoard[nx][ny] = new cell(0, copyBoard[x][y].lifePower);
									} else if (copyBoard[nx][ny] != null) {
										if (copyBoard[nx][ny].flag == false
												&& copyBoard[nx][ny].lifePower < copyBoard[x][y].lifePower) {
											copyBoard[nx][ny] = new cell(0, copyBoard[x][y].lifePower);
										}
									}
								}

							}

						}
					}
				}
				for (int x = 0; x < len; x++) {
					for (int y = 0; y < len; y++) {
						if (copyBoard[x][y] != null) {
							copyBoard[x][y].flag = true;
						}
					}
				}
				copy();

			}
//				for (cell[] C : cBoard) {
//					for (cell c : C) {
//						if (c != null)
//							System.out.print(c.lifePower + " ");
//						else
//							System.out.print("  ");
//					}
//					System.out.println();
//				}

			int answer = 0;
			for (cell[] C : cBoard) {
				for (cell c : C) {
					if (c != null && c.time < c.lifePower*2)
						answer += 1;
				}

			}
			sb.append("#").append(testcase).append(" ").append(answer).append("\n");
		}
		System.out.println(sb);
	}

	private static void copy() {
		for (int i = 0; i < len; i++) {
			cBoard[i] = Arrays.copyOf(copyBoard[i], len);
		}
	}
}
