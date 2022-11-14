#학번을 입력받아 첫번째는 학년, 두번째는 반, 세번째, 네번째는 번호
def student_number_to_info(student_number):
    grade = student_number[0]
    class_number = student_number[1]
    #반이 1, 2면 뉴미디어소프트웨어과, 3, 4면 뉴미디어웹솔루션과, 5, 6이면 뉴미디어디자인과 출력하기
    if class_number == '1' or class_number == '2':
        major = '뉴미디어소프트웨어과'
    elif class_number == '3' or class_number == '4':
        major = '뉴미디어웹솔루션과'
    elif class_number == '5' or class_number == '6':
        major = '뉴미디어디자인과'
    else:
        major = '잘못된 정보입니다.'
    student_number = student_number[2:]

    return grade, class_number, student_number, major

print(student_number_to_info("2312"))