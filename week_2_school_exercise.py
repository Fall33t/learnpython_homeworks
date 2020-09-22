grad_list = [{'school_class': '4a', 'scores': [5,4,4,5,5]},{'school_class': '5a', 'scores': [4,4,5,5,4]}]
sum_for_school = 0
score_count_for_school = 0
for grad in grad_list:
    sum_for_class = 0
    for score in grad['scores']:
        score_count_for_school += 1
        sum_for_school += score
        sum_for_class += score
    class_avg = sum_for_class / len(grad['scores'])
    print(f'Оценка классов {class_avg}')
school_avg = sum_for_school / score_count_for_school
print(f'Оценка школы {school_avg}')    
