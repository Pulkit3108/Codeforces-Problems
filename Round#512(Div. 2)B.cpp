#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    //scanf("%d",&T);
    while(T--){   
        int n,d;
        scanf("%d%d",&n,&d);
        int m;
        scanf("%d",&m);
        int i;     
        vector<int> x(m);
        vector<int> y(m);
        for(i=0;i<m;i++){
            scanf("%d%d",&x[i],&y[i]);
        }    
        for(i=0;i<m;i++){
            if((x[i]+y[i])>=d && (x[i]+y[i])<=((2*n)-d) && (x[i]-y[i])>=(-d) && (x[i]-y[i])<=d){
                printf("YES\n");
            }
            else{
                printf("NO\n");
            }
        }  
      
    
    }
    return 0;
}
