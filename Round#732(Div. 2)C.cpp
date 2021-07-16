#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const int N=1e5+10;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while (T--)
    {
        int n;
        cin>>n;
        int a[n];
        int i,j;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        int f[2][N]={0};
        for(i=0;i<n;i++){
            f[i%2][a[i]]+=1;
        }
        sort(a,a+n);
        for(i=0;i<n;i++){
            f[i%2][a[i]]-=1;
        }
        bool flag=true;
        for(i=1;i<N;i++){
            for(j=0;j<2;j++){
                if(f[j][i]>0){
                    flag=false;
                }
            }
        }
        if(flag){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }

    return 0;
}

