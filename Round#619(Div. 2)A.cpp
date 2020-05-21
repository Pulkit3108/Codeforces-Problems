#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin>>T;
    while(T--){
        string s1,s2,s3;
        cin>>s1>>s2>>s3;
        int x=1;
        for(int i=0;s3[i]!='\0';i++){
            if(s3[i]==s1[i]){
                s2[i]=s3[i];
            }
            else if(s3[i]==s2[i]){
                s1[i]=s3[i];
            }
            else{
                cout<<"NO"<<endl;
                x=0;
                break;
            }
        }
        if(x==1){
            cout<<"YES"<<endl;
        }
        
        }
    return(0);
}
