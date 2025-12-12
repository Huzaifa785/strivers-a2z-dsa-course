#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, y;
    string fruit, fruit1;

    // basic input and output
    // cin >> x;
    // cout << "hey mr. " << x;

    // taking 2 numbers as input
    // cin >> x >> y;
    // cout << "hey mr. " << x << " and mr. " << y;

    // use of \n for printing on newline
    // cin >> x >> y;
    // cout << "hey mr. " << x << "\nand mr. " << y;

    // use of endl for printing on newline
    // cin >> x >> y;
    // cout << "hey mr. " << x << endl << "and mr. " << y;

    // taking string inputs (this will take only the first word before space, ex. if we give Water Melon, it'll only print Water)
    // cin >> fruit;
    // cout << fruit;

    // to overcome this we'll have to either use two variables and print like this
    // cin >> fruit >> fruit1;
    // cout << fruit << fruit1;

    // or we could use getline function to read the entire line
    getline(cin, fruit);
    cout << fruit;

    // yeah so this all about for this chapter, let's move on to data types

    return 0;
}