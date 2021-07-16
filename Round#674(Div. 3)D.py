#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const int N=1e5+10;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while (T--)
    {
        ll n;
        cin>>n;
        ll a[n];
        int i;
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        set<ll> st;
        st.insert(0);
        ll s=0;
        ll c=0;
        for(i=0;i<n;i++){
            s+=a[i];
            if(st.find(s)!=st.end()){
                c+=1;
                s=a[i];
                st.clear();
                st.insert(0);
            }
            st.insert(s);
        }
        cout<<c<<endl;  
    }
    return 0;
}
 
