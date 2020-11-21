#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        int n,k;
        cin>>n>>k;
        int m=n*k;
        vector<int> a(m);
        int i;
        for(i=0;i<m;i++){
            cin>>a[i];
        }
        ll s=0;
        if(n==2){
            for(i=0;i<m;i+=2){
                s+=a[i];
            }
        }
        else{
            int t=(n+1)/2;
            int l=n-t+1;
            int x=1;
            int q=0;
            for(i=m-1;i>=0;i--){
                if(x%l==0){
                    s+=a[i];
                    q++;
                }
                x++;
                if(q>=k)
                    break;
            }
        }
        cout<<s<<"\n";
    }
    return 0;
}
