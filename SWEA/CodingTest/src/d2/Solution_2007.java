package d2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

class Solution_2007
{
// Compelte check
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