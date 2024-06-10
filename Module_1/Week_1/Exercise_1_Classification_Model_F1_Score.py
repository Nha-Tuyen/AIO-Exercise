def exercise(tp, fp, fn):
    print(f"exercise1 (tp = {tp} , fp = {fp}, fn = {fn})")
    if isinstance(tp, int) and isinstance(fp, int) and isinstance(fn, int):
        if tp > 0 and fp > 0 and fn > 0:
            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1_score = 2 * (precision * recall) / (precision + recall)
            print(">> precision is ", precision)
            print("recall is ", recall)
            print("f1-score is ", f1_score)
            print()
        else:
            print(">> tp, fp, fn should be greater than 0\n")
            return None
    else:
        print(">> tp, fp, fn should be integer\n")
        return None


exercise(tp=2, fp=3, fn=4)
exercise(tp='a', fp=3, fn=4)
exercise(tp=2, fp='a', fn=4)
exercise(tp=2, fp=3, fn=0)
exercise(tp=2.1, fp=3, fn=0)
