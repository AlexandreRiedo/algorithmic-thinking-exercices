with open("backforth.in") as file:
    barn1_buckets = list(map(int, file.readline().split()))
    barn2_buckets = list(map(int, file.readline().split()))


def calc_answer(buckets):
    return (-buckets[0]) + buckets[1] - buckets[2] + buckets[3]


def solve(
    barn1_buckets: list,
    barn2_buckets: list,
    day: int,
    picked: list,
    answers: set,
):
    if day == 4:
        answers.add(calc_answer(picked))
        return

    if day % 2 == 0:
        for bucket in set(barn1_buckets):
            picked.append(bucket)
            barn1_buckets.remove(bucket)
            barn2_buckets.append(bucket)
            solve(barn1_buckets, barn2_buckets, day + 1, picked, answers)
            barn1_buckets.append(bucket)
            barn2_buckets.remove(bucket)
            picked.pop()

    if day % 2 == 1:
        for bucket in set(barn2_buckets):
            picked.append(bucket)
            barn2_buckets.remove(bucket)
            barn1_buckets.append(bucket)
            solve(barn1_buckets, barn2_buckets, day + 1, picked, answers)
            barn2_buckets.append(bucket)
            barn1_buckets.remove(bucket)
            picked.pop()

    return


with open("backforth.out", "w") as file:
    answers = set()
    solve(barn1_buckets, barn2_buckets, 0, [], answers)
    file.write(str((len(answers))))


"""
NOTE:
On Monday, FJ can choose from 10 different buckets. 
On Tuesday, he will be able to choose from 11 (no matter which bucket he brings); 
on Wednesday, Thursday, and Friday, he will also have 11 choices. 

Thus, a rough upper bound for the number of different things Farmer John can do is 10∗114=146410
operations, which means we can just simulate them. 

(A good rule of thumb is that if the number is under 20,000,000, it will probably run in time. This is *far* below that number!)
"""
