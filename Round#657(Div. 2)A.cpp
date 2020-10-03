#include <bits/stdc++.h>
using namespace std;
int n;
string s;
string b="abacaba";
int occ(){
    int c=0;
    int i,j;
    for(i=0;i<n-6;i++){
        bool x=true;
        for(j=0;j<7;j++){
            if(s[i+j]!=b[j]){
                x=false;
            }
        }
        if(x){
            c+=1;
        }
    }
    return(c);
}
void fill(){
    int i;
    for(i=0;i<n;i++){
        if(s[i]=='?'){
            s[i]='x';
        }
    }
}
int main(){
    int T;
    cin>>T;
    while(T--){
        cin>>n;
        cin>>s;
        if(occ()==1){
            fill();
            cout<<"Yes\n";
            cout<<s<<"\n";
        }
        else if(occ()>1){
            cout<<"No\n";
        }
        else{
            int i,j;
            bool x=true;
            for(i=0;i<n-6;i++){
                bool t=true;
                vector<int> v;
                for(j=0;j<7;j++){
                    if(s[i+j]!=b[j]){
                        if(s[i+j]=='?'){
                            s[i+j]=b[j];
                            v.push_back(i+j);
                        }
                        else{
                            t=false;
                        }
                    }
                }
                if(t){
                    if(occ()==1){
                        fill();
                        x=false;
                        cout<<"Yes\n";
                        cout<<s<<"\n";
                        break;
                    }
                }
                for(int p:v){
                    s[p]='?';
                }
                v.clear();
            }
            if(x){
                cout<<"No\n";
            }
        }
    }
    return 0;
}
