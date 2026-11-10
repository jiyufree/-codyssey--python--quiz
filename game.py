import sys

class QuizGame:
    def __init__(self):
        """요구사항 10: 게임 전체를 관리하는 클래스 초기화"""
        pass # 이후 단계에서 퀴즈 목록과 점수 관리 기능을 추가할 예정입니다.

    def display_menu(self):
        """요구사항 2: 프로그램 실행 시 메뉴 출력"""
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
        """요구사항 3: 공통 입력/예외 처리 기준 적용"""
        while True:
            try:
                choice = input("선택: ").strip() # 공백 제거
                
                if not choice: # 빈 입력 처리
                    print("⚠️ 빈 입력입니다. 다시 입력해주세요.")
                    continue
                
                choice_int = int(choice) # 숫자 변환 시도
                if choice_int < 1 or choice_int > 5: # 허용 범위 밖 숫자 처리
                    print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                    continue
                
                return choice_int

            except ValueError: # 숫자 변환 실패 시
                print("⚠️ 잘못된 입력입니다. 숫자로만 입력해주세요.")
            except (KeyboardInterrupt, EOFError): # Ctrl+C 방어
                print("\n\n⚠️ 프로그램이 강제 종료되었습니다. 안전하게 종료합니다.")
                sys.exit(0)

    def run(self):
        """메뉴를 반복해서 띄우고 입력을 처리합니다."""
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
                print("\n게임을 종료합니다. 수고하셨습니다!")
                sys.exit(0)