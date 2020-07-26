#include<bits/stdc++.h>
using namespace std;
#define ll long long int
bool isVowel(char a){
    if(a=='a' || a=='e' || a=='i' || a=='o' || a=='u'){
        return(true);
    }
    else{
        return(false);
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string S,T;
    cin>>S>>T;
    if(S.size()!=T.size()){
        cout<<"No\n";
        return 0;
    }
    int c=1,i;
    for(i=0;i<S.size();++i){
        if((isVowel(S[i]) && isVowel(T[i])) || (isVowel(S[i]) == false && isVowel(T[i]) == false)){
            continue;
        }
        else{
            c=0;
            break;
        }
    }
    if(c){
        cout<<"Yes\n";
    }
    else{
        cout<<"No\n";
    }
    return 0;
}
