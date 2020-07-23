#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int N,M;
vector<int> f;
int d;
void hold(){
    int i;
    for(i=0;i<N;i++){
        if(--f[i]==0){
            d--;
        }
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>N>>M;
    f.assign(N,0);
    d=0;
    int i;
    for(i=0;i<M;i++){
        int a;
        cin>>a;
        a--;
        if(f[a]++==0){
            d++;
        }
        if(d==N){
            hold();
            cout<<'1';
        } 
        else{
            cout<<'0';
        }
    }
    cout<<'\n';
}
