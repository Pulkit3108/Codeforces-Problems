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
        string s;
        cin>>s;
        deque<char> dq;
        int i=0,c=1;
        char m='a',ch;
        for(i=0;i<s.size();i++){
            m=max(m,s[i]);
            dq.push_back(s[i]);
        }
        for(ch=m;ch>='a';ch--){
            if(dq.size()==0){
                c=0;
                break;
            }
            if(dq.front()==ch){
                dq.pop_front();
            }
            else if(dq.back()==ch){
                dq.pop_back();
            }
            else{
                c=0;
                break;
            }
        }
        if(c==1 and dq.size()==0){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
