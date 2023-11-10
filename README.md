# Exercise on Cryptography

To run program, can simply run
```python3 question_{number}.py```

question_one.py runtime : 136ms

question_two.py runtime : 217ms

question_three.py runtime : 162ms

question_four.py runtime : 136ms

time using 
```python3 -m timeit -n {num of loops} -c "$(cat question_{number}.py)"```

|      script       |                 runtime                  |
|:-----------------:|:----------------------------------------:|
|  question_one.py  | 500 loops, best of 5: 12.3 usec per loop |
|  question_two.py  | 500 loops, best of 5: 1.12 msec per loop |
| question_three.py |  50 loops, best of 5: 1.43 sec per loop  |
| question_four.py  | 500 loops, best of 5: 23.2 usec per loop |

Runtime loop test for question three was reduced due to code and runtime complexity of generating two images in one run. 