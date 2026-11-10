import sys
import json
from quiz import Quiz # 우리가 만든 Quiz 클래스 불러오기

class QuizGame:
    def __init__(self):
        """요구사항 10: 게임 전체를 관리하는 클래스 초기화"""
        self.quizzes = []
        self.best_score = 0
        self.data_file = "state.json"
        self.load_data() # 프로그램 시작 시 데이터 불러오기

    def load_data(self):
        """요구사항 11: state.json 파일에서 데이터 불러오기"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.quizzes = [Quiz(q['question'], q['choices'], q['answer']) for q in data.get('quizzes', [])]
                self.best_score = data.get('best_score', 0)
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ 데이터 파일이 없거나 손상되어 기본 퀴즈(HSK 3급)로 시작합니다.")
            self.setup_default_quizzes()
            
    def setup_default_quizzes(self):
        """요구사항 5: 기본 퀴즈 데이터 5개 생성"""
        self.quizzes = [
            Quiz("다음 중 '도서관'을 뜻하는 중국어 단어의 병음은?", ["túshūguǎn", "bówùguǎn", "tǐyùguǎn", "zhǎnlǎnguǎn"], 1),
            Quiz("단어 '经常(jīngcháng)'의 뜻은 무엇일까요?", ["가끔", "자주, 종종", "결코 ~않다", "방금"], 2),
            Quiz("다음 중 '중요하다'를 뜻하는 단어는?", ["需要 (xūyào)", "主要 (zhǔyào)", "重要 (zhòngyào)", "只要 (zhǐyào)"], 3),
            Quiz("단어 '突然(tūrán)'과 가장 잘 어울리는 뜻은?", ["당연히", "비로소", "여전히", "갑자기"], 4),
            Quiz("'마시다'라는 뜻의 동사 '喝(hē)'와 함께 쓰기 가장 적절한 단어는?", ["面包 (miànbāo)", "饮料 (yǐnliào)", "苹果 (píngguǒ)", "米饭 (mǐfàn)"], 2)
        ]
        self.save_data() # 생성 후 바로 저장

    def save_data(self):
        """요구사항 11: 퀴즈 데이터와 최고 점수를 JSON 파일로 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"⚠️ 데이터 저장 중 오류가 발생했습니다: {e}")

    def display_menu(self):
        print("\n========================================")
        print("        🎯 나만의 퀴즈 게임 (HSK 3급) 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def get_user_input(self):
        while True:
            try:
                choice = input("선택: ").strip()
                if not choice:
                    print("⚠️ 빈 입력입니다. 다시 입력해주세요.")
                    continue
                choice_int = int(choice)
                if choice_int < 1 or choice_int > 5:
                    print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                    continue
                return choice_int
            except ValueError:
                print("⚠️ 잘못된 입력입니다. 숫자로만 입력해주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️ 프로그램이 강제 종료되었습니다. 안전하게 종료합니다.")
                self.save_data()
                sys.exit(0)

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_input()

            if choice == 1:
                print("\n[알림] 퀴즈 풀기 기능은 곧 구현됩니다!")
            elif choice == 2:
                print("\n[알림] 퀴즈 추가 기능은 곧 구현됩니다!")
            elif choice == 3:
                print("\n[알림] 퀴즈 목록 기능은 곧 구현됩니다!")
            elif choice == 4:
                print("\n[알림] 점수 확인 기능은 곧 구현됩니다!")
            elif choice == 5:
                self.save_data()
                print("\n게임을 종료합니다. 수고하셨습니다!")
                sys.exit(0)