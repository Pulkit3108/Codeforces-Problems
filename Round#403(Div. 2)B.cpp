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
        ll n;
        cin>>n;
        vector<ll> x(n);
        vector<ll> y(n);
        for(ll i=0;i<n;i++){
            cin>>x[i];
        }
        for(ll i=0;i<n;i++){
            cin>>y[i];
        }
        double l=0; 
        double r=1e9; 
        double p=1e9;
        for(ll i=0;i<200 && l<r;i++){
            double m=l+(r-l)/2;
            double tl=0;
            double tr=0;
            for(ll i=0;i<n;i++){
                double t=abs(m-x[i])/y[i]; 
                if(x[i]<m){
                    tl=max(tl,t);
                } 
                else{
                    tr=max(tr,t);
                }
            }
            p=min(p,max(tl,tr));
            if(tl>tr){
                r=m;
            } 
            else{
                l=m;
            }
        }
        cout<<fixed<<setprecision(12)<<p<<endl;
    }
    return 0;
}

