#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T = 1;
    //cin>>T;
    while (T--){
        string s,t;
        cin>>s>>t;
        cout<<s<<" "<<t<<endl;
        int n;
        cin>>n;
        while(n--){
            string a,b;
            cin>>a>>b;
            if(a==s){
                s=b;
            }
            else if(a==t){
                t=b;
            }
            cout<<s<<" "<<t<<endl;
        }
    }
    return 0;
}
