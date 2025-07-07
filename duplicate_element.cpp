#include<iostream>
using namespace std;
int main(){
int n, arr[100];
cin >> n;
for (int i = 0; i < n; i++)
    cin >> arr[i];

for (int i = 0; i < n; i++) {
    bool printed = false;
    for (int j = 0; j < i; j++) {
        if (arr[i] == arr[j]) {
            printed = true;
            break;
        }
    }
    if (!printed) {
        int count = 0;
        for (int k = 0; k < n; k++) {
            if (arr[i] == arr[k])
                count++;
        }
        if (count > 1)
            cout << arr[i] << " appears " << count << " times" << endl;
    }
}
return 0;
}