#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin>>n;
    char A[n][n];
    int i,j,k=0;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            cin>>A[i][j];
        }
    }
    for(i=1;i<n-1;i++){
        for(j=1;j<n-1;j++){
            if(A[i][j]=='X'){
                if(A[i][j]==A[i-1][j-1] && A[i][j]==A[i-1][j+1] && A[i][j]==A[i+1][j-1] && A[i][j]==A[i+1][j+1]){
                    k+=1;
                }
            }       
        }
    }
    cout<<k<<endl;
}
