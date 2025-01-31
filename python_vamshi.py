def prep_data_inq(self, df_inq_raw):
    
    try:

        df_inq_raw.columns = df_inq_raw.columns.str.lower()
        df_inq_raw = df_inq_raw.drop(columns = ["account_type"], errors = "ignore")
        df_inq_raw = df_inq_raw\
        .rename(columns = {
            'date_of_enquiry':'inq_date',
            'enquiry_amount':'inq_amt',
            'enquiry_member_name':'inq_member_name',
            'bureau_reference_number': 'bureau_report_reference_number'
        })

        df_inq_raw['id'] =  df_inq_raw['bureau_report_reference_number']
        df_inq_raw['inq_date'] = pd.to_datetime(df_inq_raw['inq_date'], format='%Y-%m-%d')
        df_inq_raw['created_at'] = pd.to_datetime(df_inq_raw['created_at'], format='%Y-%m-%d')
        df_inq_raw['inq_date'] = df_inq_raw['inq_date'].dt.date
        df_inq_raw['created_at'] = df_inq_raw['created_at'].dt.date
        df_inq_raw['inq_date'] = pd.to_datetime(df_inq_raw['inq_date'], format='%Y-%m-%d')
        df_inq_raw['created_at'] = pd.to_datetime(df_inq_raw['created_at'], format='%Y-%m-%d')
        df_inq_raw['retro_date'] = df_inq_raw['created_at']
        df_inq_raw['inq_amt'] = pd.to_numeric(df_inq_raw['inq_amt'])
        df_inq_raw['account_type_code'] = df_inq_raw['account_type_code'].astype('int')
        df_inq_raw['account_type'] = np.where(df_inq_raw['account_type_code'] == 0 ,'Other' ,
                                    np.where(df_inq_raw['account_type_code'] == 1 ,'Auto Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 2 ,'Housing Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 3 ,'Property Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 4 ,'Loan Against Shares/Securities' ,
                                    np.where(df_inq_raw['account_type_code'] == 5 ,'Personal Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 6 ,'Consumer Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 7 ,'Gold Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 8 ,'Education Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 9 ,'Loan To Professional' ,
                                    np.where(df_inq_raw['account_type_code'] == 10, 'Credit Card' ,
                                    np.where(df_inq_raw['account_type_code'] == 11, 'Lease' ,
                                    np.where(df_inq_raw['account_type_code'] == 12, 'Overdraft' ,
                                    np.where(df_inq_raw['account_type_code'] == 13, 'Two - Wheeler Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 14, 'Non - Funded Credit Facility' ,
                                    np.where(df_inq_raw['account_type_code'] == 15, 'Loan Against Bank Deposits' ,
                                    np.where(df_inq_raw['account_type_code'] == 16, 'Fleet Card' ,
                                    np.where(df_inq_raw['account_type_code'] == 17, 'Commercial Vehicle Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 18, 'Telco - Wireless' ,
                                    np.where(df_inq_raw['account_type_code'] == 19, 'Telco - Broadband' ,
                                    np.where(df_inq_raw['account_type_code'] == 20, 'N/A' ,
                                    np.where(df_inq_raw['account_type_code'] == 21, 'Seller Financing' ,
                                    np.where(df_inq_raw['account_type_code'] == 23, 'GECL Loan Secured' ,
                                    np.where(df_inq_raw['account_type_code'] == 24, 'GECL Loan Unsecured' ,
                                    np.where(df_inq_raw['account_type_code'] == 31, 'Secured Credit Card' ,
                                    np.where(df_inq_raw['account_type_code'] == 32, 'Used Car Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 33, 'Construction Equipment Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 34, 'Tractor Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 35, 'Corporate Credit Card' ,
                                    np.where(df_inq_raw['account_type_code'] == 36, 'Kisan Credit Card' ,
                                    np.where(df_inq_raw['account_type_code'] == 37, 'Loan On Credit Card' ,
                                    np.where(df_inq_raw['account_type_code'] == 38, 'Prime Minister Jaan Dhan Yojana - Overdraft' ,
                                    np.where(df_inq_raw['account_type_code'] == 39, 'Mudra Loans - Shishu/Kishor/Tarun' ,
                                    np.where(df_inq_raw['account_type_code'] == 40, 'Microfinance Business Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 41, 'Microfinance Personal Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 42, 'Microfinance Housing Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 43, 'Microfinance Others' ,
                                    np.where(df_inq_raw['account_type_code'] == 44, 'Pradhan Mantri Awas Yojana - Credit Link Subsidy Scheme MAY CLSS' ,
                                    np.where(df_inq_raw['account_type_code'] == 45, 'P2P Personal Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 46, 'P2P Auto Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 47, 'P2P Education Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 50, 'Business Loan - Secured' ,
                                    np.where(df_inq_raw['account_type_code'] == 51, 'Business Loan - General' ,
                                    np.where(df_inq_raw['account_type_code'] == 52, 'Business Loan - Priority Sector - Small Business' ,
                                    np.where(df_inq_raw['account_type_code'] == 53, 'Business Loan - Priority Sector - Agriculture' ,
                                    np.where(df_inq_raw['account_type_code'] == 54, 'Business Loan - Priority Sector - Others' ,
                                    np.where(df_inq_raw['account_type_code'] == 55, 'Business Non - Funded Credit Facility - General' ,
                                    np.where(df_inq_raw['account_type_code'] == 56, 'Business Non - Funded Credit Facility - Priority Sector - Small Business' ,
                                    np.where(df_inq_raw['account_type_code'] == 57, 'Business Non - Funded Credit Facility - Priority Sector - Agriculture' ,
                                    np.where(df_inq_raw['account_type_code'] == 58, 'Business Non - Funded Credit Facility - Priority Sector - Others' ,
                                    np.where(df_inq_raw['account_type_code'] == 59, 'Business Loan Against Bank Deposits' ,
                                    np.where(df_inq_raw['account_type_code'] == 61, 'Business Loan - Unsecured' ,
                                    np.where(df_inq_raw['account_type_code'] == 64, 'Insurance' ,
                                    np.where(df_inq_raw['account_type_code'] == 69, 'Short Term Personal Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 70, 'Priority Sector - Gold Loan' ,
                                    np.where(df_inq_raw['account_type_code'] == 71, 'Temporary Overdraft', None))))))))))))))))))))))))))))))))))))))))))))))))))))))))


        df_inq_raw['retro_date_trunc'] = df_inq_raw['retro_date'].dt.to_period('M').dt.to_timestamp()
        df_inq_raw['Inq_Date_trunc'] = df_inq_raw['inq_date'].dt.to_period('M').dt.to_timestamp()
        df_inq_raw['mn_diff_retro_inq'] = ((df_inq_raw['retro_date_trunc'].dt.year - df_inq_raw['Inq_Date_trunc'].dt.year) * 12 + 
                                    (df_inq_raw['retro_date_trunc'].dt.month - df_inq_raw['Inq_Date_trunc'].dt.month))
        df_inq_raw['inq_date'] = df_inq_raw['inq_date'].where(df_inq_raw['inq_date'] > '1950-01-01', None)
        df_inq_raw['retro_date'] = df_inq_raw['retro_date'].where(df_inq_raw['retro_date'] > '1950-01-01', None)

        df_inq_raw['dedup_rn'] = df_inq_raw\
        .sort_values(by = ['id', 'inq_date', 'account_type', 'inq_amt'], ascending=[True, True, True, False])\
        .groupby(['id', 'inq_date', 'account_type'], dropna = False).cumcount() + 1


        df_inq_raw2 = df_inq_raw[
            (df_inq_raw['dedup_rn'] == 1) & 
            (df_inq_raw['retro_date'] > df_inq_raw['inq_date']) & 
            (df_inq_raw['mn_diff_retro_inq'] <= 36) & 
            (df_inq_raw['retro_date'].notnull()) & 
            (df_inq_raw['inq_date'].notnull()) & 
            (df_inq_raw['account_type_code'] <= 71)
        ]

        df_inq_raw3 = df_inq_raw2[['id', 'retro_date', 'inq_member_name', 'inq_date', 'account_type', 'inq_amt']]\
        .reset_index(drop = True)

        return df_inq_raw3.copy()
    
    except Exception as e:
        
        message = "Service Exception Inquiry Data prep:" + str(sys.exc_info()[-1].tb_lineno) + '-' + str(e)
        print(message, flush = True)

