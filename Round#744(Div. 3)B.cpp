#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        vector<int> a(n);
        for (int i=0;i<n;i++){
            cin>>a[i];
        }
        vector<pair<int,int>> t;
        for(int i=0;i<n-1;i++){
            int minp=i;
            for(int j=i+1;j<n;j++){
                if(a[j]<a[minp]){
                    minp=j;
                }
            }
            if(minp>i){
                t.push_back({i,minp});
                int x=a[minp];
                for(int j=minp;j>i;j--){
                    a[j]=a[j-1];
                }
                a[i]=x;
            }
        }
        cout<<t.size()<<endl;
        for(auto &it:t){
            cout<<it.first+1<<" "<<it.second+1<<" "<<it.second-it.first<<endl;
        }
    }
    return 0;
}

