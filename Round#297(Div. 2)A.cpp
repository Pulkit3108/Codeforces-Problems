#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while (T--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int c=0;
        map<char,int> mp;
        int i=0;
        for(i=0;i<s.size();i++){
            if(i%2==0){
                mp[s[i]]+=1;
            }
            else{
                if(mp[tolower(s[i])]>0){
                    mp[tolower(s[i])]-=1;
                }
                else{
                    c+=1;
                }
            }
        }
        cout<<c<<endl;
        
        
    }
    return 0;
}
