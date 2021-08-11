#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define ld long double
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        int n,k;
        cin>>n>>k;
        int a[n],t[n];
        for(int i=0;i<n;i++){
            cin>>a[i];
            t[i]=a[i];
        }
        unordered_map<int,int> mp;
        sort(t,t+n);
        int c=0;
        for(int i=0;i<n;i++){
            mp[t[i]]=i;
        }
        for(int i=0;i<n;i++){
            if(mp[a[i]]==0 or i==0 or t[mp[a[i]]-1]!=a[i-1]){
                c+=1;
            }
        }
        if(c>k){
            cout<<"NO"<<endl;
        }
        else{
            cout<<"YES"<<endl;
        }
    }
    return 0;
}
