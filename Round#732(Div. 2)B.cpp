#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while (T--)
    {
        int n,m;
        cin>>n>>m;
        int i,j;
        vector<string> x;
        int c[m][26];
        memset(c,0,sizeof(c));
        for(i=0;i<(n*2-1);i++){
            string s;
            cin>>s;
            x.push_back(s);
            for(j=0;j<m;j++){
                c[j][s[j]-'a']+=1;
            }
        }  
        string p="";
        for(i=0;i<m;i++){
            for(j=0;j<26;j++){
                if(c[i][j]%2!=0){
                    p.push_back((char)(97+j));
                }
            }
        } 
        cout<<p<<endl;
    }
    return 0;
}
