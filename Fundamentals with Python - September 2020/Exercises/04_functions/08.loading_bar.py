def case_checker(num, output_list):
    if num == 0:
        output_list = zero_progress()
    elif 10 <= num <= 90:
        output_list = middle_progress(num, output_list)
    else:
        output_list = full_progress(output_list)
    return ''.join(output_list)


def zero_progress():
    progress_visualizer = ['.' * 10]
    progress_visualizer.insert(0, '[')
    progress_visualizer.append(']')
    return progress_visualizer


def middle_progress(num, progress_visualizer):
    percents_load = num // 10
    percents_counter = 0
    for symbol in range(0, percents_load):
        progress_visualizer.append('%')
        percents_counter += 1
        if percents_counter == percents_load:
            dots_needed = 10 - percents_counter
            progress_visualizer.append('.' * dots_needed)
            break
    progress_visualizer.insert(0, '[')
    progress_visualizer.append(']')
    return progress_visualizer


def full_progress(progress_visualizer):
    progress_visualizer.append('%' * 10)
    progress_visualizer.insert(0, '[')
    progress_visualizer.append(']')
    return progress_visualizer


def template_visualizer(num, progress):
    if num == 0:
        output = f"0% {progress}\n" \
                 f"Still loading..."
    elif 10 <= num <= 90:
        output = f"{num}% {progress}\n" \
                 f"Still loading..."
    else:
        output = "100% complete!\n" \
                 f"{progress}"
    return output


# input data about progress
loading_num = int(input())
# progress list visualizer
progress_list = []
progress_list = case_checker(loading_num, progress_list)
# making user output template
output_template = template_visualizer(loading_num, progress_list)
print(output_template)
