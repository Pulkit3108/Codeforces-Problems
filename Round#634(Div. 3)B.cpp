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
        ll n,a,b;
        cin>>n>>a>>b;
        ll i=0;
        for(i=0;i<n;i++){
            char c='a'+i%b;
            cout<<c;
        }
        cout<<endl;
        
    }
    return 0;
}
