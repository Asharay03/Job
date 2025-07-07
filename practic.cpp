#include <iostream>
#include <vector>
using namespace std;
// bool isprime(int n){
//     for(
//         int i = 2; i < n; i++){
//         if(n%i == 0){
//             return false;
//         }
//         return true;
//     }

// }

// int main(){
// int a = 36;
// int prev = 2;

// for (int i = 3; i < a; i++)
// {
//    if(isprime(i)){
//        if(i + prev ==  a){
// cout<<"("<<prev<<","<<i<<")"<<endl;
// return 0;
//        }
//  prev = i;
       
//    }  
// }
// }
// int main(){
// int n, count = 0;
// cin >> n;
// while (n != 0) {
//     count++;
//     n = n / 10;
// }
// cout << "Digits = " << count;
// }
int i;
int a[5]={1,2,3,4,5};

int main() {
	for(i=4;i>=0;i--){
		cout << a[i] << " ";
	}
	return 0;
}