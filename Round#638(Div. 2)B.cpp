#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        int N,K;
        cin>>N>>K;
        set<int> s;
        for(int i=0;i<N;i++){
        int a;
        cin>>a;
        s.insert(a);
        }
        if(s.size()>K){
        cout<<-1<<endl;
        continue;
        }
        cout<<N*K<<endl;
        for(int i=0;i<N;i++){
            for(int b:s){
                cout<<b<<" ";
            }
            for(int j=0;j<K-(int)s.size();j++){
                cout<<1<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}
