#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string str;
    int len,i,k;
    while(cin>>str){
        len=str.size();
        k=0;
        for(i=0;i<len-1;i++){
            if(str[i]==str[i+1]){
                ++k;
                str.erase(i,2);
                len=str.size();
                i=-1;
            }
        }
        if(k%2!=0){
            printf("Yes");
        }
        else{
            printf("No");
        }
    }
}
