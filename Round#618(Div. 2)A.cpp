#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin>>t;
    while(t--){
        int n,k=0;
        cin>>n;
        vector<int> A(n);
        int i=0;
        for(i=0;i<n;i++){
            cin>>A[i];
        }
        vector<int>::iterator it; 
        it=find(A.begin(),A.end(),0); 
        while(it!=A.end()){
            k+=1;
            A[it-A.begin()]+=1;
            it=find(A.begin(),A.end(),0); 
        }
        if(accumulate(A.begin(),A.end(),0)==0){
            k+=1;
        }
        cout<<k<<endl;
    }

    return 0;
}
