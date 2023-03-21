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
print