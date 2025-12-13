#include <bits/stdc++.h>
using namespace std;

int main()
{
    // 1d array
    // int arr[5];
    // cin >> arr[0] >> arr[1] >> arr[2] >> arr[3] >> arr[4];

    // modifying elements of an array
    // arr[2] = 7;

    // cout << arr[2];

    // 2d array
    // int arr[3][5];
    //        ⬇️  ⬇️     
    //       row column

    // arr[1][2] = 99; // it's stored in second row and at third column
    //    ⬇️  ⬇️     
    //   row column

    // cout << arr[1][2] << endl; // prints 99
    // cout << arr[3][5]; // prints a garbage value

    // ============================= //

    // strings
    string name = "work hard!";

    cout << name << endl;
    cout << name[2] << endl; // prints 3
    cout << name[4] << endl; // prints empty space

    int len = name.size();
    cout << name[len - 1] << endl; // prints last character, that is !

    // modifying characters in a string
    name[len - 1] = '.'; // updates '!' to '.'
    cout << name;
    return 0;
}