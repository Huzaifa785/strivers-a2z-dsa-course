## 18th december 2025: patterns part 3

---

today i'll be solving fourth pattern.

q4.
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

we can see here, we need to print 5 lines, or say 5 rows, let's consider them n lines.

now, let's see what are we printing in columns and connect them to rows somehow. so what i noticed here is, whatever row number we're on, we are printing the row number that many times. for example, we are on row 3, so we'll print 3, three time, like 3 3 3.

so this is the solution that i came up with.

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        cout << i << " ";
    }
    cout << endl;
}
```

---

wrapping up 18th december 2025 and see you tomorrow!