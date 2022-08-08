package programmers;

import java.util.*;

class Solution_szip {

	public static void main(String[] args) {
		String s = "xxxxxxxxxxyyy";
		System.out.println(solution(s));
	}

	 public static int solution(String s) {
		 int answer = Integer.MAX_VALUE;
	        String origin = s;
	        int slen = origin.length();
	        if(slen == 1) return 1;
	        for(int window = 1; window< slen/2 + 1; window++) {
	        	String result = "";
	        	String left = s.substring(0,window);
	        	int count = 1;
	        	String temp = "";
	        	for(int i = window;  i< slen; i+=window) {
	        		if(window + i > slen) {
	        			temp = temp + s.substring(i, slen);
	        			break;
	        			}
	        		String right = s.substring(i , window + i);
	        		if(left.equals(right)) {
	        			count++;
	        		}
	        		else {
	        			if (count ==1 ) {
	        				result = result + left;
	        			}else {
	        				result = result + Integer.toString(count) + left; 
	        			}
	        			
	        			left = right;
	        			count = 1;
	        		}
	        	}
	        	
	        	if(count >= 2) {
	                result = result + Integer.toString(count) + left + temp;
	        	}
	            else {
	                result = result + left + temp;
	            }
	        	System.out.println(result);
	        	answer = Math.min(answer, result.length());
	        }
	        return answer;
	        
	   }

}
