from tkinter import *
import time


# 함수모음

def grade_input():
    try:
        name = e1.get()
        eng = int(e2.get())
        mat = int(e3.get())
        if name is None:
            print("이름을 입력해주세요.")

        elif eng < 0:
            print("1 ~ 100의 값만 입력하세요.")
        elif eng > 100:
            print("1 ~ 100의 값만 입력하세요.")
        elif mat < 0:
            print("1 ~ 100의 값만 입력하세요.")
        elif mat > 100:
            print("1 ~ 100의 값만 입력하세요.")

        elif name in score:
            print("입력되어 있는 학생 이름입니다.")
        else:
            score[name] = {}
            score[name]['영어'] = eng
            score[name]['수학'] = mat
            sall = eng + mat
            savg = (eng + mat) / 2
            l8.config(text=sall)
            l9.config(text=savg)
            print(name, "학생의 성적이 등록되었습니다.")
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
    except:
        print("빈칸을 확인하세요")


# 성적출력
def grade_output():
    if len(score) == 0:
        print("출력할 학생의 데이터가 없습니다.")
    else:
        for name, info in score.items():
            print("이름 :", name)
            for k, v in info.items():
                print(k, " : ", v, end=" | ")
            print("\n")


# 성적삭제
def grade_del():
    if len(score) == 0:
        print("출력할 학생의 데이터가 없습니다.")

    else:
        name = e1.get()
        if name not in score:
            print("이름을 다시 확인해주세요.")
        elif name in score:
            del score[name]
            print(name, "학생의 성적이 삭제되었습니다.")
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
        else:
            print("이름을 다시 확인해주세요.")


# 성적변경
def grade_change():
    try:
        if len(score) == 0:
            print("출력할 학생의 데이터가 없습니다.")
        else:
            name = e1.get()

            if name not in score:
                print("이름을 다시 확인해주세요.")
            elif name in score:
                score[name] = {}
                eng = int(e2.get())
                if eng < 0:
                    print("1 ~ 100의 값만 입력하세요.")
                elif eng > 100:
                    print("1 ~ 100의 값만 입력하세요.")
                score[name]['영어'] = eng
                mat = int(e3.get())
                if mat < 0:
                    print("1 ~ 100의 값만 입력하세요.")
                elif mat > 100:
                    print("1 ~ 100의 값만 입력하세요.")
                score[name]['수학'] = mat
                print(name, "학생의 성적이 성공적으로 수정되었습니다.")
                e1.delete(0, 'end')
                e2.delete(0, 'end')
                e3.delete(0, 'end')
            else:
                print("이름을 다시 확인해주세요")
    except:
        print("빈칸을 확인하세요")


# 성적차트
def grade_chart():
    if len(score) == 0:
        print("출력할 학생의 데이터가 없습니다.")
    else:
        temp = 0
        for name2, info in score.items():
            print("이름 :", name2)
            for subname, subscore in info.items():
                temp += subscore
            print("총점 :", end=" ")
            for star in range(1, temp + 1, 10):
                print("* ", end="")
            print("(", temp, "점)")
            temp = 0
            print("\n")


# 총점평균
def grade_avg():
    avg = 0
    if len(score) == 0:
        print("출력할 학생의 데이터가 없습니다.")
    else:
        num = 0
        print("총 학생 수 :", len(score))
        for name2, info in score.items():
            for subscore in info.values():
                num = num + 1
                avg = avg + subscore
        avg = avg // num
        print("모든학생들의 과목당 점수의 평균은 ", avg, "점 입니다.")


# 파일출력
def grade_text():
    if len(score) == 0:
        print("출력할 학생의 데이터가 없습니다.")
    else:
        moment = time.localtime()
        file = open("output.txt", 'w')
        file.write("%04d/%02d/%02d% 02d:%02d:%02d\n" % (
            moment.tm_year, moment.tm_mon, moment.tm_mday, moment.tm_hour, moment.tm_min, moment.tm_sec))
        for name, info in score.items():
            n1 = name
            file.write("이름 : " + n1 + " ")
            for k, v in info.items():
                file.write(str(k) + " : " + str(v) + "점 ")
            file.write("\n")
        print("파일명 : output.txt 가 생성되었습니다.")
        file.close()


# Tkinter, 기본 윈도우 설정
w = Tk()
w.title("학생성적프로그래밍")
w.geometry("800x600")
score = {}

# label 모음

l1 = Label(w, text="학생성적프로그래밍", width=45, height=2, relief="groove", font=("", 20))
l2 = Label(w, text="이름", width=10, height=2, relief="groove", font=("", 15))
l3 = Label(w, text="영어", width=10, height=2, relief="groove", font=("", 15))
l4 = Label(w, text="수학", width=10, height=2, relief="groove", font=("", 15))
l5 = Label(w, text="합계", width=10, height=2, relief="groove", font=("", 15))
l6 = Label(w, text="평균", width=10, height=2, relief="groove", font=("", 15))
l7 = Label(w, text="2015211385 이재현", width=30, height=2, relief="groove", font=("", 15))
l8 = Label(w, width=18, height=2, relief="groove", font=("", 15))
l9 = Label(w, width=18, height=2, relief="groove", font=("", 15))

# Entry 모음 (입력란)

e1 = Entry(w, bg="khaki")
e2 = Entry(w, bg="khaki")
e3 = Entry(w, bg="khaki")

# Button 모음 (실행버튼)

b1 = Button(w, bg="darkgrey", text="성적입력", width=10, height=2, relief="groove", font=("", 15), command=grade_input)
b2 = Button(w, bg="darkgrey", text="성적출력", width=10, height=2, relief="groove", font=("", 15), command=grade_output)
b3 = Button(w, bg="darkgrey", text="성적삭제", width=10, height=2, relief="groove", font=("", 15), command=grade_del)
b4 = Button(w, bg="darkgrey", text="성적변경", width=10, height=2, relief="groove", font=("", 15), command=grade_change)
b5 = Button(w, bg="darkgrey", text="성적차트", width=10, height=2, relief="groove", font=("", 15), command=grade_chart)
b6 = Button(w, bg="darkgrey", text="총점평균", width=10, height=2, relief="groove", font=("", 15), command=grade_avg)
b7 = Button(w, bg="darkgrey", text="파일출력", width=10, height=2, relief="groove", font=("", 15), command=grade_text)
b8 = Button(w, bg="darkgrey", text="종료", width=10, height=2, relief="groove", font=("", 15), command=quit)

# label 배치
l1.place(x=40, y=10)
l2.place(x=40, y=90)
l3.place(x=40, y=170)
l4.place(x=430, y=170)
l5.place(x=40, y=250)
l6.place(x=430, y=250)
l7.place(x=40, y=500)
l8.place(x=180, y=250)
l9.place(x=565, y=250)

# Entry 배치
e1.place(x=180, y=90, width=585, height=45)
e2.place(x=180, y=170, width=200, height=45)
e3.place(x=565, y=170, width=200, height=45)

# Button 배치
b1.place(x=40, y=330)
b2.place(x=240, y=330)
b3.place(x=430, y=330)
b4.place(x=640, y=330)
b5.place(x=40, y=410)
b6.place(x=240, y=410)
b7.place(x=430, y=410)
b8.place(x=640, y=410)

w.resizable(width=False, height=False)  # 크기고정
w.mainloop()
