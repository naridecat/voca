
#  `"SSSSSSSSs.      `"Ss.   `"Ss.
#       .s   S'        ss'     ss'
#       SS   '          ssssssssss
# `$SSSSSSSSSSSs.      ss      ss
#   .oOOOOOOo.         "SssssssS'
#  .O'      `O.     `$SSSSSSSSSSSSs.
#  o;        ;o           `SS
#  `o        o'            S'       
#   `OooooooO'             '; 하려고 만든 프로그램 이 아니라 공부할 시간에 만든 프로그램


expressions = [
    ["전진(하다); 진보(하다)","progress"],
    ["제안하다; (이론 등을) 제시하다", "propose"],
    ["생산[제조]하다; 농산물", "produce"],
    ["보호하다, 막다, 지키다", "protect"],
    ["찬반양론, 장단점", "pros and cons"],
    ["예언하다, 에측[예상]하다", "predict"],
    ["조심, 경계; 예방책", "precaution"],
    ["시기상조의, 조급한; 너무 이른, 조기의", "premature"],
    ["미리 보기; 시사(회), 시연(을 보다[보이다])", "preview"],
    ["이마", "forehead"],
    ["선조, 조상", "forefather"],
    ["으뜸가는, 중요한; 선두의, 맨 앞[먼저]의", "foremost"],
    ["예견[예지]하다", "foresee"],
    ["연기하다, 뒤로 미루다", "postpone"],
    ["(편지의) 추신; (책, 논문 등의) 후기", "postscript"],
    ["수입, 소득", "income"],
    ["섭취(량)", "intake"],
    ["감염시키다; 오염시키다", "infect"],
    ["통찰력", "insight"],
    ["투자하다", "invest"],
    ["결과, 성과", "outcome"],
    ["개요; 윤곽,외형", "outline"],
    ["전망, 예측;견해, 사고방식; 경치", "outlook"],
    ["뛰어난, 아주 훌륭한, 두드러진", "outstanding"],
    ["(가스.감정 등의) 배출구, 표현방법; 상점", "outlet"],
    ["...보다 뛰어나다, ...을 능가하다", "outdo"],
    ["완전한, 전적인; 말하다; (소리 등을) 내다", "utter"],
    ["최대의, 극도의", "utmost"],
    ["(곤란, 장애 등을) 극복하다, 이겨내다", "overcome"],
    ["간과하다, 못보고 넘어가다; 눈감아 주다", "overlook"],
    ["해외로; 해외에 있는", "overseas"],
    ["머리 위에, (하늘) 높이", "overhead"],
    ["따라잡다; (재난 등이) 덮치다, 압도하다", "overtake"],
    ["압도하다; 당황하게 하다", "overwhelm"],
    ["전복시키다; 폐지하다; 타도", "overthrow"],
    ["과로하다[시키다]", "overwork"],
    ["정규 교과 과정 이외의, 과외의", "extracurricular"],
    ["지구 밖의, 외계의", "extraterrestrial"],
    ["이상한; 비범한, 대단한", "extraordinary"],
    ["외향적인 사람", "extrovert"]
]
import random
re= False
k = -1
clar = "\033[32m"
text = ""
Type = random.randint(0,1)
while True:
    if not re:
        number = random.randint(0, len(expressions)-1)
    if Type == 0:
        print("\033[2J"+clar+expressions[number][0]+"\t"+text)
        for _ in range(len(expressions[number][0])*2):
            print("▔",end="")
        print("\033[37m")
        if input().lower().replace(",","") == expressions[number][1].lower().replace(",",""):
            clar, text = "\033[32m", "✓"
            re = False
            Type = random.randint(0,1)
        else:
            text="✖"
            clar="\033[31m"
            re = True
    else:
        print("\033[2J"+clar+expressions[number][1]+"\t"+text)
        for _ in range(len(expressions[number][0])*2):
            print("▔",end="")
        print("\033[37m")
        if input().lower().replace(",", "").replace(" ", "") in expressions[number][0].lower().replace(",", "").replace(" ", ""):
            clar, text = "\033[32m", "✓"
            re = False        
            Type = random.randint(0,1)
        else:
            text="✖"
            clar="\033[31m"
            re = True
