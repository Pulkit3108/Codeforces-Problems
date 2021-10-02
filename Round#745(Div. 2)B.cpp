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
        ll n,m,k;
        cin>>n>>m>>k;
        k-=2;
        if(m<n-1 || m>((n*(n-1))/2) || k<0){
            cout<<"NO"<<endl;
        }
        else{
            if(k==0){
                if(n==1){
                    cout<<"YES"<<endl;
                }
                else{
                    cout<<"NO"<<endl;
                }
            }
            else if(k==1){
                if(m==((n*(n-1))/2)){
                    cout<<"YES"<<endl;
                }
                else{
                    cout<<"NO"<<endl;
                }
            }
            else{
                cout<<"YES"<<endl;
            }
        }
    }
    return 0;
}
