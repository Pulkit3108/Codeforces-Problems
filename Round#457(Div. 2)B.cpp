#include<bits/stdc++.h>
using namespace std;
#define ll long long int

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){
        ll n;
        int m=0,k;
        cin>>n>>k;
        int i,j;
        map<int,int> c;
        for(i=0;i<=63;i++){
            if((n>>i)&1){ 
                c[i]++; 
                m++;
            }
        }
        if(m>k){ 
            cout<<"No"<<endl;
        }
        else{
            for(i=63;i>=-63;i--){
                if(m+c[i]<=k){
                    m+=c[i],c[i-1]+=c[i]*2,c[i]=0;
                }
                else{
                    break;
                }
            }
            cout<<"Yes"<<endl;
            multiset<int> ms;
            for(i=63;i>=-63;i--){
                for(j=0;j<c[i];j++){
                    ms.insert(i);
                }
            }
            while(ms.size()<k){
                int u=*ms.begin();
                ms.erase(ms.begin());
                ms.insert(u-1); 
                ms.insert(u-1);
            }
            for(auto it=ms.rbegin();it!=ms.rend();it++){
                cout<<*it<<" ";
            }
            cout<<endl;
        }
    }
    return 0;
}
