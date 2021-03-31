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
        ll n,W,i;
        cin>>n>>W;
        multiset<int> w;
        for(i=0;i<n;i++){
            ll x;
            cin>>x;
            w.insert(x);
        }
        int h=1,l=W;
        while(!w.empty()){
            auto itr=w.upper_bound(l);
            if(itr==w.begin()){
                l=W;
                h+=1;
            } 
            else{
                itr--;
                int val=*itr;
                l-=val;
                w.erase(itr);
            }
        }
        cout<<h<<"\n";
    }  
    return 0;
}
