#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
#define ld long double
const ll mod=1e9+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n,k;
        cin>>n>>k;
        vector<ll> x(k);
        for(int i=0;i<k;i++){
            cin>>x[i];
        }
        sort(x.begin(),x.end(),greater<int>());
        int s=0;
        int c=0;
        for(int i=0;i<k;i++){
            if(c<x[i]){
                c+=(n-x[i]);
                s+=1;
            }
            else{
                break;
            }
        }
        cout<<s<<endl;
        
        

    }
    return 0;
}

