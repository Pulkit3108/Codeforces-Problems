#include <bits/stdc++.h>
using namespace std;
#define ll long long int 
const ll N=1e7+10;
int findequal(vector<int> &x,int k){
    int t=0;
    int s=0;
    int i=0,j=0;
    for(i=0;i<x.size();i++){
        s+=x[i];
        if(s==k){
            t+=(i-j);
            j=i+1;
            s=0;
        }
        else if(s>k){
            t=-1;
            break;
        }
    }
    return t;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll T;
    cin>>T;
    while (T--)
    {
        int n;
        cin>>n;
        vector<int> a(n);
        int i;
        int s=0;
        for(i=0;i<n;i++){
            cin>>a[i];
            s+=a[i];
        }
        int c=n-1;
        for(i=1;i*i<=s+1;i++){
            if(s%i==0){
                int f1=i;
                int f2=s/i;
                int a1=findequal(a,f1);
                int a2=findequal(a,f2);
                if(a1!=-1){
                    c=min(c,a1);
                }
                if(a2!=-1){
                    c=min(c,a2);
                }
            }
        }
        cout<<c<<endl;
    }
    return 0;
}
 
