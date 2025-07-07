#include <iostream>
#include <vector>
using namespace std;

int main() {

    // Creating an empty vector
    vector<int> v1={1,2,3,4,5};
    cout<<"v1: ";
    for(int i=0;i<v1.size();i++){
        cout<<v1[i]<<" ";
    }
    return 0;
}
