#include <bits/stdc++.h>
using namespace std;

/* pattern 5
 * * * * *
 * * * *
 * * *
 * *
 *
 */

int solve_pattern(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = n; j > i; j--)
        {
            cout << "* ";
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