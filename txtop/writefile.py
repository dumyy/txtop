import numpy as np


def save_txt_base(data, filename, split=' '):
    n = data.shape[0]
    if n == 0:
        print("data is None")
        return -1
    else:
        f = open(filename, "w")
        inner_data = data.reshape(n, -1)
        for idx, line in enumerate(inner_data):
            nn = line.shape[0]
            temp = ("{}" + split) * (nn-1)+"{}\n"
            temp = temp.format(*line)
            f.write(temp)
        f.close()
        return 0


def save_txt_frame(data,frames,filename, split=' ', format=(5, None)):
    n = data.shape[0]
    if n == 0:
        print("data is None")
        return -1
    else:
        f = open(filename, "w")
        inner_data = data.reshape(n, -1)
        inner_frames = frames.reshape(n,)
        for idx, (frame_id,line) in enumerate(zip(inner_frames,inner_data)):
            frame = str(frame_id).zfill(format[0])
            if format[1] is not None:
                frame = "{}.{}".format(frame, format[1])
            nn = line.shape[0]
            temp = ("{}" + split) * (nn-1)+"{}\n"
            temp = temp.format(*line)
            frame_temp="{}{}{}".format(frame,split,temp)
            f.write(frame_temp)
        f.close()
        return 0
if __name__ == "__main__":
    data=np.ones((10,6))
    frame_ids=np.arange(10).reshape(10,1)
    print(data)
    ret=save_txt_frame(data,frame_ids,'saved.txt',split=' ',format=(5,None))
    print(ret)