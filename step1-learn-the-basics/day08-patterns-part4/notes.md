## 19th december 2025: patterns part 4

---

today i'll be solving fifth pattern.

q5.
```
* * * * *
* * * *
* * *
* *
*
```

now here we need to have an inverted right angled triangle, so whatever the n is, let's assume it's 5, so starting from 5 *s, we need to go down to 1 and stop.

so number of line here is 5, assume n. so it's sorted for outer loop that we need to print n number of lines.

now for columns we, need to start from n columns all the way down to 1, everytime reducing one star from the line. 

the outer loop would be simple and look like our previous solutions like this:
```cpp
for (int i = 0; i < n; i++) {
   
}
```

now for innner loop, we know we need to start from n and keep reducing, so one thing is clear to me that we need to decrement in our last condition, and we need to start from n, these two things in the inner loop are clear.

where i got stuck was the second condtion in the loop, so i referred the article on a2z dsa sheet for this specific pattern, and then realized, ahh we just need to have `j > i`, why? let's go a bit deep.

```
let's assume n = 5
when i = 0;

j = 5 -->> 5 > 0; yes; so it prints; *
j = 4 -->> 4 > 0; yes; so it adds 1 star; * *
j = 3 -->> 3 > 0; yes; so it adds another star; * * *
j = 2 -->> 2 > 0; yes; so it adds another star; * * * *
j = 1 -->> 1 > 0; yes; so it adds another star; * * * * *
j = 0 -->> 0 > 0; no; so it goes back to outer loop;
```
so our first line now has 5 stars as exptected `* * * * *`

```
now when i = 1;
j = 5 -->> 5 > 1; yes; so it prints; *
j = 4 -->> 4 > 1; yes; so it adds 1 star; * *
j = 3 -->> 3 > 1; yes; so it adds another star; * * *
j = 2 -->> 2 > 1; yes; so it adds another star; * * * *
j = 1 -->> 1 > 1; no; so it goes back to outer loop;
```
now our second line is `* * * *`.

and our pattern looks like this now:
```
* * * * *
* * * *
```

```
now when i = 2;
j = 5 -->> 5 > 2; yes; so it prints; *
j = 4 -->> 4 > 2; yes; so it adds 1 star; * *
j = 3 -->> 3 > 2; yes; so it adds another star; * * *
j = 2 -->> 2 > 2; no; so it goes back to outer loop;
```
now our third line is `* * *`.

and our pattern looks like this now:
```
* * * * *
* * * *
* * *
```

```
now when i = 3;
j = 5 -->> 5 > 3; yes; so it prints; *
j = 4 -->> 4 > 3; yes; so it adds 1 star; * *
j = 3 -->> 3 > 3; no; so it goes back to outer loop;
```
now our fourth line is `* *`.

and our pattern looks like this now:
```
* * * * *
* * * *
* * *
* *
```

```
now when i = 4;
j = 5 -->> 5 > 3; yes; so it prints; *
j = 4 -->> 4 > 4; no; so it goes back to outer loop;
```
now our fifth line is `*`.

and our pattern looks like this now and we got it as expected:
```
* * * * *
* * * *
* * *
* *
*
```

now when i = 5; on the first iteraiton in inner loop only, it'll be `is 5 > 5?` and it'll be false, and our program ends.

so our final function to solve this pattern looks like this:
```cpp
int solve_pattern(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = n; j > i; j--) {
            cout << "* ";
        }
    cout << endl;
    }
}
```

this was a bit challenging for me and took time to understand, but yeah i got it now, and i'm pretty sure i'll improve as i practice similar kind of problems.

---

wrapping up 19th december 2025 and see you tomorrow!