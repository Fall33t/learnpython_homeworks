grad_list = [{'school_class': '4a', 'scores': [5,4,4,5,2]},{'school_class': '5a', 'scores': [4,5,3,5,2]}]
sum_for_class = 0
for grad in grad_list:
    sum_for_class = 0
    for rating in grad['scores']:
        sum_for_class += rating
    class_avg = sum_for_class / len(grad['scores'])
    print(f'Оценка {class_avg}')