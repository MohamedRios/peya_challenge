import pandas as pd
import numpy as np


def apply_pipeline(f_list: list, df: pd.DataFrame, params) -> pd.DataFrame:
    for f in f_list:
        df = f(df, params)
    return df

def delete_outliers(df: pd.DataFrame, params) -> pd.DataFrame:
    df = df[
                (df['revenue'] < params['max_revenue']) 
              & (df['event_1'] < params['max_event_1']) 
              & (df['event_2'] < params['max_event_2'])
    ]
    return df


def create_country_features(df: pd.DataFrame, params) -> pd.DataFrame:
    df['country_category'] = df.country.str.lower()
    df['country_category'] = np.where(df['country_category'].isin(params['valid_countries']),
                                        df['country_category'],
                                        'otros')
    return df


def create_source_features(df: pd.DataFrame, params) -> pd.DataFrame:
    df['source_category'] = df.source.str.lower()
    df['source_category'] = np.where(~df['source_category'].isin(params['valid_sources']),
                                         'desconocido', 
                                         df['source_category'])
    return df


def create_platform_features(df: pd.DataFrame, params) -> pd.DataFrame:
    df['platform_category'] = df.platform.str.lower()
    df['platform_category'] = np.where(~df['platform_category'].isin(params['valid_platforms']),
                                         'desconocido',
                                         df['platform_category'])
    return df


def create_device_features(df: pd.DataFrame, params) -> pd.DataFrame:
    df['device_category'] = df.device_family.str.lower()
    df['device_category'] = np.where(~df['device_category'].isin(params['valid_devices']),
                                         'otros', 
                                         df['device_category'])
    return df


def create_event_1_flag(df: pd.DataFrame, params) -> pd.DataFrame:
    df['has_event_1'] = np.where(df['event_1'] > 0, 1, 0)
    return df


def create_event_2_flag(df: pd.DataFrame, params) -> pd.DataFrame:
    df['has_event_2'] = np.where(df['event_2'] > 0, 1, 0)
    return df


def drop_metadata_columns(df: pd.DataFrame, params) -> pd.DataFrame:
    return df.drop(axis=1, columns=params['metadata_columns'])