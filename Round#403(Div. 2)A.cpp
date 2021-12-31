#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const int inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int n;
        cin>>n;
        unordered_set<int> t;
        int m=t.size();
        for(int i=0;i<2*n;i++){
            int s;
            cin>>s;
            if(t.find(s)==t.end()){
                t.insert(s);
            }
            else{
                t.erase(s);
            }
            m=max(m,(int)t.size());
        }
        cout<<m<<endl;
    }
    return 0;
}

