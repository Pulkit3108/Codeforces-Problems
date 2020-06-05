#include<bits/stdc++.h>
using namespace std;
#define ll long long int
vector<int> A(1025);
vector<int> S(1025);
int n;
bool check(int k){
    int i;
    for(i=1;i<=n;++i)
        if(!A[S[i]^k]){
            return(0);
        }
    return(1);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        cin>>n;
        int i,k,c=0;
        for(i=0;i<1025;++i){
            A[i]=0;
        }
        for(i=1;i<=n;++i){
            cin>>S[i];
            A[S[i]]=1;
        }
        for(k=1;k<1024;++k){
            if(check(k)){
                cout<<k<<endl;
                c=1;
                break;
            }
        }
        if(c==0){
            cout<<"-1"<<endl;
        }
    }
    return 0;
}
