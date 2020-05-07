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
        if(n==2 and m==2){
            cout<<"YES"<<endl;
        }
        else if(n<2){
            cout<<"YES"<<endl;
        }
        else if(m<2){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }


    }
    
    return 0;
}
