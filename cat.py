import sys

if len(sys.argv) == 1:
    print('please give a file name to print.')
else:
    times_to_repeat = int(sys.argv[2]) if len(sys.argv) == 3 else 1
    file_name = sys.argv[1]
    for _ in range(times_to_repeat):
        with open(file_name, mode='r') as f:
            print(f.read())
