import java.io.*;
import java.util.List;


import java.util.ArrayList;

/**
 * The class <code>Solver</code> is an implementation of a greedy algorithm to solve the knapsack problem.
 *
 */
public class Solver {
    
    /**
     * The main class
     */
    public static void main(String[] args) {
        try {
            solve(args);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Read the instance, solve it, and print the solution in the standard output
     */
    public static void solve(String[] args) throws IOException {
        String fileName = null;
        
        // get the temp file name
        for(String arg : args){
            if(arg.startsWith("-file=")){
                fileName = arg.substring(6);
            } 
        }
        if(fileName == null)
            return;
        
        // read the lines out of the file
        List<String> lines = new ArrayList<String>();

        BufferedReader input =  new BufferedReader(new FileReader(fileName));
        try {
            String line = null;
            while (( line = input.readLine()) != null){
                lines.add(line);
            }
        }
        finally {
            input.close();
        }
        
        
        // parse the data in the file
        String[] firstLine = lines.get(0).split("\\s+");
        int items = Integer.parseInt(firstLine[0]);
        int capacity = Integer.parseInt(firstLine[1]);

        int[] values = new int[items];
        int[] weights = new int[items];

        for(int i=1; i < items+1; i++){
          String line = lines.get(i);
          String[] parts = line.split("\\s+");

          values[i-1] = Integer.parseInt(parts[0]);
          weights[i-1] = Integer.parseInt(parts[1]);
        }

        // a trivial greedy algorithm for filling the knapsack
        // it takes items in-order until the knapsack is full
        
        KnapsackSolver solver  = new DPSolver();
        solver.solve(items,capacity,values,weights);
              
    }
    public static void output(int value,int opt,int[] taken) {
        System.out.println(value+" "+opt);
        int items = taken.length;
        for(int i=0; i < items; i++){
            System.out.print(taken[i]+" ");
        }
        System.out.println("");
    }
}


interface KnapsackSolver{
    public void solve(int n,int K,int[] values,int[] weights);
}

class DPSolver implements KnapsackSolver{
    private static final int MAX_SOLVE_SPACE = 100000000;
    public void solve(int n,int K,int[] values,int[] weights){
        if(n * K > MAX_SOLVE_SPACE)
            System.err.printf("need memory %d, but MAX_SOLVE_SPACE is %d\n",n*K,MAX_SOLVE_SPACE);
        int maxv;
        int opt =1;
        int[] token = new int[n];
        int[][] dp = new int[K+1][n];
        for(int k = 1 ; k <= K ; ++k){
            dp[k][0] = (k >=weights[0]? values[0] : 0); 
            for(int j = 1 ; j < n ; ++j){
                dp[k][j] = dp[k][j-1];
                if(k-weights[j] >=0 && dp[k][j] < dp[k-weights[j]][j-1] + values[j])
                    dp[k][j] = dp[k-weights[j]][j-1] + values[j];
            }       
        }
        
        maxv = dp[K][n-1];
        int k = K;
        for(int j = n-1 ; j >0 ; --j ){
            if(k >= weights[j] && dp[k][j] == dp[k-weights[j]][j-1] +values[j]){
                token[j] =1;
                k -=weights[j];
            }
        }
        if(dp[k][0] !=0)token[0] =1;
        Solver.output(maxv, opt, token);
    }
}
