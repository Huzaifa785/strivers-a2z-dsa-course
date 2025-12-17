## 17th december 2025: patterns part 2

---

today i'll be solving the second and third pattern in the list.

q2.
```
*
* *
* * *
* * * *
* * * * *
```

so recall the 4 steps that i mentioned yesterday. first was to focus on rows and count the number of lines, so we can see we have 5 rows/lines here.

second is to focus on columns and connect them with rows somehow, so i can notice here, when we run for first time, it's printing one star, then second time, 2 stars, then third time, 3 stars and so on. so i can this is how the values of i and j will be like:
```
when i = 0, j = 0
when i = 1, j = 0, 1
when i = 2, j = 0, 1, 2
when i = 3, j = 0, 1, 2, 3
when i = 4, j = 0, 1, 2, 3, 4
```

and third step is to simply print whatever you want to, so i'll just print it and the final code would look something like this:
```cpp
int solve_pattern(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << "* ";
        }
        cout << endl;
    }
}
```

so yeah done with pattern 2.

---

moving on to pattern 3:

q3.
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
step 1, counting the number or rows/lines, they are 5, or just assume n lines.

step 2, seeing what are columns doing here, and connecting them somehow to rows, so after my observation i see, we are appending the number on which row number it is. this will look like this:
```
when i = 1, j = 1 (printing the first row number which is 1)
when i = 2; j = 1 2 (appending the row number we are on which is 2)
when i = 3; j = 1 2 3 (appending the row number we are on which is 3)
when i = 4; j = 1 2 3 4 (appending the row number we are on which is 4)
when i = 5; j = 1 2 3 4 5 (appending the row number we are on which is 5)
```

step 3 is to print whatever we want to, in our case we want to print row numbers i believe, so this is how our final code would look like:
```cpp
int solve_pattern(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j << " ";
        }
        cout << endl;
    }
}
```

so yeah that's it for today, i know this is too little practice, but i'll definitely increase gradually.

---

wrapping up 17th december 2025 and see you tomorrow!