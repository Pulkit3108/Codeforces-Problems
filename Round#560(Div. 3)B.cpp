#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin>>n;
    vector<int> A(n);
    int i,ans=0;
    for(i=0;i<n;i++){
        cin>>A[i];
    }
    sort(A.begin(),A.end());
    i=0;
    int k=1;
    while(i!=n){
        if(A[i]>=k){
            ans+=1;
            k+=1;
        }
        i+=1;
    }
    cout<<ans<<endl;
}
