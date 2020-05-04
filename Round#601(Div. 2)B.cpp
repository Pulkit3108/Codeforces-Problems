#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int findSecondSmallest(vector<int> arr, int n){
   int smallest, secondSmallest;
   if(arr[0]<arr[1]){
      smallest = arr[0];
      secondSmallest = arr[1];
   }
   else {
      smallest = arr[1];
      secondSmallest = arr[0];
   }
   for(int i=0; i<n; i++) {
      if(smallest>arr[i]) { 
         secondSmallest = smallest;
         smallest = arr[i];
      }
      else if(arr[i] < secondSmallest){
         secondSmallest = arr[i];
      }
   }
   return secondSmallest;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    while(T--){
        int n,m,i;
        ll c;
        cin>>n>>m;
        vector<int> a(n);
        for(i=0;i<n;i++){
            cin>>a[i];
        }
        if(m==1 or n==2 or m<n){
            c=-1;
            cout<<c<<endl;
            continue;
        }
        if(n==m){
            c=2*(accumulate(a.begin(), a.end(), 0));
            cout<<c<<endl;
            for(i=1;i<n;i++){
                cout<<i<<" "<<i+1<<endl;
            }
            cout<<n<<" "<<1<<endl;
            continue;
        }
        else{
            c=2*(accumulate(a.begin(), a.end(), 0));
            int u=*min_element(a.begin(), a.end());
            int x=min_element(a.begin(),a.end()) - a.begin();
            int v=findSecondSmallest(a,n);
            vector<int>::iterator indx=lower_bound(a.begin(),a.end(),v);
            int y=indx-a.begin();
            c+=(m-n)*(u+v);
            for(i=1;i<n;i++){
                cout<<i<<" "<<i+1<<endl;
            }
            cout<<n<<" "<<1<<endl;
            for(i=2;i<=(m-n);i++){
                cout<<x<<" "<<y<<endl;
            }
            continue;
        }
    }
    return 0;
}
