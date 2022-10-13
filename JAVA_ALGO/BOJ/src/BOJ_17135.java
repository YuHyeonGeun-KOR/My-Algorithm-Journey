import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class BOJ_17135 {
    static int n;
    static int m;
    static int d;
    static int[][] board;
    static int cnt;
    static int eCount;
    static int result = Integer.MIN_VALUE;
    static List<int[]> enemy = new ArrayList<>();
    static List<int[]> arch = new ArrayList<>();
    static List<int[]> newEnemy = new ArrayList<>();
    static int[][] newboard;
    static List<int[]> clist = new ArrayList<>();
    public static void com(int len, int index){
        if(clist.size() == len){
            // for (int[] is : clist) {
            //     System.out.println(Arrays.toString(is));
            // }
            play();
            System.out.println(result);
            return;
        }

        for (int i = index; i < arch.size(); i++) {
            clist.add(arch.get(i));
            com(len , i +1);
            clist.remove(clist.size()-1);
        }
        
    }

    public static void play(){
        newboard  = new int[n][m];
        for (int i = 0; i < n; i++) {
            System.arraycopy(board[i], 0, newboard[i], 0, m);
        }
        eCount = cnt;
        int killCount = 0;
        newEnemy.addAll(enemy);
        while(true){
            if(eCount == 0) {
                break;
            }

            int index = 0;
            int flag = 1;
            outer : for (int i = 0; i < 3; i++) {
                int[] archer = clist.get(i);
                int ax = archer[0];
                int ay = archer[1];
                for (int j = ay - d ; j <= ay + d; j++) {
                    if(j < 0 || j >= m) {
                        if(index == d) flag = -1;
                        index += flag;
                        continue;
                    }

                    if(ax-index >= 0 && ax - index < n){
                        if(newboard[ax-index][j] == 1){
                            newboard[ax-index][j] = 0;
                            eCount -=1;
                            killCount +=1;
                            continue outer;
                        }
                    }

                    if(ax+index >= 0 && ax + index < n)
                        if(newboard[ax+index][j] == 1){
                            newboard[ax+index][j] = 0;
                            eCount -=1;
                            killCount +=1;
                            continue outer;
                        }
                    if(index == d) flag = -1;
                    index += flag;
                    
                }
            }
            // for (int[] is : newboard) {
            //     System.out.println(Arrays.toString(is));
            // }
            move();
        }
        if(killCount > result) result = killCount;
        newEnemy.clear();
    }

    public static void move(){
        
        for (int i = 0; i < newEnemy.size(); i++) {
            int x = newEnemy.get(i)[0];
            int y = newEnemy.get(i)[1];

            if(board[x][y] == 0) {
                newEnemy.remove(i);
                eCount -=1;
                i-=1;
            }
            else{
                if(x + 1 >= n) {
                    newEnemy.remove(i);
                    i-=1;
                    eCount -=1;
                } 
                else{
                    newboard[x][y] = 0;
                    newboard[x+1][y] = 1;
                    newEnemy.set(i, new int[]{x+1 , y});
                }
            }
        }
        // for (int[] is : newboard) {
        //     System.out.println(Arrays.toString(is));
        // }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        d = sc.nextInt();

        board= new int[n][m];

        // 적 입력받고 좌표에 저장하기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int input = sc.nextInt();
                if(input == 1){
                    enemy.add(new int[]{i,j});
                    board[i][j] = 1;
                    cnt+=1;
                }
                else{
                    arch.add(new int[]{i,j});
                }
                
            }
        }

        // for (int[] s : arch) {
        //     System.out.println(Arrays.toString(s));
        // }
        com(3,0);

        System.out.println(result);




    }
}