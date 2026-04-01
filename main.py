import pandas as pd

class main:
    
    def main():

        df = pd.read_csv('Mar25-56.csv')

        # Parse with year inference (same logic as the notebook)
        df['Date'] = pd.to_datetime(df['Date'].apply(lambda x: f"{x} 2025"), format='%B %d %Y')

        for i in range(1, len(df)):
            if df.loc[i, 'Date'] < df.loc[i-1, 'Date']:
                df.loc[i:, 'Date'] = df.loc[i:, 'Date'].apply(
                    lambda d: d.replace(year=d.year + 1)
                )
                break

        df.to_csv('Mar25-56-fixed.csv', index=False)
        print(df['Date'].min(), 'to', df['Date'].max())

    if __name__ == '__main__':
        main() 