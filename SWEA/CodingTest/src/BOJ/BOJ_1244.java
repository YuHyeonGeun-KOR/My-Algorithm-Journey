package BOJ;
import java.io.*;
import java.util.*;
public class BOJ_1244 {
	static String[] switArr;
	// 스위치 바꾸기
	public static void Change(int index) {
		if (switArr[index].equals("1")) {
			switArr[index]  = "0";
		}
		else switArr[index]  = "1";
	}
	//남자 일때 스위치 동작
	public static void Man(int num) {
		for (int i = 1; i < switArr.length + 1; i++) {
			if(i%num == 0 ) {
				Change(i-1);
			}
		}
	}
	//여자일떄 스위치 동작
	public static void Woman(int num) {
		int start = num-1;//비교할 왼쪽 인덱스
		int end = num+1;// 비교할 오른쪽 인덱스
		Change(num);
		while(true) {
			if (start < 0 || end >= switArr.length) break; //범위 체크, 
			
			if(switArr[start].equals(switArr[end])) {  //대칭이면(중간포함) 스위치 바꾸기
				Change(start);
				Change(end);
				start -=1;
				end +=1;
			}
			else {
				break;
			}
			
		}
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		switArr = br.readLine().split(" ");
		
		int time = Integer.parseInt(br.readLine());
		for (int i = 0; i < time; i++) {
			String[] temp = br.readLine().split(" ");
			int sex = Integer.parseInt(temp[0]);
			int num = Integer.parseInt(temp[1]);
			
			if(sex == 1) Man(num);
			else Woman(num-1);
		}
		
		//출력
		for(int i=0; i<switArr.length; i++) {
			System.out.print(switArr[i] + " ");
			if((i+1) % 20 == 0)
				System.out.println();
		}
	}
	
}
