#include <iostream>
#include <climits>
using namespace std;
int main()
{
    int i, max=INT_MIN;
    int second_max=INT_MIN;
    int a[5];
    for(i=0;i<5;i++){
        cout<<"Enter your "<<i+1<<" number = ";
        cin>>a[i];
        if(a[i]>max)
          {
           second_max=max;
           max=a[i];
          }
        else if(a[i] > second_max && a[i] != max) {
            second_max = a[i];
        }
        
    }
    if(second_max == INT_MIN)
        cout << "No second largest element (all values might be equal)." << endl;
    else
        cout << "Second largest element is: " << second_max << endl;
}
