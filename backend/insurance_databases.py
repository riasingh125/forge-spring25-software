import pandas as pd
import numpy as np

ma_benefits = pd.read_csv('CSVs/MassachusettsSBEPUF2024/MABenefits05102024.csv')
ma_business_rules = pd.read_csv('CSVs/MassachusettsSBEPUF2024/MABusinessRules05102024.csv')
ma_networks  = pd.read_csv('CSVs/MassachusettsSBEPUF2024/MANetworks05102024.csv')
ma_plans = pd.read_csv('CSVs/MassachusettsSBEPUF2024/MAPlans05102024.csv')
ma_rates = pd.read_csv('CSVs/MassachusettsSBEPUF2024/MARates05102024.csv')
ma_service_areas = pd.read_csv('CSVs/MassachusettsSBEPUF2024/MAServiceAreas05102024.csv')

ct_benefits = pd.read_csv('CSVs/ConnecticutSBEPUF2024/CTBenefits05102024.csv')
ct_business_rules = pd.read_csv('CSVs/ConnecticutSBEPUF2024/CTBusinessRules05102024.csv')
ct_networks = pd.read_csv('CSVs/ConnecticutSBEPUF2024/CTNetworks05102024.csv')
ct_plans = pd.read_csv('CSVs/ConnecticutSBEPUF2024/CTPlans05102024.csv')
ct_rates = pd.read_csv('CSVs/ConnecticutSBEPUF2024/CTRates05102024.csv')
ct_service_areas = pd.read_csv('CSVs/ConnecticutSBEPUF2024/CTServiceAreas05102024.csv')

me_benefits = pd.read_csv('CSVs/MaineSBEPUF2024/MEBenefits05102024.csv')
me_business_rules = pd.read_csv('CSVs/MaineSBEPUF2024/MEBusinessRules05102024.csv')
me_networks = pd.read_csv('CSVs/MaineSBEPUF2024/MENetworks05102024.csv')
me_plans = pd.read_csv('CSVs/MaineSBEPUF2024/MEPlans05102024.csv')
me_rates = pd.read_csv('CSVs/MaineSBEPUF2024/MERates05102024.csv')
me_service_areas = pd.read_csv('CSVs/MaineSBEPUF2024/MEServiceAreas05102024.csv')

vt_benefits = pd.read_csv('CSVs/VermontSBEPUF2024/VTBenefits05102024.csv')
vt_business_rules = pd.read_csv('CSVs/VermontSBEPUF2024/VTBusinessRules05102024.csv')
vt_networks = pd.read_csv('CSVs/VermontSBEPUF2024/VTNetworks05102024.csv')
vt_plans = pd.read_csv('CSVs/VermontSBEPUF2024/VTPlans05102024.csv')
vt_service_areas = pd.read_csv('CSVs/VermontSBEPUF2024/VTServiceAreas05102024.csv')

ri_benefits = pd.read_csv('CSVs/RhodeIslandSBEPUF2024/RIBenefits05102024.csv')
ri_business_rules = pd.read_csv('CSVs/RhodeIslandSBEPUF2024/RIBusinessRules05102024.csv')
ri_networks = pd.read_csv('CSVs/RhodeIslandSBEPUF2024/RINetworks05102024.csv')
ri_plans = pd.read_csv('CSVs/RhodeIslandSBEPUF2024/RIPlans05102024.csv')
ri_service_areas = pd.read_csv('CSVs/RhodeIslandSBEPUF2024/RIServiceAreas05102024.csv')


new_england_benefits = pd.concat([ma_benefits, ct_benefits, me_benefits, vt_benefits, ri_benefits], ignore_index= True)
new_england_business_rules = pd.concat([ma_business_rules, ct_business_rules, me_business_rules, vt_business_rules], ignore_index= True)
new_england_networks = pd.concat([ma_networks, ct_networks, me_networks, vt_networks, ri_networks], ignore_index= True)
new_england_insurance_plans = pd.concat([ma_plans, ct_plans, me_plans,  vt_plans, ri_plans], ignore_index=True)
new_england_service_areas = pd.concat([ma_service_areas, ct_service_areas, me_service_areas, vt_service_areas, ri_service_areas], ignore_index= True)

print(new_england_benefits.isnull().sum())
print('next null\n')
print(new_england_business_rules.isnull().sum())
print('next null\n')
print(new_england_networks.isnull().sum())
print('next null\n')
print(new_england_insurance_plans.isnull().sum())
print('next null\n')
print(new_england_service_areas.isnull().sum())






