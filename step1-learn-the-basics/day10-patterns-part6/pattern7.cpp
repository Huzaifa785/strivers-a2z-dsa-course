#include <bits/stdc++.h>
using namespace std;

/* pattern 7
      *
     ***
    *****
   *******
  *********
*/

int solve_pattern(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }

        for (int j = 0; j < i * 2 + 1;j++) {
            cout << "*";
        }

        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        cout << endl;
    }
}

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;

        solve_pattern(n);

        cout << endl;
    }

    return 0;
}