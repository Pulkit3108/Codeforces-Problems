#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int f(int n){
    int x=1;
    while(n!=0){
        if(n%10!=0){
            x*=n%10;
        }
        n=n/10;
    }
    return(x);
}
int g(int n){
    if(n<10){
        return(n);
    }
    else{
        return(g(f(n)));
    }
}
int x[10][1000005];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T,i,j;
    cin>>T;
    for(i=1;i<=1000000;i++){
        x[g(i)][i]++;
    }
    for(i=1;i<10;i++){
        for(j=1;j<=1000000;j++){
            x[i][j]+=x[i][j-1];
        }
    }
    while(T--){
        int l,r,k;
        cin>>l>>r>>k;
        cout<<x[k][r]-x[k][l-1]<<"\n";
        
    }  
    return 0;
}
