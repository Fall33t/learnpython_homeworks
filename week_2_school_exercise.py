grad_list = [{'school_class': '4a', 'scores': [5,4,4,5,2]},{'school_class': '5a', 'scores': [4,5,3,5,2]}]
zero_sum = 0
for scores in grad_list:
    for numbs in ['scores']:
        zero_sum += numbs
    scores_avg = zero_sum / len(['scores'])
    print(f'Оценка {scores_avg}')