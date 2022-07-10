import pandas as pd
import numpy as np


# Validar que los input sean correctos
def validate_inputs(df: pd.DataFrame, params):
    colums = list(df.columns)
    valid_inputs = list(params.get('input_columns'))
    is_validated = all((sorted(colums) == sorted(valid_inputs)) 
                 & (df['zona'].isin(params.get('valid_zona')))
                 & (df['tipo_propiedad'].isin(params.get('valid_tipo_propiedad')))
                 & (df['vivienda_social'].isin(params.get('valid_vivienda_social')))
                 & (df['estado'].isin(params.get('valid_estado'))))
    if not is_validated:
        raise ValueError('Uno o más inputs no son válidos para el modelo')
    return df


# Dado un df y una lista de columnas, borra todas las rows que tengan nulos en cualquiera de esas columnas.
def delete_missing_values(df: pd.DataFrame, params) -> pd.DataFrame:
    for column in params.get('columns_with_missing_data_to_delete'):
        df = df[df[column].notna()]
    return df


def create_disposicion_category(df: pd.DataFrame, params) -> pd.DataFrame:
    df['disposicion_categoria'] = df['disposicion'].str.lower()
    df['disposicion_categoria'] = np.where(df['disposicion_categoria'].isin(params.get('valid_disposicion')),
                                        df['disposicion_categoria'],
                                        'desconocido')
    df['disposicion_is_missing'] = np.where(df['disposicion_categoria']=='desconocido', 0, 1)
    return df


def create_zona_feature(df: pd.DataFrame, params) -> pd.DataFrame:
    df['zona_categoria'] = df.zona.str.lower()
    df['zona_categoria'] = np.where(df['zona_categoria'].isin(params.get('zona_alta')),
                                         'alta', 
                                         'baja')
    return df


def drop_metadata_columns(df: pd.DataFrame, params) -> pd.DataFrame:
    metadata_columns = [c for c in df.columns if (c not in params.get('non_ordinal_categorical_features')
                                               and c not in params.get('ordinal_categorical_features')
                                               and c not in params.get('numerical_features'))]
    return df.drop(axis=1, columns=metadata_columns)