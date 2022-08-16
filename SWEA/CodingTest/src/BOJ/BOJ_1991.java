package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class BOJ_1991 {

	static Map<Character, Character[]> map = new HashMap<>();
	static String[] input;

	public static void pre(char root) {
		if (root == '.')
			return;

		System.out.print(root);
		pre(map.get(root)[0]);
		pre(map.get(root)[1]);
	};

	public static void in(char root) {
		if (root == '.')
			return;

		in(map.get(root)[0]);
		System.out.print(root);
		in(map.get(root)[1]);
	};

	public static void post(char root) {
		if (root == '.')return;

		post(map.get(root)[0]);
		post(map.get(root)[1]);
		System.out.print(root);
	};

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		for (int i = 0; i < n; i++) {
			input = br.readLine().split(" ");
			map.put(input[0].charAt(0), new Character[] { input[1].charAt(0), input[2].charAt(0) });
		}

		pre('A');
		System.out.println();
		in('A');
		System.out.println();
		post('A');
	}
}
