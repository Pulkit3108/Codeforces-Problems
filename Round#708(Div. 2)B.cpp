#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n,m,i,k=0;
        cin>>n>>m;
        ll a[m]={0};
        for(i=0;i<n;i++){
            ll p;
            cin>>p;
            a[p%m]+=1;
        }   
        for(i=0;i<m;i++){
            if(i==0 and a[i]>0){
                k+=1;
            }
            else if(a[m-i]==0){
                k+=a[i];
            }
            else if(i==m-i){
                k+=1;
            }
            else if(m-i>i and a[i]!=0){
                ll x=a[i];
                ll y=a[m-i];
                if(abs(x-y)<2){
                    k+=1;
                }
                else if(x>y){
                    x-=y;
                    k+=x;
                }
                else{
                    y-=x;
                    k+=y;
                }
            }   
        }
        cout<<k<<"\n";
    }
    return 0;
}
