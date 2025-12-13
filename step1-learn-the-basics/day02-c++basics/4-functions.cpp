#include <bits/stdc++.h>
using namespace std;

// void function without parameters
void printName(string name) {
    cout << "hey " << name;
}

// parametrized void function
void sum(int num1, int num2) {
    cout << num1 + num2;
}

// int function with parameters
int add(int num1, int num2) {
    return num1 + num2;
}

// pass by value example
int doSomethingWithNum(int num) {
    cout << "value outside main "  << num << endl;
    num += 7;
    cout << "value outside main "  << num << endl;
    num += 7;
    cout << "final value outside main "  << num << endl << endl;
}

// pass by reference example
int tortureNum(int &num) {
    cout << "value outside main "  << num << endl;
    num += 7;
    cout << "value outside main "  << num << endl;
    num += 7;
    cout << "final value outside main "  << num << endl << endl;
}

// modify array - pass by reference example
int modifyArray(int arr[], int n) {
    arr[0] += 7;
    cout << "value inside modifyArray function " << arr[0] << endl;
}

int main()
{
    // int num1, num2;
    // cin >> num1 >> num2;

    // sum(num1, num2);

    // ===
    // string name;
    // cin >> name;
    // printName(name);

    // ===
    // int res = add(num1, num2);
    // cout << res;
    // return 0;

    // ====================

    // pass by value - it will make a copy of our variable and do computations on it without changing the original
    // int num = 7;
    // doSomethingWithNum(num);

    // cout << "value inside int main " << num; // this will be print 7 only because it doesn't change original value in pass by value
    
    // pass by reference - it will madify the original value
    // tortureNum(num);

    // cout << "value inside int main " << num; // this will be print modified value after all calculations in tortureNum function

    // ========================

    // arrays are always pass by reference, and it will always modify the original value whenever we pass it as an argument
    int n = 5;
    int arr[n];

    for (int i = 0; i<n; i=i+1) {
        cin >> arr[i];
    }

    modifyArray(arr, n);

    for (int i = 0; i < n; i = i + 1)
    {
        cout << arr[i] << endl;
    }

    cout << "value inside int main " << arr[0];

    return 0;
}