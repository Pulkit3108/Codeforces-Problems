#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,i;
    cin>>n;
    vector<int> a(n);
    for(i=0; i<n;++i){
        cin>>a[i];
    }
    sort(a.begin(), a.end());
    a.resize(unique(a.begin(),a.end()) a.begin());
    if(a.size()>3){
        cout<<-1<< endl;
    } 
    else{
        if(a.size()==1){
            cout<<0<<endl;
        } 
        else if(a.size()==2){
            if((a[1]-a[0])%2==0){
                cout<<(a[1]-a[0])/2<<endl;
            } 
            else{
                cout<<a[1]-a[0]<<endl;
            }
        } 
        else{
            if(a[1]-a[0]!=a[2]-a[1]){
                cout<<-1<<endl;
            } 
            else{
                cout<<a[1]-a[0]<<endl;
            }
        }
    }
    return 0;
}
