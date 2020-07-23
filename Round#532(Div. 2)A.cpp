#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define sc1(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d %d",&a,&b)
#define pf1(a) printf("%d\n",a)
#define pf2(a,b) printf("%lld %lld\n",a,b)
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    //sc1(T);
    while(T--){
        int N,K;
        vector<int> A;
        sc2(N,K);
        A.resize(N);
        int i;
        for(i=0;i<N;i++){
            sc1(A[i]);
        }
        int m=0;
        int b;
        for(b=0;b<N;b++){
            int s=0;
            for(i=0;i<N;i++){
                if(i%K!=b%K){
                    s+=A[i];
                }
            }
            m=max(m,abs(s));
        }
        pf1(m);
    }  
    return 0;
}
