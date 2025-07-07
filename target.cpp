#include <iostream>
using namespace std;
int main()
{
    int i,j;
    int a[5];
    cout <<"Enter your 5 digit= ";
    for(j=0;j<5;j++)
    {cin>>a[j];}
    int target;
    cout<<"Enter your target= ";
    cin>>target;
    for(j=0;j<5;j++){
      for(i=j+1;i<5;i++){
      if(a[i]+a[j]==target)
      { 
        cout<<"This is index of two number "<<j<<" "<<i<<" ";
        return 0;
      }
      }
    }
      cout<<"not found";
      return 0; 
}