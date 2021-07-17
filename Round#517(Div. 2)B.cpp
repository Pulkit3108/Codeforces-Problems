#include<bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll N=1e7+10;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //cin>>T;
    while (T--)
    {
        int n;
        cin>>n;
        int i,j,k;
        int a[n-1],b[n-1];
        for(i=0;i<n-1;i++){ 
            cin>>a[i];
        }
        for(i=0;i<n-1;i++){ 
            cin>>b[i];
        }
        for(k=0;k<=3;k++){
            vector<int> t(n,0); 
            t[0]=k;
            bool flag=true;
            for(i=1;i<n;i++){
                if(!flag){ 
                    break;
                }
                for(j=0;j<3;j++){
                    int T=(t[i-1]&(1<<j))!=0;
                    int A=(a[i-1]&(1<<j))!=0;
                    int B=(b[i-1]&(1<<j))!=0;
                    int bit=-1;
                    for(int x:{0,1}) {
                        if((T|x)==A and (T&x)==B){
                            bit=x;
                        }
                    }
                    if(bit==-1){ 
                        flag=false;
                    }
                    else{ 
                        t[i]|=(bit*(1<<j));
                    }
                }
            }   
            if(!flag){ 
                continue;
            }
            cout<<"YES"<<endl;
            for(i=0;i<n;i++){
                cout<<t[i]<<" ";
            }
            cout<<endl;
            return 0;
        }
        cout<<"NO"<<endl;
    }
    return 0;
}
 
