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
        string s;
        cin>>s;
        int i,j=0;
        int x=s.length();
        vector<char> A(x);
        for(i=0;i<x;i++){
            A[i]=s[i];
        }
        sort(A.begin(),A.end());
        for(i=0;i<x;i++){
            if((A[0]+j)!=A[i]){
                cout<<"NO"<<endl;
                break;
            }
            j+=1;
        }
        if(j==x){
            cout<<"YES"<<endl;
        }
    }
    
    return 0;
}
