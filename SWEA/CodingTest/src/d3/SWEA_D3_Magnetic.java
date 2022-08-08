package d3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

public class SWEA_D3_Magnetic {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int test_case = 1; test_case <= 10; test_case++) {
			int N = Integer.parseInt(br.readLine());
			String[][] board = new String[100][];
			for (int i = 0; i < N; i++) {
				board[i] = br.readLine().split(" ");
			}
			int result = 0;
			Deque<String> deque = new LinkedList<>();
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if(board[j][i].equals("1") || board[j][i].equals("2")) {
						deque.addLast(board[j][i]);						
					}
				}
				
				// 하나만 있으면 어디로든지 떨어짐
				if(deque.size() == 1) continue;
				
				// 제일  아래쪽에 있는 자성체가  S극이면 떨어트리고 아니면 교착 여부 확인 대상
				while(deque.size() > 0) {
					String now = deque.removeLast();
					if(now.equals("2")) {
						deque.addLast(now);
						break;
					}
					
				}
				// 제일  아래쪽에 있는 자성체가  N극이면 떨어트리고 아니면 교착 여부 확인 대상
				while(deque.size() > 0) {
					String now = deque.removeFirst();
					if(now.equals("1")) {
						deque.addFirst(now);
						break;
					}
					
				}
				
				// 교착 상태 여부 확인이 필요한 자성체가 있다면?
				String start = "";
				if(deque.size() > 0) {
					start = deque.remove();
				}
				// 확인하고 start 자성체와 같은건 무시하고 다른 자성체를 만나면 결과 + 1 , 방금 만났던 자성체랑 다른 자성체 만날때까지 다 붙이고 start 초기화
				while(deque.size() > 0) {
					String now = deque.removeFirst();
					if(now.equals(start)) continue;
					else {
						result +=1;
						
						while(deque.size() > 0 && deque.getFirst().equals(now)) {
							deque.removeFirst();
						}
						if(deque.size() > 0 ) start = deque.removeFirst();
						else break;
					}
					
					
				}
			}
			
			
			System.out.println("#" + test_case + " " + result);
		}
	}
}
