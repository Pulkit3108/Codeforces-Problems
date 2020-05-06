#include<bits/stdc++.h>
#include<numeric> 
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
        int n,k;
        string s;
        cin>>n>>k>>s;
        vector<int> S(26);
        int i=0;
        for(i=0;s[i]!='\0';i++){
            S[s[i]-'A']++;
        }
        int x=S[0];
        for(i=0;i<k;i++){
            x=min(x,S[i]);
        }
        x*=k;
        cout<<x<<endl;
    return 0;
}
