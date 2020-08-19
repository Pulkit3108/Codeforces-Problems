#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int a[3],i;
        memset(a,0,sizeof(a));
        for(i=0;i<n;++i){
            int x;
            cin>>x;
            a[x%3]+=1;
        }
        int c=a[0];
        int m=min(a[1],a[2]);
        c+=m;
        a[1]-=m;
        a[2]-=m;
        c+=(a[1]+a[2])/3;
        cout<<c<<endl;
    }
    return 0;
}
