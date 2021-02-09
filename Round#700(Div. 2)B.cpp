#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin>>t;
    while(t--){
        ll A,B,n;
        cin>>A>>B>>n;
        int i,c=1;
        vector<pair<ll,ll>> a(n);
        for(i=0;i<n;i++){
            cin>>a[i].first;
        }
        for(i=0;i<n;i++){
            cin>>a[i].second;
        }
        sort(a.begin(),a.end());
        for(i=0;i<n;i++){
            ll x=a[i].second/A;
            ll r1=a[i].second%A;
            ll y=B/a[i].first;
            ll r2=B%a[i].first;
            if(r1>0){
                x+=1;
            }
            if(r2>0){
                y+=1;
            }
            if(y<x){
                c=0;
                break;
            }
            else{
                B-=x*a[i].first;
            }
        }
        if(c==0){
            cout<<"NO"<<"\n";
        }
        else{
            cout<<"YES"<<"\n";
        }
    }
    return 0;
}
