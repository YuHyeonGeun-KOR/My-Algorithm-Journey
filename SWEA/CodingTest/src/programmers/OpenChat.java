package programmers;
import java.util.*;
public class OpenChat {
	public static String[] solution(String[] record){
		int count = 0;
		Map<String , String> idNick = new HashMap<>();
		List<String[]> command = new ArrayList<>();
		
		for (String re : record) {
			String[] temp = re.split(" ");
			if(temp[0].equals("Enter")) {
				idNick.put(temp[1], temp[2]);
				String[] c = {temp[0] , temp[1]}; // 명령어 , 아이디
				command.add(c);
				count += 1;
			}
			else if(temp[0].equals("Leave")) {
				String[] c = {temp[0] , temp[1]}; // 명령어 , 아이디
				command.add(c);
				count += 1;
			}else if(temp[0].equals("Change")) {
				idNick.put(temp[1], temp[2]);
			}
		}
		String[] result = new String[count];
		 
		int index = 0; 
		for (String[] com : command) {
			if(com[0].equals("Enter")) {
				result[index] = idNick.get(com[1]) + "님이 들어왔습니다.";
			}else if(com[0].equals("Leave")) {
				result[index] = idNick.get(com[1]) + "님이 나갔습니다.";
			}
			index += 1;
		}
		
		for (String string : result) {
			System.out.println(string);
		}
		
		return result;
	}
	
	
	
	
	
	public static void main(String[] args) {
		String[] re = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
		solution(re);
	}
}
