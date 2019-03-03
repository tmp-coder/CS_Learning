#include<bits/stdc++.h>
using namespace std;

#define ms(x,v) memset((x),(v),sizeof(x))

typedef long long LL;

struct Node{
    int num,weight;

    bool operator<(const Node& o)const{
        return weight < o.weight;
    }
};

struct BitSet{
    LL * col;
    const static int base = 64;
    BitSet(int n){
        col = new LL[(n+base-1)/base * base];
    }
    pair<int,int> pos(int idx){
        int arr_idx = (idx + base -1)/base;
        int bit = idx % base;
        return make_pair(arr_idx,bit);
    }
    int get(int idx){
        pair<int,int> p = pos(idx);
        return (col[p.first]>>p.second) & 1;
    }
    void set(int idx){
        pair<int,int> p = pos(idx);
        col[p.first]|= 1LL << p.second;
    }
};
int n,e;
vector<vector<int> > G;
int find_min_col(int v,const vector<int> & col){
    BitSet c(n);
    for(int i : G[v])
        if(col[i]!= -1)c.set(col[i]);
    for(int cc = 0 ; cc < n ; ++cc)
        if(!c.get(cc))return cc;
}

int greedy_algorithm(vector<int> & col){
    int r = rand()  % n;
    for(int i=0 ; i < col.size() ; ++i)col[i] =-1;
    col[r] =0;
    priority_queue<Node> Q;
    Q.push(Node{r,(int)G[r].size()});
    
    while(!Q.empty()){
        Node now = Q.top();Q.pop();
        for(auto v : G[now.num]){
            if(col[v] ==-1){
                col[v] = find_min_col(v,col);
                Q.push(Node{v,(int)G[v].size()});
            }
        }
    }
    return (* max_element(col.begin(),col.end())) +1;
    return 0;
}

void init(int n){
    G.resize(n);
}

int solve(vector<int>&color){
    init(n);
    return greedy_algorithm(color);
}

int main(){
    // ios::sync_with_stdio(0);
    // cin.tie(0);
    srand (time(NULL));

    // cout << "test ok\n";
    cin >> n >> e;
    init(n);
    for(int _ =0 ; _ < e ; ++_){
        int u,v;
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    int times = 5;
    int ans = n;
    vector<int> col(n);
    
    vector<int> tmp(n);
    while(times --){
        int now_ans = solve(tmp);
        if(ans > now_ans){
            ans = now_ans;
            col = tmp;
        }
    }

    // int ans = solve();
    cout << ans << " " << "0\n";
    for(int i  : col)
        cout << i << " ";
    
    return 0;
}