#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define sc1(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%lld %lld",&a,&b)
#define pf1(a) printf("%lld\n",a)
#define pf2(a,b) printf("%lld %lld\n",a,b)
#define vsort(v) sort(v.begin(), v.end())
#define forn(i,n) for(ll i=0; i<n; i++)
#define pb push_back
const int mod=1e9+7;
const int maxn=1e3+7;
const int maxm=1e2+7;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T=1;
    //sc1(T);
    while(T--){
        // code   
        int n,k;
        cin>>n>>k;
        int a[4][105]={0};
        int i,j;
        for(i=1;i<=2;i++){
            if(k<2){ 
                break;
            }
            for(j=1;j<n/2;j++){
                if(k<2){
                    break;
                }
                k-=2;
            a[i][j]=a[i][n-j-1]=1;
            }
        }
        for(j=1;j<=2;j++){
            if(k==0){
                break;
            }
            k--;
            a[j][n/2]=1;
        }
        cout<<"YES"<<endl;
        for(i=0;i<4;i++){
            for(j=0;j<n;j++){
                if(a[i][j]==1){
                    cout<<'#';
                }
                else{
                    cout<<'.';
                }
            }
            cout<<endl;
        }
    }
    return 0;
}
