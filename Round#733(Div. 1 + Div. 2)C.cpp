#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int mod=1e9+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        int a[n],b[n];
        int i;
        ll c1=0,c2=0;
        for(i=0;i<n;i++){
            cin>>a[i];
            c1+=a[i];
        }
        for(i=0;i<n;i++){
            cin>>b[i];
            c2+=b[i];
        }
        sort(a,a+n);
        sort(b,b+n);
        int k=n/4;
        for(i=0;i<k;i++){
            c1-=a[i];
            c2-=b[i];
        }
        if(c1>=c2){
            cout<<0<<endl;
        }
        else{
            int i=k;
            int j=k-1;
            int r=n;
            int c=0;
            int cz=0;
            while(true){
                if(c1>=c2){
                    break;
                }
                c1+=100;
                cz+=1;
                if(j>=0){
                    c2+=b[j];
                    j-=1;
                }
                r+=1;
                if(r/4>k){
                    k+=1;
                    c1-=a[i];
                    i+=1;
                    if(cz<k){
                        c2-=b[j+1];
                        j+=1;
                    }
                }
                c+=1;
            }
            cout<<c<<endl;
        }
    }
    return 0;
}
