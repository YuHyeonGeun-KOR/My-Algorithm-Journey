package programmers;

import java.util.ArrayList;
import java.util.List;

public class StringCompression {

   public int solution(String s) {
      int answer = s.length(); // 결과값

      for (int i = 1; i <= s.length() / 2; i++) { // 자를수 있는 최대 단위는 문자열의 반을 넘길 수 없다.
         String list = s; // 테케 담을 문자열
         String complist = ""; // 압축할 비교 문자열 단위 []
         String reslist = ""; // 압축된거 저장할 문자열
         int count = 1; // 압축정도
         complist = list.substring(0, i);

         for (int j = i; j <= list.length(); j += i) {
            String nextlist = ""; // 같은 단위의 비교할거
            if (i + j <= list.length()) {
               nextlist = list.substring(j, i + j); // i+j 가 list.length() 보다 커지면 안됨
               
               if (complist.equals(nextlist)) {
                  count++;
               }
               else { 
                  if(count==1) { // 걍 바로 다른거일때
                     reslist += complist;
                     complist = nextlist;
                  }
                  
                  
                  // 같은거 나오다가 달라진경우
                  reslist += count + complist;
                  complist = nextlist;
                  count = 1; // 압축 갯수 초기화
                  
               }

            }
            else { // 문자열 단위 보다 비교할 남은 문자갯수가 적을 때
               nextlist = list.substring(j, list.length());
               reslist += complist + nextlist;
            }
            
         }
         if(answer >= reslist.length())
             answer = reslist.length();
         System.out.println(reslist.toString());
         System.out.println(answer);
      }
      return answer;
   }

   public static void main(String[] args) {
      StringCompression SC = new StringCompression();
      String tc = "aabbaccc";
      int result = SC.solution(tc);
      System.out.println(result);

   }

}