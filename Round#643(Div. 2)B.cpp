#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        int i;
        vector<int> a(n);
        for(i=0;i<n;++i){
            scanf("%d",&a[i]);
        }
        sort(a.begin(),a.end());
        int x=0;
        int c=0;
        for(i=0;i<n;++i){
            x+=1;
            if(x==a[i]){
                c+=1;
                x=0;
            }
        }
        printf("%d\n",c);

    }
    
    return 0;
}
