# 알림
> 본 리포지토리는 https://github.com/kimjunsung04/classcard_auto 를 포크하여 제작하였습니다.

본 프로그램은 2024/12/13일기준 모든 기능이 정상작동함을 확인하였습니다.
만약 본프로그램의 기능중 일부 혹은 전체가 동작하지 않는다면 이슈탭에 신고하여주십시오.

> [!Warning]
> 본 리포지토리를 이용하여 발생한 모든 책임은 사용자에게 있음을 고지합니다.<br>
> 또한 모든 법적책임은 사용자에게 있습니다. 자세한사항은 MIT라이선스를 참조하십시오.
> 본프로그램은 클래스카드측의 별도 통지가 있으면 사전공지 없이 삭제합니다.

# 변경사항
* 간단한 우회
   
요청 전송시 header에 일반 사용자 User-Agent 삽입

* 테스트학습 수정
   
테스트학습에서 발생된 예외 처리및 사용가능하게 수정

* 로그인 페이지XPATH수정

로그인페이지 버튼및 인풋창 위치 XPATH수정

# 지원하는 기능

* 테스트학습

* 스펠 학습

* 리콜 학습

* 암기 학습

* 스펠 학습 API 요청

* 리콜 학습 API 요청

* 암기 학습 API 요청

# 사용방법
사용은 직접 설치과 간편 설치으로 사용이 가능합니다.

## 간편 설치
본 리포지토리 릴리즈에서 설치파일을 받은후 안내에 따라 설치.(난이도 쉬움)
### 설치파일 간편설치 프로그램 서비스가 재개되었습니다!
자세한것은 https://github.com/heon0120/New-Classcard_Auto/releases/tag/V2.0.0 를 참조하세요.


표시되는 내용에 따라 진행하여 설치할수있습니다.(다른 패키지, 프로그램 설치 불필요)
### 선행조건
사용하기전 다음 조건을 충족해야합니다.

```
Kernal:Windows NT/ OS:Windows 10 32bit / 64bit 이상
여유 저장공간 500Mb이상
```
> [!Warning]
> 설치파일은 Mac에서 실행이 불가능합니다!

## 설치파일 간편설치 프로그램 서비스가 재개되었습니다!
자세한것은 https://github.com/heon0120/New-Classcard_Auto/releases/tag/V2.0.0 를 참조하세요.
#### 설치파일은 아래 내용이 포함되어있습니다.

* Python embedded package
> Python 배포용 패키지라고 생각하시면됩니다.

* 프로그램의 실행을 위한 라이브러리
> 자세한것은 requirements.txt를 참조하십시오.

* 프로그램의 과도한 실행을 막기위한 인증 프로그램
> 직접 제작한 인증 프로그램입니다. 프로그램의 소스코드는 https://github.com/heon0120/Program-Certified-Client/blob/main/renewclient.py 를 참조하세요.


## 직접 설치
본 리포지토리의 코드를 복제하여 파이썬이 설치된 환경에서 설치.(난이도 중간)
* * *


### 선행조건
사용하기전 아래 사항들이 설치가 되어있어야합니다.

```
Python, Chrome, Git
```

### 설치
1. 본 깃헙 리포지토리를 설치할 디렉토리에 복제합니다.

```Bash
git clone https://github.com/heon0120/New-Classcard_Auto.git

```

2. 실행에 필요한 라이브러리를 설치합니다.

```Bash
pip3 install -r requirements.txt 혹은
pip install -r requirements.txt
```

3. 다음명령어로 프로그램을 실행합니다.

```Bash
python3 main.py 혹은
python main.py
```
### 사용방법

1. 프로그램을 실행시킨후 나오는 텍스트에 따라 아이디, 비밀번호를 입력후 학습을 진행합니다.


# 이슈
본 프로그램사용시 발생한 코드는 이슈탭에 오류내용을남겨주세요.

# 라이센스
이 프로젝트는 MIT License 라이센스가 부여되어 있습니다.

본프로그램은 https://github.com/kimjunsung04/classcard_auto 을 참조하여 제작하였습니다.
