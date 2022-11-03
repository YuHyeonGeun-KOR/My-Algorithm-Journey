package BOJ;

import java.io.*;
import java.util.*;

public class BOJ_17825_주사위윳놀이 {
	static int[][] board = new int[2][41];
	static int[] dice = new int[10];
	static List<Horse> list = new ArrayList<>();
	static int result = 0;

	static class Horse {
		int posi;
		int sum;
		int rule;

		public Horse(int posi, int sum) {
			this.posi = posi;
			this.sum = sum;
			this.rule = 0;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] input = br.readLine().split(" ");

		for (int i = 0; i < input.length; i++) {
			dice[i] = Integer.parseInt(input[i]);
		}

		for (int i = 0; i < 4; i++) {
			list.add(new Horse(0, 0));
		}

		play(0);
		System.out.println(result);

	}

	private static void play(int step) {
		if (step == 10) {
			calculate();
			return;
		}

		int now = dice[step];

		for (int i = 0; i < 4; i++) {
			int rule = list.get(i).rule;
			int prev = list.get(i).posi;
			int sum = list.get(i).sum;
			boolean flag = false;
			boolean flag2 = false;
			if (prev == 41)
				continue;
			int next = Cango(rule, i, now);
			if (next != -1 && next != 41) {
				// 이동 시켜보고
				list.get(i).posi = next;
				// 이전이 10rule 이었는데 25를 넘어가면 룰 25로 바꿔주고
				if (rule == 10) {
					if (next >= 25) {
						list.get(i).rule = 25;
					}
					flag2 = true;
				}
				else if (rule == 20 ) {
					if (next >= 25) {
						list.get(i).rule = 25;
					}
					flag2 = true;
				}

				else if (rule == 30 ) {
					if(next == 25 || next == 30 || next == 35 || next == 40)
					list.get(i).rule = 25;
					flag2 = true;
				}
				
				else if(rule == 25) {
					list.get(i).rule = 25;
					flag2 = true;
				}
				
				if(flag2 == false && (next == 10 || next == 20 || next == 30 || next == 25)) {
					list.get(i).rule = next;
					flag = true;
				}
				
				if(flag2) {
					board[1][prev] = 0;
					board[1][next] = 1;
				}
				else {
					// 방문체크하고
					if (flag) {
						board[0][prev] = 0;
						board[1][next] = 1;
					} else {
						board[0][prev] = 0;
						board[0][next] = 1;
					}
				}
				// 더해주고
				list.get(i).sum = sum + next;
				// 다음꺼로 넘기고
				play(step + 1);
				// 되돌리기
				if(flag2) {
					board[1][prev] = 1;
					board[1][next] = 0;
				}else {
					if (flag) {
						board[0][prev] = 1;
						board[1][next] = 0;
					} else {
						board[0][prev] = 1;
						board[0][next] = 0;
					}
				}
				list.get(i).sum = sum;
				list.get(i).posi = prev;
				list.get(i).rule = rule;
			} else if (next == 41) {
				list.get(i).posi = 41;
				play(step + 1);
				list.get(i).posi = prev;
			} else if(next == -1)
				continue;
		}
	}

	private static int Cango(int rule, int horseIndex, int dice) {

		Horse horse = list.get(horseIndex);
		if (rule == 0) {
			int next = horse.posi + dice * 2;
			// 만약 도착지보다 작고 다음에 가는 곳에 말이 없다면
			if (next <= 40 && board[1][next] == 0) {
				return next;
			} else if (next > 40)
				return 41;
		} else if (rule == 10) {
			// 몇번 이동해야 하는지
			int rest = (25 - horse.posi) / 3 - 1;
			// 25를 무조건 거쳐야 한다면 25까지 이동하고 나머지 25 규칙으로 이동
			if (dice > rest) {
				int d = dice - rest;
				int next = 25 + d * 5;
				if (next > 40)
					return 41;
				if (board[1][next] == 0)
					return next;
				else
					return -1;
			}
			// 25에 도착해야 하면
			else if (dice == rest) {
				if (board[1][25] == 0)
					return 25;
			} else {
				int next = horse.posi + 3 * dice;
				if (board[1][next] == 0)
					return next;
				else
					return -1;
			}
		} else if (rule == 20) {
			// 몇번 이동해야 하는지
			int rest = (25 - horse.posi) / 2 + 1;
			// 25를 무조건 거쳐야 한다면 25까지 이동
			if (dice >= rest) {
				int d = dice - rest;
				int next = 25 + d * 5;
				if (next > 40)
					return 41;
				if (board[1][next] == 0)
					return next;
				else
					return -1;
			} else if (dice == rest) {
				if (board[1][25] == 0)
					return 25;
			} else {
				int next = horse.posi + 2 * dice;
				if (board[1][next] == 0)
					return next;
				else
					return -1;
			}
		} else if (rule == 30) {
			int npo = horse.posi;
			int d = dice;
			if (npo == 30) {
				npo = 28;
				d -= 1;
			}

			int rest = (npo - 25);
			if (d > rest) {
				d -= rest;
				int next = 25 + d * 5;
				if (next > 40)
					return 41;
				if (board[1][next] == 0)
					return next;
				else
					return -1;
			} else if (d == rest) {
				if (board[1][25] == 0)
					return 25;
			} else {
				int next = horse.posi - d;
				if (board[1][next] == 0)
					return next;
				else
					return -1;
			}

		} else if (rule == 25) {
			int next = 25 + dice * 5;
			if (next > 40)
				return 41;
			if (board[1][next] == 0)
				return next;
		}

		return -1;
	}

	private static void calculate() {
		int sum = 0;
		for (int i = 0; i < list.size(); i++) {
			sum += list.get(i).sum;
		}

		result = Math.max(sum, result);
	}
}
