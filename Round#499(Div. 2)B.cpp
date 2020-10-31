#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const int m1=1e3+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t=1;
    //cin>>t;
    while(t--){
        int n,m,i,j;
        cin>>n>>m;
        vector<int> c(101,0);
        for(i=0;i<m;i++){
            int x;
            cin>>x;
            c[x]+=1;
        }
        for(i=100;i>0;i--){
            vector<int> c1(c);
            int k=0;
            for(j=1;j<101;j++){
                while(c1[j]>=i){
                    k++;
                    c1[j]-=i;
                }
            }
            if(k>=n){
                cout<<i<<endl;
                return 0;
            }
        }
    }
    cout<<0<<endl;
}
