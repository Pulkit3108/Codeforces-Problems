#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,i,j;
    string s,t;
    cin>>n>>s>>t;
    vector<int> A;
    for(i=0;i<n;++i){
        if(s[i]==t[i]){ 
            continue;
        }
        int q=-1;
        for(j=i+1;j<n;++j){
            if(s[j]==t[i]){
                q=j;
                break;
            }
        }
        if(q==-1){
            cout<<-1<<endl;
            return 0;
        }
        for(j=q-1;j>=i;--j){
            swap(s[j],s[j+1]);
            A.push_back(j+1);
        }
    }
    cout<<A.size()<<endl;
    for(i=0;i<A.size();++i){
        cout<<A[i]<<" ";
    }
    cout<<endl;
    return 0;
}
