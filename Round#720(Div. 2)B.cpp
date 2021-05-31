#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        vector<int> a(n);
        int i,j;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        int m=1e9+5;
        int mi;
        for(i=0;i<n;i++){
            if(a[i]<m){
                m=a[i];
                mi=i;
            }
        }    
        vector<vector<int>> b;
        for(i=mi+1;i<n;i++){
            if(a[i]<a[i-1]){
                b.push_back({mi+1,i+1,m,a[i-1]+1});
                a[i]=a[i-1]+1;
            }
            else{
                b.push_back({i,i+1,a[i-1],a[i-1]+1});
                a[i]=a[i-1]+1;
            }
        }
        for(i=mi-1;i>=0;i--){
            if(a[i]<a[i+1]){
                b.push_back({mi+1,i+1,m,a[i+1]+1});
                a[i]=a[i+1]+1;
            }
            else{
                b.push_back({i+2,i+1,a[i+1],a[i+1]+1});
                a[i]=a[i+1]+1;
            }
        }
        cout<<b.size()<<"\n";
        for(auto i : b){
            for(auto j : i){ 
                cout<<j<<" ";
            }
        cout<<"\n";
        }
    }
    return 0;
}
