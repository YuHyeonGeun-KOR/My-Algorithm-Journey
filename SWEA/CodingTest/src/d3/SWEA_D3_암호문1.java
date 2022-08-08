package d3;

import java.io.*;
import java.util.*;

public class SWEA_D3_암호문1 {
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int testcase = 1; testcase <= 10; testcase++) {

			int n = Integer.parseInt(br.readLine());

			Deque<String> queue = new ArrayDeque<>();
			Deque<String> queueLeft = new ArrayDeque<>();
			String[] l = br.readLine().split(" ");
			List<String> list = Arrays.asList(l);
			queue.addAll(list);

			int m = Integer.parseInt(br.readLine());
			String[] command = br.readLine().split("I");
			String[] inCommand = {};
			for (String c : command) {
				if (c.equals(""))
					continue;

				inCommand = c.split(" ");
				int x = Integer.parseInt(inCommand[1]);
				int y = Integer.parseInt(inCommand[2]);

				for (int i = 0; i < x; i++) {
					queueLeft.addLast(queue.removeFirst());
				}

				for (int i = inCommand.length-1; i > 2; i--) {
					queue.addFirst(inCommand[i]);
				}

				while (queueLeft.size() > 0) {
					queue.addFirst(queueLeft.removeLast());
				}
			}
			System.out.print("#" + testcase + " ");
			for (int i = 0; i < 10; i++) {
				System.out.print(queue.removeFirst() + " ");
			}
		}
	}
}
