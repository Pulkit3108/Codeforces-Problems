#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        ll a,b,c,t,d,c1,c2;
        cin>>a>>b;
        if(a==b){
            c=0;
        }
        if(a<b){
            t=a;
            a=b;
            b=t;
        }
        if(a>b){
            if((a-b)%5==0){
                c=(a-b)/5;
            }
            else if((a-b)%5>0){
                d=(a-b)%5;
                c1=(a-b)/5;
                if(d%2==0){
                    c2=d/2;
                    c=c1+c2;
                }
                else if(d%2>0){
                    c2=d/2;
                    c=c1+c2+1;
                }
                else if(d%2<0){
                    c=c1+1;
                }
            }
            else if((a-b)%5<0){
                if((a-b)%2==0){
                    c=(a-b)/2;
                }
                else if((a-b)%2>0){
                    c1=(a-b)/2;
                    c=c1+1;
                }
                else if((a-b)%2<0){
                    c=1;
                }
            }

        }
        cout<<c<<endl;
    }
    return 0;
}
