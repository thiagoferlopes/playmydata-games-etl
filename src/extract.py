#Importando bibliotecas#
import pandas as pd
from pathlib import Path
#======================#


#Função de extração dos dados#
def extract(csv_path: str) -> pd.DataFrame:
    path = Path(csv_path) 
    
    if not path.exists():
        raise FileNotFoundError(f'Arquivo não encontrado: {csv_path}')
    
    df = pd.read_csv(path)
    return df
#============================#