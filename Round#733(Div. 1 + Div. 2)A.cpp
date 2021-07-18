#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll N=1e7+10;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while (T--)
    {
        ll n;
        cin>>n;
        int m=0;
        while(n>0){
            int r=n%10;
            m=max(r,m);
            n=n/10;
        }
        cout<<m<<endl;
    }
    return 0;
}
 
