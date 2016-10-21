## Anagrams - Algorithms and Data Structures Task

### Task
Make the **data structure** that for the given word return in the fastes possible (In the smallest possible computational complexity) time *anagrams* of the given word. Calculate (roughly, by estimating with small-o and big-O notation i.e *o(1)-O(n)* ) its complexity.

> Anagram - Word that lexicographically makes sense and contains the same letters
> i.e `'nope'` is anagram of `'open'`( its another word but uses the same letters )

###### Further specs:
1. It should return list as a result i.e
```find_anagrams('open')``` returns ```[]```
2. Your data structure should learn while you are asking questions to it. So **first question**:
```find_anagrams('open')``` should return ```[]``` but **second question**  ```find_anagrams('nope')``` or ```find_anagrams('open')```should return ```['open']```

##### Notes:
In principle we want to constrain the structure just to the english language.
If you feed the structure with the buzzwords without meaning your language will not be strict but the structure should work as well. i.e:
1. buzzwords test case (2 steps)
  > ```expect find_anagrams('1ss') to return [] ```,

  >```expect find_anagrams('ss1') to return ['1ss', 'ss1'] ```

### Implemenation
Implement the task in any known language using already known language data structures.

### Tests:
This repository has test file with implemented test cases shown below. To use it simply run `python anagram_test.py` or `ruby anagram_test.rb`. Depending on the language that is the subject of the repository.

### Sample test cases:
Sometimes specification is not enough so i provide you some test cases that may describe the problem in more straight forward way.

1 test case (1 step)

> ```expect find_anagrams('open') to return []```,

2 test case (2 steps)

> ```expect find_anagrams('open') to return [] ```,

>```expect find_anagrams('nope') to return ['open'] ```

3 test case (4 steps)

> ```expect find_anagrams('open') to return [] ```,

> ```expect find_anagrams('open') to return ['open'] ```,

> ```expect find_anagrams('open') to return ['open'] ```,

>```expect find_anagrams('nope') to return ['open'] ```

4 test case (1 step)

>```expect find_anagrams('') to return [] ```

5 test case (2 steps)

>```expect find_anagrams('a') to return [] ```

>```expect find_anagrams('a') to return ['a'] ```

6 test case (3 steps)

>```expect find_anagrams('a') to return [] ```

>```expect find_anagrams('aa') to return [] ```

>```expect find_anagrams('a') to return ['a'] ```

7 test case (2 steps)

> ```expect find_anagrams('open') to return [] ```,

>```expect find_anagrams('Nope') to return ['open'] ```
