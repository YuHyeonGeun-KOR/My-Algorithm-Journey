package d2;

import java.util.*;
import java.io.*;
public class Solution_14361 {
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int testcase = 1; testcase < T + 1; testcase++) {
			int[] origin = new int[10];
			String n = br.readLine();
			if(n.equals("1")) {
				System.out.printf("#%d impossible\n" , testcase);
				continue;
			}
			int in = Integer.parseInt(n);
			char[] arr = n.toCharArray();
			for (int i = 0; i < arr.length; i++) {
				origin[arr[i] - '0'] +=1;
				
			}
			
			int byNum = 1;
			boolean flag = true;
			outer : while(flag) {
				
				int newN = in * ++byNum;
				int[] byArr = new int[10];
				if (newN >= 10000000) {
					System.out.printf("#%d impossible\n" , testcase);
					break;
				}
				
				char[]  newArr  = Integer.toString(newN).toCharArray();
				for (int i = 0; i < newArr.length; i++) {
					byArr[newArr[i] - '0'] +=1;
				};
				
				
				
				for (int i = 0; i < 10; i++) {
					if(origin[i] != byArr[i])  {
						continue outer;
						}
						
				}
				
				System.out.printf("#%d possible\n" ,  testcase);
				break;
			}
		}
		
	}
}
