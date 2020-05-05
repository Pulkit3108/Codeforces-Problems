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
        int n;
        cin>>n;
        vector<pair<int,int>> A(n);
        int i,x=1;
        for(i=0;i<n;i++){
            cin>>A[i].first>>A[i].second;
        }
        sort(A.begin(),A.end());
        pair<int,int> X;
        X.first=0;
        X.second=0;
        string S;
        for(i=0;i<n;i++){
            int r=A[i].first-X.first;
            int u=A[i].second-X.second;
            if(r<0 or u<0){
                cout<<"NO"<<endl;
                x=0;
                break;
            }
            S+=string(r,'R');
            S+=string(u,'U');
            X=A[i];
        }
        if(x==1){
            cout<<"YES\n"<<S<<endl;
        }
    }
    return 0;
}
