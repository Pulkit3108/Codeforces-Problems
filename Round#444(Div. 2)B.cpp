#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T=1;
    //cin>>T;
    while(T--){
        int n;
        cin>>n;
        int a[n][6];
        int f[100]={0};
        for(int i=0;i<n;++i){
            for(int j=0;j<6;++j){
                cin>>a[i][j];
                f[a[i][j]]=1;
            }
        }
        int x;
        for(int i=0;i<n;++i){
            for(int j=i+1;j<n;++j){
                for(int k=0;k<6;++k){
                    for(int l=0;l<6;++l){
                        x=a[i][l]*10+a[j][k];
                            f[x]=1;
                        x=a[j][l]*10+a[i][k];
                            f[x]=1;
                    }
                }
            }
        }
        for(int i=1;i<100;++i){
            if(f[i]==0) {
                cout << i - 1;
                break;
            }
        }
    }
    return 0;
}
