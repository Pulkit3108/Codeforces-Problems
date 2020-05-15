#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,x,y;
    string s;
    cin>>n>>x>>y>>s;
    int ans=0,i;
    for(i=n-x;i<n;i++){
        if(i==n-y-1){
            if(s[i]=='0'){
                ans+=1;
            }
        }
        else{
            if(s[i]=='1'){
                ans+=1;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}
