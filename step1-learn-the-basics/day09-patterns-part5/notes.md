## 20th december 2025: patterns part 5

---

today i'll be solving sixth pattern.

q6.
```
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
```

this is also similar to our previous problem, we just need to print the value of j instead of *. the thing here is whatever the value of n will be, that many column values in the first line, and keep reducing by one, till you reach 1. for example, if the value of n is 3, the first line would be `1 2 3`. then `1 2` and finally `1`, so it would look something like this:
```
1 2 3
1 2 
1
```

for outer loop, we need to print the number of lines, so just run it till i < n. so our outer loop would look something like this:
```cpp
for (int i = 0; i < n; i++) {

}
```

for inner loop, we need to print the value of j and connect it somehow to rows, so we can start running this loop from 1, and we can have the condition `j <= n - i`, which means, keep printing the value of j until it's less than or equal to n-i.

so our final code would look like this:
```cpp
for (int i = 0; i < n; i++) {
    for (int j= 1; j <= n - i; j++) {
        cout << j << " ";
    }
    cout << endl;
}
```

let's look at it like this (assume n = 5):

when i = 0;
```
1 <= 5 - 0 = 5; yes; 1 is less than 5; print 1;
2 <= 5 - 0 = 5; yes; 2 is less than 5; print 2;
3 <= 5 - 0 = 5; yes; 3 is less than 5; print 3;
4 <= 5 - 0 = 5; yes; 4 is less than 5; print 4;
5 <= 5 - 0 = 5; yes; 5 is equal to 5;  print 5;
```
so our first line is:
`1 2 3 4 5`

when i = 1;
```
1 <= 5 - 1 = 4; yes; 1 is less than 4; print 1;
2 <= 5 - 1 = 4; yes; 2 is less than 4; print 2;
3 <= 5 - 1 = 4; yes; 3 is less than 4; print 3;
4 <= 5 - 1 = 4; yes; 4 is equal to 4;  print 4;
```
so our first and second lines are:
```
1 2 3 4 5
1 2 3 4
```

when i = 2;
```
1 <= 5 - 2 = 3; yes; 1 is less than 3; print 1;
2 <= 5 - 2 = 3; yes; 2 is less than 3; print 2;
3 <= 5 - 2 = 3; yes; 3 is equal to 3;  print 3;
```
so our first three lines are:
```
1 2 3 4 5
1 2 3 4
1 2 3
```

and so on till 1.

so yeah this was it for today, i made use of a bit different logic for this program than our previous one and i think this is easy to visualise too.

---

wrapping up 20th december 2025 and see you tomorrow!