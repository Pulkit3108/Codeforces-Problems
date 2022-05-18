#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const int inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        vector<string> p(n);
        set<string> st;
        for(auto &it:p) {
            cin>>it;
            st.insert(it);
        }
        int c=0;
        vector<bool> f(n,false);
        for(int i=0;i<n;++i){
            if(f[i]){
                continue;
            }
            vector<int> s;
            for(int j=i+1;j<n;++j){
                if(p[i]==p[j]){
                    s.push_back(j);
                    f[j]=true;
                    ++c;
                    for(int k=0;k<4 && p[i]==p[j];++k){
                        for(char ch='0';ch<='9';++ch){
                            string t=p[j];
                            t[k]=ch;

                            if(!st.count(t)){
                                st.insert(t);
                                p[j] = t;
                                break;
                            }
                        }
                    }
                }
            }
        }
        cout<<c<<endl;
        for(auto &it:p){
            cout<<it<<endl;
        }
    }
    return 0;
}
