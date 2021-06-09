#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T=1;
    //cin>>T;
    while(T--){
        char a[9][9];
        int i,j;
        int x,y,f=1;
        for(i=0;i<9;i++){
            for(j=0;j<9;j++){
                cin>>a[i][j];
            }
        }
        cin>>x>>y;
        x=(x%3+2)%3;
        y=(y%3+2)%3;
        for(i=3*x;i<3*x+3;i++){
            for(j=3*y;j<3*y+3;j++){
                if(a[i][j]=='.'){
                    a[i][j]='!';
                    f=0;
                }
            }
        }
        if(f){
            for(i=0;i<9;i++){
                for(j=0;j<9;j++){
                    if(a[i][j]=='.'){
                        a[i][j]='!';
                    }
                }
            }
        }
        for(i=0;i<9;i++){
            for(j=0;j<9;j++){
                cout<<a[i][j];
                if(j%3==2){
                    cout<<" ";
                }
            }
            cout<<endl;
            if(i%3==2){
                cout<<endl;
            }
        }        
    }
    return 0;
}
