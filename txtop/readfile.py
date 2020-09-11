import os

import numpy as np

def get_lines(base, filename):
    file_path = os.path.join(base, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()
        f.close()
        return lines
    else:
        print("\033[0;31;31m {} doesn't exist,!!exit!!\033[0m".format(file_path))
        raise


def item_base(lines, split=' ', mode=0):
    n = len(lines)
    result = []
    if n == 0:
        print("\033[0;31;31m ,no data exist\00[0m")
        return result
    else:
        for idx, line in enumerate(lines):
            line = line.strip('\n')
            line = line.strip(' ')
            line = line.split(split)
            line = list(map(float, line))
            result.append(line)
    """
    mode 0: all nums, each line has the same len.
    mode 1: all nums, the lines have different lens.
    mode 2: has str, return a list [[],[],...,[],[]]
    """
    if mode == 0:
        return np.asarray(result).reshape(n, -1, 2)
    if mode == 1:
        return [np.asarray(result_).reshape(-1, 2) for result_ in result]
    if mode == 2:
        return result


def item_frame(lines, split=' '):
    n = len(lines)
    frame_ids = []
    result = []
    if n == 0:
        return frame_ids, result
    else:
        for line in lines:
            line = line.strip('\n')
            line = line.strip(' ')
            line = line.split(split)
            frame_id = int(line[0])
            line = list(map(float, line[1:]))
            result.append(line)
            frame_ids.append(frame_id)
    return np.asarray(frame_ids), np.asarray(result)


if __name__ == '__main__':
    lines = get_lines('.', 'test.txt')
    frameIds, result = item_frame(lines, split=' ')
    print(frameIds)
    print(result)
    a = np.ones((3,))
    print(a)
    temp = ("{}" + ' ') * 3
    t = temp.format(*a)
    print(t)
