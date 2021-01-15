#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n;
        cin>>n;
        ll a[n];
        ll i=0,j=0;
        ll t=0,m=0;
        vector<ll> v(n);
        vector<ll> h(n);
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        for(i=1;i<n-1;i++){
            if(a[i]>a[i-1] && a[i]>a[i+1]){ 
                t+=1;
                h[i]=1;
            }
            if(a[i]<a[i-1] && a[i]<a[i+1]){ 
                t+=1;
                v[i]=1;
            }
        }
        ll ans=t; 
        for(i=0;i<n;i++){
            ll q=a[i];
            m=0;
            if(i-1>=0){
                a[i]=a[i-1];
                for(j=i-1;j<i+2;j++){
                    if(j>=1 && j<n-1){
                        if(!(a[j]>a[j-1] && a[j]>a[j+1])){
                            if(h[j]){ 
                                m+=1;
                            }
                        }
                        else{ 
                            m-=1;
                        }
                        if(!(a[j]<a[j-1] && a[j]<a[j+1])){
                            if(v[j]){ 
                                m+=1;
                            }
                        }
                        else{ 
                            m-=1;
                        }
                    }
                }
                ans=min(ans,t-m);
            }
            m=0;
            if(i+1<n){
                a[i]=a[i+1];
                for(j=i-1;j<i+2;j++){
                    if(j>=1 && j<n-1){
                        if(!(a[j]>a[j-1] && a[j]>a[j+1])){
                            if(h[j]){ 
                                m+=1;
                            }
                        }
                        else{
                            m-=1;
                        }
                        if(!(a[j]<a[j-1] && a[j]<a[j+1])){
                            if(v[j]){
                                m+=1;
                            }
                        }
                        else{ 
                            m--;
                        }
                    }
                }
                ans=min(ans,t-m);
            }
            a[i]=q;    
        }
        cout<<ans<<endl;  
    }
    return 0;
}
