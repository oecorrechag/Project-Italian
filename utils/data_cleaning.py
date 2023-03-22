def data_cleaning(df):
    '''
        Aca se realizara la limpieza 1 de datos    
    '''

    df.columns = df.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    df.columns = map(str.lower, df.columns)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(' ', '_')

    return df