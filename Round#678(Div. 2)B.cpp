#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        int n,i,j;
        cin>>n;
        if(n%2==0){
            for(i=0;i<n;i++){
                for(j=0;j<n;j++){
                    if(i==j || n-i-1==j){
                        cout<<1<<" ";
                    }
                    else{
                        cout<<0<<" ";
                    }
                }
                cout<<"\n";
            }
        }
        else{
            for(i=0;i<n;i++){
                for(j=0;j<n;j++){
                    if(i==j || n-i-1==j || (i==n/2-1 && j==n/2) || (i==n/2 && j==n/2-1)){
                        cout<<1<<" ";
                    }
                    else{
                        cout<<0<<" ";
                    }
                }
            cout<<"\n";
            }
        }
    }
    return 0;
}
