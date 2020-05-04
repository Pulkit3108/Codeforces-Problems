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
        ll a,b,c,d;
        cin>>a>>b>>c>>d;
        ll x,y,x1,y1,x2,y2;
        cin>>x>>y>>x1>>y1>>x2>>y2;
        ll ab,cd;
        ab=x+b-a;
        cd=y+d-c;
        if(ab>=x1 and ab<=x2 and cd>=y1 and cd<=y2 and (x2>x1 or a+b==0) and (y2>y1 or c+d==0)){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
