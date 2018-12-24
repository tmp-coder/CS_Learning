import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * The class <code>Solver</code> is an implementation of solve framework to solve the knapsack problem.
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

        Item[] a = new Item[items];
        for(int i=0 ; i<items ; ++i){
            a[i] = new Item();
            a[i].value = values[i];
            a[i].weight = weights[i];
            a[i].idx = i;
        }
        Arrays.sort(a);
        // for(int i=0 ; i< items ; ++i)
        //     System.out.println(a[i].value + " " + a[i].weight);
        for(int i=0 ; i<items ; ++i){
            values[i] = a[i].value;
            weights[i] = a[i].weight;
        }
        // a trivial greedy algorithm for filling the knapsack
        // it takes items in-order until the knapsack is full
        
        // KnapsackSolver solver = (long) items*capacity > DPSolver.MAX_SOLVE_SPACE?
        //                         new LDSSolver() : new DPSolver();
        
        KnapsackSolver solver = new LDSSolver();
        
        Map<String,Object> ans = solver.solve(items,capacity,values,weights);
        int[] taken = new int[items];
        int[] ansIdx = (int[])ans.get("taken");
        for(int i=0 ; i<items ; ++i)taken[a[i].idx] = ansIdx[i];
        ans.put("taken", taken);
        output(ans);
    }
    public static void output(Map<String,Object> ans) {
        int value = (int)ans.get("value");
        int opt = (int)ans.get("opt");
        int[] taken = (int[])ans.get("taken");
        System.out.println(value+" "+opt);
        int items = taken.length;
        for(int i=0; i < items; i++){
            System.out.print(taken[i]+" ");
        }
        System.out.println("");
    }
    public static Map<String,Object> constructAns(int value,int opt,int[] taken) {
        Map<String,Object> ans = new HashMap<>();
        ans.put("value", value);
        ans.put("opt", opt);
        ans.put("taken", taken);
        
        return ans;
    }


}

/**
 * Item
 */
class Item implements Comparable<Item>{
    int value,weight;
    int idx;
    public int compareTo(Item o){
        return value - o.value;
    }
}


/**
* This interface <code> KnapsackSolver </code> provides a general interface for solving knapsack problem
*/
interface KnapsackSolver{
    /**
     *  this method is a interface that given items {@code n}, capcity {@code K}, and value {@code values}  with {@code weights}
     * @param n number of items
     * @param K capcity of bag
     * @param values a int array {@code values[i]} represented the value of ith item
     * @param weights a int array {@code weights[i]} represented the weight of ith item
     */
    public Map<String,Object> solve(int n,int K,int[] values,int[] weights);
}

/**
 * this a danamic programing solver for knapsack problem
 */

class DPSolver implements KnapsackSolver{
    public static final int MAX_SOLVE_SPACE = 100000000;
    public Map<String,Object> solve(int n,int K,int[] values,int[] weights){
        int maxv;
        int[] taken = new int[n];
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
                taken[j] =1;
                k -=weights[j];
            }
        }
        if(dp[k][0] !=0)taken[0] =1;
        return Solver.constructAns(maxv, 1, taken);
    }
}

/**
 * LDSSolver,limited discrepancy search solver for knapsack problem
 */
class LDSSolver implements KnapsackSolver{

    /**
     * just for least paras in member methods
     */
    private int[] vals;
    private int[] weights;
    private int ans;
    private int[] bestVec; // the final tacken vector
    private static final long elapsedTime = 1000000000L;//10 s
    private long startTime;
    public Map<String,Object> solve(int n,int K,int[] v,int [] w) {
        vals = v;
        weights = w;
        KnapsackSolver initSolver = new DPSolver();
        int cap = Math.min(DPSolver.MAX_SOLVE_SPACE/n,K);
        Map<String,Object> initAns = initSolver.solve(n, cap, v, w);
        if((long)n*K <= DPSolver.MAX_SOLVE_SPACE) return initAns;
        ans = (int)initAns.get("value");
        // System.out.println("dp ans= " + ans);
        bestVec = (int[])initAns.get("taken");
        int tks = 0;
        for(int i=0 ; i < n ; ++i)tks += bestVec[i];
        

        int[] tmpw = weights.clone();
        Arrays.sort(tmpw);
        int min = 0;
        int s =0;
        for( ; s+weights[min] <= K && min <n ; s+= weights[min],min++ );
        for(int i=min ; i < n ; ++i)s+=weights[i];
        for(int mis = n-min; mis <=n-tks+5; ++mis){
            startTime = System.nanoTime();
            lds(0, s,K,mis, n-1, new int[n]);
        }

        return Solver.constructAns(ans, 0, bestVec);
    }
    /**
     * ths limited discrepancy search method, you can find detail at this paper {@link https://ai.dmi.unibas.ch/research/reading_group/harvey-ginsberg-ijcai1995.pdf}
     * @param best the value of cur node
     * @param estimate the best value of cur node
     * @param leftCap the left capcity
     * @param mistake  the right branch of search tree
     * @param i the ith item
     * @return
     */
    private void lds(int best,int estimate,int leftCap,int mistake,int i,int[] taken) {
        if(estimate < ans) return;// prun the branch
        if(mistake >i+1)return;
        if(leftCap <0)return;
        if(i < 0 || leftCap-weights[i]<0|| System.nanoTime() - startTime > elapsedTime){
            if(best > ans){
                ans = best;
                for(int j=taken.length-1 ; j >i ; --j)bestVec[j] = taken[j];
                for(int j=i ; j>=0 ; --j)bestVec[j] =0;
            }
            return;
        }
        // not take the ith item, mistake -1
        if(mistake>0){
            taken[i] =0;
            lds(best, estimate, leftCap, mistake-1, i-1, taken);
        }
        taken[i] =1;
        lds(best + vals[i], estimate - vals[i],leftCap-weights[i], mistake, i-1, taken);
    }
}