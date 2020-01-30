def test():
    print("test() 함수의 첫 줄")
    try:
        print("start try phase")
        return
        print("try return behind")
    except:
        print("except phase")
    else:
        print("else phase")
    finally:
        print("final phase")

test()