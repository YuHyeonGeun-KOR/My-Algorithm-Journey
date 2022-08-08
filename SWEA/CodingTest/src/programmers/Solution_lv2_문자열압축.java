package programmers;

import java.util.*;

public class Solution_lv2_문자열압축 {
	   public static void main(String[] args) {
	      String s = "aaaaaaaaaaaaaaaaaaaaaaaa";
	      int min = Integer.MAX_VALUE;
	      String res = "";
	      
	      if(s.length()==1) {
	         res = s;
	         min = 1;
	      }
	      
	      for(int i = 1; i <= s.length()/2; i++) {
	         String tmp = s.substring(0, i); // 비교할 값
	         res = ""; // 길이 잴 값
	         int cnt = 1;
	         
	         for(int j = i; j < s.length(); j += i) {
	            if(j+i < s.length()) {
	               if(tmp.equals(s.substring(j, j+i))) cnt++;
	               else {
	                  if(cnt == 1) res = res + tmp;
	                  else res = res + String.valueOf(cnt) + tmp;
	                  cnt = 1;
	               }
	               tmp = s.substring(j, j+i);
	            }
	            else {
	               if(j+i== s.length()) {
	                  if(tmp.equals(s.substring(j, s.length()))) cnt++;
	                  if(cnt == 1) res = res + tmp + s.substring(j, s.length());
	                  else res = res + String.valueOf(cnt) + tmp;
	               }
	               else {
	                  if(tmp.equals(s.substring(j, s.length()))) cnt++;
	                  if(cnt == 1) res = res + tmp + s.substring(j, s.length());
	                  else res = res + String.valueOf(cnt) + tmp + s.substring(j, s.length()-1);
	               }
	            }
	         }
	         System.out.println(res);
	         if(res.length() < min) {
	            min = res.length();
	         }
	      }
	      System.out.println(min);
	   }
	}