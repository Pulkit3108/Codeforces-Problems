#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,x;
        cin>>n>>x;
        int i,c=1;
        vector<int> A(n);
        vector<int> B(n);
        for(i=0;i<n;i++){
            cin>>A[i];
        }
        for(i=0;i<n;i++){
            cin>>B[i];
        }
        sort(A.begin(),A.end());
        sort(B.begin(),B.end(),greater<int>()); 
        for(i=0;i<n;i++){
            if(A[i]+B[i]>x){
                c=0;
                break;
            }
            else{
                continue;
            }
        }
        if(c==1){
            cout<<"Yes\n";
        }
        else{
            cout<<"No\n";
        }
    }
}
    
