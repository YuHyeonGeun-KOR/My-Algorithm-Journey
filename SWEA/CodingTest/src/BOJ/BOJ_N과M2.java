package BOJ;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class BOJ_N과M2 {
	static List<Integer> arr = new ArrayList<>();
	static int n;
	static int m;

	public static void com(int index) {
		if (arr.size() == m){

			for (Integer integer : arr) {
				System.out.print(integer + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = 0; i < n+1; i++) {
			arr.add(i);
			com(i+1);
			arr.remove(arr.size()-1);
		}
		

	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();

		com(1);
	}
}
