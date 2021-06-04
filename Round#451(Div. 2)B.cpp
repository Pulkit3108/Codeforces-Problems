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
        int n,a,b;
        int k;
        int t=0,c1=0,c2=0;
        cin>>n>>a>>b;
        if(!(n%2!=0 and a%2==0 and b%2==0)){
            if(n%a==0){
                c1=n/a;
                t=1;
            }
            else if(n%b==0){
                c2=n/b;
                t=1;
            }
            else{
                if(a>b){
                    k=n;
                    while(k>0){
                        if(k%b==0){
                            c2=k/b;
                            t=1;
                            break;
                        }
                        c1+=1;
                        k-=a;
                    }
                }
                else{
                    k=n;
                    while(k>0){
                        if(k%a==0){
                            c1=k/a;
                            t=1;
                            break;
                        }
                        c2+=1;
                        k-=b;
                    }
                }
            }
        }
        if(t==1){
            cout<<"YES"<<endl;
            cout<<c1<<" "<<c2<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
