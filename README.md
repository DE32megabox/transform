# transform
이 레파지토리는 영화 박스오피스 데이터를 변환하는 Transform 패키지의 사용법과 설치 방법에 대한 패키지입니다.
Transform 패키지는 영화 박스오피스 데이터의 ETL(Extract, Transform, Load) 과정 중 변환(Transform) 단계에서 데이터를 정제하고 가공하는 기능을 제공합니다.
## 설치방법

이 레포지토리는 다음과 같이 설치할 수 있습니다.

메인 브랜치에서 패키지를 설치하려면 다음 명령어를 사용합니다.
```bash
$ pip install git+https://github.com/DE32megabox/transform.git
```
특정 브랜치(예: dev/d1.0.0)에서 패키지를 설치하려면 다음 명령어를 사용합니다.
```bash
$ pip install git+https://github.com/DE32megabox/transform.git@dev/d1.0.0
```

## 로컬 개발 환경 설치

Transform 패키지를 로컬에서 개발하거나 수정하려면 다음 단계를 따라야합니다.

1. 레포지토리를 클론합니다.
```bash
$ git clone git@github.com:DE32megabox/transform.git
```
2. 클론한 디렉토리로 이동합니다.
```bash
$ cd transform
```
3. 가상 환경을 활성화하고 패키지를 설치합니다.
```bash
$ source .venv/bin/activate
$ pdm install
```
4. 설치가 완료되면 테스트를 실행하여 설치가 정상적으로 되었는지 확인합니다.
```bash
$ git clone git@github.com:DE32megabox/transform.git
$ cd transform
$ source .venv/bin/activate
$ pdm install
$ pytest
```
새로운 가상 환경을 생성하려면 다음 명령어를 사용합니다.
```bash
$ pdm venv create
```

## 실행예제
```
실행방법을 담은 bash 코드
```

```
코드를 실행하면 나오는 내용에 대한 코드
```
