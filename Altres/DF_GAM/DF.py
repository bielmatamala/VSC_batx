import pandas as pd
data = {
    'Gimnasta': [
        'Carlos Yulo', 'Artem Dolgopyat', 'Jake Jarman', 
        'Luke Whitehouse', 'Rayderley Zapata', 'Milad Karimi'
    ],
    'Pais': ['PHI', 'ISR', 'GBR', 'GBR', 'ESP', 'KAZ'],
    'Nota_D': [6.6, 6.4, 6.6, 6.5, 6.3, 6.3],
    'Nota_E': [8.433, 8.566, 8.266, 8.300, 8.300, 8.200],
    'Total': [15.033, 14.966, 14.866, 14.800, 14.600, 14.500],
    
    # Elementos Principales (Diagonales/Acrobacias - Valores D: A=0.1 ... I=0.9)
    'Diag_1': ['TripleBack', 'FrontDoubleTwist', 'TripleBack', 'FrontDoubleTwist', 'DoubleDoubleLayout', 'TripleBack'],
    'Val_D1': [0.7, 0.5, 0.7, 0.5, 0.8, 0.7],
    
    'Diag_2': ['FrontFullFrontDouble', 'DoubleBackFullOut', 'FrontDoubleTwist', 'DoubleBackFullOut', 'TripleBack', 'FrontDoubleTwist'],
    'Val_D2': [0.6, 0.5, 0.5, 0.5, 0.7, 0.5],
    
    'Diag_3': ['DoubleBackPike', 'DoubleBackTuck', 'DoubleBackFullOut', 'DoubleDoublePike', 'DoubleDouble', 'DoubleBackFullOut'],
    'Val_D3': [0.5, 0.4, 0.5, 0.6, 0.6, 0.5],
    
    'Salida': ['DoubleDouble', 'DoubleTuck', 'TripleBack', 'DoubleTuck', 'DoubleTuck', 'DoubleDouble'],
    'Val_Sal': [0.6, 0.4, 0.7, 0.4, 0.4, 0.6]
}

def DF_GAM():
    return pd.DataFrame(data)