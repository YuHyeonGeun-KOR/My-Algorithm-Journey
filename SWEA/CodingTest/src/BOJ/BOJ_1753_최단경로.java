package BOJ;

import java.util.*;
import java.io.*;
public class BOJ_1753_최단경로 {
	
	static class Vertex {
		
		int to , weight;

		public Vertex(int to, int weight) {
			super();
			this.to = to;
			this.weight = weight;
		}

		
	}
	
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder  sb = new StringBuilder();
		String[] input = br.readLine().split(" ");
		
		
		int V = Integer.parseInt(input[0]);
		int E = Integer.parseInt(input[1]);
		
		int K = Integer.parseInt(br.readLine());
		
		List<Vertex>[] matrix = new ArrayList[V+1];  
		
		for (int i = 0; i < E; i++) {
			input = br.readLine().split(" ");
			
			int from = Integer.parseInt(input[0]);
			int to = Integer.parseInt(input[1]);
			int weight = Integer.parseInt(input[2]);
			
			if(matrix[from] == null) matrix[from]  = new ArrayList<>();
			matrix[from].add(new Vertex(to, weight));
			
			
		}
		int[] distance = new int[V+1];
		
		Arrays.fill(distance, Integer.MAX_VALUE);
		
		distance[K] = 0;
		
		PriorityQueue<Vertex> pq = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);
		pq.add(new Vertex(K,distance[K]));
		
		while(pq.size()>0) { 
			Vertex minV = pq.poll();
			int nextStart = minV.to;
			int d = minV.weight;
			
			if(matrix[nextStart] == null) continue;
			for (int i = 0; i < matrix[nextStart].size(); i++) {
				int nnS = matrix[nextStart].get(i).to;
				int nDis = matrix[nextStart].get(i).weight;
				if(distance[nnS] > d + nDis) {
					distance[nnS] = d + nDis;
					pq.add(new Vertex(nnS ,d + nDis));
				}
			}
		}
		
		
		for (int i = 1; i <= V; i++) {
			if(distance[i] == Integer.MAX_VALUE) sb.append("INF").append("\n");
			else sb.append(distance[i]).append("\n");
		}
		System.out.println(sb);
	}
}
