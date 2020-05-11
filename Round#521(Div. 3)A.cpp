#include<bits/stdc++.h>
#include<numeric> 
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll a,b,k;
        cin>>a>>b>>k;
        ll x;
        if(k%2==0){
            x=(k/2)*a-(k/2)*b;
        }
        else{
            x=(k+1)/2*a-(k/2)*b;
        }
        cout<<x<<endl;
    }
    
    return 0;
}
