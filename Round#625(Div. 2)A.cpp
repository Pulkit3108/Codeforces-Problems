#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main(){
    int n;
    scanf("%d",&n);
    vector<int> R(n);
    vector<int> B(n);
    int i,j;
    for(i=0;i<n;i++){
        scanf("%d",&R[i]);
    }
    for(i=0;i<n;i++){
        scanf("%d",&B[i]);
    }
    
    int r=0,b=0;
    for(i=0;i<n;i++){
        if(R[i]!=B[i]){
            if(R[i]==1){
                r+=1;
            }
            else if(B[i]==1){
                b+=1;
            }
        }    
    }
    int c;
    if(r==0){
        c=-1;
    }
    else{
        if(b<r){
            c=1;
        }
        else{
            c=b/r+1;
        }
    }
    printf("%d\n",c);
}
