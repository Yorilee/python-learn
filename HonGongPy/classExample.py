class Character:
    def __init__(self, name):
        self.name = name
        self.classes = "초보자"
        self.weapon = "주먹"
        self.level = 1
    def attack(self):
        print("클래스{} {}님이 {}으로 공격하였습니다.".format(self.classes, self.name,  self.weapon))
    def levelup(self):
        self.level += 1
        print("클래스{} {}님의 레벨이 {}가 되었습니다.".format(self.classes, self.name,  self.level))

class Warrier(Character):
    def __init__(self,character):
        super().__init__(character.name)
        self.classes = "전사"
        self.weapon = "대검"
        self.level = character.level
        print("캐릭터 {}가 전사로 전직하였습니다! {}를 신나게 사용해볼까요?!?!".format(self.name, self.weapon))

class Wizard(Character):
    def __init__(self,character):
        super().__init__(character.name)
        self.classes = "마법사"
        self.weapon = "스태프"
        self.level = character.level
        print("캐릭터 {}가 전사로 전직하였습니다! {}를 신나게 사용해볼까요?!?!".format(self.name, self.weapon))



while(1):
    print("===========================")
    print("1.캐릭터 생성")
    print("2.로그인")
    print("3.레벨업")
    print("4.로그아웃")
    print("z.게임 종료")
    print("===========================")
    command = input("command 입력 >")
    if(command == 'z'):
        break
    # 1. 캐릭터 생성
    elif command == '1':
        '''
        print("=======================")
        print("1.초보자")
        print("2.검사")
        print("3.마법사")
        print("=======================")
        class_select = int(input("* 캐릭터 클래스 선택 * >"))
        character_name = str(input("* 캐릭터명 입력 >"))
        char = Character(character_name)
        if class_select == 1 :
            pass
        elif class_select == 2:
            charlist.append(Warrier(character_name))
        elif class_select == 3:
            charlist.append(Wizard(character_name))
        else :
            pass
        '''
        char1 = Character("test")
        char1.attack()
        char1.levelup()
        char2 = Warrier(char1)
        char2.attack()
        char2.levelup()
        char2.levelup()
        char3 = Wizard(char1)
        char3.attack()
        char3.levelup()