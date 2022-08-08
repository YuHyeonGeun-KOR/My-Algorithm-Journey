package BOJ;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;
import java.util.Scanner;

public class BOJ_1158 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		Deque<Integer> queue = new ArrayDeque<>();
		for (int i = 1; i < n+1; i++) {
			queue.addLast(i);
		}
		
		List<Integer> result = new ArrayList<>();
		
		while(queue.size() > 0) {
			for (int i = 0; i < k-1; i++) {
				queue.addLast(queue.removeFirst());
			}
			
			result.add(queue.removeFirst());
		}
		System.out.print("<");
		for (int i = 0; i < result.size(); i++) {
			if(i!=result.size()-1)System.out.print(result.get(i) + ", ");
			else System.out.print(result.get(i) + ">");
		}
		
	}
}
