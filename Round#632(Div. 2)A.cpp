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
        int n,m;
        cin>>n>>m;
        string S(m,'B');
        vector<string> A(n,S);
        A[0][0]='W';
        for(int i=0;i<n;i++){
            cout<<A[i]<<endl;
        }
        cout<<endl;
    }
    
    return 0;
}
