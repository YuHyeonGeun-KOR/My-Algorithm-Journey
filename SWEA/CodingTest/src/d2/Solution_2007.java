package d2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution_2007
{
	public static void main(String args[]) throws IOException
	{
		Scanner sc = new Scanner(System.in);
		int T;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T=Integer.parseInt(br.readLine()); 
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String s = br.readLine();
			for(int i = 1; i<s.length(); i++) {
				String left = s.substring(0,i);
				String right = s.substring(i,2*i);
				if(left.equals(right)) {
					System.out.printf("#%d %d%n" , test_case , left.length());
					break;
				}
			}
		}
	}
}