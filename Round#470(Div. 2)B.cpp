#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const int N = 1e6+5;
vector<int> p(N,1);                         
void sieve(){                               
    p[0]=0;
    p[1]=0;
    int i,j;
    for(i=2;i<N;i++){
        p[i]=i;
    }
    for(i=2;i*i<N;i++){     
        if(p[i]==i){
            for(j=i*i;j<N;j+=i){
                p[j]=i;
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while(T--){ 
        sieve();
        int x;
        cin>>x;
        int y,n=-1,i;
        y=x;
        for(i=2;i*i<=x;i++){
            if(x%i==0){
                n=i;
                while(x%i==0){
                    x/=i;
                }   
            }
        }
        if(x!=1){
            n=max(n,x);
        }
        int l=y-n+1;
        int r=y;
        int c=INT_MAX;
        for(i=l;i<=r;i++){
            int m=p[i];
            int t=i;
            while(t!=1){
                int f=p[t];
                m=max(m,f);
                while(t%f==0){
                    t/=f;
                }
            }
            if(i-m+1>=3){
                c=min(c,i-m+1);
            }
        }
        cout<<c<<endl;
    }
    return 0;
}
