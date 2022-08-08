package BOJ;

import java.util.*;
import java.lang.*;
import java.io.*;

class BOJ_1790 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		long m = sc.nextLong();
		int numBound = 1;
		long checker = 9;
		long prev = 0;

		while (true) {
			if (m > checker) { // 자리수 범위 보다 크면 자리수 다시 계산
				long p = (long) Math.pow(10, numBound-1); // 10의 제곱수
				checker = (long) (prev + 9 * (long) p * numBound); // 총 자리수 계산
				prev += checker; // 이전꺼 저장
				numBound += 1;
			} else
				break;
		}

		System.out.println(checker); // 2자리수 총 개수 
		System.out.println("numBound :  " + numBound);
		long jumpNum = 0;

		jumpNum = (long) (checker / numBound-1 ); //두자리수 중에 숫자 몇개인지

//		System.out.println("jumpNum :  " + jumpNum);
		long result = (long) (Math.pow(10, numBound - 1) + jumpNum);
		if (result > n) {
			System.out.println(-1);
			return;
		}
		long index = (long) (jumpNum % numBound); // 1번쨰꺼 가져오겠다
//		System.out.println("index :  " + index);
		System.out.println("result :  " + result);
		long moNum = (long) (Math.pow(10, numBound - 1));
		long indexChecker = 0;
		long answer = 0;
		//123456789   1011121314151617
		while (true) {
			answer = (long) (result / moNum);
			if (indexChecker == index)
				break;

			answer = (long) (result / moNum);
			result = (long) (result % moNum);
			moNum = (long) (moNum / 10);
			indexChecker += 1;

		}
		if(jumpNum == 0) System.out.println(answer);
		else System.out.println(answer-1);

	}
}