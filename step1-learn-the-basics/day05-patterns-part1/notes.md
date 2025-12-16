## 16th december 2025: patterns part 1

---

from today i'll be starting with patterns, printing differenet types of patterns and all as showed in a2z dsa course. 

the main goal of solving patterns is to get a strong grip on loops. because whatever topic you do in dsa. graphs, trees, binary search, arrays and all, loops are an essential part of it.

do they ask this in interviews? no. sometimes just in some service based companies like tcs and all, they ask this, but not much.

for solving any pattern question, remember these four steps, and you'll be good.
1. for outer loop, count the number of lines, that is rows.
2. for inner loop, focus on the columns, and connect them somehow to rows.
3. whatever you need to print, print them inside the inner loop
4. observe symmetry (optional, because not applicable for all patterns)

let's understand it from an example, and this is our first pattern of the series that we'll be printing.

q.
```cpp
****
****
****
****
```
so if we do step 1, count number of lines which is 4, so our outer loops will be like:
```cpp
for (int i = 0; i < 4; i++){


}
```
which shows this will run for 4 times, and i can say that i completed my 1st step.

now moving on to step 2, focusing on columns and somehow connecting them to rows.

so we can see in our pattern above there for every line, 4 *s are printed, simple. so like when we are at 0th row (i=0), we are printing 4 *s, when i=1, again 4 *s, when i=3, again 4 *s. and we need to print on new line everytime for each i.

so we can write our inner loop something like this:
```cpp
for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {

    }

}
```
second step done.

now moving on to 3rd step, printing. so here we need to print * and also make sure for that we want a newline for each i iteration, so i can write the final code like this:
```cpp
for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
        cout << "*";
    }
    cout << endl;
}
```
do we oberve any symmetry here, no. so yeah we are done. but remember we won't hardcode values like 4, so we just take input and print that required thing, you can refer my code for the same in my .cpp file.

also, in your interviews and all, you won't be solving like this on local, so make sure to practice online, as i'll do on codestudio by codingninjas for this problem as showed in the video.

so for that also, how they have multiple test cases and we run our program against it, we implemented that in our local too, so can refer in my file.

so yeah for today, that's it, i'll solve another patterns from tomorrow.

---

wrapping up 16th december 2025 and see you tomorrow!