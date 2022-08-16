package BOJ;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ_3040_백설공주일곱난쟁이 {
	static int result = Integer.MAX_VALUE;
	static List<Integer> list = new ArrayList<>();
	static int[] input; 
	public static void com(int idx , int len) {
		if(list.size() == len) {
			check();
			return;
		}
		
		for (int i = idx; i < input.length; i++) {
			list.add(input[i]);
			com(i + 1 ,len);
			list.remove(list.size() - 1);
		}
		
	}
	
	public static void check() {
		int sum = 0;
		for (int i = 0; i < list.size(); i++) {
			sum += list.get(i);
		}
		if(sum == 100) {
			for (int i : list) {
				System.out.println(i);
			}
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		
		input = new int[9];
		
		for (int i = 0; i < 9; i++) {
			input[i] = sc.nextInt();
		}
		
		com(0,7);
		
	}
}
