#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const int inf=1e9+10;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        int b,q,l,m; 
        cin>>b>>q>>l>>m;
        set<int> st;
        for(int i=0;i<m;i++){
            int x; 
            cin>>x;
            st.insert(x);
        }
        int p=0;
        while(abs(b)<=l){
            if(st.count(b)==0){ 
                p+=1;
            }
            int x=b;
            b*=q;
            if(abs(x)==abs(b)){
                if(st.count(x) && st.count(b)){
                    cout<<p<<endl; 
                    return 0;
                }
                else{
                    cout<<"inf"<<endl;
                    return 0;
                }
            }
        }
        cout<<p<<endl;;
    }
    return 0;
}

