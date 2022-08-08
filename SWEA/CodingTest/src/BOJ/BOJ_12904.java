package BOJ;

import java.io.*;
import java.util.*;



public class BOJ_12904 {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuffer S = new StringBuffer(br.readLine());
		StringBuffer target = new StringBuffer(br.readLine());
		int sLen = S.length();
		int tLen = target.length();
		while(true) {
			if(sLen == tLen)break;
			// A를 추가했다 -> 지운다.
			if(target.charAt(tLen-1) == 'A') {
				target.deleteCharAt(tLen-1);
				
			}
			//B가 추가됐다. -> B 지우고 뒤집는다.
			else if(target.charAt(tLen-1) == 'B') {
				target.deleteCharAt(tLen-1);
				target.reverse();
			}
			tLen-=1;
		}
		
		if(target.toString().equals(S.toString())) System.out.println(1);
		else System.out.println(0);
	}
}
