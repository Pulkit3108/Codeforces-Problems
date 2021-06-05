#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T=1;
    //cin>>T;
    while(T--){
        int n;
        cin>>n;
        int a[n];
        int i,f=0,j;
        bool flag;
        for(i=0;i<n;i++){
            cin>>a[i];
            if(a[i]==29){
                f+=1;
            }
        }
        if(f>1){
            cout<<"NO"<<endl;
        }
        else{
            int m[]={31,28,31,30,31,30,31,31,30,31,30,31};
            for(i=0;i<12;i++){
                flag=true;
                for(j=0;j<n;j++){
                    int k=(i+j)%12;
                    if(m[k]!=a[j]){
                        flag=false;
                    }
                    if(k==1 && a[j]==29){
                        flag=true;
                    }     
                }
                if(flag){
                    break;
                }
            }
            if(flag){
                cout<<"YES"<<endl;
            }
            else{
                cout<<"NO"<<endl;
            }
        }
        
    }
    return 0;
}
