#include<bits/stdc++.h>
using namespace std;
#define ll long long int
long long get_min(long long a, long long b, long long c, long long d) { long long x= min(a,b); x =min(x,d); return min(x,c);}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //sc1(T);
    while(T--){
        // code   
        int n,k;
        cin>>n>>k;
        char arr[n][n];
        int i,j;
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                cin>>arr[i][j];
            }
        }
        int h=0;
        int a=1, b=1;
        for(i=0;i<n;++i){
            for(j=0; j<n;++j){
                if(arr[i][j]!='.'){ 
                    continue;
                }
                int u=0, d=0, l=0, r=0;
                int sum=0;
                int x=i-1, y=j;
                while(x>=0 && arr[x][y]=='.'){ 
                    ++u, --x;
                }
                x=i+1, y=j;
                while(x<n && arr[x][y]=='.'){
                    ++d, ++x;
                }
                x=i, y=j-1;
                while(y>=0 && arr[x][y]=='.'){
                    ++l, --y;
                }
                x=i, y=j+1;
                while(y<n && arr[x][y]=='.'){ 
                    ++r, ++y;
                } 
                if(l+r+1>=k){
                    sum+=get_min(l+1, r+1, l+r+2-k, k);
                }
                if(u+d+1>=k){
                    sum+=get_min(u+1, d+1, u+d+2-k, k);
                }
                h=max(h, sum);
                if(h==sum){
                    a=i+1, b=j+1;
                }
            }
        }
        cout<<a<<" "<<b<<endl;     
    }
    return 0;
}
