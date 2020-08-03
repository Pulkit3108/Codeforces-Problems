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
int to(char a,char b){
    if(a>b){
        return('Z'-a+b-'A'+1);
    }
    else{
        return(a-'A'+'Z'-b+1);
    } 
}
int main(){
    int n;
    cin>>n;
    char A[n];
    scanf("%s",A);
    int a,b,c,d,m=INT_MAX;
    for (int i=0; i<n-3; i++){
        a=min(A[i]-'A','Z'-A[i]+1);
        b=min(abs(A[i+1]-'C'),to(A[i+1],'C'));
        c=min(abs(A[i+2]-'T'),to(A[i+2],'T'));
        d=min(abs(A[i+3]-'G'),to(A[i+3],'G'));
        m=min(m,a+b+c+d);
    }
    cout<<m<<endl;
    return 0;
}
