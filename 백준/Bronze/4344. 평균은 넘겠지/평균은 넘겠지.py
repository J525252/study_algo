Case = int(input())

for _ in range ( Case ) :
    student_list = list(map(int, input().split()))  #학생수, 학생들의 점수

    n = student_list[0]
    student_list.pop(0)   # 학생수를 n으로 빼고, student_list에서 제외.

    avg = sum(student_list) / n

    cnt = 0   #평균을 넘는 학생수.
    for student in student_list :
        if( student > avg) :
            cnt += 1

    #print(f"{round( (cnt/n)*100 , 3)}%" )  // 40.0 %로 출력됨, but 나는 40.000%필요
    print("{:.3f}%".format( (cnt/n) * 100) )

