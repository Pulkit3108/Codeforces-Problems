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
    int a=0;
    for(i=1;i<n-1;i++){
        if(A[i]==0 and A[i-1]==1 and A[i+1]==1){
            a+=1;
            A[i+1]=0;
        }
    }
    cout<<a<<endl;
    return 0;
}
