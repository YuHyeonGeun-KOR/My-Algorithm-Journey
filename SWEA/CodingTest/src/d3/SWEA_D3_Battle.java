package d3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class SWEA_D3_Battle {
	static int tankX = 0;
	static int tankY = 0;
	static String ddang = ".";
	static String stone = "*";
	static String steel = "#";
	static String water = "-";
	static String d = ">";
	static String[][] board;

	// 움직이는 명령어 동작
	static void move(String dir) {
		if (dir.equals("U")) {
			d = "^";
			if (tankX - 1 >= 0 && board[tankX - 1][tankY].equals(ddang)) {
				board[tankX][tankY] = ddang;
				board[tankX - 1][tankY] = d;
				tankX -= 1;
			} else
				board[tankX][tankY] = d;
		} else if (dir.equals("D")) {
			d = "v";
			if (tankX + 1 < board.length && board[tankX + 1][tankY].equals(ddang)) {
				board[tankX][tankY] = ddang;
				board[tankX + 1][tankY] = d;
				tankX += 1;
			} else
				board[tankX][tankY] = d;
		} else if (dir.equals("L")) {
			d = "<";
			if (tankY - 1 >= 0 && board[tankX][tankY - 1].equals(ddang)) {
				board[tankX][tankY] = ddang;
				board[tankX][tankY - 1] = d;
				tankY -= 1;
			} else
				board[tankX][tankY] = d;
		} else if (dir.equals("R")) {
			d = ">";
			if (tankY + 1 < board[0].length && board[tankX][tankY + 1].equals(ddang)) {
				board[tankX][tankY] = ddang;
				board[tankX][tankY + 1] = d;
				tankY += 1;
			} else
				board[tankX][tankY] = d;
		}
	}

	// 포탄 발싸!!
	public static void fire() {
		int indexX = 0;
		int indexY = 0;
		int bullX = tankX;
		int bullY = tankY;
		if (d.equals("^"))
			indexX = -1;
		else if (d.equals("v"))
			indexX = 1;
		else if (d.equals("<"))
			indexY = -1;
		else if (d.equals(">"))
			indexY = 1;

		while (true) {
			if (bullX + indexX < board.length && bullX + indexX >= 0 && bullY + indexY < board[0].length
					&& bullY + indexY >= 0) {
				if (board[bullX + indexX][bullY + indexY].equals(steel))
					break;
				else if (board[bullX + indexX][bullY + indexY].equals(stone)) {
					board[bullX + indexX][bullY + indexY] = ddang;
					break;
				}
			} else
				break;
			bullX = bullX + indexX;
			bullY = bullY + indexY;

		}

	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int test_case = 1; test_case <= T; test_case++) {
			String[] input = br.readLine().split(" ");
			int H = Integer.parseInt(input[0]);
			int W = Integer.parseInt(input[1]);

			board = new String[H][];
			// 탱크 위치 찾기
			for (int i = 0; i < H; i++) {
				String[] temp = br.readLine().split("");

				for (int j = 0; j < temp.length; j++) {
					if (temp[j].equals("^")) {
						d = "^";
						tankX = i;
						tankY = j;
					} else if (temp[j].equals("v")) {
						d = "v";
						tankX = i;
						tankY = j;
					} else if (temp[j].equals(">")) {
						d = ">";
						tankX = i;
						tankY = j;
					} else if (temp[j].equals("<")) {
						d = "<";
						tankX = i;
						tankY = j;
					}
				}

				board[i] = temp;

			}

			int l = Integer.parseInt(br.readLine());
			String[] command = br.readLine().split("");
			// command 동작 !
			for (String c : command) {
				if (c.equals("U") || c.equals("D") || c.equals("L") || c.equals("R")) {
					move(c);
				} else if (c.equals("S")) {
					fire();
				}
			}

			// 출력
			System.out.print("#" + test_case + " ");
			for (int i = 0; i < board.length; i++) {
				for (int j = 0; j < board[0].length; j++) {
					System.out.print(board[i][j]);
				}
				System.out.println();
			}

		}
	}
}
