package BOJ;

import java.util.*;

public class BOJ_2164_카드2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Deque<Integer> queue = new ArrayDeque<>();
		for (int i = 1; i < n+1; i++) {
			queue.addLast(i);
		}
		int throwFlag = 1;
		while(queue.size() > 1) {
			if(throwFlag == 1) {
				queue.removeFirst();
				
			}
			else {  
				int temp = queue.removeFirst();
				queue.addLast(temp);
			}
			throwFlag *=-1;
		}
		System.out.println(queue.removeFirst());
	}
}
