#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int a[150];
int b[150];
int vis[10005];
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    //scanf("%d",&T);
    while(T--){   
        int n;
        scanf("%d",&n);
        int i;        
        
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
        }    
        sort(a,a+n);
        int l=a[n-1];
        int s=0;
        for(i=0;i<n;i++){
            if(l%a[i]==0 && vis[a[i]]==0){
                vis[a[i]]=1;
                continue;
            }
            else{
                b[s++]=a[i];
            }
        }
        sort(b,b+s);
        printf("%d %d\n",l,b[s-1]);
    
    }
    return 0;
}
