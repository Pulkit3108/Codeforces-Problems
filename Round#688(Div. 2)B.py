#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll n;
        cin>>n;
        ll a[n];
        ll i;
        ll k=0;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        for(i=0;i<n-1;i++){
            k+=abs(a[i]-a[i+1]);
        }
        ll m=min(k-abs(a[0]-a[1]),k-abs(a[n-1]-a[n-2]));
        for(i=1;i<n-1;i++){
            m=min(m,k-(abs(a[i]-a[i-1])+abs(a[i+1]-a[i])-abs(a[i-1]-a[i+1])));
        }
        cout<<m<<endl;
    }
    return 0;
}
