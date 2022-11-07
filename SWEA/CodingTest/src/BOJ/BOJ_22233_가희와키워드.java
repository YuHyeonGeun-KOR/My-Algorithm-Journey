package BOJ;

import java.io.*;
import java.util.*;
public class BOJ_22233_가희와키워드 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Set<String> set = new HashSet<>();
		
		String[] input = br.readLine().split(" ");
		int N = Integer.parseInt(input[0]);
		int M = Integer.parseInt(input[1]);
		
		for (int i = 0; i < N; i++) {
			set.add(br.readLine());
		}
		
		for (int i = 0; i < M; i++) {
			input = br.readLine().split(",");
			
			for (int j = 0; j < input.length; j++) {
				if(set.contains(input[j])) {
					set.remove(input[j]);
				}
			}
			System.out.println(set.size());
		}
		
		
	}
}
