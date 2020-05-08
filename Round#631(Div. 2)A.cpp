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
        int n,x,k;
        cin>>n>>x;
        vector<int> A(201,0);
        int i;
        for(i=0;i<n;i++){
            int a;
            cin>>a;
            A[a]=1;
        }
        for(k=n+x;k>0;k--){
            int y=0;
            for(i=1;i<=k;i++){
                if(A[i]==0){
                    y+=1;
                }
            }
            if(y<=x){
                cout<<k<<endl;
                break;
            }
        }
    }
    
    return 0;
}
