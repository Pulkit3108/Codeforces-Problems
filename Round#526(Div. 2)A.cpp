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
    int i;
    for(i=0;i<n;i++){
        cin>>A[i];
    }
    int ans=0;
    for(i=1;i<n;i++){
        ans+=A[i]*4*i;
    }
    cout<<ans<<endl;


    return 0;
}
