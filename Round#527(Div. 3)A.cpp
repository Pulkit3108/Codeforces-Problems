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
        int n,k;
        cin>>n>>k;
        char c='a',s[n];
        int i,j=0,r;
        int x=n/k;
        for(i=0;i<k;i++){
            for(r=0;r<x;r++){
                s[j]=c+i;
                ++j;
            }
        }
        int w=n%k;
        for(i=0;i<w;i++){
            s[j]=c+i;
            ++j;
        }
        for(i=0;i<n;i++){
            printf("%c",s[i]);
        }
        printf("\n");

    }
    
    return 0;
}
