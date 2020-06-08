#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        int N,M;
        cin>>N>>M;
        int S[N][M];
        set<int> A,B;
        int i=0,j=0;
        for(i=0;i<N;i++){
            for(j=0;j<M;j++){
                cin>>S[i][j];
                if(S[i][j]==1){
                    A.insert(i+1);
                    B.insert(j+1);
                }
            }
        }
        int m=min((N-A.size()),(M-B.size()));
        if(m%2!=0){
            cout<<"Ashish"<<endl;
        }
        else{
            cout<<"Vivek"<<endl;
        }
    }
    return 0;
}
