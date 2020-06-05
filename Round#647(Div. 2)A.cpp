#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll getR(ll a){
    while(a%2==0){
        a/=2;
    }
    return(a);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll a,b;
        cin>>a>>b;
        if(a>b){
            swap(a,b);
        }    
        ll c=0;
        if(getR(b)!=getR(a)){
            c=-1;
        }
        else{
            b/=a;
            while(b>=8){
                b/=8;
                c+=1;
            }   
            if(b>1){
                c+=1;
            }
        }
        cout<<c<<endl;
    }
    return 0;
}
