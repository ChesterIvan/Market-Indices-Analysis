import pandas as pd
import numpy as np
from market_analysis import MarketIndexAnalyzer
import os

def test_save_data_to_csv():
    # Setup dummy data
    analyzer = MarketIndexAnalyzer()
    dates = pd.date_range(start='2023-01-01', periods=5)
    data = {
        'S&P 500': np.random.rand(5),
        'Shanghai Composite': np.random.rand(5),
        'Hang Seng': np.random.rand(5),
        'CSI 300': np.random.rand(5),
        'Shenzhen Component': np.random.rand(5),
        'FTSE 100': np.random.rand(5),
        'NASDAQ Composite': np.random.rand(5)
    }
    analyzer.data = pd.DataFrame(data, index=dates)
    
    # Run method
    analyzer.save_data_to_csv()
    
    # Verify
    df = pd.read_csv('market_indices_data.csv', index_col=0)
    
    # Check index name
    print(f"Index name: {df.index.name}")
    if df.index.name != 'snapshot_date':
        print("FAIL: Index name is not 'snapshot_date'")
    else:
        print("PASS: Index name is 'snapshot_date'")
        
    # Check column order
    expected_order = [
         'Shanghai Composite', 'Shenzhen Component', 'CSI 300', 
         'S&P 500', 'NASDAQ Composite', 'FTSE 100', 'Hang Seng'
    ]
    print(f"Columns: {df.columns.tolist()}")
    
    if df.columns.tolist() == expected_order:
        print("PASS: Columns are correctly reordered")
    else:
        print("FAIL: Column order mismatch")
        print(f"Expected: {expected_order}")
        print(f"Actual:   {df.columns.tolist()}")

    # Cleanup
    if os.path.exists('market_indices_data.csv'):
        os.remove('market_indices_data.csv')

if __name__ == "__main__":
    test_save_data_to_csv()
