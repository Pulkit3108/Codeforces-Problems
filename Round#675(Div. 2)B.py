#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll n,m;
        cin>>n>>m;
        ll a[n][m];
        ll i,j;
        ll k=0;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>a[i][j];
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                ll o1=a[i][m-j-1];
                ll o2=a[n-i-1][j];
                vector<int> b;
                b.push_back(a[i][j]);
                b.push_back(o1);
                b.push_back(o2);
                sort(b.begin(),b.end());
                a[i][j]=a[i][m-j-1]=a[n-i-1][j]=b[1];
                k+=(ll)(b[2]-b[1])+(b[1]-b[0]);
            }
        }
        cout<<k<<endl;
    }
    return 0;
}
