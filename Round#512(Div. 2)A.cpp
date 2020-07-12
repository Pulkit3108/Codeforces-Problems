#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    //scanf("%d",&T);
    while(T--){   
        int n;
        scanf("%d",&n);
        int i;
        int c=0;        
        vector<int> a(n);
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
            if(a[i]==1){
                c=1;
                break;
            }
        }    
        if(c==0){
            printf("EASY");
        }
        else{
            printf("HARD");
        }
      
    
    }
    return 0;
}
