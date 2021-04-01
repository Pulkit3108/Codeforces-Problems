#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while(T--){
        ll n,i;
        cin>>n;
        vector<int> a(n);
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        int flag=0,d=0;
        if(n>=2){
            d=a[1]-a[0];
        }
        for(i=0;i<n-1;i++){   
            if(a[i+1]-a[i]!=d){
                flag=1;
                break;
            }
        }
        if(n==1 or n==2 or flag==0){
            cout<<0<<endl;
        }
        else{
            ll d=0,m=0;
            flag=0;
            for(i=1;i<n-1;i++){
                if(a[i]<a[i-1] and a[i]<a[i+1]){
                    d=a[i+1]-a[i];
                    m=a[i-1]+d-a[i];
                    break;
                }
                else if(a[i]>a[i-1] and a[i]>a[i+1]){
                    d=a[i]-a[i-1];
                    m=a[i]+d-a[i+1];
                    break;
                }
            }
            if(m!=0){
                for(i=0;i<n-1;i++){
                    if(a[i+1]!=(a[i]+d)%m){
                        flag=1;
                        break;
                    }
 
                }   
            }
            if(a[0]>=m){
                flag=1;
            }
            if(flag==1 || m==0){
                cout<<-1<<endl;
            }
            else{
                cout<<m<<" "<<d<<endl;
            }
        }
    }
    return 0;
}
