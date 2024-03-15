#https://medium.datadriveninvestor.com/introducing-icecream-never-use-print-to-debug-your-python-code-again-fb0c1f1f2972
#https://github.com/gruns/icecream
#pip install icecream

from icecream import ic

def func(num):
    return num * 2

ic(func(3))

sample_dict = {1:"A", 2:"B", 3:"C"}

ic(sample_dict[1])

## icecream_demo.py

from icecream import ic

def func(input_num):
    if input_num == 1:
        ic()
        ...

    else:
        ic()
        ...

func(2)

from icecream import ic
ic.configureOutput(prefix='ic debug| -> ')

ic("A custom prefix")





