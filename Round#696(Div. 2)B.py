#include<bits/stdc++.h>
using namespace std;
#define ll long long int
vector<int> v;
int n=1000000;
void prime(){    
    bool p[n+1]; 
    int i,j;
    memset(p,true,sizeof(p)); 
    for(i=2;i*i<=n;i++){ 
        if(p[i]==true){   
            for(j=i*i;j<=n;j+=i){
                p[j]=false; 
            }
        } 
    } 
    for(i=2;i<=n;i++){
       if(p[i]){ 
          v.push_back(i);
       }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    prime();
    ll t;
    cin>>t;
    while(t--){
        int d;
        cin>>d;
        int i,j;
        int k=1;
        for(i=0;i<v.size();i++){
            if(v[i]-1>=d){
                k*=v[i];
                j=v[i];
                break;
            }
        } 
        for(i=0;i<v.size();i++){
            if(v[i]-j>=d){
                k*=v[i];
                break;
            }
        }
        cout<<k<<endl;  
    }
    return 0;
}
