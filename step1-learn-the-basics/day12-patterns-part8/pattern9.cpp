#include <bits/stdc++.h>
using namespace std;

/* pattern 9
      *
     ***
    *****
   *******
  *********
  *********
   *******
    *****
     ***
      *
*/

int triangle_pattern(int n)
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

int reverse_triangle_pattern(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++) {
            cout << " ";
        }

        for (int j = 0; j < n*2 - (2*i + 1);j++) {
            cout << "*";
        }

        for (int j = 0; j < i; j++) {
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

        triangle_pattern(n);
        reverse_triangle_pattern(n);

        cout << endl;
    }

    return 0;
}