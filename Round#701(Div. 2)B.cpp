#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T=1;
    while(T--){
        ll n,q,k;
        cin>>n>>q>>k;
        vector<int> a(n);
        vector<int> b(n);
        vector<int> c(n);
        int i,x=0;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        for(i=0;i<n;i++){
            if(i==0){
                if(n!=1){
                    b[i]=a[i]-2;
                }
            }
            if(i!=0 && i!=n-1){
                b[i]=a[i+1]-a[i-1]-2;
            }
        }
        c[0]=0;
        for(i=1;i<n-1;i++){
            c[i]=c[i-1]+b[i];
        }
        while(q--){
            ll l,r;
            cin>>l>>r;
            l--;
            r--;
            if(l==r){
                cout<<k-1<<"\n";
            }
            else{
                ll p;
                p=a[l+1]-2+k-a[r-1]-1;
                p+=c[r-1]-c[l];
                cout<<p<<"\n";
            }
        }   
    }
    return 0;
}
