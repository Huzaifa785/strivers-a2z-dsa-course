#include <bits/stdc++.h>
using namespace std;

/* pattern 12
1        1
12      21
123    321
1234  4321
1234554321
 */

int solve_pattern(int n)
{
    int spaces = 2 * (n - 1);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j;
        }

        for (int j = 1; j <= spaces; j++)
        {
            cout << " ";
        }

        for (int j = i; j >= 1; j--)
        {
            cout << j;
        }

        cout << endl;
        spaces = spaces - 2;
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