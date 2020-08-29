#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    int n,m,i,j;
    cin>>n>>m;
    string s[n];
    int a[m];
    int c=0;
    int b[m][5]={0};
    int k;
    for(i=0;i<n;i++){
        cin>>s[i];
    }
    for(i=0;i<m;i++){
        cin>>a[i];
    }
    for(i=0;i<m;i++){
        k=0;
        for(j=0;j<n;j++){
            b[i][s[j][i]-'A']++;
        }
        for(j=0;j<5;j++){
            k=max(k,b[i][j]);
        }
        c+=k*a[i];
    }
    cout<<c;
}
