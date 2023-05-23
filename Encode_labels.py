suppresed_level_flags = {'S': 'Suppressed to avoid disclosing data for individual companies',
                         'W': 'Suppressed to avoid disclosing data for individual companies; '
                              'data are included in higher-level totals',
                         'B': 'Suppressed to avoid disclosing data for individual companies; '
                              'data are included in higher-level totals '
                              'but are also suppressed if the total is based on fewer than three companies',
                         'U': 'Suppressed to avoid disclosing data for individual companies '
                              'and the corresponding data for all higher-level '
                              'totals that include the suppressed data',
                         'R': 'Suppressed to avoid disclosing data for individual companies; '
                              'data are included in higher-level totals but are also '
                              'suppressed if the total is based on fewer than ten companies',
                         'T': 'Suppressed to avoid disclosing data for individual companies; '
                              'data are included in higher-level totals but are also suppressed '
                              'if the total is based on fewer than 25 companies.',
                         'O': 'Suppressed to avoid disclosing data for individual companies '
                              'and higher-level totals; data are included in summary measures such '
                              'as medians and averages.',
                         'L': 'Suppressed to avoid disclosing data for individual companies '
                              'and higher-level totals; data are included in distribution-based summary '
                              'measures such as percentiles.',
                         'M': 'Suppressed to avoid disclosing data for individual companies '
                              'and higher-level totals; data are included in higher-level totals and '
                              'summary measures, but the measures are adjusted to account for the suppressed data',
                         'K': 'Suppressed to avoid disclosing data for individual companies and '
                              'higher-level totals; data are included in higher-level totals '
                              'and summary measures, but the measures are adjusted to account for '
                              'the suppressed data, and the estimates are subject to high sampling variability',
                         'I': 'Suppressed to avoid disclosing data for individual companies and higher-level totals; '
                              'data are included in higher-level totals and summary measures, '
                              'but the measures are based on imputed data'}

novalide_date_flags = {'S': 'The Census Bureau is not reporting certain information due to'
                            ' confidentiality or data quality concerns',
                       'X': 'indicating that a particular data point is not relevant'}


def make_mask(data):
    emp_flags = {'a': (data["EMP"] >= 0) & (data["EMP"] < 20), 'b': (data["EMP"] >= 20) & (data["EMP"] < 100),
                       'c': (data["EMP"] >= 100) & (data["EMP"] < 250), 'e': (data["EMP"] >= 250) & (data["EMP"] < 500),
                       'f': (data["EMP"] >= 500) & (data["EMP"] < 1000),
                       'g': (data["EMP"] >= 1000) & (data["EMP"] < 2500),
                       'h': (data["EMP"] >= 2500) & (data["EMP"] < 5000),
                       'i': (data["EMP"] >= 5000) & (data["EMP"] < 10000),
                       'j': (data["EMP"] >= 10000) & (data["EMP"] < 25000),
                       'k': (data["EMP"] >= 25000) & (data["EMP"] < 50000),
                       'l': (data["EMP"] >= 50000) & (data["EMP"] < 100000), 'm': (data["EMP"] >= 100000)}

    return emp_flags


useless_atr_list = ['NAICS2012_LABEL', 'NAICS2012_F', 'ASECB_LABEL', 'YIBSZFI_LABEL',
                    'NEWFUNDREL_LABEL', 'RCPPDEMP', 'RCPPDEMP_F',
                    'RCPPDEMP_PCT', 'RCPPDEMP_PCT_F',  'EMP',
                    'EMP_PCT_F', 'PAYANN_PCT_F', 'RCPPDEMP_S',
                    'RCPPDEMP_PCT_S', 'RCPPDEMP_PCT_S_F', 'EMP_PCT_S_F',
                    'PAYANN_PCT_S_F', 'FIRMPDEMP_S', 'FIRMPDEMP_PCT_S',
                    'EMP_S', 'EMP_S_F', 'EMP_PCT_S',
                    'EMP_PCT_S_F', 'PAYANN_S', 'PAYANN_S_F', 'PAYANN_PCT_S']