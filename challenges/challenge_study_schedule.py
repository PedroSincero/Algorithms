def study_schedule(permanence_period, target_time):
    count = 0
    # https://pt.stackoverflow.com/questions/176525/como-posso-saber-se-a-vari%C3%A1vel-%C3%A9-um-n%C3%BAmero-inteiro-em-python
    if not isinstance(target_time, int):
        return None
    for p in permanence_period:
        if not isinstance(p[0], int) or not isinstance(p[1], int):
            return None
        if p[0] <= target_time and p[1] >= target_time:
            count += 1
    return count
