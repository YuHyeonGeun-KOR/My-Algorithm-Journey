package BOJ;

import java.io.*;
import java.util.*;
public class BOJ_1806_부분합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int S = sc.nextInt();
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }
        int result = Integer.MAX_VALUE;
        int start = 0;
        int end = 0;    
        int sum = 0;
        while(true){
            if(end == N) break;
            if(S == 0)break;
            if(sum + nums[end]< S){
                sum += nums[end];
                end +=1;
            }

            else if(sum + nums[end] >= S){
                result = Math.min(end-start +1 , result);
                sum -= nums[start];
                start +=1;
            }

            
        }    
        if(result == Integer.MAX_VALUE) System.out.println(0);
        else System.out.println(result);
    }
}
