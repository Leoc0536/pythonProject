# Exercise on Cryptography
###Run Before:
| python3 -m pip install --upgrade pip|
| python3 -m pip install --upgrade Pillow|

To run specific program, replace {file} with desired program name.
```shell
python3 {file}.py
```

Timing using 
```shell
python3 -m timeit -n {num of loops} -c "$(cat {file}.py)"
```

|      script       |                 runtime                  |
|:-----------------:|:----------------------------------------:|
|  question_one.py  | 500 loops, best of 5: 12.3 usec per loop |
|  question_two.py  | 500 loops, best of 5: 1.12 msec per loop |
| question_three.py |  50 loops, best of 5: 1.43 sec per loop  |
| question_four.py  | 500 loops, best of 5: 23.2 usec per loop |

Runtime loop test for question three was reduced due to code and runtime complexity of generating two images in one run. 
