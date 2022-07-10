import pandas as pd


class Pipeline:  
    # Aplica lista de funciones sobre el dataframe dado
    def apply(self, df: pd.DataFrame, params) -> pd.DataFrame:
        for f in self.f_list:
            df = f(df, params)
        return df
    
    
    # Guardar lista de funciones a aplicar
    def set_f_list(self, f_list):
        self.f_list = f_list
        return
    
    
    # Obtener lista de funciones a aplicar
    def get_f_list(self):
        return self.f_list