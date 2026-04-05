import sys

while True:
    num_jack, num_jill = map(int, sys.stdin.readline().rstrip().split())
    if num_jack == 0 and num_jill == 0:
        break
    cds_jack = set()
    cds_jill = set()

    for _ in range(num_jack):
        cds_jack.add(int(sys.stdin.readline().rstrip()))
    for _ in range(num_jill):
        cds_jill.add(int(sys.stdin.readline().rstrip()))

    num_both = len(cds_jack.intersection(cds_jill))
    sys.stdout.write(f"{num_both}\n")