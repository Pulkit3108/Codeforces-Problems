#include<bits/stdc++.h>
using namespace std;
#define ll long long int
// const int mod=1e9+7;
// const ll N=1e7+10;
// ll f[N];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int n;
        cin>>n;
        int a[n];
        int i,j;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        int s=0;
        int c=360;
        i=0;
        j=0;
        while(i<n){
            s+=a[i];
            while(s>=180){
                c=min(c,2*abs(180-s));
                s-=a[j];
                j+=1;
            }
            c=min(c,2*abs(180-s));
            i+=1;
        }
        cout<<c<<endl;
    }
    return 0;
}
