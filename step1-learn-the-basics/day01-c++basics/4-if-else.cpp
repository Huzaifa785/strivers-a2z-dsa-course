#include <bits/stdc++.h>
using namespace std;

/*
list of problems for practicing if-else:

1. age - adult or not
write a program that takes an input of age and prints if you are adult or not

2. school grading system
a school has following rules for grading system:
a. below 25 - f
b. 25 to 44 - e
c. 45 to 49 - d
d. 50 to 59 - c
e. 60 to 79 — b
f. 80 to 100 - a
ask user to enter marks and print the corresponding grade.

3. eligible for job or not
take the age from the user and then decide accordingly
a. if age < 18,
print-> not eligible for job
b. if age >= 18,
print-> "eligble for job"
c. if age >= 55 and age <= 57,
print-> "eligible for job, but retirement soon."
d. if age > 57
print-> "retirement time"
*/

int main()
{
    // 1. age - adult or not
    //  int age;
    //  cin >> age;

    //  if (age >= 18) {
    //      cout << "you're an adult";
    //  } else {
    //     cout << "you're not an adult";
    //  }

    // ======================== //

    /*
    2. school grading system - with all ifs
    int marks;
    cin >> marks;

     if (marks < 25) {
         cout << "f";
     }
     if (marks >= 25 && marks <= 44) {
        cout << "e";
     }
     if (marks >= 45 && marks <= 49) {
        cout << "d";
     }
     if (marks >= 50 && marks <= 59) {
        cout << "c";
     }
     if (marks >= 60 && marks <= 79) {
        cout << "b";
     }
     if (marks >= 80 && marks <= 100) {
        cout << "a";
     }
     */

    /*
    2. school grading system - with if and else if
    int marks;
    cin >> marks;

     if (marks < 25) {
         cout << "f";
     }
     else if (marks <= 44) {
        cout << "e";
     }
     else if (marks <= 49) {
        cout << "d";
     }
     else if (marks <= 59) {
        cout << "c";
     }
     else if (marks <= 79) {
        cout << "b";
     }
     else if (marks <= 100) {
        cout << "a";
     }
    */

    // ======================== //

    // 3. eligible for job or not
    int age;
    cin >> age;

    if (age < 18)
    {
        cout << "not eligible for job";
    }
    else if (age <= 54)
    {
        cout << "eligible for job";
    }
    else if (age <= 57)
    {
        cout << "eligible for job, but retirement soon.";
    }
    else
    {
        cout << "retirement time";
    }

    //  so yeah this was all about for this chapter, i'll show you this same retirement example with nested if else, so check the respective file
    return 0;
}