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
        ll a,b,c,r;
        cin>>a>>b>>c>>r;
        
        ll t,temp;
        if(a>b){
            t=a;
            a=b;
            b=t;
        }
        ll x=b-a;
        if(c+r<=b and c-r>=a and c+r>=a and c-r<=b){
            t=x-(c+r-(c-r));
        }
        else if(c+r>b and c-r>=a and c-r<=b){
            t=x-(b-(c-r));
        }
        else if(c-r<a and c+r<=b and c+r>=a){
            t=x-(c+r-a);
        }
        else if(c-r<a and c+r>b){
            t=0;
        }
        else if(c+r<=b and c+r<=a or (c-r>=a and c+r>=a)){
            t=x;
        }
        cout<<t<<endl;
        
    }
    return 0;
}
