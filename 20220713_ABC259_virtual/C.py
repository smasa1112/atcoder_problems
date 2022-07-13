from numpy import s_


def RLE_for(sequence):

    #戻り値の初期化
    comp_seq = list() # 圧縮されたデータのリスト
    lengths = list() # データの連続する長さのリスト

    # 最初の要素を記録
    comp_seq.append(sequence[0])
    temp = sequence[0]
    length = 1

    # 2番目から最後まで
    for i in range(1, len(sequence)):
        if sequence[i] != temp:  # 新しいデータが来たら、これまでのデータとその長さを記録
            lengths.append(length)
            comp_seq.append(sequence[i])
            temp = sequence[i]
            length = 1
        else: # 前と同じデータが来たら、lengthをインクリメント
            length += 1

    # 最後にlengthを追加
    lengths.append(length)

    return comp_seq, lengths

S=input()
T=input()

s_comp_seq, s_lengths = RLE_for(S)
t_comp_seq, t_lengths = RLE_for(T)


flag=True
if s_comp_seq == t_comp_seq:
    for s_length,t_length in zip(s_lengths,t_lengths):
        if s_length==1:
            if s_length != t_length:
                flag=False
                break
        else:
            if s_length>t_length:
                flag=False
                break
else:
    flag=False
    

if flag:
    print("Yes")
else:
    print("No")