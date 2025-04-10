import sys

gpa_table = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

def score(gp): # 등급과 가중치를 곱한 평점을 리턴
    global gpa_table

    weighted_score = gpa_table.get(gp[2], None) * float(gp[1])
    return weighted_score

def sum_credit(lecture_list):
    sum = 0
    for lecture_for in lecture_list:
        sum += float(lecture_for[1])
    return sum

def gpa(score_list):
    list_len = len(score_list)
    sum_score = 0
    try:
        for index_for in range(list_len):
            sum_score += score(score_list[index_for])
    except Exception:
        print(Exception("잘못된 형식입니다"))
    else:
        gpa = sum_score / sum_credit(score_list)
        # print(f"gpa: {gpa:g}")
        return gpa

def func_lecture_input(count_max):
    lecture_list = []
    count_cur = 0
    while count_cur < count_max:
        # print("# 과목의 이름, 평점, 등급 입력: ", end='', flush=True)
        lecture = sys.stdin.readline().strip().split()
        try:
            if len(lecture) != 3:
                raise IndexError("잘못된 입력입니다")
        except IndexError as e:
            print(e)
        else:
            if lecture[2].lower() != 'p':
                lecture_list.append(lecture)
            count_cur += 1
    return lecture_list

print(gpa(func_lecture_input(20)))
# def func_score_mean():
#     lecture_list = func_lecture_input()
    

# score_mean = func_score_mean()
# print("20개 과목의 평점은 {}입니다".format())