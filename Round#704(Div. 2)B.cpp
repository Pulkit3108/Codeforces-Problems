#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        vector<int> a(n),b(n);
        map<int,int> mp;
        int i=0,j=0;
        for(i=0;i<n;i++){
            cin>>a[i];
            b[i]=a[i];
            mp[a[i]]=0;
        }
        sort(b.rbegin(),b.rend());
        vector<int> c;
        for(i=n-1;i>=0;i--){
            if(a[i]!=b[j]){
                c.push_back(a[i]);
                mp[a[i]]=1;
            }
            else{
                c.push_back(a[i]);
                mp[a[i]]=1;
                for(int j=c.size()-1;j>=0;j--){
                    cout<<c[j]<<" ";
                }
                while(mp[b[j]]==1){
                    j++;
                }
                c.clear();
            }
        }
        for(j=c.size()-1;j>=0;j--){
            cout<<c[j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
