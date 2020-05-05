#include<bits/stdc++.h>
using namespace std;
#define ll long long int  
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll a,b,c,n,x;
        cin>>a>>b>>c>>n;
        if(a==b and b==c and n%3==0){
            cout<<"YES"<<endl;
            continue;
        }
        ll d=a>b?(a>c?a:c):(b>c?b:c);
        if(d==a){
            x=d-b+d-c;
        }
        else if(d==b){
            x=d-a+d-c;
        }
        else if(d==c){
            x=d-a+d-b;
        }
        if(x<=n){
            if((n-x)%3==0){
                cout<<"YES"<<endl;
            }
            else{
                cout<<"NO"<<endl;
            }
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
