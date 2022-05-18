#include<bits/stdc++.h>
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
        vector<int> p(n);
        for(auto &it:p){
            cin>>it;
            --it;
        }
        vector<bool> b(n,false);
        vector<int> a(n);
        for(int i=0;i<n;++i){
            if(!b[i]){
                vector<int> c;
                while(!b[i]){
                    c.push_back(i);
                    b[i]=true;
                    i=p[i];
                }
                for(auto &it:c){ 
                    a[it]=c.size();
                }
            }
        }
        for(auto &it:a){
            cout<<it<<" ";
        }
        cout << endl;
    }
    return 0;
}







