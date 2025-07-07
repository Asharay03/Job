#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Start coding here
    int N,M;
    cout<<"Enter you array Size= ";
    cin>>N;
    cout<<"Enter you Target= ";
    cin>>M;
    vector<int> K(N);
    for(int j=0;j<N;j++){
        cout<<"Enter your "<<j+1<<" input =";
        cin>>K[j];
    }
    bool found = false;
    for(int j=0;j<N;j++){
        for(int k=0;k<j;k++){
            if((long long)K[j]*K[k]==M){
                found = true;
            }
        }
    }   
    if(found){
        cout<<"YES";
    } else {
        cout<<"NO";
    }
    return 0;
}