package BOJ;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

class Info implements Comparable<Info> {

	int left;
	int right;

	public Info(int left, int right) {
		this.left = left;
		this.right = right;
	}

	public int compareTo(Info o) {
		// TODO Auto-generated method stub

		return this.right - o.right;

	}

}

public class JO_1828_냉장고 {
	static List<Info> list = new ArrayList<>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		for (int i = 0; i < n; i++) {
			int left = sc.nextInt();
			int right = sc.nextInt();

			list.add(new Info(left, right));

		}

		int max = list.get(0).right;
		Collections.sort(list);
		int result = 1;
		for (int i = 1; i < list.size(); i++) {
			System.out.println(list.get(i).left + " " + list.get(i).right);
			if (max < list.get(i).left) {
				result += 1;
				max = list.get(i).left;
			}
		}

		System.out.println(result);

	}

}