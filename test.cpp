// #include <iostream>
// using namespace std;

// bool isPrime(int n) {
//     for (int i = 2; i < n; i++)
//         if (n % i == 0) 
//     return false;
// return true;
// }

// int main() {
//     int num;
//     cin >> num;

//     int prev = 2;

//     for (int i = 3; i < num; i++) {
//         if (isPrime(i)) {
//             if (prev + i == num) {
//                 cout << prev << " + " << i << " = " << num;
//                 return 0;
//             }
//             prev = i;
//         }
//     }
//     cout << "Not found";
// }

#include <iostream>
#include <iomanip>
#include <limits>
#include <string>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";
    int a;
    double b;
    string c;
    cin>>a;
    cin>>b;
    // cin.ignore();
    cin>>c;
    cout<<i+a<<endl;
    cout << fixed << setprecision(1) << d + b << endl;
    string e=s+c;
    cout<<e;

    return 0;
}
