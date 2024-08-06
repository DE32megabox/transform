# Transform
이 레파지토리는 영화 박스오피스 데이터를 변환하는 Transform 패키지의 사용법과 설치 방법에 대한 패키지입니다.
Transform 패키지는 영화 박스오피스 데이터의 ETL(Extract, Transform, Load) 과정 중 변환(Transform) 단계에서 데이터를 정제하고 가공하는 기능을 제공합니다.
## 설치방법

이 레파지토리는 다음과 같이 설치할 수 있습니다.

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

## 사용법
Transform 패키지는 데이터를 정제하고 가공하는 기능을 제공합니다. 아래는 주요 함수와 그 사용법에 대한 설명입니다.

### (1) apply_type2df 함수
주어진 데이터프레임의 특정 열을 숫자로 변환하고, 날짜 형식을 설정합니다.
```python
def apply_type2df(load_dt="20210101", path="~/megabox/tmp/movie_parquet"):
  df = pd.read_parquet(f"{path}/load_dt={load_dt}")
  num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']

for col in num_cols:
  df[col] = pd.to_numeric(df[col])
df['load_dt'] = load_dt
df['load_dt'] = df['load_dt'].astype(int).astype(str)
df['load_dt'] = pd.to_datetime(df['load_dt'], format='%Y%m%d')
print(df)
return df
```

### (2) transform2df 함수
데이터를 가공하여 필요한 열만 선택하여 새로운 데이터프레임을 반환합니다.
```python
def transform2df(load_dt="20210101"):
  df = apply_type2df(load_dt)
  num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange', 'load_dt']
  new_df = df[num_cols]
  return new_df
```

### (3) save2df 함수
가공된 데이터를 주어진 경로에 저장합니다.
```python
def save2df(load_dt="20210101", path="~/megabox/tmp/transform_parquet"):
  df = transform2df(load_dt)
  df.to_parquet('~/megabox/tmp/transform_parquet', partition_cols=['load_dt'])
  return df
```
