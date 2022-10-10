# show(전체 학생 정보 출력) 함수
def show(dict) :
    dict_sort = sorted(students.items(), key=lambda x : x[1][3], reverse=True)
    
    print('=' * 90)
    print('전체 학생 정보 출력')
    print('-' * 90)
    print('{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}'
          .format('Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade'))
    print('-' * 90)

    for key, val in dict_sort : 
        print('{0:^15}{1:>15}{2:^15}{3:^15}{4:^15.1f}{5:^15}'
          .format(key, val[0], val[1], val[2], val[3], val[4]))
    print('=' * 90)
    print()

    
# search(특정 학생 검색) 함수
def search() :
    global students
    input_id = input('Student ID : ')

    if input_id in students.keys() :
        print()
        print('%s 검색결과' % input_id)
        print('=' * 90)
        print('{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}'
              .format('Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade'))
        print('-' * 90)
        print('{0:^15}{1:^15}{2:^15}{3:^15}{4:^15.1f}{5:^15}'
              .format(input_id, students[input_id][0], students[input_id][1],
               students[input_id][2], students[input_id][3], students[input_id][4]))
        print('=' * 90)
    else :
        print('NO SUCH PERSON.')
    print()
        
        
# changescore(점수 수정) 함수
def changescore() :
    global students

    # 학번 예외처리
    input_id = input('Student ID : ')
    if input_id not in students.keys() :
        print('NO SUCH PERSON.')
        print()
        return

    # 중간고사/기말고사 예외처리
    input_test = input('Mid/Final? : ')
    input_test = input_test.lower()
    if input_test != 'mid' and input_test != 'final' :
        print()
        return
    
    # 점수 예외처리
    input_new_score = int(input('Input new score : '))
    if input_new_score < 0 or input_new_score > 100 :
        print()
        return
    
    # 바뀌기 전 점수 출력
    print('{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}'
          .format('Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade'))
    print('-' * 90)
    print('{0:^15}{1:^15}{2:^15}{3:^15}{4:^15.1f}{5:^15}'
          .format(input_id, students[input_id][0], students[input_id][1],
           students[input_id][2], students[input_id][3], students[input_id][4]))
    
    # 점수 수정하기
    if input_id in students.keys():
        if input_test == 'mid' :
            students[input_id][1] = int(input_new_score)
        elif input_test == 'final' :
            students[input_id][2] = int(input_new_score)

    # 평균 수정하기
    n_avg = (students[input_id][1] + students[input_id][2]) / 2
    
    # 등급 수정하기
    if n_avg >= 90 :
        n_grd = 'A'
    elif 80 <= n_avg < 90 :
        n_grd = 'B'
    elif 70 <= n_avg < 80 :
        n_grd = 'C'
    elif 60 <= n_avg < 70 :
        n_grd = 'D'
    elif n_avg < 60 :
        n_grd = 'F'
    
    students[input_id][3] = n_avg
    students[input_id][4] = n_grd
    
    # 바뀐 후 점수 출력
    print()
    print('Score changed.')
    print('{0:^15}{1:^15}{2:^15}{3:^15}{4:^15.1f}{5:^15}'
          .format(input_id, students[input_id][0], students[input_id][1],
           students[input_id][2], students[input_id][3], students[input_id][4]))
    print()
    
    
# add(학생 추가) 함수
def add():
    global students

    # 학번 에러처리
    input_id = input('Student ID : ')
    if input_id in students.keys() :
        print('ALREADY EXISTS.')
        print()
        return
    
    input_name = input('Name : ')
    input_mid_s = int(input('Midterm Score : '))
    if input_mid_s < 0 or input_mid_s > 100 :
        print()
        return
    input_fin_s = int(input('Final Score : '))
    if input_fin_s < 0 or input_fin_s > 100 :
        print()
        return
    print('Student added.')
    
    # 점수 추가하기
    add_student = [input_name, input_mid_s, input_fin_s]
    
    # 평균 추가하기
    a_avg = (add_student[1] + add_student[2]) / 2
    
    # 등급 추가하기
    if a_avg >= 90 :
        a_grd = 'A'
    elif 80 <= a_avg < 90 :
        a_grd = 'B'
    elif 70 <= a_avg < 80 :
        a_grd = 'C'
    elif 60 <= a_avg < 70 :
        a_grd = 'D'
    elif a_avg < 60 :
        a_grd = 'F'
        
    add_student.append(a_avg)
    add_student.append(a_grd)
    students[input_id] = add_student
    print()
    
    
# searchgrade(Grade 검색) 함수
def searchgrade() :
    global students
    grades = ['A', 'B', 'C', 'D', 'F']
    
    # 등급 예외처리
    input_grd = input('Grade to search : ')
    input_grd = input_grd.upper()
    
    if input_grd not in grades :
        print()
        return     
    
    print()
    print('Grade %s 검색결과' % input_grd)
    print('=' * 90)
    print('{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}'
          .format('Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade'))
    print('-' * 90)
    
    tmp = False
    for key, val in students.items() :
        if val[4] == input_grd :            
            if not tmp :
                tmp = True
            print('{0:^15}{1:>15}{2:^15}{3:^15}{4:^15.1f}{5:^15}'
                .format(key, val[0], val[1], val[2], val[3], val[4]))
            
    # 해당 grade 학생이 없는 경우 예외처리
    if not tmp :
        print('NO RESULTS')
    print('=' * 90)
    print()
    
    
# remove(특정 학생 삭제) 함수
def remove() :
    global students
    
    # 목록에 아무도 없을 경우 예외처리
    if len(students) == 0 :
        print('List is empty')
        print()
        return
    
    # 학번 예외처리        
    input_id = input('Student ID : ')
    if input_id in students.keys() :
        del(students[input_id])
        print('Student removed.')
    else :
        print('NO SUCH PERSON') 
        print()
        return
    print()
    

# quit(종료) 함수
def quit() :
    global students
    input_save = input('Save data?[yes/no] : ')
    input_save = input_save.lower()
    
    if input_save == 'yes':
        input_f_name = input('File name : ')
        new_file = open(input_f_name, 'w')
        
        for key, val in students.items() :
            new_line = key + '\t' + val[0] + '\t' + str(val[1]) + '\t' + str(val[2]) + '\t' + str(val[3]) + '\t' + str(val[4]) + '\n'
            new_file.write(new_line)
        new_file.close()
        
        

# main
import sys
import os


# 성적관리 프로그램과 파일 열기 설정
args = sys.argv[1]
file = open(args, 'r')

# 학생 딕셔너리 생성
# 중복이 없는 학번을 key로 설정
students = {}

for s in file.readlines() :
    student = s.strip().split('\t')
    student[2], student[3] = int(student[2]), int(student[3])
    stu_id = student[0]
    stu_info = student[1:]
    
    # 평균구하기
    avg = (student[2] + student[3]) / 2
    
    # 등급구하기
    if avg >= 90 :
        grd = 'A'
    elif 80 <= avg < 90 :
        grd = 'B'
    elif 70 <= avg < 80 :
        grd = 'C'
    elif 60 <= avg < 70 :
        grd = 'D'
    elif avg < 60 :
        grd = 'F'
        
    stu_info.append(avg)
    stu_info.append(grd)    
    students[stu_id] = stu_info
    
file.close()
show(students)

# 명령어 설정
while(1) :
    input_order = input('# ')
    input_order = input_order.lower()
    if input_order == 'show' :
        show(students)
    elif input_order == 'search' :
        search()
    elif input_order == 'changescore' :
        changescore()
    elif input_order == 'add' :
        add()
    elif input_order == 'searchgrade' :
        searchgrade()
    elif input_order == 'remove' :
        remove()
    elif input_order == 'quit' :
        quit()
        break
