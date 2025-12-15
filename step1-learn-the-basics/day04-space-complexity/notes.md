## 15th december 2025: space complexity

---

today i learnt about space complexity.

#### so what is space complexity?
space complexity is the memory space taken to compute a program in a very naive way. but remember we don't show space compleity in bytes, mb or something. here also we use Big O notation for showing space complexity.

so this is how exactly space complexity is calculated, it's `auxiliary space + input space`.

auxiliary space is the space that you take to store the problem.

input space is the space that you take to store the input.

let's understand it with a simple example:
`c = a + b;`

so here auxiliary space is 1, which is c.
input space is 2, which is a and b.

so the space complexity is roughly `O(3)` and we show it like `O(n)`. because we don't show in bytes, mb and all, we show it by Big O notation only.

another example would like, let's say you are declaring an array like `int arr[n]` so we say it's space complexity is `O(n)`.

---

now sometimes, let's say you are given two inputs `a` and `b`, so someone can do like `b = a + b;` which is fine, it'll take less space, but you are changing the value of the input given, and this is a very bad practice.

because in software engineering, if there's some data or input that you need to give some insights or do some computatoins on given input, you'll never modify the original input data, you do anything like calculate any outcomes or so, but don't modify the input ever.

---

whenever you do competitive programming in interviews or on leetcode, gfg or wherever, you run on their servers and not on your machine.

so at a time many people runs their program on the same server and usually it take 1s to compute a program which means it does approximately 10<sup>8</sup> operations, ignoring constant, lower values and all, it might be something a bit more or a bit less, but it's always around 10<sup>8</sup> operations in 1s.

for 2s it would be 2 * 10<sup>8</sup> and so on.

sometime in interviews they state time taken should be 1s, so now you know that your program should be roughly of O(10<sup>8</sup>) operations.

---

wrapping up 15th december 2025 and see you tomorrow!