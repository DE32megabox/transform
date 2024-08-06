import pandas as pd
import os

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

def transform2df(load_dt="20210101"):
    #TODO
    # 1. apply_type2df로 df를 받아오기
    # 2. 결정하기
    # 2-1. 새로운 df를 만들어서 가져올 column만 복사하기
    # 2-2. 기존 df에 나머지 column을 모두 제거하기

    # 3. 2에서 완성한 df를 리턴하기
    
    df = apply_type2df(load_dt)
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange', 'load_dt']
    new_df = df[num_cols]
    # new_df.to_parquet('~/megabox/tmp/transform_parquet', partition_cols=['load_dt'])
    return new_df
     
def save2df(load_dt="20210101", path="~/megabox/tmp/transform_parquet"):
    #TODO
    # 1. save2t_df에서 df를 받아오기
    # 2. path에 저장하기
    df['load_dt'] = df['load_dt'].dt.strftime('%Y%m%d')
    df['load_dt'] = df['load_dt'].astype(int)
    
    df = transform2df(load_dt)
    df.to_parquet('~/megabox/tmp/transform_parquet', partition_cols=['load_dt'])
    return df



