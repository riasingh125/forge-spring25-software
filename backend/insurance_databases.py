import pandas as pd
import numpy as np

ma_plans = pd.read_csv('backend/CSVs/MassachusettsSBEPUF2024/MAPlans05102024.csv')
ct_plans = pd.read_csv('backend/CSVs/ConnecticutSBEPUF2024/CTPlans05102024.csv')
me_plans = pd.read_csv('backend/CSVs/MaineSBEPUF2024/MEPlans05102024.csv')
vt_plans = pd.read_csv('backend/CSVs/VermontSBEPUF2024/VTPlans05102024.csv')
ri_plans = pd.read_csv('backend/CSVs/RhodeIslandSBEPUF2024/RIPlans05102024.csv')


new_england_insurance_plans = pd.concat([ma_plans, ct_plans, me_plans,  vt_plans, ri_plans], ignore_index=True)

print(new_england_insurance_plans.isnull().sum())