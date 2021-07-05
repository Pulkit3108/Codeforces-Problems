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
        ll n,a,b;
        cin>>n>>a>>b;
        bool flag=false;
        if(a==1){
            if((n-1)%b==0){
                flag=true;
            }
        }
        else{
            ll t=1;
            while(t<=n){
                if((n-t)%b==0){
                    flag=true;
                    break;
                }
                t*=a;
            }
        }
        if(flag){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }    
    }
    return 0;
}
