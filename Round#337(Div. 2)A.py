#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while (T--)
    {
        int n;
        cin>>n;
        int x=0;
        if(n%2==0){
            x=n/4;
        }
        if(n%4==0){
            x-=1;
        }
        cout<<x<<endl;
        
    }
    return 0;
}
