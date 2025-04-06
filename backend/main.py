import rankings
import GeminiScript2
import asyncio


def main():
	plan = rankings.WeightedPlanRanking(
		weights={
			'coverage_of_all_benefits': 0.0,
			'affordability': 1,
			'personalized_coverage': 1.0,
			'emergency_coverage': 0.2,
			'flexibility_of_coverage': 0.1,
			'convenience_of_coverage': 0.1,
			'geographic_coverage': 0.1
		},
		corpus='''
BLUE CROSS AND BLUE SHIELD OF TEXAS
A DIVISION OF HEALTH CARE SERVICE CORPORATION
(herein called "BCBSTX" or "HMO")
1001 East Lookout Drive
Richardson, Texas 75082
1-888-697-0683
www.bcbstx.com
EVIDENCE OF COVERAGE
NOTICE TO CONSUMER
This Consumer Choice of Benefits Health Maintenance Organization health care plan, either in
whole or in part, does not provide state-mandated health benefits normally required in evidences
of coverage in Texas. This standard Health Benefit Plan may provide a more affordable health
plan for You, although, at the same time, it may provide You with fewer health plan benefits than
those normally included as state mandated health benefits in Texas. Please consult with Your
insurance agent to discover which state-mandated health benefits are excluded in this evidence of
coverage.
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation ("HMO"), agrees to provide
You coverage for benefits in accordance with the conditions, rights, and privileges set forth in this Evidence of
Coverage. The Evidence of Coverage determines the terms and conditions of coverage. Provisions of this Evidence
of Coverage include the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS and any amendments, or attachments,
which may be delivered with the Evidence of Coverage or added later. This Evidence of Coverage is currently
certified by the Exchange as a Qualified Health Plan.
Notice of Ten-Day Right To Examine. Within ten days after its delivery to You, this Evidence of Coverage may
be surrendered by returning it to HMO at our administrative office, agent, or the entity through whom it was
purchased. Upon such surrender, any Premiums paid will be returned. Subscriber is responsible for repaying HMO
for any services rendered or claims paid by HMO on behalf of the Subscriber, or any Dependents, during the ten-
day examination period.
IN CONSIDERATION of the payment of Premiums in accordance with the provisions hereof, this Evidence of
Coverage describes Your covered health care benefits. Coverage for services or supplies is provided only if
furnished while You are a Member and this coverage is in force. Except as shown in GENERAL PROVISIONS,
coverage is not provided for any services received before coverage starts or after coverage ends.
Certain words have specific meanings in this Evidence of Coverage. Defined terms are capitalized and shown in
the appropriate provision or in the DEFINITIONS section and in the amendments or attachments to this Evidence of
Coverage, if applicable. Hereinafter, we refer to the Health Insurance Marketplace as "Exchange".
This Evidence of Coverage is not a workers' compensation insurance policy. Ask Your employer if they
subscribe to the workers' compensation system. This Evidence of Coverage is governed by applicable federal
law and the laws of Texas. Any reference to "applicable law" will include applicable laws and rules, including but
not limited to statutes, ordinances, and administrative decisions and regulations.
Please read this entire Evidence of Coverage carefully, as it describes Your rights and obligations and those of the
HMO. It is Your responsibility to understand these terms and conditions, because in some circumstances, certain
medical services are not covered or may require Prior Authorization by HMO. This Evidence of Coverage may be
delivered to You electronically, but a paper copy is available upon request.
No services are covered by this Evidence of Coverage if current Premiums have not been paid. If the Evidence of
Coverage is terminated for nonpayment of Premium, You are responsible for the cost of services received during
the grace period described in HOW THE PLAN WORKS.
This Evidence of Coverage applies only to Your HMO coverage. It does not limit Your ability to receive health care
services that are not Covered Services.
No Participating Provider or other Provider, institution, facility or agency is an agent or employee of HMO.
THIS EVIDENCE OF COVERAGE IS NOT A MEDICARE SUPPLEMENT POLICY. If You are
eligible for Medicare, review the Guide to Health Insurance for people with Medicare available from
BCBSTX..
TX-I-EX-H-CC-EOC-25
TX-I-EX-H-CC-EOC-25
Have a complaint or need help?
If You have a problem with a claim or Your Premium, call Your insurance company or HMO first. If You
can't work out the issue, the Texas Department of Insurance may be able to help.
Even if You file a complaint with the Texas Department of Insurance, You should also file a complaint or
appeal through Your insurance company or HMO. If You don't, You may lose Your right to appeal.
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation
To get information or file a complaint with Your insurance company or HMO:
Call: Blue Cross and Blue Shield of Texas
Toll-Free: 1-888-697-0683
Email: BCBSTXComplaints@bcbstx.com
Mail: P. . O. Box 660044, Dallas, TX 75266-0044
The Texas Department of Insurance
To get help with an insurance question or file a complaint with the state:
Call with a question: 1-800-252-3439
File a complaint: www.tdi.texas.gov
Email: ConsumerProtection@tdi.texas.gov
Mail: Consumer Protection, MC: CO-CP,
Texas Department of Insurance, PO Box 12030, Austin, TX 78711-2030
Tiene una queja o necesita ayuda?
Si tiene un problema con una reclamación o con su prima de seguro, llame primero a su compañía de
seguros o HMO. Si no puede resolver el problema, es posible que el Departamento de Seguros de Texas
(Texas Department of Insurance, por su nombre en inglés) pueda ayudar.
Aun si usted presenta una queja ante el Departamento de Seguros de Texas, también debe presentar una
queja a través del proceso de quejas o de apelaciones de su compañía de seguros o HMO. Si no lo hace,
podría perder su derecho para apelar.
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation
Para obtener información o para presentar una queja ante su compañía de seguros o HMO:
Llame a: Blue Cross and Blue Shield of Texas
Teléfono gratuito: 1-888-697-0683
Correo electrónico: BCBSTXComplaints@bcbstx.com
Dirección postal: P. O. Box 660044, Dallas, TX 75266-0044
El Departamento de Seguros de Texas
Para obtener ayuda con una pregunta relacionada con los seguros o para presentar una queja ante el estado:
Llame con sus preguntas al: 1-800-252-3439
Presente una queja en: www.tdi.texas.gov
Correo electrónico: ConsumerProtection@tdi.texas.gov
Dirección postal: Consumer Protection, MC: CO-CP, Texas Department of Insurance, PO Box
12030, Austin, TX 78711-2030
TX-I-EX-H-CC-EOC-25
TABLE OF CONTENTS
EVIDENCE OF COVERAGE
IMPORTANT NOTICE
SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS
ENCLOSURE
DEFINITIONS
1
WHO GETS BENEFITS
11
HOW THE PLAN WORKS
14
COMPLAINT AND APPEAL PROCEDURES
27
COVERED SERVICES AND BENEFITS
32
LIMITATIONS AND EXCLUSIONS
49
PHARMACY BENEFITS
57
GENERAL PROVISIONS
69
PEDIATRIC VISION CARE BENEFITS
83
NOTICE OF RIGHT TO AN ADEQUATE NETWORK
87
AMENDMENTS
TX-I-EX-H-CC-EOC-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
MyBlue Health BronzeSM 402
MyBlue Health Network
The following Benefit Highlights summarizes the coverage available under the offered HMO Plan. The
Evidence of Coverage (EOC) documents You will receive after You enroll will provide more detailed
information about this plan. This summary should be reviewed along with the Limitations and Exclusions.
All Covered Services (except in emergencies) must be provided by or through Member's Participating
Primary Care Physician/Practitioner, who may refer them for further treatment by Providers in the
applicable network of Participating Specialists and Hospitals. Female Members may visit a Participating
OB/GYN Physician in their Primary Care Physician's/Practitioner's Provider network for diagnosis and
treatment without a Referral from their Primary Care Physician/Practitioner. Urgent Care, Retail Health
Clinics and Virtual Visits do not require Primary Care Physician/Practitioner Referral. Some services may
require Prior Authorization by HMO.
IMPORTANT NOTE: Copayments shown below indicate the amount You are required to pay, expressed
as either a fixed dollar amount or a percentage of the Allowable Amount and applied for each occurrence,
unless otherwise indicated. You will not be liable for any Copayments/Coinsurance once applicable
Deductibles and out-of-pocket maximums have been met. Copayments/Coinsurance, Deductibles and out-
of-pocket maximums may be adjusted for various reasons as permitted by applicable law.
If You have selected Your Primary Care Physician/Practitioner from the Selected Primary Care Physicians,
Copayments for office visits and certain other services will be a $0 Copayment. Not all services received
from Your Selected PCP will be eligible for the $0 Copayment. The services that are eligible for $0
Copayment are shown below.
Out-of-Pocket Maximums Per Calendar Year
including Pharmacy Benefits
Per Individual Member
$9,200
Per Family
$18,400
Deductibles Per Calendar Year
including Pharmacy Benefits
Per Individual Member
$7,400
Per Family
$14,800
Professional Services
Primary Care Physician/Practitioner ("PCP")
$105 Copay
Office or Home Visit
Participating Specialist Physician ("Specialist")
50% Coinsurance after Deductible
Office or Home Visit
Select Professional Services
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
Selected Primary Care Physician/Practitioner
No Copay
("PCP") Office Visit
PCP Office Visit
Certain X-Rays, Ultrasound, ECG (ordered and
performed by a Selected PCP)
Allergy Testing
Minor procedures performed in the office, i.e. biopsy
and wart removal
Select Immunizations and administration
Chronic disease management programs
Health education programs/Wellness services
Telehealth
Inpatient Hospital Services
Inpatient Hospital Services, for each admission
$850 Copay, plus 50% Coinsurance after Deductible
Outpatient Facility Services
Outpatient Surgery - Hospital Setting
$600 Copay, plus 50% Coinsurance after Deductible
Outpatient Surgery - Other Facility Setting
$600 Copay, plus 40% Coinsurance after Deductible
Outpatient Surgery - Physician
$200 Copay, plus 50% Coinsurance after Deductible
-Radiation Therapy
50% Coinsurance after Deductible
-Dialysis
-Urgent Care Facility Services
Outpatient Infusion Therapy Services
Routine Maintenance Drug - Hospital Setting
$1,000 Copay
Routine Maintenance Drug - Home, Office,
$100 Copay
Infusion Suite Setting
Non-Maintenance Drug
50% Coinsurance after Deductible
Chemotherapy
50% Coinsurance after Deductible
Outpatient Laboratory and X-Ray Services
Computerized Tomography (CT Scan), Computerized
50% Coinsurance after Deductible
Tomography Angiography (CTA), Magnetic
Resonance Angiography (MRA), Magnetic Resonance
Imaging (MRI), Positron Emission Tomography (PET
Scan), SPECT/Nuclear Cardiology studies, per
procedure - Hospital Setting
Computerized Tomography (CT Scan), Computerized
40% Coinsurance after Deductible
Tomography Angiography (CTA), Magnetic
Resonance Angiography (MRA), Magnetic Resonance
Imaging (MRI), Positron Emission Tomography (PET
Scan), SPECT/Nuclear Cardiology studies, per
procedure - Other Facility Setting
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
Other X-Ray Services -Hospital Setting
50% Coinsurance after Deductible
Other X-Ray Services -Other Facility Setting
40% Coinsurance after Deductible
Outpatient Lab - Hospital Setting
50% Coinsurance after Deductible
Outpatient Lab - Other Facility Setting
40% Coinsurance after Deductible
Rehabilitation Services and Habilitation Services
Rehabilitation Services, Habilitation Services and
50% Coinsurance after Deductible; unless otherwise
Therapies, per visit
covered under Inpatient Hospital Services.
Limited to 35 visits per Calendar Year, including
chiropractic services for Rehabilitation Services.
Limited to 35 visits per Calendar Year, including
chiropractic services for Habilitation Services.
Visit limitations do not apply to Behavioral Health
Services.
Benefits for Autism Spectrum Disorder will not apply
towards and are not subject to any Rehabilitation
Services and Habilitation Services visit maximums.
Maternity Care and Family Planning Services
Maternity Care
Prenatal and Postnatal Visit - Copay is applied to
$105 Copay for PCP or 50% Coinsurance after
the first office visit only. Subsequent office visits
Deductible for Specialist
are covered in full.
Inpatient Hospital Services, for each admission
$850 Copay, plus 50% Coinsurance after Deductible
Family Planning Services
Diagnostic counseling, consultations and planning
$105 Copay for PCP or 50% Coinsurance after
services
Deductible for Specialist; unless otherwise covered
Insertion or removal of intrauterine device (IUD),
under Contraceptive Services and Supplies described
including cost of device
in Health Maintenance and Preventive Services.
Diaphragm or cervical cap fitting, including cost of
device
Insertion or removal of birth control device
implanted under the skin, including cost of device
Injectable contraceptive drugs, including cost of
drug
Vasectomy
$850 Copay, plus 50% Coinsurance after Deductible
for Inpatient Hospital Services, or Outpatient Surgery
charges as described in Outpatient Facility Services
for Outpatient Surgery
Infertility Services
Diagnostic counseling, consultations, planning and
$105 Copay for PCP or 50% Coinsurance after
treatment services
Deductible for Specialist
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a
Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
Behavioral Health Services
Outpatient Mental Health Care
40% Coinsurance after Deductible for PCP office or
home visit or
40% Coinsurance after Deductible for outpatient
services, as applicable. Other Covered Services paid
same as any other physical illness.
Inpatient Mental Health Care
$850 Copay, plus 50% Coinsurance after Deductible
Serious Mental Illness
40% Coinsurance after Deductible for PCP office or
home visit or
40% Coinsurance after Deductible for outpatient
services, as applicable. Other Covered Services paid
same as any other physical illness.
Chemical Dependency Services
40% Coinsurance after Deductible for PCP office or
home visit or
40% Coinsurance after Deductible for outpatient
services, as applicable. Other Covered Services paid
same as any other physical illness.
Emergency Services
Emergency Care
$950 Copay, plus 50% Coinsurance after Deductible,
waived if admitted. (If admitted, any charges
described in Inpatient Hospital Services will apply.)
Urgent Care
Each Member is eligible to receive two (2) Urgent Care visits covered at 100% when furnished by a
Participating Urgent Care Provider.
Urgent Care Services
$160 Copay
Any additional charges as described in Outpatient
Laboratory and X-Ray Services may also apply.
Retail Health Clinics
Retail Health Clinics
PCP amount described in Professional Services
Virtual Visits
Virtual Visits
$105 Copay for PCP or 50% Coinsurance after
Deductible for Specialist
Ambulance Services
Ambulance Services
50% Coinsurance after Deductible
Extended Care Services
Skilled Nursing Facility Services, for each day, up to
50% Coinsurance after Deductible
25 days per Calendar Year
Hospice Care, for each day
50% Coinsurance after Deductible; unless otherwise
covered under Inpatient Hospital Services.
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
Home Health Care, per visit, up to 60 visits per
50% Coinsurance after Deductible
Calendar Year
Health Maintenance and Preventive Services
Well child care through age 17
No Copay
Periodic health assessments for Members age 18 and
No Copay
older
Immunizations
Childhood immunizations required by law for
No Copay
Members through age 6
Immunizations for Members over age 6
No Copay
Bone mass measurement for osteoporosis
No Copay
Well-woman exam, once every twelve months,
No Copay
includes, but not limited to, exam for cervical cancer
(Pap smear)
Screening mammogram for female Members age 35
No Copay
and over, and for female Members with other risk
factors, once every twelve months
Outpatient facility or imaging centers
No Copay
Contraceptive Services and Supplies
Contraceptive education, counseling and certain
No Copay
female FDA approved contraceptive methods,
female sterilization procedures and devices
Breastfeeding Support, Counseling and Supplies
Electric breast pumps are limited to one per
No Copay
Calendar Year
Hearing Loss
Screening test from birth through 30 days
No Copay
Follow-up care from birth through 24 months
No Copay
Rectal screening for the detection of colorectal cancer
for Members age 45 and older:
Annual fecal occult blood test, once every twelve
No Copay
months
Flexible sigmoidoscopy with hemoccult of the
No Copay
stool, limited to 1 every 5 years
Colonoscopy, limited to 1 every 10 years
No Copay
Eye and ear screenings for Members through age 17,
$105 Copay for PCP or 50% Coinsurance after
once every twelve months
Deductible for Specialist
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
Eye and ear screening for Members age 18 and older,
$105 Copay for PCP or 50% Coinsurance after
once every two years
Deductible for Specialist
Note: Covered children to age 19 do have additional
benefits as described in PEDIATRIC VISION
CARE BENEFITS.
Early detection test for cardiovascular disease, limited
to 1 every 5 years
Computer tomography (CT) scanning - Hospital
50% Coinsurance after Deductible
Setting
Computer tomography (CT) scanning - Other
40% Coinsurance after Deductible
Facility Setting
Ultrasonography - Hospital Setting
50% Coinsurance after Deductible
Ultrasonography - Other Facility Setting
40% Coinsurance after Deductible
Early detection test for ovarian cancer (CA125 blood
$105 Copay for PCP or 50% Coinsurance after
test), once every twelve months
Deductible for Specialist
Any additional charges as described in Outpatient
Laboratory and X-Ray Services may also apply.
Exam for prostate cancer, once every twelve months
$105 Copay for PCP or 50% Coinsurance after
Deductible for Specialist
Any additional charges as described in Outpatient
Laboratory and X-Ray Services may also apply.
Dental Surgical Procedures
Dental Surgical Procedures (limited Covered
$850 Copay, plus 50% Coinsurance after Deductible
Services)
for Inpatient Hospital Services, or
Outpatient Surgery charges as described in
Outpatient Facility Services for Outpatient Surgery
Cosmetic, Reconstructive or Plastic Surgery
Cosmetic, Reconstructive or Plastic Surgery
$850 Copay, plus 50% Coinsurance after Deductible
(limited Covered Services)
for Inpatient Hospital Services, or
Outpatient Surgery charges as described in
Outpatient Facility Services for Outpatient Surgery
Allergy Care
Testing and Evaluation
50% Coinsurance after Deductible
Injections
Serum
Diabetes Care
Diabetes Self-Management Training, for each visit
$105 Copay for PCP or 50% Coinsurance after
Deductible for Specialist
Diabetes Equipment
50% Coinsurance after Deductible
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
Diabetes Supplies
50% Coinsurance after Deductible
Some Diabetes Supplies are only available utilizing
pharmacy benefits, through a Participating Pharmacy.
You must pay the applicable PHARMACY
BENEFITS amount shown in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS and any
applicable pricing differences
Prosthetic Appliances and Orthotic Devices
Prosthetic Appliances and Orthotic Devices
50% Coinsurance after Deductible
Cochlear Implants
50% Coinsurance after Deductible
Limit one (1) per impaired ear, with replacements as
Any Outpatient Surgery charges described in
Medically Necessary or audiologically necessary.
Outpatient Facility Services may also apply
Durable Medical Equipment
Durable Medical Equipment
50% Coinsurance after Deductible
Hearing Aids
Hearing Aids
50% Coinsurance after Deductible
Maximum benefit - one per ear, every 36 months
Speech and Hearing Services
Speech and Hearing Services
Benefits paid same as any other physical illness
Benefits for Autism Spectrum Disorder will not apply
towards and are not subject to any speech and hearing
services visit maximums.
Telehealth and Telemedicine Medical Services
Telehealth and Telemedicine Medical Services
Benefits paid the same as any other office visit
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
Pharmacy Benefits
Copayment
(Prescription or Refill)
Preferred Participating Pharmacy
Tier 1
$10 Copay
Retail Pharmacy
Tier 2
$20 Copay
Tier 3
30% Coinsurance after Deductible
Tier 4
35% Coinsurance after Deductible
Participating
Pharmacy
Tier 1
$20 Copay
Retail Pharmacy
Tier 2
$30 Copay
Tier 3
35% Coinsurance after Deductible
Tier 4
40% Coinsurance after Deductible
Mail-Order Program
Tier 1
$30 Copay
Tier 2
$60 Copay
Tier 3
30% Coinsurance after Deductible
Tier 4
35% Coinsurance after Deductible
Specialty Pharmacy Program
Tier 5
45% Coinsurance after Deductible
Coverage for Specialty Drugs are limited to
Tier 6
50% Coinsurance after Deductible
a 30-day supply. However, some Specialty
Drugs have FDA approved dosing
regimens exceeding the 30-day supply
limits and may be allowed greater than a 30
day-supply, if allowed by your plan
benefits. Cost share will be based on day
supply (1-30 day supply, 31-60 day supply,
61-90 day supply) dispensed.
Select Vaccinations obtained through the
No Copay
Pharmacy Vaccine Network
*The Copayment for insulin included in the Drug List will not exceed $25 per prescription for a 30-day supply,
regardless of the amount or type of insulin needed to fill the prescription.
Note: For Members with a chronic, complex, rare, or life-threatening medical condition, Covered Drugs that
will be administered by a Provider in a Physician's office may be obtained from a non-Participating Pharmacy
by the Provider, after the Provider has determined that disease progression, patient harm, or death is probable,
or where the Provider has concerns about patient adherence or timely delivery. These services are covered
under the medical benefit and the cost-sharing requirements will be the same as if they were obtained from a
Participating Pharmacy.
Certain Covered Drugs may be available at no cost through a Participating Pharmacy for the following
categories of medication: severe allergic reactions, hypoglycemia, opioid overdoses and nitrates. For further
information, call the number on the back of your identification card.
For additional information regarding the applicable Drug List, please call customer service or visit the website
atwww.bcbstx.com/member/prescription-drug-plan-information/drug-lists.
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
BlueCross BlueShield
BENEFIT HIGHLIGHTS
of Texas
The following refers to drugs as identified on the applicable Drug List.
Tier 1 - includes mostly Generic Drugs (Preferred) and may contain some Brand Name Drugs.
Tier
2 - includes mostly Generic Drugs (Non-Preferred) and may contain some Brand Name Drugs.
Tier 3 - includes mostly Brand Name Drugs (Preferred) and may contain some Generic Drugs.
Tier 4 - includes mostly Brand Name Drugs (Non-Preferred) and may contain some Generic Drugs.
Tier 5 - includes mostly Specialty Drugs (Preferred) and may contain some Generic Drugs.
Tier 6 - includes mostly Specialty Drugs (Non-Preferred) and may contain some Generic Drugs.
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation,
a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield Association
TX-I-EX-H-CC-SOC-BH-25
DEFINITIONS
Acquired Brain Injury means a neurological insult to the brain, which is not hereditary, congenital, or
degenerative. The injury to the brain has occurred after birth and results in a change in neuronal activity, which
results in an impairment of physical functioning, sensory processing, cognition, or psychosocial behavior.
Advanced Practice Nurse (APN) means a registered nurse approved by the Texas Board of Nursing to practice as
an advanced practice nurse based on completing an advanced educational program acceptable to the Board. The
term includes a nurse practitioner, nurse-midwife, nurse anesthetist, and a clinical nurse Specialist. An Advanced
Practice Nurse is prepared to practice in an expanded role to provide health care to individuals, families, and/or
groups in a variety of settings including but not limited to homes, Hospitals, institutions, offices, industry, schools,
community agencies, public and private clinics, and private practice. An Advanced Practice Nurse acts
independently and/or in collaboration with other Health Care Professionals in the delivery of health care services.
Allowable Amount means the maximum amount determined by HMO to be eligible for consideration of payment
for a particular service, supply or procedure rendered by a Participating Provider. The Allowable Amount is based
on the provisions of the Participating Provider contract and the payment methodology in effect on the date of
service, whether diagnostic related grouping (DRG), capitation, relative value, fee schedule, per diem or other.
Approved Clinical Trial means a phase I, phase II, phase III, or phase IV clinical trial that is conducted in relation
to the prevention, detection, or treatment of cancer or other Life-Threatening Disease or Condition. The trial must
be:
A. conducted under an Investigational new drug application reviewed by the United States Food and Drug
Administration;
B. exempt from obtaining an Investigational new drug application; or
C. approved or funded by:
1. the National Institutes of Health, the Centers for Disease Control and Prevention, the Agency for
Healthcare Research and Quality, the Centers for Medicare and Medicaid Services, or a cooperative
group or center of any of the foregoing entities;
2. a cooperative group or center of the United States Department of Defense or the United States
Department of Veterans Affairs;
3. a qualified nongovernmental research entity identified in the guidelines issued by the National
Institutes of Health for center support groups; or
4. the United States Departments of Veterans Affairs, Defense, or Energy if the study or investigation
has been reviewed and approved through a system of peer review determined by the United States
Secretary of Health and Human Services to:
a) be comparable to the system of peer review of studies and investigations used by the National
Institutes of Health; and
b) provide unbiased scientific review by individuals who have no interest in the outcome of the
review.
D. conducted and approved by an institutional review board of an institution in this state that has an agreement
with the Office for Human Research Protections of the United States Department of Health and Human
Services.
Autism Spectrum Disorder means a Neurobiological Disorder that includes autism, Asperger's syndrome, or
pervasive developmental disorder-not otherwise specified. "Neurobiological Disorder" means an illness of the
nervous system caused by genetic, metabolic, or other biological factors.
Biomarker means a characteristic that is objectively measured and evaluated as an indicator of normal biological
processes, pathogenic processes, or pharmacologic responses to the specific therapeutic intervention. Includes gene
mutations and protein expression.
TX-I-EX-H-CC-EOC-25
1
DEFINITIONS
Biomarker Testing means the analysis of a patient's tissue, blood, or other biospecimen for the presence of a
biomarker. The term includes single-analyte tests, multiplex panel tests and whole genome sequencing.
Calendar Year means the period beginning January 1 of any year and ending December 31 of the same year.
Chemical Dependency means the abuse of or psychological or physical dependence on or addiction to alcohol or
a Controlled Substance.
Chemical Dependency Treatment Center means a facility that provides a program for the treatment of Chemical
Dependency pursuant to a written treatment plan approved by HMO or its designated behavioral health
administrator. The facility must be:
affiliated with a Hospital under a contractual agreement with an established system for patient Referral;
accredited as such a facility by the Joint Commission on Accreditation of Healthcare Organizations;
licensed, certified or approved as a Chemical Dependency treatment program or center by an agency of the
state of Texas having legal authority to SO license, certify or approve; or
if outside Texas, licensed, certified or approved as a Chemical Dependency treatment program or center by
the appropriate agency of the state in which it is located having the legal authority to SO license, certify or
approve.
Clinical Ecology means the inpatient or outpatient diagnosis or treatment of allergic symptoms by:
cytotoxicity testing (testing the result of food or inhalant by whether or not it reduces or kills white blood
cells);
urine auto injection (injecting one's own urine into the tissue of the body);
skin irritation by Rinkel method;
subcutaneous provocative and neutralization testing (injecting the patient with allergen); or
sublingual provocative testing (droplets of allergenic extracts are placed in mouth).
Coinsurance means the percentage of the Allowable Amount required to be paid by You or on Your behalf at the
time of service to a Participating Provider in connection with Covered Services provided as described in COVERED
SERVICES AND BENEFITS.
Complications of Pregnancy means conditions, requiring Hospital confinement (when the pregnancy is not
terminated), whose diagnoses are distinct from pregnancy but are adversely affected by pregnancy or are caused by
pregnancy, such as acute nephritis, nephrosis, cardiac decompensation, missed abortion, and similar medical and
surgical conditions of comparable severity, but shall not include false labor, occasional spotting, Physician
prescribed rest during the period of pregnancy, morning sickness, hyperemesis gravidarum, pre-eclampsia, and
similar conditions associated with the management of a difficult pregnancy not constituting a nosologically distinct
complication of pregnancy; and non-elective cesarean section, termination of ectopic pregnancy, and spontaneous
termination of pregnancy, occurring during a period of gestation in which a viable birth is not possible.
Contract Month means the period of each succeeding month beginning on the Evidence of Coverage effective
date.
Controlled Substance means an abusable volatile chemical as defined in the Texas Health and Safety Code, or a
substance designated as a Controlled Substance in the Texas Health and Safety Code.
Copayment or Copay means the dollar amount required to be paid by You or on Your behalf at the time of service
to a Participating Provider in connection with Covered Services provided as described in COVERED SERVICES AND
BENEFITS.
Cosmetic, Reconstructive or Plastic Surgery means surgery that can be expected or is intended to improve Your
physical appearance, is performed for psychological purposes, or restores form but does not correct or materially
restore a bodily function.
Covered Services means those Medically Necessary health services specified and described in COVERED
SERVICES AND BENEFITS.
TX-I-EX-H-CC-EOC-25
2
DEFINITIONS
Crisis Stabilization Unit means a twenty-four (24) hour residential program that is usually short-term in nature
and provides intensive supervision and highly structured activities to Members who show signs of an acute
demonstrable psychiatric crisis of moderate to severe proportions.
Custodial Care means any service primarily for personal comfort or convenience that provides general
maintenance, preventive, and/or protective care without any clinical likelihood of improvement of Your condition.
Custodial Care Services also means those services which do not require the technical skills, professional training
and clinical assessment ability of medical and/or nursing personnel in order to be safely and effectively performed.
These services can be safely provided by trained or capable non-professional personnel, are to assist with routine
medical needs (e.g. simple care and dressings, administration of routine medications, etc.) and are to assist with
activities of daily living (e.g. bathing, eating, dressing, etc.).
Deductible means the dollar amount required to be paid by You or on Your behalf to a Participating Provider before
benefits are available in connection with Covered Services provided as described in COVERED SERVICES AND
BENEFITS and PHARMACY BENEFITS.
Dependent(s) means the Subscriber's spouse or child who has been determined eligible to enroll through the
Exchange in a Qualified Health Plan (QHP).
Dietary and Nutritional Services means Your education, counseling, or training (including printed material)
regarding diet, regulation or management of diet, or the assessment or management of nutrition.
Domestic Partner means a person with whom You have entered into a domestic partnership and who has been
determined eligible for coverage by the Exchange.
Durable Medical Equipment (DME) means equipment that can withstand repeated use, is primarily and usually
used to serve a medical purpose, is generally not useful to a person in absence of illness or injury, and is appropriate
for use in the home.
Effective Date of Coverage means the commencement date of coverage under this Evidence of Coverage as shown
on the records of HMO.
Emergency Care means health care services provided in a Hospital emergency facility, freestanding emergency
medical care facility, or comparable facility to evaluate and stabilize medical conditions of a recent onset and
severity, including but not limited to severe pain, that would lead a prudent layperson, possessing an average
knowledge of medicine and health, to believe that his condition, sickness, or injury is of such a nature that failure
to get immediate medical care could result in:
placing the patient's health in serious jeopardy;
serious impairment to bodily functions;
serious dysfunction of any bodily organ or part;
serious disfigurement; or
in the case of a pregnant woman, serious jeopardy to the health of the fetus.
Environmental Sensitivity means the inpatient or outpatient treatment of allergic symptoms by controlling
environment, sanitizing the surroundings (removal of toxic materials), or use of special nonorganic, nonrepetitive
diet techniques.
Exchange (also known as health insurance marketplace) means a governmental agency or non-profit entity that
meets the applicable Exchange standards, and other related standards established under applicable law, and makes
Qualified Health Plans (QHPs) available to Qualified Individuals and qualified employers (as these terms are
defined by applicable law). Unless otherwise identified, the term Exchange refers to the State Exchanges, regional
Exchanges, subsidiary Exchanges, a Federally-facilitated Exchange or other Exchange on which Blue Cross and
Blue Shield of Texas offers this QHP.
Experimental/Investigational means the use of any treatment, procedure, facility, equipment, drug, device or
supply not accepted as Standard Medical Treatment of the condition being treated or any of such items requiring
federal or other governmental agency Approval not granted at the time services were provided. "Approval" by a
federal agency means that the treatment, procedure, facility, equipment, drug, device or supply has been approved
TX-I-EX-H-CC-EOC-25
3
DEFINITIONS
for the condition being treated and, in the case of a drug, in the dosage used on the patient. Approval by a federal
agency will be taken into consideration by HMO in assessing Experimental/Investigational status but will not be
determinative. Medical treatment includes medical, surgical or dental treatment. "Standard Medical Treatment"
means the services or supplies that are in general use in the medical community in the United States, and:
have been demonstrated in peer-reviewed literature to have scientifically established medical value for curing
or alleviating the condition being treated;
are appropriate for the Hospital or Participating Provider; and
the Health Care Professional has had the appropriate training and experience to provide the treatment or
procedure.
HMO shall determine whether any treatment, procedure, facility, equipment, drug, device, or supply is
Experimental/Investigational, and will consider factors such as the guidelines and practices of Medicare, Medicaid,
or other government-financed programs and approval by a federal agency in making its determination.
Although a Health Care Professional may have prescribed treatment, and the services or supplies may have been
provided as the treatment of last resort, such services or supplies still may be considered to be
Experimental/Investigational within this definition. Treatment provided as part of a clinical trial or a research study
is Experimental/Investigational.
Fertility Preservation Services means the collection and preservation of sperm, unfertilized oocytes, and ovarian
tissue; and does not include the storage of such unfertilized genetic materials.
Habilitation Services means health care services that help a person keep, learn, or improve skills and functioning
for daily living. Examples include therapy for a child who is not walking or talking at the expected age. These
services may include physical and occupational therapy, speech-language pathology and other services for people
with disabilities in a variety of inpatient and/or outpatient settings.
Health Benefit Plan means a group, blanket, or franchise insurance policy, a certificate issued under a group policy,
a group Hospital service contract, or a group subscriber contract or evidence of coverage issued by a health
maintenance organization that provides benefits for health care services.
Health Care Professional(s) means Physicians, nurses, audiologists, Physician Assistants, Advanced Practice
Nurses, nurse first assistants, acupuncturists, clinical psychologists, pharmacists, occupational therapists, physical
therapists, speech and language pathologists, surgical assistants and other professionals engaged in the delivery of
health services who are licensed, practice under an institutional license, or certified, or practice under authority of
a Physician or legally constituted professional association, or other authority consistent with state law.
HMO (Health Maintenance Organization) means Blue Cross and Blue Shield of Texas, a Division of Health Care
Service Corporation, a Mutual Legal Reserve Company, an Independent Licensee of the Blue Cross and Blue Shield
Association.
Hospice means an organization, licensed by appropriate regulatory authority or certified by Medicare as a supplier
of Hospice care, which has entered into an agreement with HMO to render Hospice care to Members.
Hospital means an acute care institution which:
is duly licensed by the state in which it is located and must be accredited by the Joint Commission on
Accreditation of Healthcare Organizations or certified under Medicare;
is primarily engaged in providing, on an inpatient basis, medical care and treatment of sick and injured
persons through medical, diagnostic, and major surgical facilities;
provides all services on its premises under the supervision of a staff of Physicians;
provides twenty-four (24) hour a day nursing and Physician service; and
has in effect a Hospital utilization review plan.
Hospital Services (except as expressly limited or excluded in this Evidence of Coverage) means those Medically
Necessary Covered Services that are generally and customarily provided by acute general Hospitals; and prescribed,
directed or authorized by the PCP.
TX-I-EX-H-CC-EOC-25
4
DEFINITIONS
In Home Health Assessment means a Covered Service, which may include, but is not limited to, health history
and blood pressure and blood sugar level screening. The assessment is designed to provide You with information
regarding Your health that can be discussed with Your health care Provider, and is not a substitute for diagnosis,
management and treatment by Your health care Provider.
Infertility means the condition of a presumably healthy Member who is unable to conceive or produce conception
after a period of one year of frequent, unprotected heterosexual sexual intercourse. This does not include conditions
for male Members when the cause is a vasectomy or orchiectomy or for female Members when the cause is a tubal
ligation or hysterectomy.
Infusion Suite means a place of treatment that is an alternative to Hospital and clinic-based infusion settings where
specialty medications can be infused.
Infusion Therapy involves the administration of medication through a needle or catheter. It is prescribed when a
patient's condition is SO severe that it cannot be treated effectively by oral medications. Typically, "infusion therapy"
means that a drug is administered intravenously, but the term also may refer to situations where drugs are provided
through other non-oral routes, such as intramuscular injections and epidural routes (into the membranes surrounding
the spinal cord). Infusion therapy in most cases requires Health Care Professional services for the safe and effective
administration of the medication.
Life-Threatening Disease or Condition means, for the purposes of a clinical trial, any disease or condition from
which the likelihood of death is probable unless the course of the disease or condition is interrupted.
Marriage and Family Therapy means the provision of professional therapy services to individuals, families, or
married couples, singly or in groups, and involves the professional application of family systems theories and
techniques in the delivery of therapy services to those persons. The term includes the evaluation and remediation
of cognitive, affective, behavioral, or relational dysfunction within the context of marriage or family systems.
Medical Director means a Physician of HMO, or his designee, who is responsible for monitoring the provision of
Covered Services to Members.
Medical Social Services means those social services relating to the treatment of a Member's medical condition.
Such services include, but are not limited to assessment of the:
social and emotional factors related to Member's illness, need for care, response to treatment and adjustment
to care; and
relationship of Member's medical and nursing requirements to the home situation, financial resources, and
available community resources.
Medically Necessary means services or supplies (except as limited or excluded herein) that are:
essential to, consistent with, and provided for the diagnosis or the direct care and treatment of the condition,
sickness, disease, injury, or bodily malfunction;
provided in accordance with and consistent with generally accepted standards of medical practice in the
United States;
not primarily for Your convenience, or the convenience of Your Participating Provider; and
the most economical supplies or levels of service appropriate for Your safe and effective treatment.
if more than one health intervention meets the requirements listed above, Medically Necessary means "the
most cost effective in terms of type of intervention or setting, frequency, extent, or duration, which is safe
and effective for the patient's illness, injury, or disease, and supports improved health".
When applied to hospitalization, this further means that You require acute care as an inpatient due to the nature of
the services rendered or Your condition, and You cannot receive safe or adequate care as an outpatient. In
determining whether a service is Medically Necessary, HMO may consider the views of the state and national
medical communities and the guidelines and practices of Medicare, Medicaid, or other government-financed
programs and peer reviewed literature. Although a Participating Provider may have prescribed treatment, such
treatment may not be Medically Necessary within this definition. This definition applies only to the HMO's
determination of whether health care services are Covered Services under this Evidence of Coverage.
TX-I-EX-H-CC-EOC-25
5
DEFINITIONS
HMO does not determine Your course of treatment or whether You receive particular health care services. The
decision regarding the course of treatment and receipt of particular health care service is entirely between You and
Your Participating Provider. HMO's determination of Medically Necessary care is limited to merely whether a
proposed admission, continued hospitalization, outpatient service or other health care service is Medically
Necessary under this Evidence of Coverage.
Medicare means Title XVIII of the Social Security Act and all amendments thereto.
Member means a Subscriber or Dependent(s) covered under this HMO Evidence of Coverage. This Evidence of
Coverage may refer to a Member as You or Your.
Mental Health Care means any one or more of the following:
1. The diagnosis or treatment of a mental disease, disorder, or condition listed in the Diagnostic and Statistical
Manual of Mental Disorders of the American Psychiatric Association, as revised, or any other diagnostic
coding system as used by HMO or its designated behavioral health administrator, whether or not the cause
of the disease, disorder, or condition is physical, chemical, or mental in nature or origin;
2. The diagnosis or treatment of any symptom, condition, disease, or disorder by a Participating Provider
when the Covered Service is:
individual, group, family, or conjoint psychotherapy;
counseling;
psychoanalysis;
psychological testing and assessment;
the administration or monitoring of psychotropic drugs; or
Hospital visits (if applicable) or consultations in a facility listed in item 5, below;
3. Electroconvulsive treatment;
4.
Psychotropic drugs;
5. Any of the services listed in items 1-4, above, performed in or by a Hospital (if applicable), or other licensed
facility or unit providing such care.
Mental Health Treatment Facility means a facility that:
meets licensing standards;
mainly provides a program for diagnosis, evaluation and treatment of acute mental or nervous disorders;
prepares and maintains a written plan of treatment for each patient based on medical, psychological and
social needs;
provides all normal infirmary level medical services or arranges with a Hospital for any other medical
services that may be required;
is under the supervision of a psychiatrist; and
provides skilled nursing care by licensed nurses who are directed by a registered nurse.
Minimum Essential Coverage means health insurance coverage that is recognized as coverage that meets
substantially all requirements under federal law pertaining to adequate individual, group or government health
insurance coverage. For additional information on whether particular coverage is recognized as "Minimum
Essential Coverage", please call the customer service telephone number shown on the back of Your identification
card or visit www.cms.gov.
Obstetrician/Gynecologist means a Participating Physician contracted by HMO as an Obstetrician and/or
Gynecologist who may be selected by a female to provide:
well-woman exams;
obstetrical care;
care for all active gynecological conditions; and
TX-I-EX-H-CC-EOC-25
6
DEFINITIONS
diagnosis, treatment, and Referral for any disease or condition within the scope of the professional practice
of the Obstetrician/Gynecologist.
Open Enrollment Period means the period each year during which a Qualified Individual may enroll or change
coverage in a Qualified Health Plan (QHP) through the Exchange.
Out-of-Area means not within the Service Area.
Participating means a Provider that has entered into a contractual agreement with HMO for the provision of
Covered Services to Members.
Physician means a Doctor of Medicine (M.D.) or Doctor of Osteopathy (D.O.) who is properly licensed or certified
to provide medical care (within the scope of his license) under the laws of the state where the individual practices.
Physician Assistant (PA) means a Physician assistant licensed under Texas Occupations Code Chapter 204.
Post-Delivery Care means postpartum health care services provided in accordance with accepted maternal and
neonatal physical assessments, including parent education, assistance and training in breast and bottle feeding, and
the performance of necessary and appropriate clinical tests.
Post-Service Medical Necessity Review means a review, sometimes referred to as a retrospective medical
necessity review, is the process of determining coverage after treatment has already occurred and is based on
medical necessity guidelines.
Premium means the amount You are required to pay to HMO to continue coverage.
Premium Tax Credit means a refundable premium tax credit an eligible individual may receive for taxable years
ending after December 31, 2013, to the extent provided under applicable law, where the credit is meant to offset all
or a portion of the Premium paid by the individual for coverage obtained through an Exchange during the preceding
Calendar Year.
Primary Care Physician/Practitioner or PCP means the Participating Physician, Physician Assistant or Advanced
Practice Nurse who is primarily responsible for providing, arranging and coordinating all aspects of Your health
care. You and Your Dependents must each select a PCP from those listed by HMO to provide primary care services.
You may choose a PCP who is a family practitioner, internist, pediatrician and/or Obstetrician/Gynecologist. The
PA or APN must work under the supervision of a Participating family practitioner, internist, pediatrician and/or
Obstetrician/Gynecologist in the same HMO network.
Prior Authorization means a determination by HMO that health care services proposed to be provided to a patient
are Medically Necessary and appropriate. Prior Authorization processes will be conducted in accordance with Texas
Insurance Code, chapter 843, or in accordance with the laws in the state of Texas.
Professional Services means those Medically Necessary Covered Services rendered by Physicians and other Health
Care Professionals in accordance with this Evidence of Coverage. All services must be performed, prescribed,
directed, or authorized in advance by the PCP.
Prosthetic Appliances means artificial devices including limbs or eyes, braces or similar prosthetic or orthopedic
devices, which replace all or part of an absent body organ (including contiguous tissue) or replace all or part of the
function of a permanently inoperative or malfunctioning body organ (dental appliances and the replacement of
cataract lenses are not considered Prosthetic Appliances).
Provider means any duly licensed institution, Physician, Health Care Professional or other entity which is licensed
to provide health care services.
Psychiatric Day Treatment Facility means an institution that is appropriately licensed and is accredited by the
Joint Commission on Accreditation of Healthcare Organizations as a Psychiatric Day Treatment Facility for the
provision of Serious Mental Illness services to Members for periods of time not to exceed eight hours in any 24-
hour period. Any treatment in such facility must be certified in writing by the attending Physician to be in lieu of
hospitalization.
TX-I-EX-H-CC-EOC-25
7
DEFINITIONS
Qualified Health Plan (QHP) means a health care benefit program that has in effect a certification that it meets
the applicable government standards, issued or recognized by each Exchange through which such program is
offered.
Qualified Health Plan Issuer or QHP Issuer means a health plan issuer that offers a QHP in accordance with a
certification from an Exchange.
Qualified Individual(s) means, an individual who has been determined eligible to enroll through the Exchange in
a Qualified Health Plan (QHP).
Recommended Clinical Review means an optional voluntary review of a Provider's recommended medical
procedure, treatment or test, that does not require Prior Authorization, to make sure it meets approved Blue Cross
and Blue Shield medical policy guidelines and medical necessity requirements.
Reconstructive Surgery for Craniofacial Abnormalities means surgery to improve the function of, or to attempt
to create a normal appearance of, an abnormal structure caused by congenital defects, developmental deformities,
trauma, tumors, infections, or disease.
Referral means specific directions or instructions from Your PCP, in conformance with HMO's policies and
procedures that direct You to a Participating Provider for Covered Services.
Rehabilitation Services means health care services, including devices, provided to help a person regain,
maintain, or prevent deterioration of a skill or function that has been acquired but then lost or impaired due to
illness, injury, or disabling condition.
Research Institution means an institution or Provider (person or entity) conducting a phase I, phase II, phase III,
or phase IV clinical trial.
Residential Treatment Center means a facility setting (including a Residential Treatment Center for Children and
Adolescents) offering a defined course of therapeutic intervention and special programming in a controlled
environment which also offers a degree of security, supervision, structure and is licensed by the appropriate state
and local authority to provide such service. It does not include half-way houses, wilderness programs, supervised
living, group homes, boarding houses or other facilities that provide primarily a supportive environment and address
long-term social needs, even if counseling is provided in such facilities. Patients are medically monitored with 24-
hour medical availability and 24-hour onsite nursing service for Mental Health Care and/or treatment of Chemical
Dependency. HMO requires that any Mental Health Treatment Facility, Residential Treatment Center and/or
Chemical Dependency Treatment Center must be licensed in the state where it is located, or accredited by a national
organization that is recognized by HMO as set forth in its current credentialing policy, and otherwise meets all other
credentialing requirements set forth in such policy.
Residential Treatment Center for Children and Adolescents means a childcare institution that provides
residential care and treatment for emotionally disturbed children and adolescents and that is accredited as a
Residential Treatment Center by the Council on Accreditation, the Joint Commission on Accreditation of Healthcare
Organizations or the American Association of Psychiatric Services for Children.
Retail Health Clinic means a Participating Provider that has entered into a contractual agreement with HMO to
provide treatment of uncomplicated minor illnesses. Retail Health Clinics are typically located in retail stores and
are typically staffed by Advanced Practice Nurses or Physician Assistants.
Routine Patient Care Costs means the costs of any Medically Necessary health care service for which benefits are
provided under the Health Benefit Plan, without regard to whether the Member is participating in a clinical trial.
Routine Patient Care Costs do not include:
the cost of an Investigational new drug or device that is not approved for any indication by the United States
Food and Drug Administration, including a drug or device that is the subject of the clinical trial;
the cost of a service that is not a health care service, regardless of whether the service is required in
connection with participation in a clinical trial;
the cost of a service that is clearly inconsistent with widely accepted and established standards of care for a
particular diagnosis;
TX-I-EX-H-CC-EOC-25
8
DEFINITIONS
a cost associated with managing a clinical trial; or
the cost of a health care service that is specifically excluded from coverage under the HMO.
Select Primary Care Physician means a Primary Care Physician in certain areas as reflected in the Service Area
Map. These Select PCP's will be identified in the HMO Provider directory. Choosing a Select Primary Care
Physician may result in a lower Copayment for PCP office visits as indicated in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS.
Serious Mental Illness means the following psychiatric illnesses as defined by the American Psychiatric
Association in the Diagnostic and Statistical Manual (DSM):
schizophrenia;
paranoid and other psychotic disorders;
bipolar disorders (hypomanic, manic, depressive and mixed);
major depressive disorders (single episode or recurrent);
schizo-affective disorders (bipolar or depressive);
obsessive-compulsive disorders; and
depression in childhood or adolescence.
Service Area means the geographical area served by HMO and approved by state regulatory authorities. The
applicable Service Area includes the area shown and described in SERVICE AREA.
Skilled Nursing Facility means an institution or distinct part of an institution that is licensed or approved under
state or local law, and primarily provides skilled nursing care and related services as a Skilled Nursing Facility,
extended care facility or nursing care facility approved by the Joint Commission on Accreditation of Health Care
Organizations, the Bureau of Hospitals of the American Osteopathic Association or as otherwise determined by
HMO to meet the reasonable standards applied by either of those authorities.
Specialist means a duly licensed Physician, other than a PCP.
Subscriber means a person who meets all applicable eligibility and enrollment requirements of this Evidence of
Coverage, and whose enrollment application and Premium payment have been received by HMO.
Teledentistry Dental Services means a health care service delivered by a Dentist or a health professional acting
under the delegation and supervision of a Dentist, acting within the scope of the Dentist's or health professional's
license or certification to a patient at a different physical location than the Dentist or health professional using
telecommunications or information technology.
Telehealth Services means a health service, other than a Telemedicine Medical Service or a Teledentistry Dental
Service, delivered by a health professional licensed, certified, or otherwise entitled to practice in Texas and acting
within the scope of the health professional's license, certification, or entitlement to a patient at a different physical
location than the health professional using telecommunications or information technology.
Telemedicine Medical Services means a health care service delivered by a Physician licensed in Texas, or a health
professional acting under the delegation and supervision of a Physician licensed in Texas, and acting within the
scope of the Physician's or health professional's license to a patient at a different physical location than the
Physician or health professional using telecommunications or information technology.
Tobacco User means a person who is permitted under state and federal law to legally use tobacco, with tobacco use
(other than religious or ceremonial use of tobacco), occurring on average four or more times per week that last
occurred within the past six months (or such other meaning required or permitted by applicable law). Tobacco
includes, but is not limited to, cigarettes, cigars, pipe tobacco, smokeless tobacco, snuff, etc. For additional
TX-I-EX-H-CC-EOC-25
9
DEFINITIONS
information, please call customer service at the toll-free number on the back of Your identification card or visit the
website at www.bcbstx.com.
Urgent Care means medical or health care services provided in a situation other than an emergency that are
typically provided in a setting such as an Urgent Care Provider's office or Participating Urgent Care facility, as a
result of an acute injury or illness that is severe or painful enough to lead a prudent layperson, possessing an average
knowledge of medicine and health, to believe that the person's condition, illness, or injury is of such a nature that
failure to obtain treatment within a reasonable period of time would result in serious deterioration of the condition
of the person's health.
Urgent Care Provider means a Participating Provider that has entered into a contractual agreement with HMO for
the provision of Covered Services for Urgent Care to Members.
Virtual Network Provider means a licensed Participating Provider that has entered into a contractual agreement
with HMO to provide diagnosis and treatment of injuries and illnesses through either (i) interactive audio
communication (via telephone or other similar technology), or (ii) interactive audio/video examination and
communication (via online portal, mobile application or similar technology).
Virtual Visits means services provided for the treatment of non-emergency medical and behavioral health
conditions as described in COVERED SERVICES AND BENEFITS.
You and Your means any Member, including Subscriber and Dependents.
TX-I-EX-H-CC-EOC-25
10
WHO GETS BENEFITS
Eligibility
No eligibility rules or variations in Premium will be imposed based on Your health status, medical condition,
claims experience, receipt of care, medical history, genetic information, evidence of insurability, disability, or
other health status related factor. Coverage under this Evidence of Coverage is provided regardless of Your race,
color, national origin, disability, age, sex, gender identity, sexual orientation, political affiliation or expression.
Coverage under this Evidence of Coverage does not require documentation certifying COVID-19 vaccination or
require documentation of post-transmission recovery as a condition for obtaining coverage or receiving benefits
under this Evidence of Coverage. Variations in the administration, processes or benefits of this Evidence of
Coverage are based on clinically indicated, reasonable medical management practices, or are part of permitted
wellness incentive; disincentives and/or other programs do not constitute discrimination.
Eligibility for this coverage will be determined by the Exchange in accordance with applicable law. For questions
regarding eligibility, refer to healthcare.gov.
Subscriber Eligibility. To be eligible to enroll as a Subscriber, a person must:
1. reside, live or work in the Service Area; and
2. have been determined eligible to enroll through the Exchange.
Dependent Eligibility. To be eligible to enroll as a Dependent, a person must meet all eligibility requirements as
determined by the Exchange and:
1. reside in the Service Area or permanently reside with a Subscriber who works in the Service Area, except
as provided in item 5, below; and
2. be Subscriber's spouse or Domestic Partner. Subscriber may be required to submit a certified copy of a
marriage license or declaration of informal marriage with Dependent's enrollment application before
coverage will be extended; or
3. be a Dependent child, which hereafter means a natural child, eligible foster child, a stepchild, an adopted
child (including a child for whom the Subscriber or Subscriber's spouse is a party in a suit in which the
adoption of the child is sought) or a Dependent child of a Domestic Partner under twenty-six (26) years of
age, regardless of presence or absence of a child's financial dependency, residency, student status,
employment status, marital status, enrolled in or eligibility for other coverage or any combination of those
factors. To be eligible for coverage, a child of a Subscriber's child must also be dependent upon Subscriber
for federal income tax purposes at the time application for coverage is made.
In addition, a Dependent shall include a child for whom Subscriber or Subscriber's spouse is a court-
appointed legal guardian, provided proof of such guardianship is submitted with the prospective
Dependent's enrollment application; or
4. be a child of any age, as defined in item 3 above, who is and continues to be incapable of sustaining
employment by reason of mental retardation or physical handicap and is chiefly dependent upon Subscriber
for economic support and maintenance. Subscriber must provide HMO with a Dependent Child's Statement
of Disability form, including a medical certification of disability, and subsequently as may be required by
HMO, but not more often than once per year. HMO's determination of eligibility shall be conclusive; or
5. have a court order for coverage to be provided for a spouse or minor child under Subscriber's Health Benefit
Plan and application shall be made within sixty (60) days after issuance of the court order.
Coverage of Subscriber shall be a condition precedent to coverage of eligible Dependents, and no Dependent shall
be covered hereunder prior to Subscriber's Effective Date of Coverage.
Loss of Eligibility. You must notify HMO and the Exchange of any changes that will affect Your eligibility, or that
of Your Dependents, for services or benefits under this Evidence of Coverage within sixty (60) days of the change.
TX-I-EX-H-CC-EOC-25
11
WHO GETS BENEFITS
Enrollment
Annual Open Enrollment Periods/Effective Date of Coverage. Annual Open Enrollment Periods have been
designated during which You may apply for or change coverage for Yourself and/or Your eligible Dependents.
When You enroll during the annual Open Enrollment Period Your and/or Your eligible Dependents' effective date
will be the following January 1, unless otherwise designated by the Exchange and HMO, as appropriate.
Coverage under this Evidence of Coverage is contingent upon timely receipt by HMO of necessary information and
initial Premium.
This section Annual Open Enrollment Periods/Effective Date of Coverage is subject to change by the Exchange,
HMO and/or applicable law, as appropriate.
Newborn Children Coverage. Coverage will be automatic for Subscriber or Subscriber's spouse's newborn child
for the first thirty-one (31) days following the date of birth. Coverage will continue beyond the thirty-one (31)
days only if the child is an eligible Dependent and You verbally notify HMO or submit an enrollment application
within thirty-one (31) days and make or agree to make any additional Premium payments in accordance with this
Evidence of Coverage. ]NOTE: Application must be made to the Exchange within 30 days and You make or agree
to make any additional Premium payments in accordance with this Evidence of Coverage. The Effective Date of
Coverage for newborn children shall be the newborn's date of birth.
Late Enrollees
Special Enrollment Periods/Effective Dates of Coverage
Special enrollment periods have been designated during which You may apply for or change coverage in a QHP
through the Exchange for Yourself and/or Your eligible Dependents. You must apply for or request a change in
coverage within 60 days from the date of a special enrollment event in order to qualify for the changes described in
this SPECIAL ENROLLMENT PERIODS/EFFECTIVE DATES OF COVERAGE section.
Except as otherwise provided by HMO, if Your application is received on or before the day of the qualifying event,
the effective date is the first day of the month following the qualifying life event. Unless otherwise designated by
HMO, if the application is received after the qualifying event, the effective date is the first of the month following
the date of receipt of the application.
Special Enrollment Events:
You may reference an up to date listing of on-Exchange special enrollment qualifying life events via
www.healthcare.gov/coverage-outside-open-enrollment/special-enrollment-period/
Coverage resulting from any of the special enrollment events outlined above is contingent upon timely
completion of the application and remittance of the appropriate Premiums in accordance with the
guidelines as established by the Exchange and HMO, as appropriate.
Removing a Dependent From Coverage
To remove a Dependent from coverage, the Subscriber must submit a request to HMO and the Exchange, as
appropriate. You may re-enroll these terminated individuals under the Evidence of Coverage only during the Open
Enrollment Period or special enrollment period. If an individual is being removed from coverage because of losing
his/her eligibility under the Evidence of Coverage, the individual is eligible to enroll under the Evidence of
Coverage only during the Open Enrollment Period or special enrollment period, as applicable, by submitting
application(s) to the Exchange and HMO, as applicable.
TX-I-EX-H-CC-EOC-25
12
WHO GETS BENEFITS
Child-Only Coverage
Eligible children that have not attained age 21 may enroll as the Subscriber under this Evidence of Coverage
(health care plan). In such event, this Evidence of Coverage is considered child-only coverage and the following
restrictions apply:
The parent or legal guardian is not covered and is not eligible for benefits under this health care plan.
If a child is under the age of 18, his/her parent, legal guardian, or other responsible party must submit the
application for child-only insurance form, along with any exhibits, appendices, addenda and/or other
required information to HMO and the Exchange, as appropriate. For any child under 18 covered under this
Evidence of Coverage, any obligations set forth in this Evidence of Coverage, any exhibits, appendices,
addenda and/or other required information will be the obligations of the parent, legal guardian, or other
responsible party applying for coverage on the child's behalf. Application for a child-only coverage will not
be accepted for an adult child that has attained age 21 as of the beginning of the plan year. Adult children
(at least 18 years of age but no older than 20 years of age) who are applying for coverage as a Subscriber
under this Evidence of Coverage must sign or authorize the application(s).
TX-I-EX-H-CC-EOC-25
13
HOW THE PLAN WORKS
Provider Information
You are entitled to medical care and services from Participating Providers including Medically Necessary medical,
surgical, diagnostic, therapeutic and preventive services that are generally and customarily provided in the Service
Area. Some services may not be covered. To be covered, a service that is Medically Necessary must also be
described in COVERED SERVICES AND BENEFITS. Even though a Physician or other Health Care Professional has
performed, prescribed or recommended a service does not mean it is Medically Necessary or that it is covered
under COVERED SERVICES AND BENEFITS.
Only services that are performed, prescribed, directed or authorized in advance by the PCP or HMO are covered
benefits under this Evidence of Coverage except Emergency Care, Participating Urgent Care, Virtual Visits or
Retail Health Clinic visits.
HMO and Participating Providers do not have any financial responsibility for any services You seek or receive
from a non-Participating Provider or facility, except as set forth below, unless both Your PCP and HMO have
made prior Referral authorization arrangements.
Utilization Management
Utilization Management may be referred to as medical necessity reviews, utilization review (UR), or medical
management reviews. A medical necessity review for a procedure/service, inpatient admission, and length of stay
is based on HMO Medical Policy and/or level of care review criteria. Medical necessity reviews may occur prior
to services rendered, during the course of care, or after care has been completed for a Post-Service Medical
Necessity Review. Some services may require a Prior Authorization before the start of services, while other services
will be subject to a concurrent or Post-Service Medical Necessity Review. If requested, services normally subject
to a Post-Service Medical Necessity Review may be reviewed for medical necessity prior to the service through a
Recommended Clinical Review as defined below.
Refer to the definition of Medically Necessary under the DEFINITIONS section of this Certificate for additional
information regarding any limitations and/or special conditions pertaining to Your benefits.
Prior Authorization
Prior Authorization establishes in advance the medical necessity or Experimental/Investigational nature of certain
care and services covered under this Plan. It ensures that the care and services described below for which You have
obtained Prior Authorization will not be denied on the basis of medical necessity or Experimental/Investigational.
Some Covered Services may also require Prior Authorization which requires the Provider to get approval from
HMO before You are admitted to the Hospital or for certain types of Covered Services. Prior Authorization
processes will be conducted in accordance with Texas Insurance Code, chapter 843 or in accordance with the laws
in the state of Texas. Renewal of an existing Prior Authorization issued by HMO can be requested by a Physician
or Health Care Provider up to 60 days prior to the expiration of the existing Prior Authorization.
On receipt of a request from a Participating Physician or Provider for Prior Authorization, HMO shall review and
issue a determination:
not later than the third calendar day after the date the request is received by the HMO for non-hospitalization
care;
within 24 hours of receipt of the request for inpatient and concurrent hospitalization care;
within the time appropriate to the circumstances relating to the delivery of the services and the condition of
the Member but not to exceed one hour from receipt of the request if the proposed services involve post-
stabilization treatment or a Life-Threatening Condition.
Some Texas-licensed Providers may qualify for an exemption from Prior Authorization requirements for a particular
health care service if the Provider met criteria set forth by applicable law for the particular health care service. If
so, where an exemption applies for a particular service, Prior Authorization is not required and will not be denied
TX-I-EX-H-CC-EOC-25
14
HOW THE PLAN WORKS
based on medical necessity or medical appropriateness of care. Other Providers providing Your care may not be
exempt from such requirements. Exemptions do not apply for services that are materially misrepresented or where
the Provider failed to substantially perform the particular service.
For additional information and a current list of medical and health care services that require Prior Authorization,
please visit the website at www.bcbstx.com/find-care/where-you-go-matters/utilization-management.com
Extension of Length of Stay/Service Review (Concurrent Review)
Length of stay/service review is not a guarantee of benefits. Actual availability of benefits is subject to
eligibility and the other terms, conditions, limitations and exclusions under this Plan.
An extension of a previously approved length of stay/service review will be based solely on whether continued
Inpatient care or other health care services are Medically Necessary. If the extension is determined not to be
Medically Necessary, the coverage for the length of stay/service will not be extended, except as otherwise described
in the COMPLAINT AND APPEAL PROCEDURES section.
An extension of length of stay/service review, also known as a concurrent medical necessity review, is when You,
Your Provider, or other authorized representative may submit a request to HMO for continued services. If You, Your
Provider or authorized representative requests to extend care beyond the approved time limit, HMO will make a
determination on the request within the timeframes described in the Review of Claim Determinations provision of
this Evidence of Coverage.
Recommended Clinical Review Option
There are services that do not require Prior Authorization that may be subject to a Post-Service Medical Necessity
Review before the claim is paid. There is an option for Your Provider to request a Recommended Clinical Review
to determine if the service meets approved HMO medical policy and/or level of care review criteria before services
are provided to You. Once a decision has been made on the services reviewed as part of the Recommended Clinical
Review process, the same services will not be reviewed for medical necessity after they have been performed.
To determine if a Recommended Clinical Review is available for a specific service, visit our website at
www.bcbstx.com/find-care/where-you-go-matters/utilization-management.com for the Recommended Clinical
Review list, which is updated when new services are added or when services are removed. You can also call
BCBSTX Customer Service at the number on the back of Your identification card. You or Your Provider may request
a
Recommended Clinical Review. This website also includes information on which services require Prior
Authorization before services are performed.
Recommended Clinical Review is a determination of the medical necessity of a proposed service, but it is not
a guarantee of benefits. Actual availability of benefits is subject to eligibility and the other terms, conditions,
limitations and exclusions of this Benefit Booklet. Please coordinate with Your Provider to submit a written
request for Recommended Clinical Review.
In the event a Recommended Clinical Review determines the proposed services are not Medically Necessary,
You have the right to file an appeal as described in the COMPLAINT AND APPEAL PROCEDURES section. All
appeal and review requirements related to medical necessity determinations, including independent review,
apply to services where Your Provider requests a Recommended Clinical Review.
Contacting Behavioral Health
You, Your Physician or Provider of services or Your authorized representative may contact BCBSTX for a Prior
Authorization or Recommended Clinical Review by calling the toll-free number shown on the back of Your
identification card and following the prompts to the Behavioral Health Unit. During regular business hours (8:00
a.m. and 6:00 p.m., Central Time, on business days), the caller will be routed to the appropriate behavioral health
clinical team for review. Outpatient requests should be requested during regular business hours. After 6:00 p.m., on
weekends, and on holidays, the same behavioral health line is answered by clinicians available for Inpatient acute
reviews only. Requests for residential or partial hospitalization are reviewed during regular business hours.
TX-I-EX-H-CC-EOC-25
15
HOW THE PLAN WORKS
General Provisions Applicable to All Recommended Clinical Reviews
1. No Guarantee of Payment
A Recommended Clinical Review is a determination of the medical necessity of a proposed service, but it
is not a guarantee of benefits or payment of benefits by BCBSTX. Actual availability of benefits is subject
to eligibility and the other terms, conditions, limitations, and exclusions of this Plan. Even if the service
has been approved on Recommended Clinical Review, coverage or payment can be affected for reasons
other than medical necessity. For example, You may have become ineligible as of the date of service or the
Member's benefits may have changed as of the date of service.
2. Request for Additional Information
The Recommended Clinical Review process may require additional documentation from Your Provider or
pharmacist. In addition to the written request for Recommended Clinical Review, the Provider or
pharmacist may be required to include pertinent documentation explaining the proposed services, the
functional aspects of the treatment, the projected outcome, treatment plan and any other supporting
documentation, study models, prescription, itemized repair and replacement cost statements, photographs,
x-rays, etc., as may be requested by BCBSTX to make a determination of coverage pursuant to the terms
and conditions of this Plan.
Post-Service Medical Necessity Review
A Post-Service Medical Necessity Review or Post-Service Claims request, also known as a retrospective medical
necessity review, is the process of determining coverage after treatment has been provided and is based on medical
necessity guidelines. A Post-Service Medical Necessity Review confirms Your eligibility, availability of benefits at
the time of service, and reviews necessary clinical documentation to ensure service was Medically Necessary. A
Post-Service Medical Necessity Review may be performed when a Prior Authorization or Recommended Clinical
Review was not obtained prior to services being rendered under certain circumstances.
General Provisions Applicable to All Post-Service Medical Necessity Reviews
1. No Guarantee of Payment
A Post-Service Medical Necessity Review is not a guarantee of payment. Actual availability of benefits is
subject to eligibility and the other terms, conditions, limitations, and exclusions of HMO. Post-Service
Medical Necessity Review does not guarantee payment of benefits by HMO, for instance You may become
ineligible as of the date of service or Your benefits may have changed as of the date of service.
2. Request for Additional Information
The Post-Service Medical Necessity Review process may require additional documentation from Your
health care Provider or pharmacist. In addition to the written request for Post-Service Medical Necessity
Review, the health care Provider or pharmacist may be required to include pertinent documentation
explaining the services rendered, the functional aspects of the treatment, the projected outcome, treatment
plan and any other supporting documentation, study models, prescription, itemized repair and replacement
cost statements, photographs, x-rays, etc., as may be requested by the plan to make a determination of
coverage pursuant to the terms and conditions of HMO.
Coverage Determinations
Certain services are covered pursuant to HMO medical policies and clinical procedure and coding policies, which
are updated throughout the Calendar Year. The medical policies are guides considered by HMO when making
coverage determinations and lay out the procedure and criteria to determine whether a procedure, treatment, facility,
equipment, drug or device is Medically Necessary and is eligible as a Covered Service or is
Experimental/Investigational, cosmetic, or a convenience item. The clinical procedure and coding policies provide
TX-I-EX-H-CC-EOC-25
16
HOW THE PLAN WORKS
information about what services are reimbursable under the Evidence of Coverage. The most up-to-date medical
and clinical procedure and coding policies are available at www.bcbstx.com or call customer service at the toll-free
number on the back of Your identification card.
Selecting a PCP
At the time You enroll, You must choose a PCP. If any Member is a minor or otherwise incapable of selecting a
PCP, the Subscriber should select a PCP on Member's behalf. If Your Dependents enroll, You and Your Dependents
must choose a PCP from HMO's directory of Participating Providers in order to receive Covered Services. For the
most current list of Participating Providers visit the website at www.bcbstx.com. You may also refer to Your
Provider directory or call customer service at the toll-free telephone number on the back of Your identification card.
You may also request a written copy of the Participating Provider directory, which is updated quarterly, by calling
customer service. Each directory identifies those Providers who are accepting existing patients only. HMO may
assign a PCP if one has not been selected. Until a PCP is selected or assigned, benefits will be limited to coverage
for Emergency Care.
In addition to a PCP, female Members may also select a Participating Obstetrician/Gynecologist (OB/GYN Care)
for gynecological and obstetric conditions, including annual well-woman exams and maternity care, without first
obtaining a Referral from a PCP or calling HMO.
Members who have been diagnosed with a chronic, disabling or life-threatening illness may request approval to
choose a Participating Specialist as a PCP using the process described in Specialist as PCP.
If You select a PCP from the Select Primary Care Physicians, You may be eligible for a lower Copayment for PCP
office visits as indicated in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS. Select PCPs will be
identified in the HMO Provider directory or You can call customer service at the toll-free telephone number on the
back of Your identification card.
Your PCP
Your PCP coordinates Your medical care, as appropriate, either by providing treatment or by issuing Referrals to
direct You to Participating Providers. Except for Emergency Care/medical emergencies or certain direct-access
Specialist benefits described in this Evidence of Coverage, only those services which are provided by or referred
by Your PCP will be covered. It is Your responsibility to consult with the PCP in all matters regarding Your medical
care.
If Your PCP performs, suggests, or recommends a course of treatment for You that includes services that are not
Covered Services, the entire cost of any such non-Covered Services will be Your responsibility.
Changing Your PCP
You may change Your PCP by calling the customer service toll-free telephone number listed on Your identification
card to make the change or to request a change form or assistance in completing that form. The change will become
effective on the first day of the month following HMO's receipt and approval of the request.
In the event of termination of a Participating Provider of any kind, HMO will use best efforts to provide reasonable
advance notice to Members receiving care from such Participating Provider that termination is imminent. Special
circumstances may render You eligible to continue receiving treatment from a Participating Provider after the
effective date of termination, which is fully described in Continuity of Care.
Continuity of Care
If You are under the care of a Participating Provider who stops participating in HMO's network (for reasons other
than failure to meet applicable quality standards, including medical incompetence or professional behavior, or for
fraud), HMO will continue coverage for that Provider's Covered Services if all the following conditions are met:
You are undergoing a course of treatment for a serious and complex condition, You are undergoing
institutional or inpatient care, You are scheduled to undergo nonelective surgery from the Provider (including
TX-I-EX-H-CC-EOC-25
17
HOW THE PLAN WORKS
receipt of postoperative care from such Provider with respect to such surgery), You are pregnant or
undergoing a course of treatment for the pregnancy, or You are determined to be terminally ill. A serious and
complex condition is one that (1) for an acute illness, is serious enough to require specialized medical
treatment to avoid the reasonable possibility of death or permanent harm care (for example, You are currently
receiving chemotherapy, radiation therapy, or post-operative visits for a serious acute disease or condition),
and (2) for a chronic illness or condition, is (i) life-threatening, degenerative, disabling or potentially
disabling, or congenital, and (ii) requires specialized medical care over a prolonged period of time.
the Provider submits a request to HMO to continue coverage of Your care that identifies the condition for
which You are being treated and, where required, indicates that the Provider reasonably believes that
discontinuing treatment could cause You harm; and
the Provider agrees to continue accepting the same reimbursement that applied when participating in HMO's
network, and not to seek payment from You for any amounts for which You would not be responsible if the
Provider were still participating in HMO's network.
Continuity coverage shall continue until the treatment is complete but shall not extend for more than ninety (90)
days (or more than nine (9) months if You have been diagnosed with a terminal illness) beyond the date the
Provider's termination takes effect. If You are past the thirteenth (13th) week of pregnancy when the Provider's
termination takes effect, coverage may be extended through delivery, immediate postpartum care and the follow-
up check-up within the first six (6) weeks of delivery.
You have the right to appeal any decision made for a request for benefits under this subsection as explained in the
COMPLAINT AND APPEAL PROCEDURES section of this Evidence of Coverage.
Specialist as PCP
If You have been diagnosed with a chronic, disabling, or life-threatening illness, You may contact customer service
at the toll-free telephone number on Your identification card to get information to submit for approval from the
HMO Medical Director to choose a Participating Specialist as Your PCP. The Medical Director will require both
You and the Participating Specialist interested in serving as Your PCP to sign a certification of medical need,
to
submit along with all supporting documentation. The Participating Specialist must meet HMO's requirements for
PCP participation and be willing to accept the coordination of all Your healthcare needs. If Your request is denied,
You may appeal the decision as described in COMPLAINT AND APPEAL PROCEDURES. If Your request is
approved, the Specialist's designation as Your PCP will not be effective retroactively. As used herein, "Life
Threatening," means a disease or condition for which the likelihood of death is probable unless the course of the
disease or condition is interrupted.
Availability of Providers
HMO cannot guarantee the availability or continued participation of a particular Provider. Either HMO or any
Participating Provider may terminate the Provider contract or limit the number of Members that will be accepted
as patients. If the PCP initially selected cannot accept additional patients, You will be given an opportunity to
make another PCP selection. You must then cooperate with HMO to select another PCP.
Out-of-Network Services
You may obtain Covered Services, including emergency room services for Mental Health Care or Chemical
Dependency, from Providers who are not part of HMO's network of Participating Providers when receiving
Emergency Care. Also, court-ordered Dependents living outside the Service Area may use non-Participating
Providers.
If Inpatient Hospital Services and post stabilization care are required after receiving Emergency Care at a non-
Participating Hospital, we request that You notify HMO within forty-eight (48) hours of receiving Emergency
Care, or as soon as possible without being medically harmful or injurious to You.
You will not be required to change Your PCP or Participating Specialist Providers to receive Covered Services that
are not available from Participating Providers within the Limited Provider Network but the following apply:
TX-I-EX-H-CC-EOC-25
18
HOW THE PLAN WORKS
the request must be from a Participating Provider;
reasonably requested documentation must be received by HMO;
the Referral will be provided within an appropriate time, not to exceed five business days, based on the
circumstances and Your condition;
when HMO has allowed Referral to a non-Participating Provider, HMO will reimburse the non-Participating
Provider at the usual and customary rate or otherwise agreed rate less the applicable Copayment(s)
Coinsurance and any Deductibles. You are responsible only for the Copayments/Coinsurance and any
Deductibles for such Covered Services; and
before HMO denies a Referral, a review will be conducted by a Specialist of the same or similar specialty as
the type of Provider to whom a Referral is requested.
In some instances where You do not have the ability to choose a network Provider, such as when You receive
services from a non-Participating Facility-Based Provider in a Network Facility, or when Your receive services from
a non-Participating laboratory or diagnostic imaging facility in connection with care provided by Your Participating
Provider. In these instances, Your services may be covered and You would not be responsible for any amounts
beyond the Copayment/Coinsurance or any Deductibles. If You receive a bill from an out-of-network Provider in
such circumstances please contact HMO.
If You elect to use out-of-network Providers for non-Emergency Care services and supplies available from
Participating Providers, benefits will not be covered.
Federal Balance Billing and Other Protections
This section is based upon the No Surprises Act, a federal law enacted in 2020 and effective for Plan Years beginning
on or after January 1, 2022. Unless otherwise required by federal or Texas law, if there is a conflict between the
terms of this Federal Balance Billing and Other Protections section and the terms in the rest of this Certificate,
the terms of this section will apply.
1. Protections from Unexpected Costs for Medical Services from Non-Participating Providers
Your Plan contains provisions related to protection from surprise balance billing under Texas law. The
federal laws provide additional financial protections for You when You receive some types of care from
Providers who do not participate in Your network. If You receive the types of care listed below, Your in-
network cost-sharing levels will apply to any in-network Deductible and out-of-pocket maximums.
Additionally, for services below that are governed by federal law (instead of state law), Your cost-share
amount may be calculated on an amount that generally represents the median payment rate that BCBSTX
has negotiated with Participating Providers for similar services in the area.
Emergency Care from facilities or Providers who do not participate in Your network; and
Care furnished by non-Participating Providers during Your visit to a Participating facility; and
Air ambulance services from non-Participating Providers if the services would be covered with
a
Participating Provider.
Non-Participating Providers may not bill You for more than Your Deductible, Coinsurance or Copayment
for these types of services. There are limited instances when a non-Participating Provider of the care listed
above may send You a bill for up to the amount of that Provider's billed charges. You are only responsible
for payment of the non-Participating Provider's billed charges if, in advance of receiving services, You
signed a written notice form that complies with applicable state and/or federal law.
The requirements of federal law that impact Your costs for care from non-Participating Providers may not
apply in all cases. Sometimes, Texas law provisions relating to balance billing prohibitions may apply. You
may contact BCBSTX at the number on the back of Your identification card with questions about
claims or bills You have received from Providers.
2. Primary Care Physician/Practitioner Selection
TX-I-EX-H-CC-EOC-25
19
HOW THE PLAN WORKS
The Plan generally requires the designation of a Primary Care Physician/Practitioner (PCP). You have the
right to designate any PCP who participates in our network and who is available to accept You or Your
family members. Until You make this designation, Blue Cross and Blue Shield of Texas (BCBSTX)
designates one for You. For information on how to select a PCP and for a list of the Participating PCPs,
contact BCBSTX at www.bcbstx.com or customer service at the toll-free number on the back of Your
identification card.
For Dependent children, You may designate any Participating Provider who specializes in pediatric care as
their Primary Care Physician/Practitioner (PCP).
3. Obstetrics or Gynecological Care
You are not required to obtain a Referral or authorization from Your Primary Care Physician/Practitioner
(PCP) before obtaining Covered Services from any Participating Provider specializing in obstetrics or
gynecology. However, before obtaining covered obstetrical or gynecological care, the Provider must
comply with certain policies and procedures required by Your Plan, including Prior Authorization and
Referral policies. For a list of Participating Providers who specialize in obstetrics or gynecology, visit
www.bcbstx.com or contact customer service at the toll-free number on the back of Your identification
card.
To the extent state and federal regulations are adopted or additional guidance is issued by federal regulatory
agencies that alter the terms of this section, the regulations and any additional guidance will control over
conflicting language in this section.
Inpatient Care by Non-PCP
During an inpatient stay at a Participating Hospital, Skilled Nursing Facility or other Participating facility, it may
be appropriate for a Physician other than Your PCP to direct and oversee Your care, if Your PCP does not do SO.
However, upon discharge, You must return to the care of Your PCP or have Your PCP coordinate care that may be
Medically Necessary.
Provider Communication
HMO will not prohibit, attempt to prohibit or discourage any Provider from discussing or communicating to You
or Your designee any information or opinions regarding Your health care, any provisions of the Health Benefit
Plan as it relates to Your medical needs or the fact that the Provider's contract with HMO has terminated or that
the Provider will no longer be providing services under HMO.
Your Responsibilities
You shall complete and submit an application or other forms or statements that may be reasonably
requested. You agree that all information contained in the applications, forms and statements submitted to
HMO and the Exchange due to enrollment under this Evidence of Coverage or the administration herein
shall be true, correct, and complete to the best of Your knowledge and belief.
You shall notify HMO immediately of any change of address for You or any of Your covered Dependents.
You understand that HMO and the exchange are acting in reliance upon all information You provided at
time of enrollment and afterwards and represents that information SO provided is true and accurate.
By electing coverage pursuant to this Evidence of Coverage, or accepting benefits hereunder, all Members
who are legally capable of contracting, and the legal representatives of all Members who are incapable of
contracting, at time of enrollment and afterwards, represent that all information SO provided is true and
accurate and agree to all terms, conditions and provisions hereof.
You are subject to and shall abide by the rules and regulations of each Provider from which benefits are
provided.
TX-I-EX-H-CC-EOC-25
20
HOW THE PLAN WORKS
Refusal to Accept Treatment
You may, for personal reasons, refuse to accept procedures or treatment by a Participating Provider. Participating
Providers may regard such refusal to accept their recommendations as incompatible with continuance of the
Provider-patient relationship and as obstructing the provision of proper medical care. Participating Providers shall
use their best efforts to render all necessary and appropriate Professional Services in a manner compatible with
Your wishes, insofar as this can be done consistent with the Participating Provider's judgment as to the
requirements of proper medical practice. If You refuse to follow a recommended treatment or procedure, and the
Participating Provider informed You of his belief that no professionally acceptable alternative exists, neither HMO
nor any Participating Provider shall have any further responsibility to provide care for the condition under
treatment.
Premium Payment
On or before the Premium due date, You shall remit payment on behalf of each Subscriber and Dependents the
amount specified by HMO.
A Tobacco User may be subject to a Premium increase of up to 1.5 times the rate applicable to those who are not
Tobacco Users, to the extent permitted by applicable law.
Only if HMO receives Your stipulated payment, shall You be entitled to health services covered hereunder and
then only for the Contract Month for which such payment is received. If any required payment is not received by
the Premium due date of the Contract Month for You and/or Your Dependents or there is a bank draft failure, then
You will be terminated at the end of the grace period. You will be responsible for the cost of services rendered to
You during the grace period of the Contract Month in the event that Premium payments are not made by You.
A grace period of 31 days, or such other grace period, if any, permitted by applicable law or regulatory guidance,
will be granted for the payment of each Premium falling due after the first Premium, during which grace period,
the Evidence of Coverage shall continue in force. After a grace period of 31 days, coverage under this Evidence
of Coverage will automatically terminate on the last day of the coverage period for which Premiums have been
paid unless coverage is extended as described in the next paragraph.
In the event You are receiving a Premium Tax Credit under the Affordable Care Act, You have a three-month grace
period, or such other time period as required or permitted by applicable law, regulation or guidance, for paying
Premiums. If full Premium is not paid within one month of the Premium due date, Claim payments for Covered
Services received during the second and third calendar months of the grace period under this Evidence of Coverage
will be pended until full Premium payment is made. If full payment of the Premium is not made within the three
months grace period, then coverage under this Plan will automatically terminate on the last day of the first month
of the three-month grace period. HMO will not process any claims for services after the date of termination.
During the grace period in the event You are receiving a Premium Tax Credit, HMO will:
pay all appropriate claims for services rendered during the first month of the grace period and may pend
claims for services rendered in the second and third months of the grace period;
notify the Department of Health and Human Services of such non-payment; and
notify Providers of the possibility of denied claims during the second and third months of Your grace period.
HMO reserves the right to change the schedule of Premium payments on each anniversary date of this Evidence of
Coverage upon 60 days written notice.
Third Party Payments
HMO follows the Premium payment process established by the Affordable Care Act in accordance with all Federal
requirements. HMO only accepts cost-sharing and Premium payments from:
A. the Member;
B. the Member's family;
TX-I-EX-H-CC-EOC-25
21
HOW THE PLAN WORKS
C. HMO accepts Premium payments from the following third party entities on behalf of enrollees:
1. A Ryan White HIV/AIDS Program under title XXVI of the Public Health Service Act;
2. An Indian tribe, tribal organization or urban Indian organization; and
3. A local, State, or Federal government program, including a grantee directed by a government program
to make payments on its behalf.
D.HMO may accept Premium payments on behalf of enrollees from private, not-for-profit foundations, if the
payments are:
1. for the entire coverage period of the enrollee's policy;
2. based solely on the financial status of the enrollees;
3. regardless of the coverage the enrollee chooses; and
4. regardless of the enrollee's health status.
E. HMO may accept Premium payments on behalf of enrollees from a Trust, Power of Attorney or Legal
Guardian.
F. HMO will not construe payments from an employer as impermissible third party payments, provided such
payments do not create an Employee Retirement Income Security Act (ERISA) group health plan and either:
1. the employer facilitates Premium payment collection through payroll deduction or a similar method
for the employee, and the employer is not paying any part of the Premium either directly or through
reimbursement; or
2. the employee is participating in an Individual Coverage Health Reimbursement Arrangement
(ICHRA) or a Qualified Small Employer Health Reimbursement Arrangement (QSEHRA) offered by
their employer in place of group health insurance.
G.HMO will accept payments on behalf of an enrollee directly from an employer engaged in an ICHRA or
QSEHRA, or a third party payment coordination service, when such payments are made using allowable
payment methods.
HMO does not accept Premium and cost-sharing payments from any other third party. Unauthorized Premium and
cost-sharing payments will not be credited to the Member's account and will be refunded to the unauthorized payer.
If HMO fails to receive payment in full from an authorized source by the end of any Premium grace period, HMO
will retroactively terminate or cancel this coverage in accordance with the Termination provision of this Evidence
of Coverage.
When You renew HMO coverage or reenroll by selecting a new product, You will need to be current on Your
Premium payments. Any past due Premium payments for coverage HMO provided will be due at the beginning of
the new plan year in addition to current Premium charges. New coverage will not be effective until all such
payments are made.
Member Complaint Procedure
Any problem or claim between You and HMO or between You and a Participating Provider must be dealt with
using the process described in COMPLAINT AND APPEAL PROCEDURES. Complaints may concern non-medical
or medical aspects of care as well as this Evidence of Coverage, including its breach or termination.
TX-I-EX-H-CC-EOC-25
22
HOW THE PLAN WORKS
Identification Card
Cards issued to Members under this Evidence of Coverage are for identification only. The identification card
confers no right to services or other benefits under this Evidence of Coverage. To be entitled to any services or
benefits, the holder of the identification card must be a Member on whose behalf all applicable Premiums under
this Evidence of Coverage have actually been paid.
The card offers a convenient way of providing important information specific to Your coverage including, but not
limited to, the following:
Your Member identification number. This unique identification number is preceded by a three-character
alpha prefix that identifies Blue Cross and Blue Shield of Texas as Your insurer;
any Copayment Amounts that may apply to Your coverage;
important telephone numbers.
Always remember to carry Your identification card with You and present it to Your Providers or Pharmacies when
receiving health care services or supplies.
Please remember that any time a change in Your family takes place it may be necessary for a new identification
card to be issued to You and/or each covered Dependent (refer to the WHO GETS BENEFITS section for instructions
when changes are made). Upon receipt of the change in information, HMO will provide a new identification card.
Unauthorized, Fraudulent, Improper, or Abusive Use of Identification Cards
1. The unauthorized, fraudulent, improper, or abusive use of identification cards issued to You and Your
covered Dependents will include, but not be limited to, the following actions, when intentional:
a. use of the identification card prior to Your Effective Date of Coverage;
b. use of the identification card after Your date of termination of coverage under the Evidence of
Coverage;
c. obtaining prescription drugs or other benefits for persons not covered under the Evidence of Coverage;
d. obtaining prescription drugs or other benefits that are not covered under the Evidence of Coverage;
e. obtaining Covered Drugs for resale or for use by any person other than the person for whom the
Prescription Order is written, even though the person is otherwise covered under the Evidence of
Coverage;
f. obtaining Covered Drugs without a Prescription Order or through the use of a forged or altered
Prescription Order;
g. obtaining quantities of prescription drugs in excess of Medically Necessary or prudent standards of
use or in circumvention of the quantity limitations of the Evidence of Coverage;
h. obtaining prescription drugs using Prescription Orders for the same drugs from multiple Providers;
i. obtaining prescription drugs from multiple Pharmacies through use of the same Prescription Order.
2. The fraudulent or intentionally unauthorized, abusive, or other improper use of identification cards by any
Member can result in, but is not limited to, the following sanctions being applied to all Members covered
under Your coverage:
a. denial of benefits;
b. cancellation of coverage under the Evidence of Coverage for all Members under Your coverage;
c. recoupment from You or any of Your covered Dependents of any benefit payments made;
d. pre-approval of drug purchases and medical services for all Members receiving benefits under Your
coverage;
e. notice to proper authorities of potential violations of law or professional ethics.
TX-I-EX-H-CC-EOC-25
23
HOW THE PLAN WORKS
Member Claims Refund
You are not expected to make payments, other than required Copayments/Coinsurance and any applicable
Deductibles, for any benefits provided hereunder. However, if You make such payments, You may send HMO a
claim for reimbursement, and when a refund is in order, the Provider shall make such refund to You. Your claim
will be allowed only if You notify HMO within ninety (90) days from the date on which covered expenses were
first incurred, unless it can be shown that it was not reasonably possible to give notice within the time limit, and
that notice was given as soon as reasonably possible. However, benefits will not be allowed if notice of claim is
made beyond one (1) year from the date covered expenses were incurred, except for Prescription Drug claims
which must be filed within ninety (90) days of the date of purchase to qualify for reimbursement under Pharmacy
Benefits. You must provide written proof of such payment to HMO within one (1) year of occurrence.
Within fifteen (15) days of receipt of written notice of a claim, HMO shall acknowledge receipt of claim and begin
any necessary investigation. It may be necessary for HMO to request additional information from You. Claims
shall be acted upon within fifteen (15) business days of receipt of a completed claim unless You are notified that
additional time is needed and why. HMO will act on a completed claim no later than forty-five (45) days after the
additional time notification is given to You. If HMO notifies You that HMO will pay a claim or part of a claim,
HMO will pay an approved claim not later than five (5) business days after the date notice is made. Visit the
website at www.bcbstx.com or call customer service at the toll-free number on the back of Your identification
card to obtain a medical claim form or a prescription reimbursement claim form.
Claim or Benefit Reconsideration
If a claim or a request for benefits is partly or completely denied by HMO, You will receive a written explanation
of the reason for the denial and be entitled to a full review. If You wish to request a review or have questions
regarding the explanation of benefits, call or write customer service at the phone number or address on the back
of Your identification card. If You are not satisfied with the information received either on the call or in written
correspondence, You may request an appeal of the decision or file a Complaint. You may obtain a review of the
denial by following the process set out in COMPLAINT AND APPEAL PROCEDURES.
Service Area
See Service Area map and description on the following page(s).
TX-I-EX-H-CC-EOC-25
24
SERVICE AREA
SERVICE AREA
The Service Area covered by this Evidence of Coverage includes the counties shaded on the map below and
as listed by county number on the next page.
14
32
4
1
9
12
5
6
13
8
15
7
16
10
11
TX-I-EX-H-CC-EOC-25
25
SERVICE AREA
County
Legend
#
1.
Dallas
2.
Collin
3.
Denton
4.
Tarrant
5.
Williamson
6.
Travis
7.
Bexar
8.
Harris
9.
El Paso
10.
Hidalgo
11.
Cameron
12.
McLennan
13.
Comal
14.
Rockwall
15.
Jefferson
16.
Nueces
TX-I-EX-H-CC-EOC-25
26
COMPLAINT AND APPEAL PROCEDURES
Customer Inquiries
You or a designated representative may direct inquiries to an HMO customer service representative by mail or by
calling the toll-free telephone number on the back of Your identification card. Inquiries resolved to Your
satisfaction will be tracked by the HMO. If an inquiry is not resolved promptly to Your satisfaction, it will be
handled according to the Complaint procedure described below.
How to File a Complaint with the HMO
A "Complainant" means You or another person, including a Physician or Provider, designated to act on Your behalf,
who files a Complaint.
A "Complaint" means any dissatisfaction expressed by a Complainant orally or in writing to HMO about any aspect
of HMO's operation, including, but not limited to:
information relied upon in making the benefit determination;
HMO administration;
procedures related to review or appeal of an Adverse Determination;
the denial, reduction or termination of a service for reasons not related to medical necessity, including an
Out-of-Network denial because services rendered do not meet the definition of Emergency Care as shown in
the DEFINITIONS section;
the way a service is provided; or
disenrollment decisions.
It does not mean a misunderstanding or problem of misinformation that is resolved promptly by clearing up the
misunderstanding or supplying the appropriate information to Your satisfaction. A Complaint also does not include
a Provider's or Member's oral or written expression of dissatisfaction or disagreement with an Adverse
Determination, which is defined under How to Appeal an Adverse Determination.
Within five (5) business days of receiving a Complaint, the HMO will send Complainant a letter acknowledging
the date of receipt, along with a description of the HMO's Complaint process and timeframes. If the Complaint
was oral, HMO will also enclose a one-page Complaint form clearly stating that the form must be filled out and
returned to HMO for prompt resolution of the Complaint.
Within thirty (30) calendar days after HMO receives the written Complaint or Complaint form, HMO will
investigate and resolve the Complaint and send Complainant a letter explaining HMO's resolution. The letter will
include: 1) the specific medical and contractual reasons for the decision, including any applicable benefit
exclusion, limitation or medical circumstance; 2) additional information required to adjudicate a claim, if needed;
3) the specialization of any Provider consulted; and 4) a full description of the Complaint appeal process, including
deadlines for the appeal process and for the final decision on the appeal.
If You dispute the resolution of the Complaint, You may follow the HMO's Complaint appeals process described
under How to Appeal an HMO Complaint Decision.
Complaints concerning emergencies or denial of continued Hospital stays will be investigated and resolved in
accordance with the medical or dental immediacy of the case, but no later than one business day from HMO's
receipt of the Complaint.
HMO will not engage in any retaliatory action against You, including termination or refusal to renew this Evidence
of Coverage, because You have reasonably filed a Complaint against the HMO or appealed a decision of HMO.
HMO also shall not retaliate against a Physician or Provider, including termination or refusal to renew their
contract, because the Physician or Provider has, on behalf of a Member, reasonably filed a Complaint against the
HMO or appealed a decision of HMO.
TX-I-EX-H-CC-EOC-25
27
COMPLAINT AND APPEAL PROCEDURES
How to Appeal an HMO Complaint Decision
If the Complaint is not resolved to Your satisfaction, the HMO Complaint appeal process gives You the right to
appear in person, by telephone or other technological methods before a Complaint appeal panel in the Service
Area where You normally receive health care services, unless Complainant agrees to another site. The Complaint
appeal panel can also consider a written appeal.
HMO will send Complainant an acknowledgment letter no later than five (5) business days after the date HMO
receives the written request for appeal and will complete the appeals process no later than thirty (30) calendar
days after receiving the written request for appeal.
To advise HMO on resolution of the dispute, HMO will appoint persons to a Complaint appeal panel composed
of an equal number of HMO staff, Physicians or other Providers, and Members of the HMO. Complaint appeal
panel representatives will not have been previously involved in the disputed decision. Physicians or other
Providers must have experience in the area of care that is in dispute and must be independent of any Physician or
Provider who made any prior determination. If specialty care is in dispute, the Complaint appeal panel must
include a person who is a Specialist in that field. Members of the HMO on the Complaint appeal panel will not be
employees of the HMO.
No later than the fifth business day before the scheduled meeting of the Complaint appeal panel, unless Complainant
agrees otherwise, HMO will provide to Complainant or Complainant's designated representative:
documentation to be presented to the Complaint appeal panel by HMO staff;
the specialization of any Physicians or Providers consulted during the investigation;
the name and affiliation of each HMO representative on the Complaint appeal panel; and
the date and location of the hearing.
Complainant or a designated representative, if Member is a minor or disabled, is entitled to appear before the
Complaint appeal panel in person or by conference call or other appropriate technology, and to:
present written or oral information;
present alternative expert testimony;
request the presence of and question those responsible for making the prior determination that resulted in the
appeal; and
bring any person Complainant wishes, but only Complainant may directly question meeting participants.
Complainant or designee will receive a written decision of the Complaint appeal, including the specific medical
determination, clinical basis and contractual criteria used to reach the final decision, and the toll-free telephone
number and address of the Texas Department of Insurance (TDI). Additionally, in the case of a denied Complaint
appeal due to services not meeting the definition of Emergency Care as shown in the DEFINITIONS section, the
written decision will also include notice of Your right to have an Independent Review Organization (IRO) review
the denial and the procedures to obtain a review as shown below in How to Appeal to an Independent Review
Organization (IRO).
Complaint appeals relating to an ongoing emergency or denial of continued hospitalization shall be investigated
and resolved in accordance with the medical or dental immediacy of the case, but no later than one business day
from HMO's receipt of the Complainant's request for an appeal. At the request of Complainant, HMO shall provide
(instead of a Complaint appeal panel) a review by a Physician or Provider who has not previously reviewed the
case and is of the same or similar specialty that typically manages the medical or dental condition, procedure or
treatment under consideration in the appeal. The Physician or Provider reviewing the appeal may interview the
patient or patient's designated representative and will decide the appeal. The Physician or Provider may deliver
initial notice of the appeal decision orally if he then provides written notice no later than the third day after the
date of the decision.
Upon request and free of charge, Complainant or designee may have reasonable access to, and copies of, all
documents, records and other information relevant to the claim or appeal, including:
information relied upon to make the decision;
TX-I-EX-H-CC-EOC-25
28
COMPLAINT AND APPEAL PROCEDURES
information submitted, considered or generated in the course of making the decision, whether or not it was
relied upon to make the decision;
descriptions of the administrative process and safeguards used to make the decision;
records of any independent reviews conducted by HMO;
medical judgments, including whether a particular service is Experimental, Investigational or not Medically
Necessary or appropriate; and
expert advice and consultation obtained by HMO in connection with the denied claim, whether or not the
advice was relied upon to make the decision.
How to Appeal to the Texas Department of Insurance
Anyone, including persons who attempted to resolve Complaints through HMO's Complaint process and are
dissatisfied with the resolution, may report an alleged violation to TDI, Consumer Protection, MC: CO-CP, Texas
Department of Insurance, PO Box 12030, Austin, TX 78711-2030.
You may file a TDI Complaint:
by mailing to the address listed above; or
online at www.tdi.texas.gov.
For general information or information about how to resolve insurance-related Complaints call TDI Consumer Help
line between 8 a.m. and 5 p.m., Central Time, Monday through Friday at (800) 252-3439. To request a TDI
Complaint form call (800) 599-SHOP, or in Austin call (800) 252-3439.
The Commissioner will investigate a Complaint against HMO within sixty (60) days after TDI receives the
Complaint and all information necessary to determine if a violation occurred. The Commissioner may extend the
time to complete an investigation if:
additional information is needed;
an on-site review is necessary;
HMO, the Physician or Provider, or Complainant does not provide all documentation necessary to complete
the investigation; or
other circumstances beyond TDI's control occur.
How to Request a Drug List Exception
Please refer to the PHARMACY BENEFITS section for information on Drug List Exception Requests.
How to Appeal an Adverse Determination
An "Adverse Determination" means a determination by HMO or a utilization review agent that the health care
services provided or proposed to be provided to You are not Medically Necessary or are
Experimental/Investigational. Adverse Determination does not mean a denial of health care services due to the
failure to request prospective or concurrent utilization review.
HMO or a utilization review agent must notify You of an Adverse Determination:
within one (1) working day if You are hospitalized at the time of the Adverse Determination;
within three (3) working days if You are not hospitalized at the time of the Adverse Determination;
within the time appropriate to the circumstance, but in no case to exceed one hour after the time of the request
if You require post-stabilization care after an Emergency.
In life-threatening or Urgent Care circumstances, if HMO has discontinued coverage of prescription drugs or
intravenous infusions for which You were receiving health benefits under this Evidence of Coverage, or if You do
TX-I-EX-H-CC-EOC-25
29
COMPLAINT AND APPEAL PROCEDURES
not receive a timely decision, You are entitled to an immediate appeal to an Independent Review Organization
("IRO") and are not required to comply with HMO's appeal of an Adverse Determination process. An IRO is an
organization independent of the HMO which may perform a final administrative review of an Adverse
Determination made by HMO.
The HMO maintains an internal appeal system that provides reasonable procedures for notification, review, and
resolution of an oral or written appeal concerning dissatisfaction or disagreement with an Adverse Determination.
You, a person acting on Your behalf, or Your Provider of record must initiate an appeal of an Adverse Determination
(which is not part of the Complaint process).
When You, a person acting on Your behalf, or Your Provider of record expresses orally or in writing any
dissatisfaction or disagreement with an Adverse Determination, HMO or a utilization review agent will treat that
expression as an appeal of an Adverse Determination.
Within five (5) business days after HMO receives an appeal of Adverse Determination, HMO will send to the
appealing party a letter acknowledging the date HMO received the appeal and a list of documents the appealing
party must submit. If the appeal was oral, HMO will enclose a one-page appeal form clearly stating that the form
must be returned to HMO for prompt resolution. HMO has thirty (30) calendar days from receipt of a written appeal
of Adverse Determination or the appeal form to complete the appeal process and provide written notice of the appeal
decision to the appealing party. The appeal will be reviewed by a health care Provider not involved in the initial
decision, who is in the same or similar specialty that typically manages the medical or dental condition, procedure
or treatment under review.
Notice of HMO's final decision on the appeal will include the dental, medical and contractual reasons for the
resolution; clinical basis for the decision and the specialization of Provider consulted. A denial will also include
notice of Your right to have an IRO review the denial and the procedures to obtain a review.
NOTE: If HMO is seeking to discontinue coverage of prescription drugs or intravenous infusions for which You are
receiving health benefits under this Evidence of Coverage, You will be notified no later than the 30th day before the
date on which coverage will be discontinued.
Expedited Appeal of Adverse Determination (Emergencies or Continued Hospitalization
Situations)
Appeals relating to ongoing emergencies, denials of continued Hospital stays, or the discontinuance by HMO of
prescription drugs or intravenous infusions for which You were receiving health benefits under this Evidence of
Coverage are referred directly to an expedited appeal process for investigation and resolution. They will be
concluded in accordance with the medical or dental immediacy of the case but in no event will exceed one (1)
working day from the date all information necessary to complete the appeal is received. Initial notice of the decision
may be delivered orally if followed by written notice of the decision within three (3) days.
The
appeal will be reviewed by a health care Provider not involved in the initial decision, who is in the same or
similar specialty that typically manages the medical or dental condition, procedure or treatment under review. The
Physician or Provider reviewing the appeal may interview the patient or patient's designated representative.
How to Appeal to an Independent Review Organization (IRO)
This procedure (not part of the Complaint process) pertains only to appeals of Adverse Determinations and
Complaint appeals concerning denials because services do not meet the definition of Emergency Care as shown in
the DEFINITIONS section. In life-threatening or Urgent Care circumstances, if HMO has discontinued coverage of
prescription drugs or intravenous infusions for which You were receiving health benefits under this Evidence of
Coverage, or if You do not receive a timely decision, You are entitled to an immediate appeal to an IRO and are not
required to comply with HMO's appeal of an Adverse Determination process.
Any party whose appeal of an Adverse Determination is denied by HMO may seek review of the decision by an
IRO assigned to the appeal. At the time the appeal is denied, HMO will provide You, Your designated representative
or Your Provider of record, information on how to appeal the denial, including the approved form, which You, Your
designated representative, or Your Provider of record must complete and return to HMO to begin the independent
TX-I-EX-H-CC-EOC-25
30
COMPLAINT AND APPEAL PROCEDURES
review process. A request for review by an IRO must be submitted within four (4) months after Your receipt of the
Adverse Determination:
in life-threatening, Urgent Care situations, or if HMO has discontinued coverage of prescription drugs or
intravenous infusions for which You were receiving health benefits under this Evidence of Coverage, You,
Your designated representative, or Your Provider of record may contact HMO by telephone to request the
review and provide the required information.
HMO will submit medical records, names of Providers and any documentation pertinent to the decision of
the IRO.
HMO will comply with the decision by the IRO.
HMO will pay for the independent review.
Upon request and free of charge, Member or designee may have reasonable access to, and copies of, all documents,
records and other information relevant to the claim or appeal, including:
information relied upon to make the decision;
information submitted, considered or generated in the course of making the decision, whether or not it was
relied upon to make the decision;
descriptions of the administrative process and safeguards used to make the decision;
records of any independent reviews conducted by HMO;
medical judgements, including whether a particular service is Experimental, Investigational or not Medically
Necessary or appropriate; and
expert advice and consultation obtained by HMO in connection with the denied claim, whether or not the
advice was relied upon to make the decision.
The appeal process does not prohibit You from pursuing other appropriate remedies, including: injunctive relief; a
declaratory judgment or other relief available under law, if the requirement to exhaust the process for appeal and
review places Your health in serious jeopardy.
TX-I-EX-H-CC-EOC-25
31
COVERED SERVICES AND BENEFITS
This section lists the Covered Services under Your Certificate.
Please note that services must be determined to be Medically Necessary by the Plan in order to be covered
under this Certificate.
Coverage of items and services provided to You is subject to BCBSTX policies and guidelines, including, but not
limited to, medical, medical management, utilization or clinical review, utilization management, and clinical
payment and coding policies, which are updated throughout the plan year. These policies are resources utilized by
BCBSTX when making coverage determinations and lay out the procedure and/or criteria to determine whether a
procedure, treatment, facility, equipment, drug or device is Medically Necessary and is eligible as a Covered Service
or is Experimental/Investigational, cosmetic, or a convenience item.
The clinical payment and coding policies are intended to ensure accurate documentation for services performed and
require all Providers to submit claims for services rendered using valid code combinations from Health Insurance
Portability and Accountability Act ("HIPAA") approved code sets. Under the clinical payment and coding policies,
claims are required to be coded correctly according to industry standard coding guidelines including, but not limited
to:
- Uniform Billing ("UB") Editor;
- American Medical Association ("AMA");
-
Current Procedural Terminology ("CPT");
-
CPT® Assistant;
- Healthcare Common Procedure Coding System ("HCPCS");
-
ICD-10 CM and PCS;
- National Drug Codes ("NDC");
- Diagnosis Related Group ("DRG") guidelines;
-
Centers for Medicare and Medicaid Services ("CMS");
- National Correct Coding Initiative ("NCCI");
-
Policy Manual;
- CCI table edits; and
-
other CMS guidelines.
Coverage for Covered Services is subject to the code edit protocols for services/procedures billed and claim
submissions are subject to applicable claim review which may include, but is not limited to, review of any terms of
benefit coverage, Provider contract language, medical and medical management policies, utilization or clinical
review or utilization management policies, clinical payment and coding policies as well as coding software logic,
including but not limited to lab management or other coding logic or edits.
Any line on the claim that is not correctly coded and is not supported with accurate documentation (where
applicable) may not be included in the covered charge and will not be eligible for payment by the Plan. The clinical
payment and coding policies apply for purposes of coverage regardless of whether the Provider rendering the item
or service or submitting the claim is a Participating or non-Participating Provider. The most up-to-date medical
policies and clinical procedure and coding policies are available at www.bcbstx.com or by contacting a Customer
Service Representative at the number shown on Your identification card.
Copayments/Coinsurance
You are liable for certain Copayments/Coinsurance and any applicable Deductibles to Participating Providers,
which are due at the time of service. The Copayment/Coinsurance and any Deductibles due for specific Covered
Services, benefit limitations and out-of-pocket maximums can be found in the SCHEDULE OF COPAYMENTS AND
BENEFIT LIMITS
TX-I-EX-H-CC-EOC-25
32
COVERED SERVICES AND BENEFITS
Deductibles
Benefits are available under this Evidence of Coverage after satisfaction of any applicable Deductibles shown in
the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS.
If You have several covered Dependents, all charges used to apply toward an individual Deductible amount will be
applied towards the family Deductible amount shown in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS.
When the family Deductible amount is reached, no further individual Deductibles will have to be satisfied for the
remainder of that Calendar Year.
Out-of-Pocket Maximums
HMO will determine when maximums have been reached for Covered Services and for Covered Drugs based on
information provided to HMO by You and Participating Providers to whom You have made payments for Covered
Services and for Covered Drugs. Out-of-pocket maximums will include Copayments Coinsurance and Deductibles.
Once You reach the out-of-pocket maximum, You are not required to make additional payments for Covered
Services or Covered Drugs for the remainder of the Calendar Year.
If You have several covered Dependents, all charges used to apply toward an individual out-of-pocket maximum
will be applied towards the family out-of-pocket maximum amount shown in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS. When the family out-of-pocket maximum amount is reached, You are
not required to make additional payments for Covered Services or Covered Drugs for the remainder of the Calendar
Year.
Requirements
All Covered Services, unless otherwise specifically described:
must be Medically Necessary;
must be performed, prescribed, directed or authorized in advance by the PCP and/or the HMO;
must be rendered by a Participating Provider;
are subject to the Copayment/Coinsurance and any other amounts due shown in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS;
may have limitations, restrictions or exclusions described in LIMITATIONS AND EXCLUSIONS; and
may require Prior Authorization.
Professional Services
Services must be provided or arranged by the PCP (except for Virtual Visits) and rendered by a licensed Physician.
HMO may allow other health Providers to provide Covered Services that may be provided under applicable state
law by such Providers. Certain services may be restricted in LIMITATIONS AND EXCLUSIONS.
PCP or Specialist Office Visits. Services provided in the medical office of the PCP or authorized Specialist
for the diagnosis and treatment of illness or injury.
Select PCP Office Visits. Services provided in the medical office of a Select PCP for the diagnosis and
treatment of illness or injury may be eligible for a lower Copayment as indicated in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS.
PCP or Specialist Home Visits. Medically Necessary home visits provided by Participating Physicians
when, in the judgment of the PCP or authorized Specialist, the nature of the illness or injury SO indicates.
Virtual Visits. Services provided for the treatment of conditions as described below in Virtual Visits. Virtual
Visits do not require Referral by the PCP and/or HMO.
Services of Participating Physicians for diagnosis, treatment and consultation are provided while You are an
inpatient or outpatient in a facility for authorized Medically Necessary Covered Services or Emergency Care as
defined herein. Inpatient care may be directed by a Participating Physician other than Your PCP.
TX-I-EX-H-CC-EOC-25
33
COVERED SERVICES AND BENEFITS
Inpatient Hospital Services
Services, except Emergency Care and treatment of breast cancer, must be arranged by Your PCP and approved
through Prior Authorization by HMO. Covered Services include:
1. semi-private room and board, with no limit to number of days unless otherwise indicated;
2. private rooms when Medically Necessary and authorized by the PCP;
3. special diets and meals when Medically Necessary and authorized by the PCP;
4.
use of intensive care or cardiac care units and related services when Medically Necessary and authorized
by the PCP;
5. use of operating and delivery rooms and related facilities;
6. anesthesia and oxygen services;
7. laboratory, x-ray and other diagnostic services;
8. drugs, medications, biologicals and their administration;
9. general nursing care;
10. special duty and private duty nursing when Medically Necessary and authorized by the PCP;
11. radiation therapy, inhalation therapy and chemotherapy;
12. whole blood, including cost of blood, blood plasma, and blood plasma expanders, which is not replaced by
or for You;
13. administration of whole blood and blood plasma;
14. short-term Rehabilitation therapy services in an acute Hospital setting;
15. treatment of breast cancer, for a minimum of forty-eight (48) hours following a mastectomy and twenty-
four (24) hours following a lymph node dissection (with no Prior Authorization required); provided,
however, that such minimum hours of coverage are not required if You and Your attending Physician
determine that a shorter period of inpatient care is appropriate. Upon request, the length of stay may be
extended if HMO determines that an extension is Medically Necessary; and
16. organ and tissue transplants. Prior Authorization is required for any organ or tissue transplant, even if the
patient is already in a Hospital under another Prior Authorization. At the time of Prior Authorization, HMO
will assign a length of stay for the admission. Upon request, the length of stay may be extended if HMO
determines that an extension is Medically Necessary.
a. Services, including donor expenses, for organ and tissue transplants are covered but only if all the
following conditions are met:
1. the transplant procedure is not Experimental/Investigational in nature;
2. donated human organs or tissue or a United States Food and Drug Administration approved
artificial device are used;
3.
the recipient is a Member;
4.
the Member meets all of the criteria established by HMO in pertinent written medical
policies; and
5. the Member meets all of the protocols established by the Hospital in which the transplant is
performed.
b. Covered Services and supplies related to an organ or tissue transplant include, but are not limited to
x-rays, laboratory testing, chemotherapy, radiation therapy, prescription drugs, procurement of
organs or tissues from a living or deceased donor, and complications arising from such transplant.
C.
Benefits will be determined on the same basis as any other sickness when the transplant procedure
is considered Medically Necessary and meets all of the conditions cited above. Benefits will be
available for:
1. a recipient who is a Member covered under the HMO;
2. a donor who is a Member covered under the HMO; or
TX-I-EX-H-CC-EOC-25
34
COVERED SERVICES AND BENEFITS
3. a donor who is not a Member covered under the HMO.
d. Covered Services and supplies include those provided for the:
1. donor search and acceptability testing of potential live donors;
2. evaluation of organs or tissues including, but not limited to, the determination of tissue
matches;
3.
removal of organs or tissues from living or deceased donors; and
4.
transportation and short-term storage of donated organs or tissues.
e.
No benefits are available for a Member for the following services and supplies:
1. living and/or travel expenses of the recipient or a live donor;
2.
expenses related to maintenance of life of a donor for purposes of organ or tissue donation;
3. purchase of the organ or tissue other than payment for Covered Services and supplies
identified above; and
4. organ or tissue (xenograft) obtained from another species.
5. if the transplant operation or post-transplant care is performed in China or another country
known to have participated in forced organ harvesting; or
6. the human organ to be transplanted was procured by a sale or donation originating in China
or another country known to have participated in forced organ harvesting.
Outpatient Facility Services
Services provided through a Participating Hospital outpatient department or a free-standing facility must be
prescribed by the PCP. Prior Authorization may be required for the following services:
1. Infusion Therapy (including chemotherapy);
2. outpatient surgery;
3. radiation therapy; and
4. dialysis.
Outpatient Infusion Therapy Services
Services must be arranged by Your PCP and approved through Prior Authorization by HMO. Some outpatient
Infusion Therapy services for routine maintenance drugs have been identified as capable of being safely
administered, outside of a Hospital. Your out-of-pocket expenses may be lower when Covered Services are provided
in an Infusion Suite, a home or an office instead of an outpatient Hospital setting. Non-maintenance outpatient
Infusion Therapy services will be covered the same as any other illness. The SCHEDULE OF COPAYMENTS AND
BENEFIT LIMITS describes payment for Infusion Therapy services.
Outpatient Laboratory and X-Ray Services
Laboratory and radiographic procedures, services and materials, including (but not limited to) diagnostic x-rays, X-
ray therapy, chemotherapy, fluoroscopy, electrocardiograms, laboratory tests and therapeutic radiology services
must be ordered, authorized or arranged by the PCP and provided through a Participating facility. Prior
Authorization may be required.
Clinician-Administered Drugs
For Members with a chronic, complex, rare, or life-threatening medical condition, Covered Drugs that will be
administered by a Provider in a Physician's office may be obtained from a non-Participating Pharmacy by the
Provider, after the Provider has determined that disease progression, patient harm, or death is probable, or where
the Provider has concerns about patient adherence or timely delivery. These services are covered under the medical
benefit and the cost-sharing requirements will be the same as if they were obtained from a Participating Pharmacy.
TX-I-EX-H-CC-EOC-25
35
COVERED SERVICES AND BENEFITS
Rehabilitation Services and Habilitation Services
Rehabilitation Services and physical, speech and occupational therapies that in the opinion of a Physician are
Medically Necessary and meet or exceed Your treatment goals are provided when Prior Authorization is obtained
or prescribed by Your PCP or Specialist. For a physically disabled person, treatment goals may include maintenance
of functioning or prevention or slowing of further deterioration. Rehabilitation Services and Habilitation Services
may be provided in the Provider's office, in a Hospital as an inpatient, in an outpatient facility, or as home health
care visits. Rehabilitation Services and Habilitation Services, including coverage for chiropractic services, are
available from a Participating Provider when Prior Authorization is obtained or prescribed by Your PCP.
Benefits are provided for Habilitation Services provided for a Member with a disabling condition when both of the
following conditions are met:
the treatment is administered by one of the following Participating Providers: a licensed speech-
language pathologist, licensed audiologist, licensed occupational therapist, licensed physical
therapist, Physician, licensed nutritionist, licensed social worker or licensed psychologist.
the initial or continued treatment must be proven and not Experimental/Investigational.
Benefits for Habilitation Services do not apply to those services that are solely educational in nature or otherwise
paid under state or federal law for purely educational services. Custodial Care, respite care, day care, therapeutic
recreation, vocational training and residential treatment are not Habilitation Services. A service that does not help
the Member to meet functional goals in a treatment plan within a prescribed time frame is not a Habilitation Service.
Benefits for Durable Medical Equipment and prosthetic devices, when used as a component of Habilitation
Services, are described under Durable Medical Equipment and Prosthetic Appliances and Orthotic Devices.
Treatment of Acquired Brain Injury will be covered the same as any other physical condition. Cognitive
Rehabilitation therapy, cognitive communication therapy, neurocognitive therapy and Rehabilitation;
neurobehavioral, neurophysiological, neuropsychological and psychophysiological testing or treatment;
neurofeedback therapy, remediation, post-acute transition services and community reintegration services, including
outpatient day treatment services, or any other post-acute treatment services are covered, if such services are
necessary as a result of and related to an Acquired Brain Injury. To ensure that appropriate post-acute care treatment
is provided, HMO includes coverage for periodic reevaluation for a Member who: (1) has incurred an Acquired
Brain Injury; (2) has been unresponsive to treatment; and (3) becomes responsive to treatment at a later date.
Services may be provided at a Hospital, an acute or post-acute Rehabilitation Hospital, an assisted living facility or
any other facility at which appropriate services or therapies may be provided.
Benefits for Autism Spectrum Disorder will not apply towards and are not subject to any Rehabilitation and
Habilitation services visits maximum indicated on Your SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS.
Maternity Care and Family Planning Services
Maternity Care. HMO provides coverage for inpatient care for the mother and the newborn in a Hospital for a
minimum of forty-eight (48) hours following an uncomplicated vaginal delivery, or ninety-six (96) hours following
an uncomplicated delivery by cesarean section. Prior Authorization is not required. Upon request, the length of stay
may be extended if HMO determines that an extension is Medically Necessary.
Covered Services, which may require Prior Authorization, include:
1. prenatal visits;
2. use of Hospital delivery rooms and related facilities. A separate Hospital admission
Copayment/Coinsurance is required for a newborn child at time of delivery. If a newborn child is
discharged and readmitted to a Hospital more than five (5) days after the date of birth, a separate Hospital
admission Copayment/Coinsurance and any Deductible for such readmission will be required.;
3.
administration of a newborn screening test, including the test kit, required by the state of Texas;
4.
use of newborn nursery and related facilities;
5. special procedures as may be Medically Necessary and authorized by the PCP or designated
Obstetrician/Gynecologist; and
TX-I-EX-H-CC-EOC-25
36
COVERED SERVICES AND BENEFITS
6.
postnatal visits. If the mother or newborn is discharged before the minimum hours of inpatient coverage
have passed, the HMO provides coverage for Post-Delivery Care for the mother and newborn. Post-
Delivery Care may be provided at the mother's home or a Participating Provider's office or facility. A
newborn child will not be required to receive health care services only from Participating Providers if born
outside the Service Area due to an emergency or born in a non-network facility to a mother who is not
a
Member. HMO may require the newborn to be transferred to a Participating facility, at HMO's expense,
when determined to be medically appropriate by the newborn's treating Physician.
Complications of Pregnancy. Covered Services for Complications of Pregnancy will be the same as treatment for
any other physical illness and may require Prior Authorization.
Family Planning. Covered Services, which may require Prior Authorization, include:
1.
diagnostic counseling, consultations and planning services for family planning;
2.
insertion or removal of an intrauterine device (IUD), including the cost of the device;
3.
diaphragm or cervical cap fitting, including the cost of the device;
4. insertion or removal of birth control device implanted under the skin, including the cost of the device;
5.
injectable contraceptive drugs, including the cost of the drug; and
6.
voluntary sterilizations, including but not limited to vasectomy and tubal ligation.
NOTE: some benefits for family planning are available under Health Maintenance and Preventive Services.
Infertility Services. Covered Services, which may require Prior Authorization, include diagnostic counseling,
consultations, planning services and treatment for problems of fertility and Infertility, subject to the exclusions in
LIMITATIONS AND EXCLUSIONS. Once the Infertility workup and testing have been completed, subsequent
workups and testing will require approval of the HMO Medical Director.
Abortion Services. Abortions for a pregnancy which, as certified by a Physician, places the woman in danger of
death unless an abortion is performed are covered.
Fertility Preservation Services Benefits for Fertility Preservation Services for Members who will receive
Medically Necessary treatment for cancer, including surgery, chemotherapy, or radiation, that the American Society
of Clinical Oncology or the American Society for Reproductive Medicine has established may directly or indirectly
cause impaired fertility.
The Fertility Preservation Services must be standard procedures to preserve fertility consistent with established
medical practices or professional guidelines published by the American Society of Clinical Oncology or the
American Society for Reproductive Medicine.
Behavioral Health Services
Benefits and coverage for behavioral health services are provided under the same terms and conditions applicable
to this plan's medical and surgical benefits and coverage.
Outpatient Mental Health Care. Covered Services include diagnostic evaluation and treatment or crisis
intervention when authorized by HMO or its designated behavioral health administrator.
Inpatient Mental Health Care. Covered Services include inpatient Mental Health Care when authorized by HMO
or its designated behavioral health administrator. Covered Services must be rendered based on an individual
treatment plan with specific attainable goals and objectives appropriate to both the patient and the treatment
modality of the program.
Services in a Residential Treatment Center for Children and Adolescents, a Residential Treatment Center or a
Crisis Stabilization Unit are available only when the Member has an acute condition that substantially impairs
thought, perception of reality, emotional process or judgment, or grossly impairs behavior as manifested by recent
disturbed behavior, which would otherwise necessitate confinement in a Participating Mental Health Treatment
Facility.
TX-I-EX-H-CC-EOC-25
37
COVERED SERVICES AND BENEFITS
Serious Mental Illness. Covered Services include treatment of Serious Mental Illness when authorized by HMO
or its designated behavioral health administrator and rendered by a Participating Provider which includes a
Psychiatric Day Treatment Facility. Services are subject to the same terms and conditions as medical and surgical
benefits for any other physical illness.
Chemical Dependency Services. Coverage for treatment of Chemical Dependency is the same as coverage for
treatment of any other physical illness, but is restricted as described in LIMITATIONS AND EXCLUSIONS.
Inpatient treatment of Chemical Dependency must be provided in a Chemical Dependency Treatment Center.
Some services may require Prior Authorization by HMO or its designated behavioral health administrator.
Emergency Services
PCPs provide coverage for Members 24 hours a day, 365 days a year. You must notify Your PCP within forty-eight
(48) hours of receiving Emergency Care, or as soon as possible without being medically harmful or injurious to
You. HMO will pay for a medical screening examination or other evaluation required by Texas or federal law and
provided in the emergency department of a Hospital emergency facility, freestanding emergency medical care
facility, or comparable emergency facility that is necessary to determine whether an emergency medical condition
exists.
Emergency Care. You may obtain Emergency Care, including the treatment and stabilization of an emergency
medical condition that originated in a Hospital emergency facility or in a comparable facility, from a Participating
or non-Participating Provider and the Emergency Care will be covered, based upon the signs and symptoms
presented at the time of treatment as documented by the attending health care personnel, whether the Emergency
Care services were received within the Service Area or Out-of-Area. When receiving emergency room services for
Mental Health Care or Chemical Dependency, benefits will be provided under the same terms and conditions
applicable to this plan's Emergency Care for medical conditions.
Emergency Care services are subject to the Copayment/Coinsurance and any Deductible, unless You are admitted
as an inpatient directly from the emergency room, in which case You pay the inpatient Hospital
Copayment/Coinsurance and any Deductibles. You are not responsible for any amounts beyond the
Copayment/Coinsurance or any Deductibles as indicated on the SCHEDULE OF COPAYMENTS AND BENEFIT
LIMITS.
You may be entitled to protection from balance billing if You receive out-of-network Emergency Care. If You
received services because You believed that failing to get care placed Your health or the health of a spouse, child or
unborn child in danger, but You have questions about whether Your claim was processed as Emergency Care or
questions about a balance bill, please call the number on the back of Your Member identification card.
If post stabilization care is required after an Emergency Care condition that originated in a Participating Hospital
emergency facility or in a Participating comparable facility (as defined in this paragraph), has been treated and
stabilized, the treating Physician or Provider will contact HMO or its designee, who must approve or deny coverage
of the post stabilization care requested within the time appropriate to the circumstances relating to the delivery of
the services and the condition of the patient, but in no case may approval or denial exceed one hour of receiving
the call. If post stabilization care is required in a non-Participating Hospital after an Emergency Care condition that
originated in a Hospital emergency facility or in a Participating comparable facility (as defined in this paragraph),
has been treated and stabilized, the treating Physician or Provider may contact HMO or its designee, but Prior
Authorization is not required for post-stabilization care in a non-Participating Hospital. For purposes of this
paragraph, "comparable facility" includes the following:
1.
any stationary or mobile facility, including, but not limited to, Level V Trauma Facilities and Rural Health
Clinics that have licensed or certified or both licensed and certified personnel and equipment to provide
advanced cardiac life support consistent with American Heart Association and American Trauma Society
standards of care and a free-standing emergency medical care facility as that term is defined in Insurance
Code $843.002 (concerning Definitions);
2. for purposes of Emergency Care related to mental illness, a mental health facility that can provide 24-hour
residential and psychiatric services and that is:
a.
a facility operated by the Texas Department of State Health Services;
TX-I-EX-H-CC-EOC-25
38
COVERED SERVICES AND BENEFITS
b. a private mental Hospital licensed by the Texas Department of State Health Services;
C.
a community center as defined by Texas Health and Safety Code $534.001 (concerning
Establishment);
d.
a facility operated by a community center or other entity the Texas Department of State Health
Services designates to provide mental health services;
e.
an identifiable part of a general Hospital in which diagnosis, treatment, and care for persons with
mental illness is provided and that is licensed by the Texas Department of State Health Services; or
f.
a Hospital operated by a federal agency.
Regardless of other provisions in this Evidence of Coverage to the contrary, for Emergency Care rendered by
Providers who are not part of HMO's network of Participating Providers (non-Participating Provider) or otherwise
contracted with HMO, HMO shall fully reimburse such Providers at its usual and customary rate or an agreed-upon
rate not to exceed billed charges. This amount is calculated excluding any in-network Copayment/Coinsurance and
Deductible imposed with respect to the Member.
Out-of-Area Services. Only Emergency Care services as described above are covered. Continuing or follow-up
treatment for accidental injury or Emergency Care is limited to care required before You can return to the Service
Area without medically harmful or injurious consequences. Emergency Care services for Out-of-Area services are
subject to the Copayment/Coinsurance and any Deductible, as indicated on Your SCHEDULE OF COPAYMENTS AND
BENEFIT LIMITS.
Urgent Care Services
Urgent Care services are covered when rendered by a Participating Urgent Care Provider for the immediate
treatment of a medical condition that requires prompt medical attention but where a brief time lapse before receiving
services will not endanger life or permanent health and does not require Emergency Care services. A PCP Referral
is not required. Additional charges described in Outpatient Laboratory and X-ray Services or Outpatient
Facility Services may also apply.
Each Member is eligible to receive two (2) Urgent Care visits covered at 100% when furnished by a Participating
Urgent Care Provider.
Unless designated and recognized by HMO as an Urgent Care center, neither a Hospital nor an emergency room
will be considered an Urgent Care center.
Retail Health Clinics
Retail Health Clinics provide diagnosis and treatment of uncomplicated minor conditions in situations that can be
handled without a traditional PCP office visit, Urgent Care visit or Emergency Care visit. A PCP Referral is not
required to obtain Covered Services.
Virtual Visits
Virtual Visits provide You with access to Virtual Network Providers that can provide diagnosis and treatment of
non-emergency medical and behavioral health conditions in situations that can be handled without a traditional PCP
office visit, behavioral health office visit, Urgent Care visit or Emergency Care visit. Covered Services may be
provided via a consultation with a licensed medical professional through interactive audio via telephone or
interactive audio-video via online portal or mobile application. For information on accessing this service, You may
access the website at www.bcbstx.com or contact customer service at the toll-free number on the back of Your
identification card. A PCP Referral is not required to obtain Covered Services.
NOTE: Not all medical or behavioral health conditions can be appropriately treated through Virtual Visits. The
Virtual Network Provider will identify any condition for which treatment by an in-person Provider is necessary.
TX-I-EX-H-CC-EOC-25
39
COVERED SERVICES AND BENEFITS
Ambulance Services
For Emergency Care (as defined in this Evidence of Coverage) professional local ground ambulance services or air
ambulance services to the nearest Hospital appropriately equipped and staffed for treatment of the Member's
condition is covered. For non-Emergency Care, professional local ground ambulance services or air ambulance
services is covered, when Medically Necessary and authorized by the PCP, to or from a facility appropriately
equipped and staffed for treatment of the Member's condition. This includes but is not limited to transportation
from one Hospital to another Hospital and from a Hospital to a Rehabilitation facility or Skilled Nursing Facility.
The Member's condition must be such that any other form of transportation would be medically contraindicated.
For non-Emergency Care, air ambulance services are only covered when authorized by the PCP or HMO and 1)
ambulance transportation is Medically Necessary, 2) terrain, distance, Your physical condition, or other
circumstances require the use of air ambulance services rather than ground ambulance services, and 3) transfer is
to the nearest facility with the capabilities to perform the medically necessary services not available at the
originating facility.
Extended Care Services
Covered Services include the following when prescribed by the PCP and authorized by the HMO. Services may
have additional limitations as indicated on the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS and restrictions
or exclusions described in LIMITATIONS AND EXCLUSIONS.
Skilled Nursing Facility Services. Services must be temporary and lead to rehabilitation and an increased ability
to function. Custodial Care is not covered. If You remain in a Skilled Nursing Facility after the PCP discharges You
or after You reach the maximum benefit period or period authorized by HMO, You will be liable for all subsequent
costs incurred.
Hospice Care. Care that is provided by a Hospital, Skilled Nursing Facility, Hospice, or a duly licensed Hospice
Care agency, is approved by HMO, and is focused on a palliative rather than curative treatment. Services include
bereavement counseling. For care provided in a Hospital, charges described in Inpatient Hospital Services will
apply.
Home Health Care. Care in the home by Health Care Professionals who are Participating Providers, including but
not limited to registered nurses, licensed practical nurses, physical therapists, inhalation therapists, speech or
hearing therapists or home health aides. Services must be provided or arranged by the PCP.
Health Maintenance and Preventive Services
Covered Services, which may require Prior Authorization and will not be subject to any Copayment Coinsurance,
Deductible or dollar maximums, include evidence-based items or services that have in effect a rating of "A" or "B"
in the current recommendations of the United States Preventive Services Task Force ("USPSTF") or as required by
state law.
The services listed below may include requirements pursuant to state regulatory mandates and are to be covered at
no cost to the Member:
1.
well-child care for Members through age twenty-two (22) which includes evidenced-informed preventive
care and screenings provided for in the comprehensive guidelines supported by the Health Resources and
Services Administration ("HRSA") for infants, children, and adolescents;
2.
periodic health assessments for Members eighteen (18) and older, based on age, sex and medical history;
3.
routine immunizations recommended by the American Academy of Pediatrics, U.S. Public Health Service
for people in the United States and required by law and immunizations recommended by the Advisory
Committee on Immunization Practices of the Centers for Disease Control and Prevention ("CDC") with
respect to the individual involved. Examples of covered immunizations include diphtheria, haemophilus
influenza type b, hepatitis B, measles, mumps, pertussis, polio, rubella, tetanus, varicella, rotavirus,
COVID-19, and any other immunization that is required by the law for a child. (Allergy injections are not
considered immunizations under this benefit provision.);
TX-I-EX-H-CC-EOC-25
40
COVERED SERVICES AND BENEFITS
4.
bone mass measurement for the detection of low bone mass and to determine risk of osteoporosis and
fractures associated with osteoporosis, for Qualified Individuals including postmenopausal women who
are not receiving estrogen replacement therapy; individuals with vertebral abnormalities, primary
hyperparathyroidism or a history of bone fractures; or individuals receiving long-term glucocorticoid
therapy or being monitored to assess the response to or efficacy of an approved osteoporosis drug therapy;
5.
preventive care and screenings provided with respect to women, such additional preventive care and
screenings provided for in comprehensive guidelines supported by the HRSA such as a well-woman
gynecological exam (once every twelve months) for female Members, and an exam for the early detection
of cervical cancer for female Members age eighteen (18) and older. Your PCP or any
Obstetrician/Gynecologist in Your PCP's network of Participating Providers may perform the well-woman
exam. The exam may include, but is not limited to, a conventional Pap smear screening; a screening using
liquid-based cytology methods alone or in combination with a test approved by the United States Food
and Drug Administration for the detection of human papillomavirus. You must first obtain a Referral from
Your PCP for follow-up services related to treatment of a disease or condition that is not within the scope
of an Obstetrician/Gynecologist. For help in selecting an Obstetrician/Gynecologist, refer to the HMO
Provider directory, contact Your PCP or call customer service;
6.
a screening (non-diagnostic) low-dose mammogram to detect the presence of occult breast cancer for
female Members age thirty-five (35) and over (once every twelve months), and for female Members with
other risk factors. Mammograms may be obtained whether or not a well-woman exam is performed at the
same time. Low-dose mammograms include digital mammography or breast tomosynthesis;
7.
preventive care and screenings provided with respect to women's services will be provided for the
following Covered Services and will not be subject to a Copayment/Coinsurance or Deductible:
Contraceptive Services and Supplies. Benefits are available for female sterilization procedures and
Outpatient Contraceptive Services for women of reproductive capacity. Outpatient Contraceptive Services
means a consultation, examination, procedure, or medical service that is related to the use of a drug or
device intended to prevent pregnancy.
Benefits will be provided to women with reproductive capacity for specified drugs and devices in each of
the following categories of FDA approved contraceptive drugs and devices, including certain: progestin-
only contraceptives; combination contraceptives; emergency contraceptives; extended-cycle/continuous
oral contraceptives; cervical caps; diaphragms; implantable contraceptives; intra-uterine devices;
injectables; transdermal contraceptives; condoms and vaginal contraceptive devices. This list may change
as FDA guidelines, medical management and medical policies are modified. NOTE: Prescription
contraceptive medications are covered under PHARMACY BENEFITS.
To determine if a specific contraceptive drug or device is available under this Preventive Services benefit
contact customer service at the toll-free number on the back of Your identification card.
Benefits will also be provided to women with reproductive capacity for FDA approved over-the-counter
contraceptives such as spermicide and female condoms for women with a written prescription by a
Participating Provider. You will be required to pay the full amount and submit a reimbursement claim form
along with the written prescription to HMO with itemized receipts. Visit the website at www.bcbstx.com
to obtain a claim form.
Contraceptive drugs and devices not available under this Preventive Services benefit may be covered under
other sections of this Evidence of Coverage, and may be subject to any applicable Copayments/Coinsurance
and Deductible.
Breastfeeding Support, Counseling and Supplies. Covered Services include support and counseling
services obtained from a Participating Provider during pregnancy and/or in the post-partum period. Benefits
will also be provided for rental of Hospital-grade breast pumps (not to exceed the total cost) or purchase of
manual or electric breast pump, breast pump supplies, and breast milk storage supplies, with a written
prescription from a Provider and are not subject to Coinsurance, Deductible, Copayment or benefit
maximums when received from a Participating Provider. The benefit for the purchase of an electric breast
TX-I-EX-H-CC-EOC-25
41
COVERED SERVICES AND BENEFITS
pump is limited to one per Calendar Year. You may be required to pay the full amount and submit a
reimbursement claim form along with the written prescription to HMO with itemized receipts for the
manual, electric or Hospital grade breast pump and supplies. Visit the website at www.bcbstx.com to obtain
a claim form.
Benefits are limited as indicated on the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS.
8.
a screening test for hearing loss for Members from birth through age thirty (30) days, and necessary
diagnostic follow-up care related to the screening test from birth through age twenty-four (24) months;
and
9.
a medically recognized rectal screening exam for the detection of colorectal cancer for Members age forty
five (45) or older.
all colorectal cancer examinations, preventive services, and laboratory tests assigned a grade of "A"
or "B" by the United States Preventive Services Task Force for average-risk individuals, including
the services that may be assigned a grade of "A" or "B" in the future; and
an initial colonoscopy or other medical test or procedure for colorectal cancer screening and a
follow-up colonoscopy, which may be subject to any applicable Copayments, Coinsurance and
Deductible, if the results of the initial colonoscopy, test, or procedure are abnormal.
Examples of other covered preventive services that are not subject to Copayment/Coinsurance, Deductible or dollar
maximums include smoking cessation counseling services (including FDA-approved tobacco cessation
medications), healthy diet counseling and obesity screening/counseling. NOTE: smoking cessation medications are
covered under PHARMACY BENEFITS with a Prescription Order from Your Health Care Practitioner.
Preventive drugs (including both prescription and over-the-counter products) that meet the preventive
recommendations outlined above and that are listed on the No-Cost Preventive Drug List (to be implemented in
the quantities and within the time period allowed under applicable law) will be covered and will not be subject to
any Copayment Amount, Coinsurance Amount, Deductible, or dollar maximum when obtained from a
Participating Pharmacy. Drugs on the No-Cost Preventive Drug List that are obtained from a non-Participating
Pharmacy may be subject to Copayment Amount, Coinsurance Amount, Deductibles, or dollar maximum, if
applicable.
A copay waiver can be requested for drugs or immunizations that meet the preventive recommendations outlined
above that are not on the No-Cost Preventive Drug List.
The covered preventive services described above may change as the USPSTF, CDC, HRSA guidelines and state
laws are modified. If a recommendation or guideline for a particular preventive service does not specify the
frequency, method, treatment or setting in which it must be provided, HMO may use reasonable medical
management techniques to determine benefits. For more information, contact customer service at the toll-free
number on Your identification card.
If a covered preventive service is provided during an office visit and is billed separately from the office visit, You
may be responsible for a Copayment/Coinsurance and any applicable Deductible for the office visit only. If an
office visit and the preventive health service are not billed separately and the primary purpose of the visit was not
the preventive health service, You may be responsible for Copayment/Coinsurance and any applicable Deductible
for the office visit including the preventive health service.
Additional preventive screening services, which may require Prior Authorization and may be subject to
Copayment/Coinsurance, Deductibles or dollar maximums, include:
1.
eye and ear screenings (once every twelve months) performed or authorized by the PCP for Members
through age seventeen (17) to identify vision and hearing problems. Eye screenings may be performed in
the PCP office and do not include refractions;
TX-I-EX-H-CC-EOC-25
42
COVERED SERVICES AND BENEFITS
2.
eye and ear screenings (once every two years) performed or authorized by the PCP for Members eighteen
(18) and older to identify vision and hearing problems. Eye screenings may be performed in the PCP office
and do not include refractions.
NOTE: Covered children to age 19 do have additional benefits as described in PEDIATRIC VISION CARE
BENEFITS.
3.
early detection test for cardiovascular disease. Benefits are available for one of the following noninvasive
screening tests for atherosclerosis and abnormal artery structure and function every five years when
performed by a laboratory that is certified by a recognized national organization: (1) computed tomography
(CT) scanning measuring coronary artery calcifications; or (2) ultrasonography measuring carotid intima-
media thickness and plaque.
Tests are available to each covered Member who is (1) a male older than 45 years of age and younger than
76 years of age, or (2) a female older than 55 years of age and younger than 76 years of age. The Member
must be a diabetic or have a risk of developing coronary heart disease, based on a score derived using the
Framingham Heart Study coronary prediction algorithm that is intermediate or higher.
Benefits are limited as indicated on the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS.
4.
early detection test for ovarian cancer. Benefits are available for a CA 125 blood test once every twelve
months and any other test or screenings approved by the United States Food and Drug Administration for
the detection of ovarian cancer for female Members age eighteen (18) and older. Your PCP or any
Obstetrician/Gynecologist in Your PCP's network of Participating Providers may administer the test.
Limitations: To the extent that providing coverage for ovarian cancer screening under Chapter 1370 of the
Texas Insurance Code would otherwise require the State of Texas to make a payment under 42 U.S.C.
Section 18031(d)(3)(B)(ii), a Qualified Health Plan, as defined by 45 C.F.R. Section 155.20, is not required
to provide a benefit for the ovarian cancer screening under Chapter 1370 of the Texas Insurance Code that
exceeds the specified essential health benefits required under 42 U.S.C. Section 18022(b).
5.
a physical exam and an annual prostate-specific antigen (PSA) test (once every twelve months) for the
detection of prostate cancer for male Members who are at least fifty (50) years of age and asymptomatic;
or at least forty (40) years of age with a family history of prostate cancer or another prostate cancer risk
factor.
Dental Surgical Procedures
General dental services are not covered, but limited oral surgical procedures are covered when prescribed by Your
PCP and performed in a Participating Provider's office or in the inpatient or outpatient setting. The following
Covered Services may require Prior Authorization by HMO:
1.
treatment for accidental injury and such injury resulting from domestic violence or a medical condition to
Sound Natural Adult Teeth, the jaw bones or surrounding tissues, not caused by biting or chewing. "Sound
Natural Adult Teeth" means teeth that are free of active or chronic clinical decay, have at least 50% bony
support, are functional in the arch, and have not been excessively weakened by multiple dental procedures;
2.
treatment or correction of a non-dental physiological condition which has resulted in severe functional
impairment;
3.
treatment for tumors and cysts requiring pathological examination of the jaws, cheeks, lips, tongue, roof
and floor of the mouth;
4.
diagnostic and surgical treatment of conditions affecting the temporomandibular joint (including the jaw
or craniomandibular joint) as a result of an accident, a trauma, a developmental defect, or a pathology;
5.
services provided which are necessary for treatment or correction of a congenital defect;
6.
removal of complete bony impacted teeth; and
7.
includes consultation by an oral surgeon (or appropriate Specialist) and associated x-rays or diagnostic
tests.
TX-I-EX-H-CC-EOC-25
43
COVERED SERVICES AND BENEFITS
Cosmetic, Reconstructive or Plastic Surgery
Coverage will be the same as for treatment of any other physical illness generally, only when prescribed or arranged
by Your PCP, and may require Prior Authorization by HMO. Covered Services are limited to the following:
1.
surgery to correct a defect resulting from accidental injury;
2.
reconstructive surgery following cancer surgery;
3. surgery to correct a functional defect which results from a congenital and/or acquired disease or anomaly;
4.
surgical reconstruction of the breast following a mastectomy, and surgical reconstruction of the other breast
to achieve a symmetrical appearance; and
5.
reconstructive Surgery for Craniofacial Abnormalities.
Allergy Care
Covered Services for testing and treatment must be provided or arranged by the PCP.
Diabetes Care
Diabetes Self-Management Training. Covered Services, which may require Prior Authorization, include
instructions enabling a person with diabetes and/or his caretaker to understand the care and management of diabetes;
development of an individualized management plan; nutritional counseling and proper use of diabetes equipment
and supplies. Diabetes self-management training is provided upon the following occasions:
1. the initial diagnosis of diabetes;
2. a significant change in symptoms or condition that requires changes in Your self-management regime, as
diagnosed by a Participating Physician or practitioner;
3.
the prescription of periodic or episodic continuing education warranted by the development of new
techniques and treatments for diabetes; or
4.
the need for a caretaker or a change in caretakers for the person with diabetes necessitates diabetes
management training for the caretaker.
Diabetes Equipment and Supplies. Diabetes equipment and supplies are covered for Members diagnosed with
insulin dependent or non-insulin dependent diabetes; elevated blood glucose levels induced by pregnancy; or
another medical condition associated with elevated blood glucose levels.
When the following diabetes equipment and supplies are obtained, You may be required to pay the full amount of
their bill and submit a reimbursement claim form to HMO with itemized receipts. Visit the website at
www.bcbstx.com to obtain a medical claim form. If You choose to purchase diabetes supplies utilizing pharmacy
benefits, You must pay the applicable PHARMACY BENEFITS Copayment/Coinsurance in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS and any applicable pricing differences as well as any Deductibles. No claim
forms are required.
Diabetes equipment and supplies include, but are not limited to:
blood glucose monitors, including monitors designed to be used by blind individuals;
insulin pumps and associated appurtenances;
insulin infusion devices;
biohazard disposable containers;
podiatric appliances (shoes, shoe inserts and foot orthotics) for prevention of complications associated
with diabetes. Includes up to two pairs of therapeutic footwear per Calendar Year;
infusion sets;
insulin cartridges;
alcohol wipes;
adhesive supplies;
TX-I-EX-H-CC-EOC-25
44
COVERED SERVICES AND BENEFITS
batteries; and
durable and disposable devices to assist in the injection of insulin.
Also included are repairs and necessary maintenance of insulin pumps not otherwise provided for under the
manufacturer's warranty or purchase agreement, rental fees for pumps during the repair and necessary maintenance
of insulin pumps, neither of which shall exceed the purchase price of a similar replacement pump.
The diabetes equipment and supplies in the list below are only available utilizing pharmacy benefits. When You
purchase these items utilizing pharmacy benefits, You must pay the applicable PHARMACY BENEFITS Copayment
in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS and any applicable pricing differences as well as any
Deductibles. No claim forms are required.
glucose meter solution;
test strips specified for use with a corresponding blood glucose monitor;
visual reading and urine test strips and tablets that test for glucose, ketones and protein;
lancets and lancet devices;
injection aids, including devices used to assist with insulin injection and needleless systems;
glucagon emergency kits;
prescription orders for insulin and insulin analog preparations;
insulin syringes;
prescriptive and nonprescriptive oral agents for controlling blood sugar levels.
As new or improved treatment and monitoring equipment or supplies become available and are approved by the
U.S. Food and Drug Administration (FDA), such equipment or supplies may be covered if determined to
be
Medically Necessary and appropriate by the treating Physician or Provider who issues the written order for the
supplies or the equipment.
Prosthetic Appliances and Orthotic Devices
The following covered appliances and devices must be provided or arranged by the PCP, and may require Prior
Authorization by HMO.
1. Initial Prosthetic Appliances, including professional fitting services related to the fitting and use of these
devices, are covered subject to restrictions in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS and
LIMITATIONS AND EXCLUSIONS.
2. Repair and replacement of Prosthetic Appliances and orthotic devices are covered unless the repair or
replacement is a result of misuse or loss by You.
3. Orthopedic braces, such as orthopedic appliances used to support, align, or hold bodily parts in a correct
position; crutches, including rigid back, leg or neck braces; casts for treatment of any part of the legs, arms,
shoulders, hips or back; special surgical and back corsets; and Physician-prescribed, directed or applied
dressings, bandages, trusses and splints that are custom designed for the purpose of assisting the function
of a joint.
4.
Breast prostheses and surgical brassieres after mastectomy.
5.
Medically Necessary foot orthotics that are consistent with the Medicare Benefit Policy Manual are
covered. There is no Calendar Year maximum. This is in addition to, and does not affect, the coverage for
podiatric appliances shown in Diabetes Care.
6.
One cochlear implant, which includes an external speech processor and controller, per impaired ear is
covered. Coverage also includes related treatments such as Habilitation and Rehabilitation Services, fitting
and dispensing services and the provision of ear molds as necessary to maintain optimal fit of hearing aids.
Implant components may be replaced as Medically Necessary or audiologically necessary.
TX-I-EX-H-CC-EOC-25
45
COVERED SERVICES AND BENEFITS
Durable Medical Equipment
You must obtain services and devices through a Participating DME Provider, which must be consistent with the
Medicare DME Manual, and may require Prior Authorization by HMO. HMO will determine whether DME is
rented or purchased, and retains the option to recover the DME upon cancellation or termination of Your coverage.
Examples of DME are: standard wheelchairs, crutches, walkers, orthopedic tractions, Hospital beds, oxygen,
bedside commodes, suction machines, etc. Excluded items are listed in LIMITATIONS AND EXCLUSIONS.
Ostomy Supplies
Benefits for supplies related to ostomy may include, but are not limited to:
1.
Pouches, face plates and belts;
2.
Irrigation sleeves, bags and ostomy irrigation catheters;
3.
Skin barriers; and
4.
Deodorants, filters, lubricants, tape, appliance cleaners, adhesive and adhesive remover.
Medical Supplies
Medical or disposable supplies prescribed by a Physician include, but are not limited to:
1. Urinary catheters;
2.
Wound care or dressing supplies given by a Provider during treatment for covered health services; and
3.
Medical-grade compression stockings when considered Medically Necessary. The stockings must be
prescribed by a Physician, individually measured and fitted to the patient.
Coverage also includes disposable supplies necessary for the effective use of Durable Medical Equipment and
diabetic supplies for which benefits are provided as described under Durable Medical Equipment and Diabetes
Services.
Hearing Aids
Covered Services and equipment, which may require Prior Authorization, include one audiometric examination to
determine type and extent of hearing loss once every thirty-six (36) months and the fitting and purchase of hearing
aid device(s). Coverage also includes fitting and dispensing services, the provision of ear molds as necessary to
maintain optimal fit of hearing aids and Habilitation and Rehabilitation Services. Exclusions are listed in
LIMITATIONS AND EXCLUSIONS.
Speech and Hearing Services
Covered Services, which may require Prior Authorization, include inpatient and outpatient care and treatment for
loss or impairment of speech or hearing that is not less favorable than for physical illness generally.
Benefits for Autism Spectrum Disorder will not apply towards and are not subject to any speech and hearing services
visits maximum indicated on Your SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS.
Therapies for Children with Developmental Delays
Covered Services include treatment for "Developmental Delays", which means a significant variation in normal
development as measured by appropriate diagnostic instruments and procedures in one or more of the following
areas:
cognitive;
physical;
communication;
social or emotional; or
adaptive.
TX-I-EX-H-CC-EOC-25
46
COVERED SERVICES AND BENEFITS
Treatment includes the necessary rehabilitative and habilitative therapies in accordance with an "Individualized
Family Service Plan", which is the initial and ongoing treatment plan developed and issued by the Interagency
Council on Early Childhood Intervention under Chapter 73 of the Human Resources Code for a Dependent child
with Developmental Delays, including:
occupational therapy evaluations and services;
physical therapy evaluations and services;
speech therapy evaluations and services; and
dietary or nutritional evaluations.
You must submit an Individualized Family Service Plan to HMO before You receive any services, and again if the
Individualized Family Service Plan is changed. After a child is three (3) years of age and services under the
Individualized Family Service Plan are completed, the standard contractual provisions in this Evidence of Coverage
and any benefit exclusions or limitations will apply.
Autism Spectrum Disorder
Generally recognized services prescribed in relation to Autism Spectrum Disorder by Your PCP in a treatment plan
recommended by that Physician are covered. No benefit maximums will apply.
Individuals providing treatment prescribed under that plan must be a health care practitioner:
who is licensed, certified, or registered by an appropriate agency of the state of Texas;
whose professional credential is recognized and accepted by an appropriate agency of the United States;
or
who is certified as a Provider under the TRICARE military health system.
Treatment may include services such as:
evaluation and assessment services;
screening at 18 and 24 months;
applied behavior analysis;
behavior training and behavior management;
speech therapy;
occupational therapy;
physical therapy; or
medications or nutritional supplements used to address symptoms of Autism Spectrum Disorder.
All standard contractual provisions of this Evidence of Coverage will apply, including but not limited to, defined
terms, limitations and exclusions.
Benefits for Autism Spectrum Disorder will not apply towards any visit maximum indicated on Your SCHEDULE
OF COPAYMENTS AND BENEFIT LIMITS. Please review the Rehabilitation and Habilitation Services provision and
the Speech and Hearing Services provisions in this section of the Certificate.
Routine Patient Costs for Participants in Certain Clinical Trials
Covered Services for Routine Patient Care Costs, as defined in DEFINITIONS are provided in connection with a
phase I, phase II, phase III, or phase IV clinical trial that is conducted in relation to the prevention, detection, or
treatment of cancer or other Life-Threatening Disease or Condition and is recognized under state and/or federal
law.
Services are not available under this section for services that are a part of the subject matter of the clinical trial
and that are customarily paid for by the Research Institution conducting the clinical trial. Services must be
provided or arranged by the PCP.
TX-I-EX-H-CC-EOC-25
47
COVERED SERVICES AND BENEFITS
Teledentistry, Telehealth and Telemedicine Medical Services
Teledentistry, Telehealth and Telemedicine Medical Services are covered as defined in DEFINITIONS and may
require Prior Authorization.
Diagnostic Mammography and Other Breast Imaging
Diagnostic Imaging is covered to the same extent as screening mammograms as described in the COVERED
SERVICES AND BENEFITS; Health Maintenance and Preventive Services.
In addition to the applicable terms provided in the DEFINITIONS section of the Evidence of Coverage, the following
term will apply specifically to this provision.
Diagnostic Imaging means an imaging examination using mammography, ultrasound imaging, or magnetic
imaging that is designed to evaluate:
1.
a subjective or objective abnormality detected by a Physician or patient in a breast;
2.
an abnormality seen by a Physician on a screening mammogram;
3.
an abnormality previously identified by a Physician as probably benign in a breast for which follow-up
imaging is recommended by a Physician; or
4.
an individual with a personal history of breast cancer or dense breast tissue.
The Copayment/Coinsurance Amounts indicated in the SCHEDULE OF COPAYMENTS AND BENEFIT
LIMITS; Health Maintenance and Preventive Services for screening mammograms will apply but without
Member age restrictions.
Biomarker Testing
Covered Services for Medically Necessary Biomarker Testing for the purpose of diagnosis, treatment, appropriate
management, or ongoing monitoring of a member's disease or condition to guide treatment when the test is
supported by medical and scientific evidence, including:
a labeled indication for a test approved or cleared by the FDA;
a labeled indication for a test approved or cleared by the FDA;
an indicated test for a drug approved by the FDA;
a national coverage determination made by CMS or a local coverage determination made by a Medicare
administrative contractor;
nationally recognized clinical practice guidelines; or
consensus statements.
Biomarker Testing will be covered only when use of Biomarker Testing provides clinical utility because use of the
test for the condition is evidence-based, is scientifically valid based on the medical and scientific evidence, informs
the members outcome and a provider's clinical decision, and predominantly addresses the acute or chronic issue
for which the test is ordered. This coverage will be provided in a manner that limits disruptions in care, including
limiting the number of biopsies and biospecimen samples.
Routine Foot Care
Medically Necessary routine foot care is covered, when obtained from a licensed Provider.
TX-I-EX-H-CC-EOC-25
48
LIMITATIONS AND EXCLUSIONS
The following benefits are not covered unless specifically provided for in COVERED SERVICES AND
BENEFITS or PHARMACY BENEFITS:
1. Services or supplies of non-Participating Providers or self-Referral to a Participating Provider,
except:
a. Emergency Care;
b. when authorized by HMO or Your PCP; and
C. female Members may directly access an Obstetrician/Gynecologist for: (1) well-woman
exams; (2) obstetrical care; (3) care for all active gynecological conditions; and (4) diagnosis,
treatment and Referral for any disease or condition within the scope of the professional
practice of the Obstetrician/Gynecologist.
2. Services or supplies which in the judgment of the PCP or HMO are not Medically Necessary and
essential to the diagnosis or direct care and treatment of a sickness, injury, condition, disease or
bodily malfunction as defined herein.
3. If a service is not covered, HMO will not cover any services related to it, except for routine patient
care for participants in an Approved Clinical Trial. Related services are:
a. services in preparation for the non-covered service;
b. services in connection with providing the non-covered service;
C. hospitalization required to perform the non-covered service; or
d. services that are usually provided following the non-covered service, such as follow-up care
or therapy after surgery.
4. Experimental/Investigational services and supplies. Denials based on Experimental/Investigational
services and supplies are Adverse Determinations and are subject to the utilization review process,
including reviews by an Independent Review Organization (IRO) as described in the COMPLAINT
AND APPEAL PROCEDURES section.
5. Any charges resulting from the failure to keep a scheduled visit with a Participating Provider or for
acquisition of medical records.
6. Special medical reports not directly related to treatment.
7. Examinations, testing, vaccinations or other services required by employers, insurers, schools,
camps, courts, licensing authorities, other third parties or for personal travel.
8. Services or supplies provided by a person who is related to a Member by blood or marriage and self-
administered services.
9. Services or supplies for injuries sustained as a result of war, declared or undeclared, or any act of
war or while on active or reserve duty in the armed forces of any country or international authority.
10. Benefits You are receiving through Medicare or for which You are eligible through entitlement
programs of the federal, state, or local government, including but not limited to Medicaid and its
successors.
11. Care for conditions that federal, state or local law requires to be treated in a public facility.
TX-I-EX-H-CC-EOC-25
49
LIMITATIONS AND EXCLUSIONS
12. Appearances at court hearings and other legal proceedings, and any services relating to judicial or
administrative proceedings or conducted as part of medical research.
13. Services or supplies provided in connection with an occupational sickness or an injury sustained in
the scope of and in the course of any employment whether or not benefits are, or could upon proper
claim be, provided under the Workers' Compensation law.
14. Subject to the Emergency Care benefits as described in COVERED SERVICES AND BENEFITS; any
services and supplies provided to a Member incurred outside the United States if the Member traveled
to the location for the purpose of receiving medical services, supplies, or drugs.
15. Transportation services except as described in Ambulance Services, or when approved by HMO.
16. Personal or comfort items, including but not limited to televisions, telephones, guest beds,
admission kits, maternity kits and newborn kits provided by a Hospital or other inpatient facility.
17. Private rooms unless Medically Necessary and authorized by the HMO. If a semi-private room is
not available, HMO covers a private room until a semi-private room is available.
18. Any and all transplants of organs, cells, and other tissues, except as described in Inpatient Hospital
Services. Services or supplies related to organ and tissue transplant or other procedures when You
are the donor and the recipient is not a Member are not covered.
19. Services or supplies for Long Term or Custodial Care.
20. Services or supplies furnished by an institution that is primarily a place of rest, a place for the aged
or any similar institution.
21. Private duty nursing, except when determined to be Medically Necessary and ordered or authorized
by the PCP.
22. Services or supplies for Dietary and Nutritional Services, including home testing kits, vitamins,
dietary supplements and replacements, and special food items, except:
a. an inpatient nutritional assessment program provided in and by a Hospital and approved by
HMO;
b. dietary formulas necessary for the treatment of phenylketonuria or other heritable diseases;
C. as described in Diabetes Care;
d. as described in Autism Spectrum Disorder; or
e. as described in Therapies for Children with Developmental Delays.
23. Services or supplies for Cosmetic, Reconstructive or Plastic Surgery, including breast augmentation
(enlargement) surgery, even when Medically Necessary, except as described in Cosmetic,
Reconstructive or Plastic Surgery.
24. Services or supplies provided primarily for:
a. Environmental Sensitivity; or
b. Clinical Ecology or any similar treatment not recognized as safe and effective by the American
Academy of Allergists and Immunologists; or
C. inpatient allergy testing or treatment; or
d. allergen specific IgG measurement.
TX-I-EX-H-CC-EOC-25
50
LIMITATIONS AND EXCLUSIONS
25. Services or supplies provided for, in preparation for, or in conjunction with the following, except
as described in Maternity Care and Family Planning Services:
a. sterilization reversal (male or female);
b.
treatment of sexual dysfunction including medications, penile prostheses and other surgery,
and vascular or plethysmographic studies that are used only for diagnosing impotence;
C.
promotion of fertility through extra-coital reproductive technologies including, but not limited
to, artificial insemination, intrauterine insemination super ovulation uterine capacitation
enhancement, direct-intraperitoneal insemination, trans-uterine tubal insemination, gamete
intrafallopian transfer, pronuclear oocyte stage transfer, zygote intrafallopian transfer and
tubal embryo transfer;
d.
any services or supplies related to in vitro fertilization or other procedures when You are the
donor and the recipient is not a Member;
e. in vitro fertilization and fertility drugs.
26. Treatment of decreased blood flow to the legs with pneumatic compression device or high-pressure
rapid inflation-deflation cycle.
27. Treatment of tissue damage or disease in any location with platelet-rich plasma.
28. Services or supplies in connection with foot care for flat feet, fallen arches, or chronic foot strain.
29. Services or supplies for reduction of obesity or weight, including surgical procedures and
prescription drugs, even if the Member has other health conditions which might be helped by a
reduction of obesity or weight, except for healthy diet counseling and obesity screening/counseling
as may be provided under Preventive Services.
30. Services or supplies for, or in conjunction with, chelation therapy, except for treatment of acute
metal poisoning.
31. Services or supplies for dental care, except as described in Dental Surgical Procedures.
32. Non-surgical or non-diagnostic services or supplies for treatment or related services to the
temporomandibular (jaw) joint or jaw-related neuromuscular conditions with oral appliances, oral
splints, oral orthotics, devices, prosthetics, dental restorations, orthodontics, physical therapy, or
alteration of the occlusal relationships of the teeth or jaws to eliminate pain or dysfunction of the
temporomandibular joint and all adjacent or related muscles and nerves. Medically Necessary
diagnostic and/or surgical treatment is covered for conditions affecting the temporomandibular joint
(including the jaw or craniomandibular joint) as a result of an accident, trauma, congenital defect,
developmental defect or pathology, as described in Dental Surgical Procedures.
33. Alternative treatments such as acupuncture, dry needling, trigger-point acupuncture, acupressure,
hypnotism, massage therapy and aromatherapy.
34. Services or supplies for:
a. intersegmental traction;
b. all types of home traction devices and equipment;
C. vertebral axial decompression sessions;
d. surface EMGs;
e. spinal manipulation under anesthesia;
TX-I-EX-H-CC-EOC-25
51
LIMITATIONS AND EXCLUSIONS
f. muscle testing through computerized kinesiology machines such as Isostation, Digital
Myograph, and Dynatron; and
g. balance testing through computerized dynamic posturography sensory organization test.
35. Galvanic stimulators or TENS units.
36. Scanning the visible front portion of the eye with computerized ophthalmic diagnostic imaging, or
measuring the firmness of the front of the eye with corneal hysteresis by air impulse stimulation.
37. Disposable or consumable outpatient supplies, such as syringes, needles, blood or urine testing
supplies (except as used in the treatment of diabetes); sheaths, bags, elastic garments, stockings and
bandages, garter belts.
38. Excluded supplies include, but are not limited to, compression stockings, ace bandages, wound care
or dressing supplies, prescribed or non-prescribed medical and disposable supplies that can be
purchased over the counter.
This exclusion does not apply to:
a. Ostomy bags and related supplies for which benefits are provided as described under Ostomy
Supplies section;
b. Disposable supplies necessary for the effective use of Durable Medical Equipment for which
benefits are provided as described under Durable Medical Equipment section;
C. Urinary catheters, wound care or dressing supplies given by a Provider during treatment for
Covered Services;
d. Medical grade compression stockings when considered Medically Necessary. The stockings
must be prescribed by a Physician, individually measured and fitted to the patient;
e. Diabetic supplies for which benefits are provided as described under Diabetes Services
section;
f. Batteries, tubing, nasal cannulas, connectors and masks except when used with Durable
Medical Equipment.
Not all Medical Supplies are Covered Services and all are subject to medical review.
39. Prosthetic Appliances or orthotic devices not described in Diabetes Care or Prosthetic Appliances
and Orthotic Devices including, but not limited to:
a. orthodontic or other dental appliances or dentures;
b. splints or bandages provided by a Physician in a non-Hospital setting or purchased over the
counter for the support of strains and sprains;
C. corrective orthopedic shoes, including those which are a separable part of a covered brace;
specially-ordered, custom-made or built-up shoes and cast shoes; shoe inserts designed to
support the arch or affect changes in the foot or foot alignment; arch supports; braces; splints
or other foot care items.
40. Testing of:
a. blood for measurement of levels of: Lipoprotein a; small dense low density lipoprotein;
lipoprotein subclass high resolution; lipoprotein subclass particle numbers; lipoprotein
associated phospholipase A2, which are fat/protein substances in the blood that might be
ordered in people with suspected deposits in the walls of blood vessels;
TX-I-EX-H-CC-EOC-25
52
LIMITATIONS AND EXCLUSIONS
b. urine for measurement of collagen cross links, which is a substance that might be ordered in
people with suspected high bone turnover;
C. cervicovaginal fluid for amniotic fluid protein during pregnancy, which might be ordered in
people suspected to have fluid leaking from around the baby (premature ruptured membranes).
41. The following psychological/neuropsychological testing and psychotherapy services:
a. educational testing;
b. employer/government mandated testing;
C. testing to determine eligibility for disability benefits;
d. testing for legal purposes (e.g., custody/placement evaluations, forensic evaluations, and court
mandated testing);
e. testing for vocational purposes (e.g., interest inventories, work related inventories, and career
development);
f. services directed at enhancing one's personality or lifestyle;
g. vocational or religious counseling;
h. activities primarily of an educational nature;
i. music or dance therapy; or
j. bioenergetic therapy.
42. Biofeedback (except for an Acquired Brain Injury diagnosis) or other behavior modification
services.
43. Mental health services except as described in Behavioral Health Services or as may be provided
under Autism Spectrum Disorder.
44. Residential Treatment Centers for Chemical Dependency that are not:
a. affiliated with a Hospital under a contractual agreement with an established system for patient
Referral;
b. accredited as such a facility by the Joint Commission on Accreditation of Hospitals;
C. licensed as a Chemical Dependency treatment program by the Texas Commission on Alcohol
and Drug Abuse; or
d. licensed, certified or approved as a Chemical Dependency treatment program or center by any
other state agency having legal authority to SO license, certify or approve.
45. Trauma or wilderness programs for behavioral health or Chemical Dependency treatment.
46. Replacement for loss, damage or functional defect of hearing aids. Batteries are not covered unless
needed at the time of the initial placement of the hearing aid device(s).
47. Deluxe equipment such as motor driven wheelchairs and beds (unless determined to be Medically
Necessary); comfort items; bedboards; bathtub lifts; over-bed tables; air purifiers; sauna baths;
exercise equipment; stethoscopes and sphygmomanometers; Experimental and/or research items;
and replacement, repairs or maintenance of the DME.
48. Over-the-counter supplies or medicines and prescription drugs and medications of any kind, except:
a. as provided while confined as an inpatient;
b. as provided under Autism Spectrum Disorder;
C. as provided under Diabetes Care;
TX-I-EX-H-CC-EOC-25
53
LIMITATIONS AND EXCLUSIONS
d. contraceptive devices and FDA-approved over-the-counter contraceptives for women with a
written prescription from a Participating Provider; or
e. if covered under PHARMACY BENEFITS.
49. Any procedures, equipment, services, supplies, or charges for abortions except for abortions to
terminate a pregnancy which, as certified by a Physician, places You in danger of death unless an
abortion is performed.
50. Male contraceptive devices, including over-the-counter contraceptive products such as condoms;
female contraceptive devices, including over-the-counter contraceptive products such as spermicide,
when not prescribed by a Participating Provider.
51. Self-administered drugs dispensed or administered by a Physician in his/her office.
52. Any services or supplies from more than one Provider on the same day(s) to the extent benefits
were duplicated.
53. Cannabis - This plan does not cover cannabis. Cannabis means all parts of the plant genus Cannabis
containing delta-9-tetrahydrocannabinol (THC) as an active ingredient, whether growing or not, the
seeds of the plant, the resin extracted from any part of the plant, and every cannabis-derived
compound, manufacture, salt, derivative, mixture or preparation of the plant, its seeds or its resin.
Cannabis with THC as an active ingredient may be called marijuana.
54. Some laboratory services are not covered by Your plan. The following laboratory services are not
covered:
a. Vitamin B12 testing or screening for a Vitamin B12 deficiency in healthy, asymptomatic
individual; homocysteine or holotranscobalamin testing to screen for or confirm a Vitamin B
12 deficiency; or Vitamin B12 testing within three (3) months of beginning treatment for a
B12 deficiency;
b. Vitamin D testing - Routine screening for vitamin D deficiency with serum testing in
asymptomatic individuals and/or during general encounters;
C. Hemoglobin A1c testing in the following situations:
if You have had a blood transfusion within the past 120 days; or
if You have a condition associated with increased red blood cell turnover; or
if You are also being measured for fructosamine;
d. Influenza Testing - Viral culture testing for influenza in an outpatient setting; outpatient
influenza testing in asymptomatic patients; Serology testing for influenza under any
circumstance;
e.
Cardiac Biomarkers - Measurement of cardiac biomarkers for the diagnosis a heart attack if
You have symptoms of acute coronary syndrome such as chest pain; or Measurement of
cardiac biomarkers if You have symptoms of acute coronary syndrome and received services
in a setting that cannot perform an evaluation for a heart attack, such as an independent lab or
Physician's office;
f. Drug testing in an outpatient setting is not covered in the following situations:
testing to confirm the presence and/or amount of drugs in Your system is not covered
when laboratory-based definitive drug testing is requested without any prior screening
test results, or when laboratory-based definitive drug testing is requested for larger
than seven drug classes panels;
use of proprietary drug tests such as RiskviewRX Plus;
TX-I-EX-H-CC-EOC-25
54
LIMITATIONS AND EXCLUSIONS
specific validity testing, including, but not limited to the following tests: urine specific
gravity, urine creatinine, pH, urine oxidant level, and genetic identity testing, are
included in the panel test and therefore will not be covered if submitted individually
if a urine panel test was also ordered at the same time;
testing for any American Medical Association definitive drug class codes;
same-day testing for the same drug or metabolites from two different samples (e.g.
both a blood and a urine specimen);
testing of samples with abnormal validity tests;
drug testing for patients in a facility setting (inpatient or outpatient) are not separately
covered, as they are included in the daily charge at the facility;
Your plan does not cover both qualitative (type of drug) testing and presumptive (to
verify presence of drugs) testing on the same specimen.
g. Folate testing - Measurement of RBC folate is not covered. Measurement of serum folate
concentration is only covered when You have been diagnosed with megaloblastic or
macrocytic anemia and those conditions do not resolve after folic acid treatment;
h. Pancreatic Enzyme Testing is not covered the following situations:
more than once per visit; or
as part of ongoing assessment or therapy of chronic pancreatitis; or
during a general exam without abnormal findings if You do not have symptoms and
are not pregnant;
for measurement of the following biomarkers for the diagnosis or assessment of acute
pancreatitis, prognosis, and/or determination of severity of acute pancreatitis is not
covered: measurement of both amylase AND serum lipase, serum
trypsin/trypsinogen/TAP (trypsinogen activation peptide), C-Reactive Protein (CRP);
Interleukin-6 (IL-6); Interleukin-8 (IL-8); or Procalcitonin.
i. Cardiovascular disease risk assessment testing is not covered in the following situations:
High-sensitivity C-Reactive Protein is not covered except when a risk based treatment
decision is not certain after having a quantitative risk assessment using American
College of Cardiology/ American Heart Association (ACC/AHA) calculator to
calculate 10-year risk of Cardiovascular disease CVD;
testing for High-sensitivity C-Reactive Protein is not covered as a screening test for
the general population or for monitoring response to therapy;
measurement of High-sensitivity cardiac troponin T is not covered for cardiovascular
risk assessment and stratification in the outpatient setting;
Homocysteine testing for cardiovascular disease risk assessment screening,
evaluation and management is not covered;
novel Cardiovascular Biomarkers such as measurement of novel lipid and non-lipid
biomarkers is not covered as an add on to LDL cholesterol in the risk assessment of
cardiovascular disease;
cardiovascular risk panels, consisting of multiple individual biomarkers intended to
assess cardiac risk (other than simple lipid panels), are not covered;
Serum Intermediate Density Lipoprotein is not covered as an indicator of
cardiovascular disease risk;
measurement of lipoprotein-associated phospholipase is not covered as an indicator
of risk of cardiovascular disease;
measurement of secretory type II phospholipase is not covered in the assessment of
cardiovascular risk for all indications;
TX-I-EX-H-CC-EOC-25
55
LIMITATIONS AND EXCLUSIONS
measurement of long-chain omega-3 fatty acids in red blood cell membranes,
including but not limited to its use as a cardiac risk factor is not covered;
all other tests for assessing CHD risk are not covered.
j. Allergen Testing is not covered in the following situations:
routine re-testing for confirmed allergies to the same allergens is not covered except
in children and adolescents with positive food allergen results to monitor for allergy
resolution;
the Antigen Leukocyte Antibody test (ALCAT) is not covered;
in-vitro testing of allergen specific IgG or non-specific IgG, IgA, IgM, and/or IgD in
the evaluation of suspected allergy is not covered;
Basophil Activation flow cytometry testing for measuring hypersensitivity to
allergens is not covered;
in-vitro allergen testing using bead-based epitope assays is not covered;
in-vitro testing of allergen non-specific IgE is not covered.
k. Erectile Dysfunction - The following tests for the diagnosis of erectile dysfunction are not
covered:
angiotensin-converting enzyme insertion/deletion polymorphism testing;
endothelial nitric oxide synthase polymorphism (4 VNTR, G894T, and T786C)
testing for estimating risk of erectile dysfunction;
iron binding capacity;
prostatic acid phosphatase.
1. Testosterone testing - The following tests are not covered:
testing for serum free testosterone and/or bioavailable testosterone as primary testing
(i.e., in the absence of prior serum TOTAL testosterone testing);
testing for serum total testosterone, free testosterone, and/or bioavailable testosterone
in asymptomatic individuals or in individuals with non-specific symptoms;
testing for serum testosterone for the identification of androgen deficiency in women;
salivary testing for testosterone;
measurement of serum dihydrotestosterone in individuals except in diagnosing 5-
alpha reductase deficiency in individuals with ambiguous genitalia, hypospadias, or
microphallus.
m. Thyroid Disease Testing is not covered in the following situations:
Testing for thyrotropin-releasing hormone (TRH) or thyroxine-binding globulin
(TBG) for the evaluation of the cause of hyperthyroidism or hypothyroidism is not
covered
Testing for thyroid dysfunction during a general exam without abnormal findings for
asymptomatic nonpregnant individuals is not covered
n. Onychomycosis Testing is not covered in the following situations:
Nucleic acid testing, attenuated total-reflectance fourier transform infrared (ATR-
FTIR) spectroscopy and testing for the presence of fungal-derived sterols (e.g.,
ergosterol) to screen for, diagnose, or confirm onychomycosis is not covered
TX-I-EX-H-CC-EOC-25
56
PHARMACY BENEFITS
Definitions
In addition to the applicable terms provided in the DEFINITIONS section of this Evidence of Coverage, the following
terms will apply specifically to this PHARMACY BENEFITS section.
Allowable Amount means the maximum amount determined by HMO to be eligible for consideration of payment
for a particular Covered Drug. As applied to Participating Pharmacies the Allowable Amount is based on the
provisions of the contract between HMO and the Participating Pharmacy in effect on the date of service. As applied
to Prescription Drugs Purchased Outside of the Service Area, the Allowable Amount is based on the
Participating Pharmacy contract rate.
Brand Name Drug means a drug or product manufactured by a single manufacturer as defined by a nationally
recognized Provider of drug product database information. There may be some cases where two manufacturers will
produce the same product under one license, known as a co-licensed product, which would also be considered as a
Brand Name Drug. There may also be situations where a drug's classification changes from generic to brand name
due to a change in the market resulting in the generic being a single source, or the drug product database information
changing, which would also result in a corresponding change in Copayment/Coinsurance obligations from generic
to brand name.
Brand Name Drug (Non-Preferred) means a Brand Name Drug which appears on the applicable Drug List as
Non-Preferred Brand Name Drug. The Drug List is available by accessing the website at www.bcbstx.com/rx-
drugs/drug-lists/drug-lists.
Brand Name Drug (Preferred) means a Brand Name Drug which appears on the applicable Drug List as Preferred
Brand Name Drug. The Drug List is available by accessing the website at www.bcbstx.com/rx-drugs/drug-
lists/drug-lists.
Coinsurance means the percentage amount paid by the Member for each Prescription Order filled or refilled
through a Participating Pharmacy.
Copayment or Copay means the dollar amount paid by the Member for each Prescription Order filled or refilled
through a Participating Pharmacy.
Covered Drug(s) means any Legend Drug:
1.
which is included on the applicable Drug List;
2. which is Medically Necessary and is ordered by an authorized Health Care Practitioner naming a Member
as the recipient;
3. for which a written or verbal Prescription Order is provided by an authorized Health Care Practitioner;
4. for which a separate charge is customarily made;
5. which is not consumed at the time and place that the Prescription Order is written;
6. for which the U.S. Food and Drug Administration (FDA) has given approval for at least one indication; and
7. which is dispensed by a Participating Pharmacy and is received by the Member while covered under this
Evidence of Coverage, except when received from a Provider's office, or during confinement while a patient
in a Hospital or other acute care institution or facility (refer to Limitations and Exclusions).
NOTE: Covered Drug(s) under Your Pharmacy Benefits also means insulin, insulin analogs, insulin pens, and
prescriptive and non-prescriptive oral agents for controlling blood sugar levels, including disposable syringes and
needles needed for self-administration.
Drug List means a list of all drugs that may be covered under Your Pharmacy Benefits. The Drug List is available
by accessing the website at www.bcbstx.com/rx-drugs/drug-lists/drug-lists.You may also contact customer service
at the toll-free number on Your identification card for more information.
Generic Drug means a drug that has the same active ingredient as the Brand Name Drug and is allowed to be
produced after the Brand Name Drug's patent has expired. In determining the brand or generic classification for
Covered Drugs, HMO utilizes the generic/brand status assigned by a nationally recognized Provider of drug product
database information. You should know that not all drugs identified as "generic" by the drug product database,
TX-I-EX-H-CC-EOC-25
57
PHARMACY BENEFITS
manufacturer, Pharmacy, or Your Physician will adjudicate as generic by HMO. Generic Drugs are shown on the
Drug List which is available by accessing the website at www.bcbstx.com/rx-drugs/drug-lists/drug-lists.or You
may contact customer service at the toll-free number on Your identification card.
Generic Drug (Non-Preferred) means a Generic Drug which appears on the applicable Drug List as Non-Preferred
Generic Drug. The Drug List is available by accessing the website at www.bcbstx.com/rx-drugs/drug-lists/drug-
lists.
Generic Drug (Preferred) means a Generic Drug which appears on the applicable Drug List as Preferred Generic
Drug. The Drug List is available by accessing the website at www.bcbstx.com/rx-drugs/drug-lists/drug-lists.
Health Care Practitioner means an Advanced Practice Nurse, doctor of medicine, doctor of dentistry, Physician
Assistant, doctor of osteopathy, doctor of podiatry, or other licensed person with prescription authority.
Legend Drug means a drug, biological, or compounded prescription which is required by law to have a label stating
"Caution - Federal Law Prohibits Dispensing Without a Prescription," and which is approved by the FDA for a
particular use or purpose.
Participating Pharmacy means an independent retail Pharmacy, or chain of retail Pharmacies, or mail-order
program Pharmacy, or a Specialty Pharmacy Provider which have entered into a written agreement with HMO to
provide pharmaceutical services to Members under this Evidence of Coverage.
Pharmacy means a state and federally licensed establishment where the practice of pharmacy occurs, that is
physically separate and apart from any Provider's office, and where Legend Drugs and devices are dispensed under
Prescription Orders to the general public by a pharmacist licensed to dispense such drugs and devices under the
laws of the state in which he practices.
Pharmacy Vaccine Network means the network of Participating Pharmacies which have entered into a written
agreement with HMO to provide certain vaccinations to Members under this Evidence of Coverage.
Preferred Participating Pharmacy means a Participating Pharmacy which has a written agreement with HMO to
provide pharmaceutical services to Members or an entity chosen by HMO to administer its prescriptions drug
program that has been designated as a Preferred Participating Pharmacy.
Prescription Order means a written or verbal order from Your authorized Health Care Practitioner to a pharmacist
for a drug or device to be dispensed.
Specialty Drugs means a high cost prescription drug that meets any of the following criteria:
1.
used in limited patient populations or indications;
2.
typically self-injected;
3.
limited availability, requires special dispensing, or delivery and/or patient support is required and therefore,
they are difficult to obtain via traditional Pharmacy channels; and/or
4.
complex reimbursement procedures are required.
To determine which drugs are Specialty Drugs, refer to the Drug List which is available by accessing the website
at www.bcbstx.com/rx-drugs/drug-lists/drug-lists.
Specialty Drug (Non-Preferred) means a Specialty Drug which appears on the applicable Drug List as Non-
Preferred Specialty Drug. The Drug List is available by accessing the website
at
www.bcbstx.com/member/prescription-drug-plan-information/drug-lists.
Specialty Drug (Preferred) means a Specialty Drug which appears on the applicable Drug List as Preferred
Specialty Drug. The Drug List is available by accessing the website at www.bcbstx.com/member/prescription-drug-
plan-information/drug-lists.
Specialty Pharmacy Provider means a Participating Pharmacy which has entered into a written agreement with
HMO to provide Specialty Drugs to Members under this Evidence of Coverage.
TX-I-EX-H-CC-EOC-25
58
PHARMACY BENEFITS
Covered Drugs
Benefits for Medically Necessary Covered Drugs prescribed to treat You for a chronic, disabling, or life-threatening
illness covered by HMO are available if the drug is on the applicable Drug List and has been approved by the United
States Food and Drug Administration (FDA) for at least one indication and is recognized by the following for
treatment of the indication for which the drug is prescribed:
a prescription drug reference compendium approved by the Texas Department of Insurance; or
substantially accepted peer-reviewed medical literature.
For a list of Covered Drugs, You can access the website at www.bcbstx.com/rx-drugs/drug-lists/drug-lists or You
can also contact customer service at the toll-free number on Your identification card.
You are responsible for any Copayment/Coinsurance and any Deductible for Covered Drugs shown in the
SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS and pricing differences that may apply to the Covered Drug
dispensed.
Injectable Drugs. Injectable drugs approved by the FDA for self-administration are covered. Benefits will not be
provided under PHARMACY BENEFITS for any self-administered drugs dispensed by a Physician.
Diabetes Supplies for Diabetes Care. Insulin, insulin analogs, insulin pens, insulin syringes, needles, injection
devices, glucagon emergency kits, lancets, lancet devices, glucose meter solution, test strips specified for use with
a corresponding blood glucose monitor, visual reading strips and urine and blood testing strips, and tablets which
test for glucose, ketones, and protein, and prescriptive and nonprescriptive oral agents for controlling blood sugar
levels are covered.
A separate Copayment/Coinsurance and any Deductible will apply to each fill of a prescription purchased on the
same day for insulin and insulin syringes.
All supplies, including medications and equipment for the control of diabetes will be dispensed as written, unless
substitution is approved by Your prescribing Physician or other Health Care Practitioner who issues the written
order for the supplies or equipment.
Emergency Refills of Insulin or Insulin-Related Equipment and Supplies
A pharmacist may exercise their professional judgement in refilling a Prescription Order for Insulin or Insulin-
Related Equipment or Supplies without the authorization of the prescribing Health Care Practitioner in the following
situations:
the pharmacist is unable to contact Your Health Care Practitioner after reasonable effort;
the pharmacist has documentation showing the patient was previously prescribed insulin or insulin-related
equipment or supplies by a Health Care Practitioner; and
the pharmacist assesses the patient to determine whether the emergency refill is appropriate.
The quantity of an emergency refill will be the smallest available package and will not exceed a 30-day supply.
In addition to the applicable terms provided in the DEFINITIONS section of the Certificate, the following terms
will apply specifically to this provision:
Insulin means an insulin analog and an insulin-like medication, regardless of the activation period or whether
the solution is mixed before the prescription is dispensed.
Insulin-Related Equipment or Supplies means needles, syringes, cartridge systems, prefilled pen systems,
glucose meters, continuous glucose monitor supplies, and text strips but does not include insulin pumps.
You are responsible for the same Copayment and any pricing differences that may apply to the items dispensed in
the same manner as for nonemergency refills of diabetes equipment or supplies.
Insulin Drug Program
The total amount You may pay for a Covered Drug that contains insulin and is used to treat diabetes will not exceed
the amount shown on Your SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS, up to a 30-day supply, regardless
TX-I-EX-H-CC-EOC-25
59
PHARMACY BENEFITS
of the amount or type of insulin needed to fill the Prescription Order. The preferred insulin drugs are identified on
Your Drug List and does not include an insulin drug administered intravenously.
Insulin drugs obtained from a non-Participating Pharmacy or not identified as a Preferred insulin drug may be
subject to Copayment amount Coinsurance amount, Deductibles or dollar maximums, if applicable.
Exceptions will not be made for drugs not identified as a Preferred insulin drug or for an excluded drug.
Preventive Care. Prescription and over-the-counter drugs which have in effect a rating of "A" or "B" in the current
recommendations of the United States Preventive Services Task Force ("USPSTF") (to be implemented in the
quantities and within the time period allowed under applicable law) or as required by state law will be covered and
will not be subject to any Copayment Coinsurance, Deductibles or dollar maximums.
Select Vaccinations obtained through certain Participating Pharmacies. Benefits for select vaccinations are
shown in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS. These vaccinations are available through certain
Participating Pharmacies that have contracted with HMO to provide this service. To locate one of these Participating
Pharmacies in the Pharmacy Vaccine Network in Your area and to determine which vaccinations are covered under
this benefit, access the website at www.bcbstx.com or contact customer service at the toll-free number on Your
identification card.
Each Participating Pharmacy included in the Pharmacy Vaccine Network that has contracted with HMO to provide
this service may have age, scheduling, or other requirements that will apply, SO You are encouraged to contact them
in advance.
Formulas for the Treatment of Phenylketonuria or Other Heritable Diseases. Dietary formulas necessary for
the treatment of phenylketonuria or other heritable diseases are covered to the same extent as any other Covered
Drug available only on the orders of a Health Care Practitioner.
Amino Acid-Based Elemental Formulas. Formulas, regardless of the formula delivery method, used for the
diagnosis and treatment of:
immunoglobulin E and non-immunoglobulin E mediated allergies to multiple food proteins;
severe food protein-induced enterocolitis syndromes;
eosinophilic disorders, as evidenced by the results of biopsy; and
disorders affecting the absorptive surface, functional length, and motility of the gastrointestinal tract.
A Prescription Order from Your Health Care Practitioner is required.
Orally Administered Anticancer Medication. Benefits are available for Medically Necessary orally administered
anticancer medication that is used to kill or slow the growth of cancerous cells. Copayments/Coinsurance and any
Deductible will not apply to certain orally administered anticancer medications. To determine if a specific drug is
included in this benefit contact customer service at the toll-free number on Your identification card.
Specialty Drugs. Benefits are available for Specialty Drugs as described in Specialty Pharmacy Program.
Selecting a Pharmacy
When You need a Prescription Order filled, You should use a Participating Pharmacy. Each prescription or refill is
subject to the Copayment /Coinsurance and any Deductible shown in the SCHEDULE OF COPAYMENTS AND
BENEFIT LIMITS and any applicable pricing differences. You may be required to pay for limited or non-Covered
Services. No claim forms are required.
Although You can go to any Participating Pharmacy, Your benefits for drugs and other items covered under this
provision will be greater when You obtain them from a Preferred Participating Pharmacy. Your
Copayment/Coinsurance will be less when using a Preferred Participating Pharmacy.
If You are unsure whether a Pharmacy is a Participating Pharmacy, You may access the website at
www.bcbstx.com/rx-drugs/pharmacy/find-a-pharmacy or contact customer service at the toll-free number on Your
identification card. Preferred Participating Pharmacies will also be identified. You can also call customer service at
TX-I-EX-H-CC-EOC-25
60
PHARMACY BENEFITS
the toll-free telephone number on the back of Your identification card for information regarding Participating
Pharmacies and Preferred Participating Pharmacies.
Mail-Order Program. If You elect to use the mail-order service, You must mail Your Prescription Order to the
address provided on the mail-order prescription form and send in Your payment for each prescription filled or
refilled. Each prescription or refill is subject to the Copayment/Coinsurance and any Deductible shown in the
SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS and any applicable pricing differences, payable by Member
directly to the mail order Pharmacy.
Some drugs may not be available through the mail-order program. If You have any questions about this mail-order
program, need assistance in determining the amount of Your payment, or need to obtain the mail-order prescription
claim form, access the website at www.bcbstx.com or contact customer service at the toll-free number on Your
identification card. Mail the completed form, Your Prescription Order(s) and payment to the address indicated on
the form.
Specialty Pharmacy Program. The Specialty Drug delivery service integrates Specialty Drug benefits with the
Member's overall medical and prescription drug benefits. This program provides delivery of medications directly
from the Specialty Pharmacy Provider to Your Health Care Practitioner, administration location or to the Member
that is undergoing treatment for a complex Medical Condition.
The HMO Specialty Pharmacy Program delivery service offers:
coordination of coverage between You, Your Health Care Practitioner and HMO;
educational materials about the patient's particular condition and information about managing potential
medication side effects;
syringes, sharps containers, alcohol swabs and other supplies with every shipment for FDA approved self-
injectable medications; and
access to a pharmacist for urgent medication issues 24 hours a day, 7 days a week, 365 days each year.
The Drug List which includes these Specialty Drugs is available by accessing the website at www.bcbstx.com/rx-
drugs/drug-lists/drug-lists or by contacting customer service at the toll-free number on Your identification card.
Your cost will be the applicable Copayment/Coinsurance and any Deductible shown in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS as well as any applicable pricing differences.
Prescription Drugs Purchased Outside of the Service Area. HMO will reimburse You for the Allowable Amount
of the prescription drugs less the Out-of-Area Drug Copayment/Coinsurance shown in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS, for covered prescription drugs which You purchase outside of the Service
Area. You must submit a completed claim form to HMO within ninety (90) days of the date of purchase to qualify
for reimbursement under the PHARMACY BENEFITS. You may access the website at
www.bcbstx.com/member/forms/formfinder to obtain a prescription drug claim form. Any Deductible shown in the
SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS will also apply
Meds Your Way
MedsYour Way1 ("MedsYourWay") may lower Your out-of-pocket costs for select covered drugs purchased at
select in-network retail pharmacies. Meds Your Way is a program that automatically compares available drug
discount card prices and prices under Your benefit plan for select covered drugs and establishes Your out-of-pocket
cost to the lower price available. At the time You submit or pick up Your prescription, present Your BCBSTX
identification card to the pharmacist. This will identify You as a participant in Meds Way and allow You the
lower price available for select covered drugs.
The amount You pay for Your prescription will be applied, if applicable, to Your Deductible and out-of-pocket
maximum. Available select covered drugs and drug discount card pricing through Meds Way may change
occasionally. Certain restrictions may apply and certain covered drugs or drug discount cards may not be available
for the Meds Your Way program. You may experience a different out-of-pocket amount for select Covered Drugs
depending upon which retail pharmacy is utilized. For additional information regarding MedsYourWay, please
contact a customer service representative at the toll-free telephone number on the back of Your identification card.
TX-I-EX-H-CC-EOC-25
61
PHARMACY BENEFITS
Participation in MedsYour Way is not mandatory and You may choose not to participate in the program at any time
by contacting Your customer service representative at the toll-free telephone number on the back of Your
identification card. In the event Meds Your Way fails to provide, or continue to provide, the program as stated, there
will be no impact to You. In such an event, You will pay the plan's pharmacy benefit Copay.
Your Cost
How Copayment/Coinsurance Amounts Apply. If the Allowable Amount of the drug is less than the
Copayment/Coinsurance, You pay the lower cost. When that lower cost is more than the amount You would pay if
You purchased the drug without using Your HMO pharmacy benefits or any other source of drug benefits or
discounts, You pay such purchase price.
You will pay no more than the applicable Brand Name Drug Copayment/Coinsurance if the prescription has no
generic equivalent. If You receive a Brand Name Drug when a generic equivalent is available, the
Copayment/Coinsurance will be the total of the Generic Drug Copayment/Coinsurance plus the difference between
the cost of the Generic Drug equivalent and the cost of the Brand Name Drug. You will also be responsible for any
Deductible that may apply. Exceptions to this may be allowed for certain preventive medications (including
prescription contraceptive medications) if Your Health Care Practitioner submits a request to HMO indicating that
the Generic Drug would be medically inappropriate, along with supporting documentation. If HMO grants the
exception request, any difference between the Allowable Amount for the Brand Name Drug and the Generic Drug
equivalent will be waived.
You may not be required to pay the difference in cost between the Allowable Amount of the Brand Name Drug and
the Allowable Amount of the Generic Drug if there is a medical reason (e.g., adverse event) You need to take the
Brand Name Drug and certain criteria are met. Your Health Care Practitioner can submit a request to waive the
difference in cost between the Allowable Amount of the Brand Name Drug and Allowable Amount of the Generic
Drug. In order for this request to be reviewed, Your Health Care Practitioner must send in a MedWatch form to the
Food and Drug Administration (FDA) to let them know the issues You experienced with the generic equivalent.
Your Health Care Practitioner must provide a copy of this form when requesting the waiver. The FDA MedWatcl
form is used to document adverse events, therapeutic inequivalence/failure, product quality problems, and product
use/medication error. This form is available on the FDA website. If the waiver is granted, applicable
Copayment/Coinsurance and any Deductible will still apply. For additional information, You may access the
website at www.bcbstx.com or contact customer service at the toll-free number on Your identification card.
Deductible. The Deductible per Calendar Year for each Member is shown in the SCHEDULE OF COPAYMENTS
AND
BENEFIT LIMITS. This is the dollar amount that each Member must pay during a Calendar Year before benefits are
available. This Deductible will be applied to each covered Prescription Order filled or refilled until it is satisfied
and will be based on the Allowable Amount of the drugs. After the Deductible is met, You will only pay the
appropriate Copayment/Coinsurance for Covered Drugs and any pricing difference that may apply.
How Member Payment is Determined. Prescription drug products are separated into tiers. Generally, each drug
is placed into one of six drug tiers:
Tier 1 - includes mostly Generic Drugs (Preferred) and may contain some Brand Name Drugs.
Tier 2 - includes mostly Generic Drugs (Non-Preferred) and may contain some Brand Name Drugs.
Tier 3 - includes mostly Brand Name Drugs (Preferred) and may contain some Generic Drugs.
Tier 4 - includes mostly Brand Name Drugs (Non-Preferred) and may contain some Generic Drugs.
Tier 5 - includes mostly Specialty Drugs (Preferred) and may contain some Generic Drugs.
Tier 6 - includes mostly Specialty Drugs (Non-Preferred) and may contain some Generic Drugs.
Copayments/Coinsurance and any Deductible for Covered Drugs on each drug tier is shown in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS. To determine the tier in which a drug is included, access the website at
TX-I-EX-H-CC-EOC-25
62
PHARMACY BENEFITS
www.bcbstx.com/rx-drugs/drug-lists/drug-lists. or by contacting customer service at the toll-free number on Your
identification card.
If a Covered Drug was paid for using any third-party payments, financial assistance, discount, product voucher, or
other reduction in out-of-pocket expenses made by You or on Your behalf, that amount will be applied to Your cost-
sharing requirements (including deductible, copayment, or out-of-pocket maximum).
About Your Benefits
Covered Drug List. Drugs listed on the Drug List are selected by HMO based upon the recommendations of a
committee, which is made up of current and previously practicing Physicians and pharmacists from across the
country, some of whom are employed by or affiliated with HMO. The committee considers existing drugs approved
by the FDA, as well as those newly FDA approved for inclusion on the Drug List. Entire drug classes are also
regularly reviewed. Some of the factors committee members evaluate include each drug's safety, effectiveness, cost
and how it compares with drugs currently on the Drug List.
Positive changes (e.g., adding drugs to the Drug List, drugs moving to a lower payment tier) occur quarterly after
review by the committee. Changes to the Drug List that could have an adverse impact to You (e.g., drug exclusion,
drug moving to a higher payment tier, or drugs requiring step therapy or Prior Authorization) only occur annually
upon coverage renewal, consistent with Texas Insurance Code 1369.0541 and 1369.055.
The Drug List and any modifications will be made available to You. By accessing the Blue Cross and Blue Shield
website at www.bcbstx.com/rx-drugs/drug-lists/drug-lists or calling the customer service toll-free number on Your
identification card, You will be able to determine the Drug List that applies to You and whether a particular drug is
on the Drug List. BCBSTX may uniformly modify drug coverage under the plan at the time of coverage renewal
upon at least 60 days written notice as required by applicable law.
Drug List Exception Requests. You, or Your prescribing Physician or other Health Care Practitioner with
prescriptive authority, can ask for a Drug List exception if Your drug is not on the Drug List (also known as a
formulary). To request this exception, You or Your prescribing Physician or other Health Care Practitioner can call
the number on the back of Your identification card to ask for a review. You may be required to submit a supporting
statement from Your prescribing Physician or other Health Care Practitioner.
If You have a health condition that may jeopardize Your life, health or Your ability to regain maximum function or
You are undergoing a current course of treatment using a drug that is not on the Drug List, an expedited review may
be requested. You or Your prescribing Physician or other Health Care Practitioner will be notified of the coverage
decision within 24 hours after the request for an expedited review is received. If Your request is granted, coverage
will be provided for the duration of the exigency.
For requests that do not meet the criteria for expedited review, a standard review will be completed and You or Your
prescribing Physician or other Health Care Practitioner will be notified of the coverage decision within 72 hours
after the request for a standard review is received. If Your request is granted, coverage will be provided for the
duration of the prescription, including refills.
If Your expedited or standard Drug List exception request is denied, the decision notice will include information
explaining Your right to request review by an Independent Review Organization (IRO). You and Your prescribing
Physician or other Health Care Practitioner will be notified of the IRO's decision within 24 hours for an expedited
review and within 72 hours for a standard review. If Your expedited exception request is granted, coverage will be
provided for the duration of the exigency. If Your standard exception is granted, coverage will be provided for the
duration of the prescription, including refills.
Day Supply. Benefits for Covered Drugs obtained from a Participating Pharmacy are provided up to the maximum
day supply limit as shown in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS. HMO has the right to
determine the day supply. Payment for benefits covered by HMO may be denied if drugs are dispensed or delivered
in a manner intended to change, or having the effect of changing or circumventing, the stated maximum day supply
limitation.
Extended Prescription Drug Supply Program. Your coverage includes benefits for up to a 90-day supply of
covered maintenance type drugs purchased from a Participating Pharmacy (which may only include retail or mail
TX-I-EX-H-CC-EOC-25
63
PHARMACY BENEFITS
order Pharmacies). Each prescription or refill is subject to the Copayment/Coinsurance and any Deductible shown
in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS and any applicable pricing differences.
Benefits will not be provided for more than a 30-day supply of drugs purchased from a Pharmacy that is not a
Preferred Participating Pharmacy.
Prescription Refills. You may obtain prescription drug refills from any Participating Pharmacy. Once every 12
months, You will be able to synchronize the start time of certain Covered Drugs used for treatment and management
of a chronic illness SO they are refilled on the same schedule for a given time period. When necessary to fill a partial
Prescription Order to permit synchronization, HMO will prorate the Copayment due for Covered Drugs based on
the proportion of days the reduced Prescription Order covers to the regular day supply outlined in the SCHEDULE
OF COPAYMENTS AND BENEFIT LIMITS.
Covered prescription contraceptives may be obtained as follows:
An initial three-month supply at one time
Up to a 12-month supply at one time for subsequent refills
Maximum of 12-month supply during each 12-month period.
Refills for prescription eye drops to treat a chronic eye disease or condition will be refilled if (1) the original
Prescription Order states that additional quantities of the eye drops are needed; (2) the refill does not exceed the
total quantity of dosage units authorized by the prescribing Health Care Practitioner on the original Prescription
Order, including refills; and (3) the refill is dispensed on or before the last day of the prescribed dosage period. The
refills are allowed:
not earlier than the 21st day after the date a Prescription Order for a 30-day supply is dispensed; or
not earlier than the 42nd day after the date a Prescription Order for a 60-day supply is dispensed; or
not earlier than the 63rd day after the date a Prescription Order for a 90-day supply is dispensed.
Dispensing Limits. Dispensing limits are based upon FDA dosing recommendations and nationally recognized
guidelines. Coverage limits are placed on medications in certain drug categories. Limits may include: quantity of
covered medication per prescription, quantity of covered medication in a given time period, coverage only for
Members within a certain age range, or coverage only for Members of a specific gender. Quantities of some drugs
are restricted regardless of the quantity ordered by the Health Care Practitioner. To determine if a specific drug is
subject to this limitation, You may access the website at www.bcbstx.com or contact customer service at the toll-
free number on Your identification card.
If You require a Prescription Order in excess of the dispensing limit established by HMO, ask Your Health Care
Practitioner to submit a request for clinical review on Your behalf. The Health Care Practitioner can obtain an
override request form by accessing our website at www.bcbstx.com/Provider. Any pertinent medical information
along with the completed form should be faxed to Clinical Pharmacy Programs at the fax number indicated on the
form. The request will be approved or denied after evaluation of the submitted clinical information. HMO has the
right to determine dispensing limits at its sole discretion. Payment for benefits covered by HMO may be denied if
drugs are dispensed or delivered in a manner intended to change, or having the effect of changing or circumventing,
the stated maximum quantity limitation.
Multi-Category Split Fill Program. If this is Your first time using select medications in certain drug classes (e.g.,
medications for cancer, multiple sclerosis, lung disorders, etc.) or if You have not filled one of these medications
within 120 days, You may only be able to receive a partial fill (14-15 day supply) of the medication for up to the
first 3 months of therapy. This is to help see how the medication is working for You. If You receive a partial fill,
Your Copayments and/or Coinsurance will be adjusted to align with the quantity of medication dispensed. If the
medication is working for You and Your Physician wants You to continue on this medication, You may be eligible
to receive up to a 30-day supply after completing up to 3 months of the partial supply. For a list of drugs that are
included in this program, please visit the www.bcbstx.com/rx-drugs/pharmacy/pharmacy-programs website.
Controlled Substance Limits. In the event HMO determines that a Member may be receiving quantities of a
Controlled Substance not supported by FDA approved dosages or recognized safety or treatment guidelines, any
TX-I-EX-H-CC-EOC-25
64
PHARMACY BENEFITS
additional drugs may be subject to a review for medical necessity, appropriateness and other coverage restrictions
which may include but not be limited to services provided by a certain Provider and/or Pharmacy for the prescribing
and dispensing of the Controlled Substance and/or limiting coverage to certain quantities. Additional
Copayment/Coinsurance and any Deductible may apply.
Step Therapy. Coverage for certain prescription drugs or drug classes is subject to a step therapy program. Step
therapy programs favor the use of clinically acceptable alternative medications that may be less costly for You prior
to those medications on the step therapy list of drugs being covered under HMO.
When You submit a Prescription Order to a Participating Pharmacy for one of these designated medications, the
pharmacist will be alerted if the online review of Your prescription claims history indicates an acceptable alternative
medication has not been previously tried. A list of step therapy medications is available to You and Your Health
Care Practitioner on our website at www.bcbstx.com/rx-drugs/pharmacy/pharmacy-programs or contact customer
service at the toll-free number on Your identification card.
If it is Medically Necessary, coverage can be obtained for the prescription drugs or drug classes subject to the step
therapy program without trying an alternative medication first. In this case, Your Health Care Practitioner must
contact HMO to obtain Prior Authorization for coverage of such drug. If authorization is granted, the Health Care
Practitioner will be notified and the medication will then be covered at the applicable Copayment/Coinsurance and
after any Deductible.
Although You may currently be on a drug that is part of the step therapy program, Your Claim may need to be
reviewed to see if the criteria for coverage of further treatment has been met. A documented treatment with a generic
or brand therapeutic alternative medication may be required for continued coverage of the Brand Name Drug.
Step therapy programs do not apply to prescription drug treatment for the treatment of Stage-Four Advanced,
Metastatic Cancer or Associated Conditions. Coverage for prescription drug treatment for Stage-Four Advanced,
Metastatic Cancer or Associated Conditions do not require You to fail to successfully respond to a different drug or
provide a history of failure of a different drug, before providing coverage of a prescription drug. This applies only
to a prescription drug treatment that is consistent with best practices for the treatment of Stage-Four Advanced,
Metastatic Cancer or an Associated Condition; supported by peer-reviewed, evidence-based literature; and
approved by the United States Food and Drug Administration.
In addition to the DEFINITIONS of this Evidence of Coverage, the following definitions are applicable to this
provision:
1.
"Stage-Four Advanced, Metastatic Cancer" means a cancer that has spread from the primary or original
site of the cancer to nearby tissues, lymph nodes, or other areas or parts of the body.
2.
"Associated Conditions" means the symptoms or side effects associated with Stage-Four Advanced,
Metastatic Cancer or its treatment and which, in the judgment of the Health Care Practitioner, further
jeopardize the health of a patient if left untreated.
For treatment of Serious Mental Illness for Members 18 years or older, for Covered Drugs approved by the FDA
will not require that the Member
1.
fail to successfully respond to more than one different drug for each drug prescribed, excluding the generic
or pharmaceutical equivalent of the prescribed drug; or
2.
prove a history of failure of more than one different drug for each drug prescribed, excluding the generic
or pharmaceutical equivalent of the prescribed.
Step Therapy may be required for a trial of a generic or pharmaceutical equivalent of a prescribed prescription drug
as a condition of continued coverage of the prescribed drug only:
1.
once in a plan year; and
2.
if the generic or equivalent drug is added to the plan's Drug List.
Step Therapy Exception Requests: Your prescribing Physician or other Health Care Practitioner may submit a
written request for an exception to the Step Therapy requirements. The Step Therapy Exception Request will be
considered approved if we do not deny the request within 72 hours after receipt of the request. If Your prescribing
Physician or other Health Care Practitioner reasonably believes that denial of the Step Therapy Exception Request
TX-I-EX-H-CC-EOC-25
65
PHARMACY BENEFITS
could cause You serious harm or death, submission of the request with Urgent noted and documenting these
concerns will be considered approved if we do not deny the request within 24 hours after receipt of the request. If
Your Step Therapy Exception Request is denied, You have the right to request an expedited internal appeal and also
have the right to request review by an Independent Review Organization as explained in the COMPLAINT AND
APPEAL PROCEDURES section of this Evidence of Coverage.
Prior Authorization. Coverage for certain designated prescription drugs is subject to Prior Authorization criteria.
This means that in order to ensure that a drug is safe, effective, and part of a specific treatment plan, certain
medications may require Prior Authorization and the evaluation of additional clinical information before dispensing.
You and Your Health Care Practitioner may access a list of the medications which require Prior Authorization by
accessing the website at www.bcbstx.com/rx-drugs/pharmacy/pharmacy-programs or contact customer service at
the toll-free number on Your identification card.
When You submit a Prescription Order to a Participating Pharmacy for one of these designated medications, the
pharmacist will be alerted online if Your Prescription Order is on the list of medications which require Prior
Authorization before it can be filled. If this occurs, Your Health Care Practitioner will be required to submit an
authorization form. This form may also be submitted by Your Health Care Practitioner in advance of the request to
the Pharmacy. The Health Care Practitioner can obtain the authorization form by accessing our website at
www.bcbstx.com/Provider. The requested medication may be approved or denied for coverage by HMO based upon
its accordance with established clinical criteria.
Prior Authorization will not be required more than once annually for Covered Drugs used to treat an autoimmune
disease, hemophilia or Von Willebrand disease, except for:
1.
opioids, benzodiazepines, barbiturates, or carisoprodol;
2.
prescription drugs that have a typical treatment period of less than 12 months;
3. drugs that:
a.
have an FDA boxed warning for use; and
b.
must have specific provider assessment; or
4.
use in a manner other than the FDA approved use.
Right of Appeal. You have the right to appeal as explained in the COMPLAINT AND APPEAL PROCEDURES section
of this Evidence of Coverage.
Limitations and Exclusions
Pharmacy benefits are not available for:
1.
Drugs/products which are not included on the Drug List, unless specifically covered elsewhere in this
Evidence of Coverage and/or such coverage is required in accordance with applicable law or regulatory
guidance.
2.
Non-FDA approved drugs.
3.
Drugs which by law do not require a Prescription Order, except as indicated under Preventive Care in
PHARMACY BENEFITS, from an authorized Health Care Practitioner and Legend Drugs or covered devices
for which no valid Prescription Order is obtained. (Insulin, insulin analogs, insulin pens, prescriptive and
nonprescriptive oral agents for controlling blood sugar levels, and select vaccinations administered through
certain Participating Pharmacies shown in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS are
covered.)
4.
Prescription drugs if there is an over-the-counter product available with the same active ingredient(s) in
the same strength, unless otherwise determined by HMO.
5.
Drugs required by law to be labeled: "Caution - Limited by Federal Law to Investigational Use," or
Experimental drugs, even though a charge is made for the drugs.
6.
Drugs, that the use or intended use of would be illegal, unethical, imprudent, abusive, not Medically
Necessary, or otherwise improper.
TX-I-EX-H-CC-EOC-25
66
PHARMACY BENEFITS
7.
Drugs obtained by unauthorized, fraudulent, abusive, or improper use of the identification card.
8.
Drugs used or intended to be used in the treatment of a condition, sickness, disease, injury, or bodily
malfunction that is not covered under HMO, or for which benefits have been exhausted.
9.
Drugs injected, ingested, or applied in a Physician's office or during confinement while a patient in a
Hospital, or other acute care institution or facility, including take-home drugs; and drugs dispensed by a
nursing home or custodial or chronic care institution or facility.
10. Drugs for which the Pharmacy's usual retail price to the general public is less than or equal to the
Copayment.
11. Drugs purchased from a non-Participating Pharmacy in the Service Area, except as provided in the
Clinician-Administered Drugs section in COVERED SERVICES AND BENEFITS.
12. Devices, technologies, and/or Durable Medical Equipment (DME) such as but not limited to therapeutic
devices, including support garments and other non-medicinal substances, digital health technologies and/or
applications, even though such devices may require a Prescription Order. (Disposable hypodermic needles,
syringes for self-administered injections and contraceptive devices are covered). However, You do have
certain DME benefits available under the Durable Medical Equipment section in COVERED SERVICES
AND BENEFITS. Coverage for female contraceptive devices and the rental (or, at HMO's option the
purchase) of manual or electric breast pumps is provided as indicated under the Health Maintenance and
Preventives Services section in COVERED SERVICES AND BENEFITS.
13. Pharmaceutical aids such as excipients found in the USP-NF (United States Pharmacopeia - National
Formulary), including but not limited to preservatives, solvents, ointment bases, and flavoring, coloring,
diluting, emulsifying, and suspending agents.
14. Male contraceptive devices, including over-the-counter contraceptive products such as condoms; female
contraceptive devices, including over-the-counter contraceptive products such as spermicide when not
prescribed by a Participating Provider.
15. Any special services provided by a Pharmacy, including but not limited to counseling and delivery. Select
vaccinations shown in the SCHEDULE OF COPAYMENTS AND BENEFIT LIMITS administered through
certain Participating Pharmacies are an exception to this exclusion.
16. Drugs dispensed in quantities in excess of the day supply amounts indicated in the SCHEDULE OF
COPAYMENTS AND BENEFIT LIMITS or refills of any prescriptions in excess of the number of refills
specified by the authorized Health Care Practitioner or by law, or any drugs or medicines dispensed more
than one (1) year after the Prescription Order date.
17. Administration or injection of any drugs.
18. Injectable drugs except self-administered Specialty Drugs or those approved by the FDA for self-
administration.
19. Non-commercially available compounded medications, regardless of whether or not one or more
ingredients in the compound requires a Prescription Order. (Non-commercially available compounded
medications are those made by mixing or reconstituting ingredients in a manner or ratio that is inconsistent
with United States Food and Drug Administration-approved indications provided by the ingredients'
manufacturers.)
20. Fluids, solutions, nutrients or medications (including all additives and chemotherapy) used or intended to
be used by intravenous or intramuscular injection (unless approved by the FDA for self-administration),
intrathecal, intraarticular injection or gastrointestinal (enteral) infusion in the home setting.
21. Vitamins (except those vitamins which by law require a Prescription Order and for which there is no non-
prescription alternative or as indicated under Preventive Care in PHARMACY BENEFITS).
22. Allergy serum and allergy testing materials. However, You do have certain benefits available under Allergy
Care in COVERED SERVICES AND BENEFITS.
TX-I-EX-H-CC-EOC-25
67
PHARMACY BENEFITS
23. Athletic performance enhancement drugs.
24. Rogaine, minoxidil or any other drugs, medications, solutions or preparations used or intended for use in
the treatment of hair loss, hair thinning or any related condition, whether to facilitate or promote hair
growth, to replace lost hair, or otherwise.
25. Any prescription antiseptic or fluoride mouthwashes, mouth rinses or topical oral solutions or preparations.
26. Fluoride supplements except as required by law.
27.
Cosmetic drugs used primarily to enhance appearance, including, but not limited to, correction of skin
wrinkles and skin aging.
28. Drugs prescribed and dispensed for the treatment of obesity or for use in any program of weight reduction,
weight loss or dietary control.
29. Drugs to treat sexual dysfunction including but not limited to sildenafil citrate, phentolamine,
apomorphine, and alprostadil in oral and topical form.
30. Drugs for the treatment of Infertility (oral and injectable).
31. Prescription Orders which do not meet the required step therapy criteria.
32. Prescription Orders which do not meet the required Prior Authorization criteria.
33. Replacement of drugs or other items that have been lost, stolen, destroyed or misplaced.
34. Shipping, handling or delivery charges.
35. Certain drug classes where there is an over-the-counter alternative available.
36. Prescription Orders written by a member of Your immediate family, or a self-prescribed Prescription Order.
37. Institutional packs and drugs which are repackaged by anyone other than the original manufacturer.
38. Drugs determined by HMO to have inferior efficacy or significant safety issues.
39. Bulk powders.
40. Diagnostic agents. This exclusion does not apply to diabetic test strips.
41. Self-administered drugs dispensed or administered by a Physician in his/her office.
42. Drugs that are not considered Medically Necessary or treatment recommendations that are not supported
by evidence-based guidelines or clinical practice guidelines.
43. Some drugs have therapeutic equivalents/therapeutic alternatives. In some cases, Blue Cross and Blue
Shield may limit benefits to only certain therapeutic equivalents/therapeutic alternatives. If You do not
choose the therapeutic equivalents/therapeutic alternatives that are covered under Your benefit, the drug
purchased will not be covered under any Benefit level.
TX-I-EX-H-CC-EOC-25
68
GENERAL PROVISIONS
Termination of Coverage
If this Evidence of Coverage is terminated for nonpayment of Premium, Your coverage shall be terminated effective
after the last day of the grace period. In the event You are receiving a Premium Tax Credit, You have a three-month
grace period, or such other grace period, if any, permitted by applicable law or regulatory guidance. Only Members
for whom the stipulated payment is actually received by HMO shall be entitled to health services covered hereunder
and then only for the Contract Month for which such payment is received. If any required payment is not received
by the Premium due date, then You shall be terminated at the end of the grace period. You shall be responsible for
the cost of services rendered to You during the grace period in the event that Premium payments are not made by
You. Refer to HOW THE PLAN WORKS for additional information regarding grace periods.
If Your coverage is terminated, Premium payments received on Your account applicable to periods after the effective
date of termination shall be refunded to You within thirty (30) days, and neither HMO nor Participating Providers
shall have any further liability under this Evidence of Coverage. Any claims for refunds by You must be made
within sixty (60) days from the effective day of termination of Your coverage or otherwise such claims shall
be
deemed waived.
Non-Renewal of All Coverage
HMO may not renew this Evidence of Coverage if HMO elects to discontinue this type of coverage issued hereunder
in the Service Area, but only if coverage is discontinued uniformly without regard to the health status related factors
of a covered individual. HMO may cancel coverage after ninety (90) days prior written notice of termination, or
such other notice, if any, permitted by applicable law or regulatory guidance. HMO must offer each Member on a
guaranteed issue basis the option to purchase any other individual coverage offered by the HMO in the same Service
Area.
HMO may elect to discontinue all individual HMO contracts issued in the Service Area, but only if coverage is
discontinued uniformly without regard to the health status related factors of a covered individual. HMO may cancel
coverage after one hundred eighty (180) days prior written notice of termination, or such other notice, if any,
permitted by applicable law or regulatory guidance.
Member Termination in a Qualified Health Plan
If Your coverage in this QHP is terminated by HMO, You will be provided with a written notice of termination of
coverage, or such other notice, if any, permitted by applicable law or regulatory guidance that includes the reason
for termination. HMO will also notify the Exchange of the termination.
You and Your covered Dependent's coverage will be terminated due to the following events and will end on the
dates specified below:
1. You terminate Your coverage in this QHP, including as a result of Your obtaining other Minimum Essential
Coverage, with reasonable, appropriate notice to the Exchange and HMO. For the purposes of this section,
reasonable notice is defined as 14 days from the requested effective date of termination.
The last day of coverage will be:
the termination date specified by You, if You provide reasonable notice;
14 days after the termination is requested by You, if You do not provide reasonable notice; or
on a date determined by HMO, if HMO is able to effectuate termination in fewer than 14 days and
You request an earlier termination effective date.
2. When You are no longer eligible for QHP coverage through the Exchange. The last day of coverage is the
last day of the month following the month in which the notice is sent by the Exchange unless You request an
earlier termination effective date.
3. When HMO does not receive the Premium payment on time (Refer to HOW THE PLAN WORKS; Premium
Payments for additional information).
4. Your coverage has been rescinded.
TX-I-EX-H-CC-EOC-25
69
GENERAL PROVISIONS
5. You change from one QHP to another during an annual Open Enrollment Period or special enrollment period.
The last day of coverage in Your prior QHP is the day before the Effective Date of Coverage in Your new
QHP.
6. Events otherwise provided for under federal or state law or as Exchange rules may dictate.
Member Termination by HMO
HMO may terminate this Evidence of Coverage for a Member in the case of:
Cause
Effective Date of Termination
(1) Fraud or intentional misrepresentation of a
After fifteen (15) days written notice
material fact, except as described in
Incontestability of this Evidence of
Coverage
(2) Fraud in the use of services or facilities
After fifteen (15) days written notice
(3) Failure to meet eligibility requirements
Immediately
(4) A Member not residing, living or working in
After thirty (30) days written notice, except for a
the Service Area of the HMO, but only if
child who is subject of a medical support order
coverage is terminated uniformly without
and cannot be terminated solely because the child
regard to any health status-related factor of
does not reside, live or work in the Service Area
the Member.
In the event that there is a conflict between Member Termination in a Qualified Health Plan and Member
Termination by HMO sections above, the provision that is most favorable to the Member will apply.
Renewal of Member Coverage.
HMO will renew Your Evidence of Coverage unless You were terminated under Termination of Coverage;
Member Termination by HMO.
Continuation of Coverage
If a covered person's coverage terminates due to a change in marital status You may be issued coverage that most
nearly approximates the coverage of the Evidence of Coverage which was in effect prior to the change in marital
status without furnishing evidence of insurability. In order to convert, You must continue to reside, live or work in
the Service Area, submit a completed application within thirty-one (31) days after the date of the change in
marital
status and submit Premium payments required under such Evidence of Coverage. The effective date of such
coverage shall be the Effective Date of Coverage under the prior Evidence of Coverage.
Reinstatement
In any case where termination resulted from failure to make timely payment of Premium, the subsequent acceptance
of such Premium payments by HMO or our duly authorized agents shall reinstate the coverage. For purposes of this
provision, mere receipt and/or negotiation of a late Premium payment does not constitute acceptance. The reinstated
Evidence of Coverage shall cover only loss resulting from injury as may be sustained after the date of reinstatement
and loss due to sickness as may begin more than ten days after such date. In all other respects, the Subscriber and
HMO shall have the same rights hereunder as they had under the Evidence of Coverage immediately before the due
date of the defaulted Premiums, including the right of the Subscriber to apply the period of time this Evidence of
Coverage was in effect immediately before the due date of the defaulted Premiums toward satisfaction of any
waiting periods for benefits, if any, subject to any provisions endorsed hereon or attached hereto in connection with
the reinstatement. Any Premium payments accepted in connection with a reinstatement shall be applied to a period
for which Premiums have not been previously paid, but not to any period more than 60 days prior to the date of
reinstatement.
TX-I-EX-H-CC-EOC-25
70
GENERAL PROVISIONS
Coordination of Benefits
Coordination of Benefits ("COB") applies when You have health care coverage through more than one Health Care
Plan. The order of benefit determination rules govern the order in which each Health Care Plan will pay a claim for
benefits. The Health Care Plan that pays first is called the primary plan. The primary plan must pay benefits in
accord with its policy terms without regard to the possibility that another plan may cover some expenses. The Health
Care Plan that pays after the primary plan is the secondary plan. The secondary plan may reduce the benefits it pays
SO that payments from all plans equal 100 percent of the total Allowable Expense.
For purposes of this Coordination of Benefits section only, the following words and phrases have the following
meanings:
Allowable Expense means a health care expense, including Deductibles, Coinsurance, and Copayments, that
is covered at least in part by any Health Care Plan covering the person for whom claim is made. When a Health
Care Plan (including this Health Care Plan) provides benefits in the form of services, the reasonable cash value
of each service rendered is considered to be both an Allowable Expense and a benefit paid. An expense that is
not covered by any plan covering the person is not an Allowable Expense. In addition, any expense that a health
care Provider or Physician by law or in accord with a contractual agreement is prohibited from charging a
covered person is not an Allowable Expense.
1.
The difference between the cost of a semi-private Hospital room and a private Hospital room is not an
Allowable Expense, unless one of the plans provides coverage for private Hospital room expenses.
2.
If a person is covered by two or more plans that do not have negotiated fees and compute their benefit
payments based on the usual and customary fees, Allowed Amounts, or relative value schedule
reimbursement methodology, or other similar reimbursement methodology, any amount in excess of
the highest reimbursement amount for a specific benefit is not an Allowable Expense.
3.
If a person is covered by two or more plans that provide benefits or services on the basis of negotiated
fees, an amount in excess of the highest of the negotiated fees is not an Allowable Expense.
4.
If a person is covered by one plan that does not have negotiated fees and that calculates its benefits or
services based on usual and customary fees, Allowed Amounts, relative value schedule reimbursement
methodology, or other similar reimbursement methodology, and another plan that provides its benefits
or services based on negotiated fees, the primary plan's payment arrangement must be the Allowable
Expense for all plans. However, if the health care Provider or Physician has contracted with the
secondary plan to provide the benefit or service for a specific negotiated fee or payment amount that
is different than the primary plan's payment arrangement and if the health care Provider's or
Physician's contract permits, the negotiated fee or payment must be the Allowable Expense used by
the secondary plan to determine its benefits.
5.
The amount of any benefit reduction by the primary plan because a covered person has failed to comply
with the plan provisions is not an Allowable Expense. Examples of these types of plan provisions
include second surgical opinions, Prior Authorization of admissions, and preferred health care Provider
and Physician arrangements.
Allowed Amount means the amount of a billed charge that a carrier determines to be covered for services
provided by a nonpreferred health care Provider or Physician. The Allowed Amount includes both the carrier's
payment and any applicable Deductible, Copayment, or Coinsurance amounts for which the insured is
responsible.
Closed Panel Health Care Plan means a plan that provides health care benefits to covered persons primarily
in the form of services through a panel of health care Providers and Physicians that have contracted with or are
employed by the Health Care Plan, and that excludes coverage for services provided by other health care
Providers and Physicians, except in cases of emergency or Referral by a panel member.
Custodial Parent means the parent with the right to designate the primary residence of a child by a court order
under the Texas Family Code or other applicable law, or in the absence of a court order, is the parent with whom
the child resides more than one-half of the Calendar Year, excluding any temporary visitation.
TX-I-EX-H-CC-EOC-25
71
GENERAL PROVISIONS
Health Care Plan means any of the following (including this Health Care Plan) that provide benefits or services
for, or by reason of, medical care or treatment. If separate contracts are used to provide coordinated coverage
for members of a group, the separate contracts are considered parts of the same plan and there is no COB among
those separate contracts:
Group, blanket, or franchise accident and health insurance policies, excluding disability income protection
coverage; individual and group health maintenance organization evidences of coverage; individual accident
and health insurance policies; individual and group preferred Provider benefit plans and exclusive Provider
benefit plans; group insurance contracts, individual insurance contracts and subscriber contracts that pay
or reimburse for the cost of dental care; medical care components of individual and group long-term care
contracts; limited benefit coverage that is not issued to supplement individual or group in force policies;
uninsured arrangements of group or group-type coverage; the medical benefits coverage in automobile
insurance contracts; and Medicare or other governmental benefits, as permitted by law.
Health Care Plan does not include: disability income protection coverage; the Texas Health Insurance Pool;
workers' compensation insurance coverage; Hospital confinement indemnity coverage or other fixed indemnity
coverage; specified disease coverage; supplemental benefit coverage; accident only coverage; specified
accident coverage; school accident-type coverages that cover students for accidents only, including athletic
injuries, either on a "24-hour" or a "to and from school" basis; benefits provided in long-term care insurance
contracts for non-medical services, for example, personal care, adult day care, homemaker services, assistance
with activities of daily living, respite care, and Custodial Care or for contracts that pay a fixed daily benefit
without regard to expenses incurred or the receipt of services; Medicare supplement policies; a state plan under
Medicaid; a governmental plan that, by law, provides benefits that are in excess of those of any private insurance
plan; or other nongovernmental plan; or an individual accident and health insurance policy that is designed to
fully integrate with other policies through a variable Deductible.
Each contract for coverage is a separate plan. If a plan has two parts and COB rules apply only to one of the two,
each of the parts is treated as a separate plan.
This Health Care Plan means, in a COB provision, the part of the contract providing the health care benefits to
which the COB provision applies and which may be reduced because of the benefits of other plans. Any other part
of the contract providing health care benefits is separate from this plan. A contract may apply one COB provision
to certain benefits, such as dental benefits, coordinating only with like benefits, and may apply other separate COB
provisions to coordinate other benefits.
The order of benefit determination rules determine whether this Health Care Plan is a primary plan or secondary
plan when the person has health care coverage under more than one plan. When this Health Care Plan is primary, it
determines payment for its benefits first before those of any other plan without considering any other plan's benefits.
When this Health Care Plan is secondary, it determines its benefits after those of another plan and may reduce the
benefits it pays SO that all plan benefits equal 100 percent of the total Allowable Expense.
HMO has the right to coordinate benefits between This Health Care Plan and any other Health Care Plan covering
You. When a person is covered by two or more plans, the rules establishing the order of benefit determination
between this Evidence of Coverage and any other Health Care Plan covering You on whose behalf a claim is made
are as follows:
1.
The benefits of a Health Care Plan that does not have a Coordination of Benefits provision shall in all cases
be determined before the benefits of this Evidence of Coverage unless the provisions of both Health Care
Plans state that the complying Health Care Plan is primary.
2.
If according to the rules set forth below in this section the benefits of another Health Care Plan that contains
a provision coordinating its benefits with this Health Care Plan would be determined before the benefits
of this Health Care Plan have been determined, the benefits of the other Health Care Plan will be considered
before the determination of benefits under this Health Care Plan.
3.
Coverage that is obtained by virtue of membership in a group that is designed to supplement a part of a
basic package of benefits and provides that this supplementary coverage must be excess to any other parts
of the Health Care Plan provided by the contract holder. Examples of these types of situations are major
TX-I-EX-H-CC-EOC-25
72
GENERAL PROVISIONS
medical coverages that are superimposed over base plan Hospital and surgical benefits, and insurance type
coverages that are written in connection with a Closed Panel Health Care Plan to provide out-of-network
benefits.
4.
A Health Care Plan may consider the benefits paid or provided by another Health Care Plan in calculating
payment of its benefits only when it is secondary to that other Health Care Plan.
5.
If the primary Health Care Plan is a Closed Panel Health Care Plan and the secondary Health Care Plan
is
not, the secondary Health Care Plan must pay or provide benefits as if it were the primary Health Care
Plan when a covered person uses a noncontracted health care Provider or Physician, except for emergency
services or authorized Referrals that are paid or provided by the primary Health Care Plan.
6.
When multiple contracts providing coordinated coverage are treated as a single Health Care Plan under
this subchapter, this section applies only to the Health Care Plan as a whole, and coordination among the
component contracts is governed by the terms of the contracts. If more than one carrier pays or provides
benefits under the Health Care Plan, the carrier designated as primary within the Health Care Plan must be
responsible for the Health Care Plan's compliance with this subchapter.
7.
If a person is covered by more than one secondary Health Care Plan, the order of benefit determination
rules below decide the order in which secondary Health Care Plans' benefits are determined in relation to
each other. Each secondary Health Care Plan must take into consideration the benefits of the primary
Health Care Plan or Health Care Plans and the benefits of any other Health Care Plan that, under the rules
of this contract, has its benefits determined before those of that secondary Health Care Plan.
The order of benefits for Your claim relating to paragraphs 1 through 7 above, is determined using the first of the
following rules that applies:
1.
Nondependent or Dependent. The Health Care Plan that covers the person other than as a Dependent, for
example as an employee, Member, policyholder, Subscriber, or retiree, is the primary plan, and the Health
Care Plan that covers the person as a Dependent is the secondary plan. However, if the person is a Medicare
beneficiary and, as a result of federal law, Medicare is secondary to the Health Care Plan covering the
person as a Dependent and primary to the Health Care Plan covering the person as other than a Dependent,
then the order of benefits between the two plans is reversed SO that the Health Care Plan covering the
person as an employee, Member, policyholder, Subscriber, or retiree is the secondary plan and the other
Health Care Plan is the primary plan. An example includes a retired employee.
2.
Dependent Child Covered Under More Than One Health Care Plan. Unless there is a court order
stating otherwise, Health Care Plans covering a Dependent child must determine the order of benefits using
the following rules that apply:
a.
For a Dependent child whose parents are married or are living together, whether or not they have
ever been married:
1.
The Health Care Plan of the parent whose birthday falls earlier in the Calendar Year is the
primary plan; or
2.
If both parents have the same birthday, the Health Care Plan that has covered the parent the
longest is the primary plan.
b.
For a Dependent child whose parents are divorced, separated, or not living together, whether or not
they have ever been married:
1.
if a court order states that one of the parents is responsible for the Dependent child's health
care expenses or health care coverage and the Health Care Plan of that parent has actual
knowledge of those terms, that Health Care Plan is primary. This rule applies to plan years
commencing after the Health Care Plan is given notice of the court decree.
2.
if a court order states that both parents are responsible for the Dependent child's health care
expenses or health care coverage, the provisions of 2.a. must determine the order of benefits.
TX-I-EX-H-CC-EOC-25
73
GENERAL PROVISIONS
3.
if a court order states that the parents have joint custody without specifying that one parent
has responsibility for the health care expenses or health care coverage of the Dependent child,
the provisions of 2.a. must determine the order of benefits.
4.
if there is no court order allocating responsibility for the Dependent child's health care
expenses or health care coverage, the order of benefits for the child are as follows:
the Health Care Plan covering the Custodial Parent;
the Health Care Plan covering the spouse of the Custodial Parent;
the Health Care Plan covering the non-Custodial Parent; then
the Health Care Plan covering the spouse of the non-Custodial Parent.
C.
For a Dependent child covered under more than one Health Care Plan of individuals who are not
the parents of the child, the provisions of 2.a or 2.b. must determine the order of benefits as if those
individuals were the parents of the child.
d.
For a Dependent child who has coverage under either or both parents' Health Care Plans and has
his or her own coverage as a Dependent under a spouse's Health Care Plan, paragraph 5. below
applies.
e.
In the event the Dependent child's coverage under the spouse's Health Care Plan began on the same
date as the Dependent child's coverage under either or both parents' Health Care Plans, the order of
benefits must be determined by applying the birthday rule in 2.a. to the Dependent child's parent(s)
and the Dependent's spouse.
3.
Active, Retired, or Laid-off Employee. The Health Care Plan that covers a person as an active employee,
that is, an employee who is neither laid off nor retired, is the primary plan. The Health Care Plan that
covers that same person as a retired or laid-off employee is the secondary plan. The same would hold true
if a person is a Dependent of an active employee and that same person is a Dependent of a retired or laid-
off employee. If the Health Care Plan that covers the same person as a retired or laid-off employee or as a
Dependent of a retired or laid-off employee does not have this rule, and as a result, the Health Care Plans
do not agree on the order of benefits, this rule does not apply. This rule does not apply if paragraph 1.
above can determine the order of benefits.
4.
COBRA or State Continuation Coverage. If a person whose coverage is provided under COBRA or
under a right of continuation provided by state or other federal law is covered under another Health Care
Plan, the Health Care Plan covering the person as an employee, Member, Subscriber, or retiree or covering
the person as a Dependent of an employee, Member, Subscriber, or retiree is the primary plan, and the
COBRA, state, or other federal continuation coverage is the secondary plan. If the other Health Care Plan
does not have this rule, and as a result, the Health Care Plans do not agree on the order of benefits, this
rule does not apply. This rule does not apply if paragraph 1. above can determine the order of benefits.
5.
Longer or Shorter Length of Coverage. The Health Care Plan that has covered the person as an
employee, Member, policyholder, Subscriber, or retiree longer is the primary plan, and the Health Care
Plan that has covered the person the shorter period is the secondary plan.
6.
If the preceding rules do not determine the order of benefits, the Allowable Expenses must be shared
equally between the Health Care Plans meeting the definition of Health Care Plan. In addition, this Health
Care Plan will not pay more than it would have paid had it been the primary plan.
When this Health Care Plan is secondary, it may reduce its benefits SO that the total benefits paid or provided by all
Health Care Plans are not more than the total Allowable Expenses. In determining the amount to be paid for any
claim, the secondary plan will calculate the benefits it would have paid in the absence of other health care coverage
and apply that calculated amount to any Allowable Expense under its Health Care Plan that is unpaid by the primary
plan. The secondary plan may then reduce its payment by the amount SO that, when combined with the amount paid
by the primary plan, the total benefits paid or provided by all Health Care Plans for the claim equal 100 percent of
TX-I-EX-H-CC-EOC-25
74
GENERAL PROVISIONS
the total Allowable Expense for that claim. In addition, the secondary plan must credit to its plan Deductible (if
applicable) any amounts it would have credited to its Deductible in the absence of other health care coverage.
If a covered person is enrolled in two or more Closed Panel Health Care Plans and if, for any reason, including the
provision of service by a non-panel Provider, benefits are not payable by one Closed Panel Health Care Plan,
COB must not apply between that Health Care Plan and other Closed Panel Health Care Plans.
If inpatient care began when You were enrolled in a previous Health Care Plan, after You make Your Copayment
under this Evidence of Coverage, HMO will pay the difference between benefits under this Evidence of Coverage
and benefits under the previous contract or insurance policy for services on or after the effective date of this
Evidence of Coverage.
Benefits provided directly through a specified Provider of an employer shall in all cases be provided before the
benefits of this Evidence of Coverage.
For purposes of this provision, HMO may, subject to applicable confidentiality requirements set forth in this
Evidence of Coverage, release to or obtain from any insurance company or other organization necessary information
under this provision. If You claim benefits under this Evidence of Coverage, You must furnish all information
deemed necessary by HMO to implement this provision.
None of the above rules as to coordination of benefits shall delay Your health services covered under this Evidence
of Coverage.
Whenever payments have been made by HMO with respect to Allowable Expenses in a total amount, at any time,
in excess of 100% of the amount of payment necessary at that time to satisfy the intent of this Part, HMO shall have
the right to recover such payment, to the extent of such excess, from among one or more of the following as HMO
shall determine: any insurance company or companies; or any Physician or Provider to which such payments were
made.
A payment made under another Health Care Plan may include an amount that should have been paid under this
Health Care Plan. If it does, HMO may pay that amount to the organization that made that payment. That amount
will then be treated as though it were a benefit paid under this Health Care Plan. HMO will not have to pay that
amount again. The term "payment made" includes providing benefits in the form of services, in which case
"payment made" means the reasonable cash value of the benefits provided in the form of services.
You must complete and submit consents, releases, assignments and other documents requested by HMO to obtain
or assure reimbursement under workers' compensation. If You fail to cooperate, You will be liable for the amount
of money HMO would have received if You had cooperated. Benefits under workers' compensation will
be
determined first and benefits under this Evidence of Coverage may be reduced accordingly.
Reimbursement - Acts of Third Parties
HMO will provide services to You due to the act or omissions of another person. However, if You are entitled to a
recovery from any third party with respect to those services, You shall agree in writing, subject to the provisions of
Section 140.005 of the Civil Practice and Remedies Code:
1.
To reimburse HMO to the extent of the Allowable Amount that would have been charged to You for health
care services if You were not covered under this Evidence of Coverage. Such reimbursement must be made
immediately upon collection of damages for Hospital or medical expenses by You whether by action at
law, settlement or otherwise.
2.
To assign to HMO a right of recovery from a third party for Hospital and medical expenses paid by HMO
on Your behalf and to provide HMO with any reasonable help necessary for HMO to pursue a recovery. In
addition, HMO will be entitled to recover attorneys' fees and court costs related to its subrogation efforts
only if the HMO aids in the collection of damages from a third party.
Actuarial Value
The use of a metallic name, such as Platinum, Gold, Silver or Bronze, or other statements with respect to a Health
Benefit Plan's actuarial value, is not an indicator of the actual amount of expenses that a particular person will be
TX-I-EX-H-CC-EOC-25
75
GENERAL PROVISIONS
responsible to pay out of his/her own pocket. A person's out of pocket expenses will vary depending on many
factors, such as the particular health care services, health care Providers and particular benefit plan chosen. Please
note that metallic names reflect only an approximation of the actuarial value of a particular benefit plan.
Assignment
This Evidence of Coverage is not assignable by a Member without the written consent of HMO.
Cancellation
Except as otherwise provided herein, HMO or the Exchange shall not have the right to cancel or terminate any
Subscriber while the Evidence of Coverage remains in force and effect, and while said Subscriber remains eligible,
and his Premiums are paid in accordance with the terms of this Evidence of Coverage.
Clerical Error
Clerical error of HMO or the Exchange, in keeping any records pertaining to the coverage hereunder will not
invalidate coverage otherwise validly in force or continue coverage otherwise validly terminated.
Entire Evidence of Coverage
This Evidence of Coverage, any attachments, amendments, and the applications, if any, of Subscribers constitute
the entire contract between the parties and as of the effective date hereof, supersede all other contracts between the
parties.
Force Majeure
In the event that due to circumstances not within the commercially reasonable control of HMO, the rendering of
professional or Hospital Services provided under this Evidence of Coverage is delayed or rendered impractical,
HMO shall make a good faith effort to arrange for an alternative method of providing coverage. These
circumstances may include, but are not limited to, a major disaster, epidemic, the complete or partial destruction of
facilities, riot, civil insurrection, disability of a significant part of the Participating Providers' personnel or similar
causes. In such event, Participating Providers shall render the Hospital and Professional Services provided for under
the Evidence of Coverage in SO far as practical, and according to their best judgment; but HMO and Participating
Providers shall incur no liability or obligation for delay, or failure to provide or arrange for services if such failure
or delay is caused by such an event.
Form or Content of Evidence of Coverage
No agent or employee of HMO is authorized to change the form or content of this Evidence of Coverage except to
make necessary and proper insertions in blank spaces. Changes can be made only through endorsement authorized
and signed by an officer of HMO. No agent or other person, except an authorized officer of HMO, has authority to
waive any conditions or restrictions of this Evidence of Coverage, to extend the time for making a payment, or to
bind HMO by making any promise or representation or by giving or receiving any information.
Gender
The use of any gender herein shall be deemed to include the other gender and, whenever appropriate, the use of the
singular herein shall be deemed to include the plural (and vice versa).
Identity Theft Protection
As a Member, BCBSTX makes available at no additional cost to You, identity theft protection services, including
credit monitoring, fraud detection, credit/identity repair and insurance to help protect Your information. These
identity theft protection services are currently provided by BCBSTX's designated outside vendor and acceptance
or declination of these services is optional to the Member. Members who wish to accept such identity theft
protection services will need to individually enroll in the program online at www.bcbstx.com or telephonically by
TX-I-EX-H-CC-EOC-25
76
GENERAL PROVISIONS
calling the number on the back of Your identification card. Services may automatically end when the person is no
longer an eligible Member. Services may change or be discontinued at any time with reasonable notice. BCBSTX
does not guarantee that a particular vendor or service will be available at any given time.
Incontestability
All statements made by You are considered representations and not warranties. A statement may not be used to void,
cancel or non-renew Your coverage or reduce benefits unless it is in a written application signed by Subscriber and
a signed copy of the application has been furnished to Subscriber or to the Subscriber's personal representative.
Coverage may only be contested because of fraud or intentional misrepresentation of material fact on the enrollment
application.
Interpretation of Evidence of Coverage
The laws of the state of Texas shall be applied to interpretations of this Evidence of Coverage. Where applicable,
the interpretation of this Evidence of Coverage shall be guided by the direct-service nature of HMO's operations as
opposed to a health insurance program. If the Evidence of Coverage contains any provision not in conformity with
the Texas Health Maintenance Organization Act or other applicable laws, the Evidence of Coverage shall not be
rendered invalid but shall be construed and applied as if it were in full compliance with the Texas Health
Maintenance Organization Act and other applicable laws. Changes in state or federal law or regulations, or
interpretation thereof, may change the terms and conditions of coverage.
Limitation of Liability
Liability for any errors or omissions by HMO (or its officers, directors, employees, agents, or independent
contractors) in the administration of this Evidence of Coverage, or in the performance of any duty of responsibility
contemplated by this Evidence of Coverage, shall be limited to the maximum benefits which should have been paid
under the Evidence of Coverage had the errors or omissions not occurred, unless any such errors or omissions are
adjudged to be the result of willful misconduct or gross negligence of HMO.
Member Data Sharing
You may, under certain circumstances, as specified below, apply for and obtain, subject to any applicable terms and
conditions, replacement coverage. The replacement coverage will be that which is offered by Blue Cross and Blue
Shield of Texas, a division of Health Care Service Corporation, or, if You do not reside in the Blue Cross and Blue
Shield of Texas Service Area, by the Host Blues whose service area covers the geographic area in which You reside.
The circumstances mentioned above may arise in various circumstances, such as from involuntary termination of
Your health coverage sponsored by the Subscriber. As part of the overall plan of benefits that Blue Cross and Blue
Shield of Texas offers to, You, if You do not reside in the Blue Cross and Blue Shield of Texas Service Area, Blue
Cross and Blue Shield of Texas may facilitate Your right to apply for and obtain such replacement coverage, subject
to applicable eligibility requirements, from the Host Blue in which You reside. To do this we may (1) communicate
directly with You and/or (2) provide the Host Blues whose service area covers the geographic area in which You
reside with Your personal information and may also provide other general information relating to Your coverage
under the Evidence of Coverage the Subscriber has with Blue Cross and Blue Shield of Texas to the extent
reasonably necessary to enable the relevant Host Blues to offer You coverage continuity through replacement
coverage.
Modifications
This Evidence of Coverage shall be subject to amendment, modification, and termination in accordance with any
provision hereof or by mutual agreement between HMO the Exchange and Subscriber without the consent or
concurrence of Members. By electing medical and Hospital coverage under HMO or accepting HMO benefits, all
Subscribers legally capable of contracting, and the legal representatives of all Subscribers incapable of contracting,
agree to all terms, conditions, and provisions hereof.
TX-I-EX-H-CC-EOC-25
77
GENERAL PROVISIONS
Non-Agency
The Member understands that this Evidence of Coverage constitutes an Evidence of Coverage solely between the
Member and Blue Cross and Blue Shield of Texas (BCBSTX). BCBSTX is a Division of Health Care Service
Corporation, a Mutual Legal Reserve Company (HCSC), an Independent Licensee of the Blue Cross and Blue
Shield Association. The license from the Association permits Blue Cross and Blue Shield of Texas to use the Blue
Cross and Blue Shield Service Marks in the State of Texas. BCBSTX is not contracting as the agent of the
Association. The Member also understands that he has not entered into this Evidence of Coverage based upon
representations by any person other than BCBSTX. No person, entity, or organization other than BCBSTX shall be
held accountable or liable to the Member for any of its obligations created under this Evidence of Coverage. This
section shall not create any additional obligations whatsoever on the part of BCBSTX other than those obligations
created under other provisions of this Evidence of Coverage.
Notice
You may send a notice to HMO via first-class mail, postage prepaid through the United States Postal Service to the
address on the face page of this Evidence of Coverage.
HMO may send You notices under this Evidence of Coverage. These notices may be delivered:
through the United States Postal Service at the last address known to HMO; or
electronically, if permitted by applicable law.
Paper Check - Automatic Clearing House/Electronic Funds Transfer
BCBSTX will not charge an additional fee to a Payee if such person elects to receive the payment by paper check
instead of by an automated clearinghouse transaction or other electronic funds transfer.
In addition to the DEFINITIONS of this Evidence of Coverage, the following definition is applicable to this
provision:
"Payee" means individual who resides in this state or a corporation, trust, partnership, association, or other
private legal entity authorized to do business in this state that receives money as payment under an
agreement.
Patient/Provider Relationship
Participating Providers maintain a Provider-patient relationship with Members and are solely responsible to You for
all health services. If a Participating Provider cannot establish a satisfactory Provider-patient relationship, the
Participating Provider may send a written request to HMO to terminate the Provider-patient relationship, and this
request may be applicable to other Providers in the same group practice, if applicable.
Premium Rebates and Premium Abatements
Rebate. In the event federal or state law requires Blue Cross and Blue Shield of Texas (BCBSTX) to rebate a portion
of annual Premiums paid, BCBSTX will directly provide any rebate owed Subscribers or former Subscribers to
such persons in amounts as required by law.
If any rebate is owed a Subscriber or former Subscriber, BCBSTX will provide the rebate to the Subscriber or
former Subscriber as required by law.
BCBSTX will provide any rebate owed to a Subscriber in the form of a Premium credit, lump-sum check or, if a
Subscriber paid the Premium using a credit card or direct debit, by lump-sum reimbursement to the account used
to pay the Premium. However, BCBSTX will provide any rebate owed to a former Subscriber in the form of lump-
sum check or lump-sum reimbursement using the same method used for payment, such as credit card or direct debit.
If a rebate is provided in the form of a Premium credit, BCBSTX will provide any rebate by applying the full
amount due to the first Premium payment due as required by law. If the rebate owed is greater than the Premium
due, BCBSTX will apply any overage to succeeding Premium payments until the full amount of the rebate has been
credited.
TX-I-EX-H-CC-EOC-25
78
GENERAL PROVISIONS
At the time any rebate is provided, BCBSTX will provide to each BCBSTX Subscriber or former Subscriber who
receives a rebate a notice containing at least the following information:
a general description of the concept of an MLR;
the purpose of setting an MLR standard;
the applicable MLR standard;
BCBSTX's MLR;
BCBSTX's aggregate Premium revenue as reported under federal MLR regulations (minus
any federal and state taxes and licensing and regulatory fees that may be excluded from
Premium revenue under those regulations); and
the rebate percentage and amount owed based upon the difference between the BCBSTX's
MLR and the applicable MLR standard.
Abatement. BCBSTX may from time to time determine to abate (in whole or in part) the Premium due under this
Contract for particular period(s).
Any abatement of Premium by BCBSTX represents a determination by BCBSTX not to collect Premium for the
applicable period(s) and does not affect a reduction in the rates under this contract. An abatement for one period
shall not constitute a precedent or create an expectation or right as to any abatement in any future period(s).
BCBSTX makes no representation or warranty that any rebate or abatement owed or provided is exempt from any
federal, state, or local taxes (including any related notice, withholding or reporting requirements). It will be the
obligation of each Subscriber or former Subscriber (if applicable) owed or provided a rebate or an abatement to
determine the applicability of and comply with any applicable federal, state or local laws or regulations.
Refund of Benefit Payments
If BCBSTX pays benefits for Covered Services incurred by You or Your Dependents and it is found that the payment
was more than it should have been, or was made in error ("Overpayment"), BCBSTX has the right to obtain a
refund of the Overpayment from: (i) any insurance company or plan, or (ii) any other persons, entities or
organizations, including, but not limited to, Participating Providers or non-Participating Providers to which such
payments were made.
If no refund is received, BCBSTX (in its capacity as HMO, insurer, or administrator) has the right to deduct any
refund for any Overpayment due, up to an amount equal to the Overpayment, from:
any future benefit payment made to any person or entity under this Evidence of Coverage,
whether for the same or a different Member; or
any future benefit payment made to any person or entity under another BCBSTX-
administered ASO benefit program and/or BCBSTX-administered insured benefit program
or policy; or
any future benefit payment made to any person or entity under another BCBSTX-insured
group benefit plan or individual policy; or
any future benefit payment, or other payment, made to any person or entity; or
any future payment owed to one or more Participating Providers or non-Participating
Providers.
Further, BCBSTX has the right to reduce Your benefit plan's or policy's payment to a Provider by the amount
necessary to recover another BCBSTX plan's or policy's overpayment to the same Provider and to remit the
recovered amount to the other BCBSTX plan or policy.
Relationship of Parties
The relationship between HMO and Participating Providers is that of an independent contractor relationship.
Participating Providers are not agents or employees of HMO; HMO or any employee of HMO is not an employee
or agent of Participating Providers. HMO shall not be liable for any claim or demand on account of damages arising
out of, or in any manner connected with, any injuries suffered by You while receiving care from any Participating
TX-I-EX-H-CC-EOC-25
79
GENERAL PROVISIONS
Provider. HMO makes no express or implied warranties or representations concerning the qualifications, continued
participation, or quality of services of any Physician, Hospital or other Participating Provider.
If this plan is purchased through the Exchange, in no event shall HMO be considered the agent of the Exchange or
be responsible for the Exchange. All information You provide to the Exchange and received by HMO from the
Exchange will be relied upon as accurate and complete. The Member will promptly notify the Exchange and HMO
of any changes to such information.
HMO or a HMO subsidiary may have a direct or indirect financial interest in certain Participating Providers or an
ownership interest in one or more entities that provide non-clinical services to certain Participating Providers.
Participating Providers and Members are solely responsible for any health care services rendered to Members.
Reports and Records
HMO is entitled to receive from any Provider of services to Members, information reasonably necessary to
administer this Evidence of Coverage subject to all applicable confidentiality requirements described below. By
accepting coverage under this Evidence of Coverage, the Subscriber, for himself or herself, and for all Dependents
covered hereunder, authorizes each and every Provider who renders services to You hereunder to:
disclose all facts pertaining to Your care, treatment and physical condition to HMO, or a
medical, dental, or mental health professional that HMO may engage to assist it in reviewing
a treatment or claim;
render reports pertaining to Your care, treatment and physical condition to HMO, or a
medical, dental, or mental health professional that HMO may engage to assist it in reviewing
a treatment or claim; and
permit copying of Your records by HMO.
Information contained in Your medical records and information received from Physicians, surgeons, Hospitals or
other Health Care Professionals incident to the Physician-patient relationship or Hospital-patient relationship shall
be kept confidential in accordance with applicable law.
Rescission of Coverage
Rescission is the retroactive cancellation or discontinuance of coverage due to an act, practice, or omission that
constitutes fraud or an intentional misrepresentation of a material fact by You or by a person seeking coverage on
Your behalf. A retroactive cancellation or discontinuance of coverage due to failure to timely pay required Premiums
or contributions toward the cost of coverage (including COBRA Premiums), a cancellation or discontinuance
initiated by You or Your authorized representative, a cancellation initiated by the Exchange or a prospective
cancellation or discontinuance of coverage is not considered a Rescission. Rescission is subject to 30 days' prior
notification and is retroactive to the Effective Date. In the event of such cancellation, HMO may deduct from the
Premium refund any amounts made in claim payments during this period and You may be liable for any claims
payment amount greater than the total amount of Premiums paid during the period for which cancellation is affected.
At any time when HMO is entitled to rescind coverage already in force, or is otherwise permitted to make retroactive
changes to this Evidence of Coverage, HMO may at its option make an offer to reform the Evidence of Coverage
already in force and/or change the rating category/level. In the event of reformation, the Evidence of Coverage will
be reissued retroactive in the form it would have been issued had the misstated or omitted information been known
at the time of application. Please call HMO at the toll-free number listed on the back of Your identification card for
additional information regarding Your appeal rights concerning Rescission and/or reformation.
Subtitles
The subtitles included within this Evidence of Coverage are provided for the purpose of identification and
convenience and are not part of the complete Evidence of Coverage as described in Entire Evidence of Coverage.
TX-I-EX-H-CC-EOC-25
80
GENERAL PROVISIONS
Transfer of Residence
Within the HMO Service Area: If Subscriber changes primary residence, notification must be
made to HMO and the Exchange within sixty (60) days of such change.
Outside the HMO Service Area: If Subscriber no longer resides, lives or works in the Service
Area, such change will result in loss of eligibility and Subscriber must notify HMO and the
Exchange within sixty (60) days of such change.
TX-I-EX-H-CC-EOC-25
81
PEDIATRIC VISION
CARE BENEFITS
TX-I-EX-H-CC-EOC-25
82
PEDIATRIC VISION CARE BENEFITS
Pediatric Vision Care is made part of, and is in addition to any information You may have in Your HMO Evidence
of Coverage. Information about coverage for the routine vision care services are outlined below and are specifically
excluded under Your medical health care plan. (Services that are covered under Your medical plan are not covered
under this Pediatric Vision Care Benefit.) All provisions in the Evidence of Coverage apply to Pediatric Vision Care
Benefits unless specifically indicated otherwise below.
Definitions
Eye Care Expenses - For purposes of this Pediatric Vision Care Benefit - Expenses related to vision or medical
eye care services, procedures, or products.
Medically Necessary Contact Lenses - Contact lenses may be determined to be Medically Necessary and
appropriate in the treatment of patients affected by certain conditions. In general, contact lenses may be Medically
Necessary and appropriate when the use of contact lenses, in lieu of eyeglasses, will result in significantly better
visual and/or improved binocular function, including avoidance of diplopia or suppression. Contact lenses may be
determined to be Medically Necessary in the treatment of the following conditions: keratoconus, pathological
myopia, aphakia, anisometropia, aniseikonia, aniridia, corneal disorders, post-traumatic disorders, irregular
astigmatism.
Provider - For purposes of this Pediatric Vision Care Benefit, a licensed therapeutic optometrist, ophthalmologist
or optometrist operating within the scope of his or her license, or a dispensing optician.
Vision Materials - Corrective lenses and/or frames or contact lenses.
Eligibility
Children who are covered under Your Evidence of Coverage, to age 19, are eligible for coverage under this Pediatric
Vision Care Benefit. NOTE: Once coverage is lost under Your Evidence of Coverage, all benefits cease under this
Pediatric Vision Care Benefit.
Limitations and Exclusions
The limitations and exclusions in this section apply to all pediatric vision benefits. Although HMO may list a
specific service as a benefit, HMO will not cover it unless we determine it is necessary for the prevention, diagnosis,
care or treatment of a covered condition.
We do not cover the following:
any vision service, treatment or materials not specifically listed as a covered service;
services and materials that are Experimental/Investigational;
services and materials that are rendered prior to Your effective date;
services and materials incurred after the termination date of Your coverage unless otherwise indicated;
services and materials not meeting accepted standards of optometric practice;
services and materials resulting from Your failure to comply with professionally prescribed treatment;
telephone consultations;
any charges for failure to keep a scheduled appointment;
any services that are strictly cosmetic in nature including, but not limited to, charges for personalization or
characterization of Prosthetic Appliances;
office infection control charges;
charges for copies of Your records, charts, or any costs associated with forwarding/mailing copies of Your
records or charts;
state or territorial taxes on vision services performed;
medical treatment of eye disease or injury;
TX-I-EX-H-CC-EOC-25
83
PEDIATRIC VISION CARE BENEFITS
visual therapy;
special lens designs or coatings other than those described in this benefit;
replacement of lost/stolen eyewear;
non-prescription (Plano) lenses;
non-prescription sunglasses;
two pairs of eyeglasses in lieu of bifocals;
services not performed by licensed personnel;
prosthetic devices and services;
insurance of contact lenses;
professional services You receive from immediate relatives or household members, such as a spouse,
parent, child, brother or sister, by blood, marriage or adoption;
orthoptic or vision training;
aniseikonic spectacle lenses.
How the Vision Benefits Work
You may visit any Participating Provider and receive benefits for a vision examination and covered Vision Materials.
Before You go to a Participating Provider for an eye examination, eyeglasses, or contact lenses, please call ahead
for an appointment. When You arrive, show the receptionist Your identification card. If You forget to take Your
card, be sure to say that You are a Member of the HMO vision care plan SO that Your eligibility can be verified.
For the most current list of Participating Providers visit the website at www.bcbstx.com. You may also refer to Your
Provider directory or call customer service at the toll-free telephone number on the back of Your identification card.
You may receive Your eye examination and eyeglasses/contacts on different dates or through different Provider
locations, if desired. However, complete eyeglasses must be obtained at one time, from one Participating Provider.
Continuity of care will best be maintained when all available services are obtained at one time from one
Participating Provider and there may be additional professional charges if You seek contact lenses from a
Participating Provider other than the one who performed Your eye examination.
Fees charged for services other than a covered vision examination or covered Vision Materials, and amounts in
excess of those payable under this Pediatric Vision Care Benefit, must be paid in full by You to the Provider, whether
or not the Provider participates in the vision care plan. These Pediatric Vision Care Benefits may not be combined
with any discount, promotional offering, or other group benefit plans. Allowances are one-time use benefits; no
remaining balances are carried over to be used later.
Coordination of Benefits
If You are covered by at least two different benefit plans that provide benefits for Eye Care Expenses and each plan
provides coverage for the same vision or medical eye care services, procedures or products:
The issuer of the primary Health Benefit Plan or vision benefit plan, as described in the COORDINATION
OF BENEFITS section of this Evidence of Coverage, is responsible for Eye Care Expenses covered under
the plan up to the full amount of any plan coverage limit applicable to the covered Eye Care Expenses.
Before the plan coverage limit described above is reached, the issuer of a secondary Health Benefit Plan or
vision benefit plan is responsible only for Eye Care Expenses covered under the plan that are not covered
under the Health Benefit Plan or vision benefit plan issued by the primary plan issuer.
After the plan coverage limit described above has been reached, the secondary plan issuer, in addition to the
responsibilities for services not covered by the primary plan but covered by the secondary plan, is responsible
for any Eye Care Expenses covered by both plans that exceed the plan coverage limit of the primary plan,
up to the coverage limit of the secondary plan.
TX-I-EX-H-CC-EOC-25
84
PEDIATRIC VISION CARE BENEFITS
When an You are covered by more than one Health Benefit Plan or vision benefit plan that provides benefits
for Eye Care Expenses, You may use each plan on the same date of service up to the coverage limit of each
plan.
A vision benefit plan issuer shall coordinate benefits with a Health Benefit Plan issuer if both provide benefits
for Eye Care Expenses.
A vision benefit plan issuer may not require a claim denial before adjudicating a claim up to the coverage
limit of the plan.
Nothing in this section prevents a secondary plan issuer from requiring proof that a related claim has been
submitted to a primary plan issuer for purposes of determining the remaining balance up to the secondary
plan's coverage limits.
If a secondary plan issuer requires proof that a related claim has been submitted to a primary plan issuer, the
mechanism of providing proof must be through an online submission.
Schedule of Pediatric Vision Copayments and Benefit Limits
Member Cost or Discount
Out-of-Network
(When a fixed-dollar Copay is
Allowance
Vision Care Services
due from the Member, the
(maximum reimbursement
remainder is payable by HMO up
amount payable by HMO, not to
to the covered charge*)
exceed the retail cost)*
Exam (with dilation as necessary):
No Copay
$30 reimbursement
Frames:
Provider Designated frame
No Copay
$75 reimbursement
Non-Provider Designated frame
You receive 20% off balance of
$75 reimbursement
retail cost over $150 allowance
Frequency:
Examination, Lenses/Frames, or
Once every Calendar Year
Contact Lenses
Standard Plastic, Glass, or Poly
Spectacle Lenses:
Single Vision
No Copay
$25 reimbursement
Bifocal
No Copay
$40 reimbursement
Trifocal
No Copay
$55 reimbursement
Lenticular
No Copay
$55 reimbursement
Note: Lenses include ultraviolet
protective coating, fashion and gradient
tinting, oversized and glass-grey #3
prescription sunglasses lenses.
Lens Options (added to lens prices above):
Tint (Solid and Gradient)
No Copay
$12 reimbursement
TX-I-EX-H-CC-EOC-25
85
PEDIATRIC VISION CARE BENEFITS
Standard Plastic Scratch Coating
No Copay
$12 reimbursement
Standard Polycarbonate
No Copay
$32 reimbursement
Contact Lenses: covered once every
Calendar Year - in lieu of spectacle lenses
Elective:
Conventional
You receive 15% off balance of
retail cost over $150 allowance
$150 reimbursement
Disposable
$150 allowance
$150 reimbursement
Medically Necessary Contact Lenses -
Covered
$210 reimbursement
Prior Authorization is required
Note: Additional benefits over
allowance are available from
Participating Providers
Routine eye exams do not include professional services for contact lens evaluations. Any applicable fees are the
responsibility of the patient.
Additional Benefits
Medically Necessary Contact Lenses are dispensed in lieu of other eyewear. Participating Providers will
obtain the necessary Prior Authorization for these services.
Low Vision: Low vision is a significant loss of vision but not total blindness. Ophthalmologists and
optometrists specializing in low vision care can evaluate and prescribe optical devices, and provide training
and instruction to maximize the remaining usable vision for our Members with low vision. After Prior
Authorization, covered low vision services will include one comprehensive low vision evaluation every 5
years, low vision aid items such as high-power spectacles, magnifiers and telescopes; and follow-up care -
four visits in any five-year period. Participating Providers will obtain the necessary Prior Authorization for
these services.
Warranty: Warranty limitations may apply to Provider or retailer supplied frames and/or eyeglass lenses.
Please ask Your Provider for details of the warranty that is available to You.
* The "covered charge" is the rate negotiated with Participating Providers for a particular covered service.
HMO pays the lesser of the maximum allowance noted or the retail cost. Retail prices vary by location.
TX-I-EX-H-CC-EOC-25
86
NOTICE OF RIGHT TO AN ADEQUATE NETWORK
A health maintenance organization (HMO) plan provides no benefits for services you receive from out-of-
network physicians or providers, with specific exceptions as described in your Evidence of Coverage and
below.
You have the right to an adequate network of in-network physicians and providers (known as
network Physicians and Providers).
If you believe that the network is inadequate, you may file a complaint with the Texas Department
of Insurance at: www.tdi.texas.gov/consumer/complfrm.html
If your HMO approves a Referral for out-of-network services because no network physician or
provider is available, or if you have received out-of-network emergency care, the HMO must, in
most cases, resolve the out-of-network physician's or provider's bill SO that you only have to pay
any applicable in-network copayment, coinsurance, and deductible amounts.
You may obtain a current directory of network physicians and providers at the following website:
www.bcbstx.com/find-a-doctor-or-hospital or by calling 1-888-697-0683 for assistance in finding
available network physicians and providers. If you relied on materially inaccurate directory information,
you may be entitled to have a claim by an out-of-network physician or provider paid as if it were from a
network physician or provider, if you present a copy of the inaccurate directory information to the HMO,
dated not more than 30 days before you received the service.
TX-I-EX-H-CC-EOC-25
87
AMENDMENTS
TX-I-EX-H-CC-EOC-25
NOTICES
BlueCross BlueShield of Texas
Health care coverage is important for everyone.
If you, or someone you are helping, have questions, you have the right to get help and information in your language at no cost. To
talk to an interpreter, call 855-710-6984. We provide free communication aids and services for anyone with a disability or who needs
language assistance.
We do not discriminate on the basis of race, color, national origin, sex, gender identity, age, sexual orientation, health status or
disability. If you believe we have failed to provide a service, or think we have discriminated in another way, contact us to file a
grievance.
Office of Civil Rights Coordinator
Phone:
855-664-7270 (voicemail)
300 E. Randolph St., 35th Floor
TTY/TDD:
855-661-6965
Chicago, IL 60601
Fax:
855-661-6960
You may file a civil rights complaint with the U.S. Department of Health and Human Services, Office for Civil Rights, at:
U.S. Dept. of Health & Human Services
Phone:
800-368-1019
200 Independence Avenue SW
TTY/TDD:
800-537-7697
Room 509F, HHH Building 1019
Complaint Portal: https://ocrportal.hhs.gov/ocr/smartscreen/main.jsf
Washington, DC 20201
Complaint Forms: https://www.hhs.gov/civil-rights/filing-a-
complaint/complaint-process/index.html
To receive language or communication assistance free of charge, please call us at 855-710-6984.
Espanol
Llámenos al 855-710-6984 para recibir asistencia lingüistica o comunicación en otros formatos sin costo.
.855-710-6984 Lis Jhail dilas
Français
Pour bénéficier gratuitement d'une assistance linguistique ou d'une aide à la communication, veuillez nous appeler au 855-710-6984.
Deutsch
Um kostenlose Sprach- oder Kommunikationshilfe zu erhalten, rufen Sie uns bitte unter 855-710-6984 an.
green
CHILL 24211 21014 HEAHT Heraal His, self 24H 855-710-6984 42 sig sel
A:
HT
AT
918
855-710-6984
Italiano
Per assistenza gratuita alla lingua o alla comunicazione, chiami il numero 855-710-6984.
855-710-6984
B
Niná: Doo bilagáana bizaad dinits'á'góó, shá ata' hodooni ninizingo, t'áájiik'eh bee
Navajo
náhaz'á. 1-866-560-4042 ji' hodiilni.
855-710-6984 shawl lib whill, 664314 Security
Polski
Aby
uzyskac bezplatna pomoc jezykowa lub komunikacyjna, prosimy o kontakt pod numerem 855-710-6984.
, HAM no
TenedoHy 855-710-6984.
Tagalog
Para makatanggap ng tulong sa wika o komunikasyon nang walang bayad, pakitawagan kami sa 855-710-6984.
USUS 855-710-6984 S
Tiéng Viet
Dè duoc ho tro ngôn ngû hoãc giao tiép mien phí, vui löng goi cho chung tôi theo só 855-710-6984.
bcbstx.com
NOTICE
Adverse Benefit Determinations
This Notice is to advise You that in addition to the processes outlined in HMO COMPLAINT AND APPEAL
PROCEDURES section of the Evidence of Coverage (EOC) and in the Plan Description and Member Handbook,
You have the right to seek and obtain a review by HMO of any Adverse Benefit Determinations made by HMO in
accordance with the benefits and procedures detailed in Your Evidence of Coverage.
Review of Claim Determinations
Claim Determinations. When HMO receives a properly submitted claim, it has authority and discretion under the
plan to interpret and determine benefits in accordance with the plan provisions. You have the right to seek and
obtain a review by HMO of any determination of a claim, any determination of a request for Prior Authorization,
or any other determination made by HMO in accordance with the benefits and procedures detailed in Your plan.
If a Claim is Denied or Not Paid in Full. If the claim is denied in whole or in part, You will receive a written
notice from HMO with the following information, if applicable:
The reasons for the determination;
A reference to the benefit Plan provisions on which the determination is based, or the contractual,
administrative or protocol basis for the determination;
A description of additional information which may be necessary to perfect the claim and an explanation of
why such material is necessary;
Subject to privacy laws and other restrictions, if any, the identification of the claim, date of service, health
care provider, claim amount (if applicable), and a statement describing denial codes with their meanings
and the standards used. Upon request, diagnosis/treatment codes with their meanings and the standards
used are also available;
An explanation of HMO's internal review/appeals and external review processes (and how to initiate a
review/appeal or external review);
In certain situations, a statement in non-English language(s) that written notice of claim denials and certain
other benefit information may be available (upon request) in such non-English language(s);
In certain situations, a statement in non-English language(s) that indicates how to access the language
services provided by HMO;
The right to request, free of charge, reasonable access to and copies of all documents, records and other
information relevant to the claim for benefits;
Any internal rule, guideline, protocol or other similar criterion relied on in the determination, and a
statement that a copy of such rule, guideline, protocol or other similar criterion will be provided free of
charge on request;
An explanation of the scientific or clinical judgment relied on in the determination as applied to claimant's
medical circumstances, if the denial was based on medical necessity, experimental treatment or similar
exclusion, or a statement that such explanation will be provided free of charge upon request;
In the case of a denial of an Urgent Care Clinical Claim, a description of the expedited review procedure
applicable to such claim. An Urgent Care Clinical Claim decision may be provided orally, SO long as a
written notice is furnished to the claimant within 3 days of oral notification; and
Contact information for applicable office of health insurance consumer assistance or ombudsman.
NOTICE-ABD-IND-HMO-22
1
NOTICE
Adverse Benefit Determinations
Timing of Required Notices and Extensions. Separate schedules apply to the timing of required notices and
extensions, depending on the type of claim. There are three types of claims as defined below.
Urgent Care Clinical Claim is any pre-service claim that requires Prior Authorization, as described in
this Certificate, for benefits for medical care or treatment with respect to which the application of regular
time periods for making health claim decisions could seriously jeopardize the life or health of the claimant
or the ability of the claimant to regain maximum function or, in the opinion of a Physician with knowledge
of the claimant's medical condition, would subject the claimant to severe pain that cannot be adequately
managed without the care or treatment.
Pre-Service Claim is any non-urgent request for benefits or a determination with respect to which the
terms of the benefit Plan condition receipt of the benefit on approval of the benefit in advance of obtaining
medical care.
Post-Service Claim is notification in a form acceptable to HMO that a service has been rendered or
furnished to You. This notification must include full details of the service received, including Your name,
age, sex, identification number, the name and address of the Provider, an itemized statement of the service
rendered or furnished, the date of service, the diagnosis, the claim charge, and any other information which
HMO may request in connection with services rendered to You.
Urgent Care Clinical Claims
Type of Notice or Extension
Timing
If Your claim is incomplete, HMO must notify You within:
24 hours
If You are notified that Your claim is incomplete, You must then
provide completed claim information to HMO within:
48 hours after receiving notice
HMO must notify You of the claim determination (whether adverse or not):
If the initial claim is complete as soon as possible (taking into account
72 hours
medical exigencies), but no later than:
After receiving the completed claim (if the initial claim is
48 hours
incomplete), within:
* You do not need to submit Urgent Care Clinical Claims in writing. You should call HMO at the toll-free number listed on
the back of Your identification card as soon as possible to submit an Urgent Care Clinical Claim.
Pre-Service Claims
Type of Notice or Extension
Timing
If Your claim is filed improperly, HMO must notify You within:
5 days
If Your claim is incomplete, HMO must notify You within:
15 days
If You are notified that Your claim is incomplete, You must then
provide completed claim information to HMO within:
45 days after receiving notice
HMO must notify You of the claim determination (whether adverse or not):
If the initial claim is complete, within:
15 days
NOTICE-ABD-IND-HMO-22
2
NOTICE
Adverse Benefit Determinations
After receiving the completed claim (if the initial claim is
incomplete), within:
30 days
the time appropriate to the
If You require post-stabilization care after an Emergency within:
circumstance not to exceed one hour
after the time of request
* This period may be extended one time by HMO for up to 15 days, provided that HMO both (1) determines that such an
extension is necessary due to matters beyond the control of the Plan and (2) notifies You, prior to the expiration of the
initial 15-day period, of the circumstances requiring the extension of time and the date by which HMO expects to render
a decision.
Post-Service Claims
Type of Notice or Extension
Timing
If Your claim is incomplete, HMO must notify You within:
30 days
If You are notified that Your claim is incomplete, You must then
provide completed claim information to HMO within:
45 days after receiving notice
HMO must notify You of any adverse claim determination:
If the initial claim is complete, within:
30 days*
After receiving the completed claim (if the initial claim is
incomplete), within:
45 days
* This period may be extended one time by HMO for up to 15 days, provided that HMO both (1) determines that such an
extension is necessary due to matters beyond the control of the Plan and (2) notifies You in writing, prior to the expiration
of the initial 30-day period, of the circumstances requiring the extension of time and the date by which HMO expects
to
render a decision.
Concurrent Care. For benefit determinations relating to care that is being received at the same time as the
determination, such notice will be provided no later than 24 hours after receipt of Your claim for benefits.
Note: If HMO is seeking to discontinue coverage of prescription drugs or intravenous infusions for which You are
receiving health benefits under the plan, You will be notified no later than the 30th day before the date on which
coverage will be discontinued. This notice will explain Your rights to expedited appeal and immediate review by
an Independent Review Organization.
Claim Appeal Procedures
Claim Appeal Procedures - Definitions. An "Adverse Benefit Determination" means a denial, reduction, or
termination of, or a failure to provide or make payment (in whole or in part) for, a benefit, including any such denial,
reduction, termination, or failure to provide or make payment for, a benefit resulting from the application of any
utilization review, as well as a failure to cover an item or service for which benefits are otherwise provided because
it is determined to be Experimental/Investigational or not Medically Necessary or appropriate. If an ongoing course
of treatment had been approved by HMO and HMO reduces or terminates such treatment (other than by amendment
or termination of the Employer's benefit Plan) before the end of the approved treatment period, that is also an
Adverse Benefit Determination. A rescission of coverage is also an Adverse Benefit Determination. A rescission
does not include a termination of coverage for reasons related to non-payment of Premium.
A "Final Internal Adverse Benefit Determination" means an Adverse Benefit Determination that has been upheld
by HMO at the completion of HMO's internal review/appeal process.
NOTICE-ABD-IND-HMO-22
3
NOTICE
Adverse Benefit Determinations
Expedited Clinical Appeals. If Your situation meets the definition of an expedited clinical appeal, You may be
entitled to an appeal on an expedited basis. An "expedited clinical appeal" is an appeal of a clinically urgent nature
related to health care services, including but not limited to, procedures or treatments ordered by a health care
provider, the denial of emergency care or continued hospitalization, or the discontinuance by HMO of prescription
drugs or intravenous infusions for which You were receiving health benefits under the plan. Before authorization
of benefits for an ongoing course of treatment/continued hospitalization is terminated or reduced, HMO will provide
You with notice and an opportunity to appeal. For the ongoing course of treatment, coverage will continue during
the appeal process.
Upon receipt of an expedited pre-service or concurrent clinical appeal, HMO will notify the party filing the
appeal, as soon as possible, but in no event later than 24 hours after submission of the appeal, of all the
information needed to review the appeal. HMO will render a decision on the appeal within 24 hours after it
receives the requested information, but no later than 72 hours after the appeal has been received by HMO.
How to Appeal to an Adverse Benefit Determination. You have the right to seek and obtain a review of any
determination of a claim, any determination of a request for Prior Authorization, or any other determination made
by HMO in accordance with the benefits and procedures detailed in Your Plan. An appeal of an Adverse Benefit
Determination may be filed by You or a person authorized to act on Your behalf. In some circumstances, a health
care provider may appeal on his/her own behalf. Your designation of a representative must be in writing as it is
necessary to protect against disclosure of information about You except to Your authorized representative. To obtain
an Authorized Representative Form, You or Your representative may call HMO at the number on the back of
Your
identification card. If You believe HMO incorrectly denied all or part of Your benefits, You may have Your claim
reviewed. HMO will review its decision in accordance with the following procedure:
Within 180 days after You receive notice of an Adverse Benefit Determination, You may call or write to
HMO to request a claim review. HMO will need to know the reasons why You do not agree with the
Adverse Benefit Determination. Send Your request to:
Claim Review Section
Blue Cross and Blue Shield of Texas
P. O. Box 660044
Dallas, Texas 75266-0044
HMO will honor telephone requests for information; however, such inquiries will not constitute a request
for review.
In support of Your claim review, You have the option of presenting evidence and testimony to the HMO.
You and Your authorized representative may ask to review Your file and any relevant documents and may
submit written issues, comments and additional medical information within 180 days after You receive
notice of an Adverse Benefit Determination or at any time during the claim review process.
During the course of Your internal appeal(s), HMO will provide You or Your authorized representative (free
of charge) with any new or additional evidence considered, relied upon or generated by HMO in connection
with the appealed claim, as well as any new or additional rationale for a denial at the internal appeals stage.
Such new or additional evidence or rationale will be provided to You or Your authorized representative as
soon as possible and sufficiently in advance of the date a final decision on appeal is made in order to give
You a reasonable opportunity to respond. BCBSTX may extend the time period described in this Evidence
of Coverage for its final decision on appeal to provide You with a reasonable opportunity to respond to such
new or additional evidence or rationale. If the initial benefit determination regarding the claim is based in
whole or in part on a medical judgment, the appeal will be conducted by individuals associated with HMO
and/or by external advisors, but who were not involved in making the initial denial of Your claim. No
deference will be given to the initial Adverse Benefit Determination. Before You or Your authorized
representative may bring a cause of action pursuant to Chapter 88 of the Texas Civil Practice and Remedies
NOTICE-ABD-IND-HMO-22
4
NOTICE
Adverse Benefit Determinations
Code, the claimant must exhaust the appeal process and must raise all issues with respect to a claim and
must file an appeal or appeals and the appeals must be finally decided by the HMO.
If You have any questions about the claims procedures or the review procedure, write to the HMO's
Administrative Office or call the toll-free Customer Service Helpline number shown on Your identification
card.
Timing of Appeal Determinations
HMO will render a determination of the non-urgent concurrent or pre-service appeal as soon as practical, but in no
event more than 30 days after the appeal has been received by HMO.
HMO will render a determination of the post-service appeal as soon as practical, but in no event more than 60 days
after the appeal has been received by HMO.
If You Need Assistance. If You have any questions about the claims procedures or the review procedure, write or
call the HMO at 1-888-697-0683. The Customer Service Helpline is accessible from 8:00 A.M. to 8:00 P.M.,
Monday through Friday.
Claim Review Section
Blue Cross and Blue Shield of Texas
P. O. Box 660044
Dallas, Texas 75266-0044
If
You need assistance with the internal claims and appeals or the external review processes that are described below,
You may call the number on the back of Your identification card for contact information.
Notice of Appeal Determination
HMO will notify the party filing the appeal, You, and, if a clinical appeal, any health care provider who
recommended the services involved in the appeal, orally of its determination followed-up by a written notice of the
determination.
The written notice to You or Your authorized representative will include:
The reasons for the determination;
A reference to the benefit plan provisions on which the determination is based on and or the contractual,
administrative or protocol for the determination;
Subject to privacy laws and other restrictions, if any, the identification of the claim, date of service, health
care provider, claim amount (if applicable), and a statement describing denial codes with their meanings
and the standards used. Upon request, diagnosis/treatment codes with their meanings and the standards
used are also available;
An explanation of HMO's external review processes (and how to initiate an external review);
In certain situations, a statement in non-English language(s) that written notice of claim denials and certain
other benefit information may be available (upon request) in such non-English language(s);
In certain situations, a statement in non-English language(s) that indicates how to access the language
services provided by HMO;
The right to request, free of charge, reasonable access to and copies of all documents, records and other
information relevant to the claim for benefits;
NOTICE-ABD-IND-HMO-22
5
NOTICE
Adverse Benefit Determinations
Any internal rule, guideline, protocol or other similar criterion relied on in the determination, and a
statement that a copy of such rule, guideline, protocol or other similar criterion will be provided free of
charge on request;
An explanation of the scientific or clinical judgment relied on in the determination, or a statement that such
explanation will be provided free of charge upon request;
A description of the standard that was used in denying the claim and a discussion of the decision; and
Contact information for applicable office of health insurance consumer assistance or ombudsman.
If HMO denies Your appeal, in whole or in part or You do not receive timely decision, You may be able to request
an external review of Your claim by an independent third party, who will review the denial and issue a final decision.
Note: You have the right to immediate review by an Independent Review Organization and do not have to comply
with the internal appeal process in life-threatening or urgent care circumstances, if HMO has discontinued
prescription drugs or intravenous infusions for which You were receiving health benefits under the plan, or if You
do not receive a timely decision on Your appeal.
How to Appeal a Final Adverse Determination to an Independent Review Organization
(IRO)
External Review Criteria
External Review is available for Adverse Benefit Determinations and Final Adverse Benefit Determinations that
involve rescission and determinations that involve medical judgment including, but not limited to, those based on
requirements for medical necessity, appropriateness, health care setting, level of care, or effectiveness or a covered
benefit; determinations that a treatment is experimental or investigational; determinations whether You are entitled
to a reasonable alternative standard for a reward under a wellness program; or a determination of compliance with
the nonquantitative treatment limitation provisions of the Mental Health Parity and Addiction Equity Act.
Standard External Review
You or Your authorized representative (as described above) may make a request for a standard external review or
expedited external review of an Adverse Benefit Determination or Final Internal Adverse Benefit Determination by
an Independent Review Organization (IRO).
1.
Request for external review. Within four months after the date of receipt of a notice of an Adverse Benefit
Determination or Final Internal Adverse Benefit Determination from the HMO, You or Your authorized
representative must file Your request for standard external review.
2.
Preliminary review. Within five business days following the date of receipt of the external review request,
the HMO must complete a preliminary review of the request to determine whether:
a.
You are, or were, covered under the plan at the time the health care item or service was requested;
b.
The Adverse Benefit Determination or the Final Adverse Internal Benefit Determination does not
relate to Your failure to meet the requirements for eligibility under the terms of the plan (e.g., worker
classification or similar determination);
c.
You have exhausted the HMO's internal appeal process unless You are not required to
exhaust the internal appeals process under the interim final regulations. Please read the
Exhaustion section below for additional information and exhaustion of the internal
appeal process; and
d.
You or Your authorized representative have provided all the information and forms required to
process an external review.
NOTICE-ABD-IND-HMO-22
6
NOTICE
Adverse Benefit Determinations
You will be notified within one business day after we complete the preliminary review if Your request is
eligible or if further information or documents are needed. You will have the remainder of the four-month
external review request period (or 48 hours following receipt of the notice), whichever is later, to perfect
the request for external review. If Your claim is not eligible for external review, we will outline the reasons
it is ineligible in the notice, and provide contact information for the Department of Labor's Employee
Benefits Security Administration (toll-free number 1-866-444-EBSA (3272)) and or state consumer
ombudsman as appropriate.
3.
Referral to Independent Review Organization (IRO). When an eligible request for external review is
completed within the time period allowed, the HMO will assign the matter to an IRO. The IRO assigned
will be accredited by URAC or by similar nationally-recognized accrediting organization. Moreover, the
HMO will ensure that the IRO is unbiased and independent. Accordingly, the HMO must contract with at
least three IROs for assignments under the plan and rotate claims assignments among them (or incorporate
other independent, unbiased methods for selection of IROs, such as random selection). In addition, the
IRO may not be eligible for any financial incentives based on the likelihood that the IRO will support the
denial of benefits.
The IRO must provide the following:
a.
Utilization of legal experts where appropriate to make coverage determinations under the plan.
b.
Timely notification to You or Your authorized representative, in writing, of the request's eligibility
and acceptance for external review. This notice will include a statement that You may submit in
writing to the assigned IRO within 10 business days following the date of receipt of the notice
additional information that the IRO must consider when conducting the external review. The IRO
is not required to, but may, accept and consider additional information submitted after 10 business
days.
c.
Within five business days after the date of assignment of the IRO, the HMO must provide to the
assigned IRO the documents and any information considered in making the Adverse Benefit
Determination or Final Internal Adverse Benefit Determination. Failure by the HMO to timely
provide the documents and information must not delay the conduct of the external review. If the
HMO fails to timely provide the documents and information, the assigned IRO may terminate the
external review and make a decision to reverse the Adverse Benefit Determination or Final Internal
Adverse Benefit Determination. Within one business day after making the decision, the IRO must
notify the HMO and You or Your authorized representative.
d. Upon receipt of any information submitted by You or Your authorized representative, the assigned
IRO must within one business day forward the information to the HMO. Upon receipt of any such
information, the HMO may reconsider the Adverse Benefit Determination or Final Internal Adverse
Benefit Determination that is the subject of the external review. Reconsideration by the HMO must
not delay the external review. The external review may be terminated as a result of the
reconsideration only if the HMO decides, upon completion of its reconsideration, to reverse the
Adverse Benefit Determination or Final Internal Adverse Benefit Determination and provide
coverage or payment. Within one business day after making such a decision, the HMO must provide
written notice of its decision to You and the assigned IRO. The assigned IRO must terminate the
external review upon receipt of the notice from the HMO.
e.
Review all of the information and documents timely received. In reaching a decision, the assigned
IRO will review the claim de novo and not be bound by any decisions or conclusions reached during
the HMO's internal claims and appeals process. In addition to the documents and information
provided, the assigned IRO, to the extent the information or documents are available and the IRO
considers them appropriate, will consider the following in reaching a decision:
1.
Your medical records;
NOTICE-ABD-IND-HMO-22
7
NOTICE
Adverse Benefit Determinations
2.
The attending health care professional's recommendation;
3.
Reports from appropriate health care professionals and other documents submitted by the
HMO, You, or Your treating provider;
4.
The terms of Your plan to ensure that the IRO's decision is not contrary to the terms of the
plan, unless the terms are inconsistent with applicable law;
5.
Appropriate practice guidelines, which must include applicable evidence-based standards and
may include any other practice guidelines developed by the Federal government, national or
professional medical societies, boards, and associations;
6.
Any applicable clinical review criteria developed and used by HMO, unless the criteria are
inconsistent with the terms of the plan or with applicable law; and
7.
The opinion of the IRO's clinical reviewer or reviewers after considering information
described in this notice to the extent the information or documents are available and the clinical
reviewer or reviewers consider appropriate.
f.
Written notice of the final external review decision must be provided within 45 days after the IRO
receives the request for the external review. The IRO must deliver the notice of final external
review decision to the HMO and You or Your authorized representative.
g.
The notice of final external review decision will contain:
1.
A general description of the reason for the request for external review, including
information sufficient to identify the claim (including the date or dates of service, the health
care provider, the claim amount (if applicable), the diagnosis code and its corresponding
meaning, the treatment code and its corresponding meaning, and the reason for the previous
denial);
2. The date the IRO received the assignment to conduct the external review and the date of
the IRO decision;
3.
References to the evidence or documentation, including the specific coverage provisions
and evidence-based standards, considered in reaching its decision;
4.
A discussion of the principal reason or reasons for its decision, including the rationale for
its decision and any evidence-based standards that were relied on in making its decision;
5.
A statement that the determination is binding except to the extent that other remedies may
be available under State or Federal law to either the HMO or You or your authorized
representative;
6.
A statement that judicial review may be available to You or Your authorized representative;
and
7.
Current contact information, including phone number, for any applicable office of health
insurance consumer assistance or ombudsman established under PHS Act section 2793.
h.
After a final external review decision, the IRO must maintain records of all claims and notices
associated with the external review process for six years. An IRO must make such records
available for examination by the HMO, State or Federal oversight agency upon request, except
where such disclosure would violate State or Federal privacy laws, and You or Your authorized
representative.
NOTICE-ABD-IND-HMO-22
8
NOTICE
Adverse Benefit Determinations
4. Reversal of plan's decision. Upon receipt of a notice of a final external review decision reversing the
Adverse Benefit Determination or Final Internal Adverse Benefit Determination, the HMO must
immediately provide coverage or payment (including immediately authorizing or immediately paying
benefits) for the claim.
Expedited External Review
1.
Request for expedited external review. You may request for an expedited external review with the HMO
at the time You receive:
a.
An Adverse Benefit Determination, if the Adverse Benefit Determination involved a medical
condition of Yours for which the timeframe for completion of an expedited internal appeal under
the interim final regulations would seriously jeopardize Your life or health or would jeopardize Your
ability to regain maximum function and You have filed a request for an expedited internal appeal;
or
b.
A Final Internal Adverse Benefit Determination, if the determination involved a medical condition
of Yours for which the timeframe for completion of a standard external review would seriously
jeopardize Your life or health or would jeopardize Your ability to regain maximum function, or if
the Final Internal Adverse Benefit Determination concerns an admission, availability of care,
continued stay, or health care item or service for which You received emergency services, but have
not been discharged from a facility.
2. Preliminary review. Immediately upon receipt of the request for expedited external review, the HMO
must determine whether the request meets the reviewability requirements set forth in the Standard
External Review section above. The HMO must immediately send You a notice of its eligibility
determination that meets the requirements set forth in Standard External Review section above.
3.
Referral to Independent Review Organization (IRO). Upon a determination that a request is eligible
for external review following the preliminary review, the HMO will assign an IRO pursuant to the
requirements set forth in the Standard External Review section above. The HMO must provide or
transmit all necessary documents and information considered in making the Adverse Benefit
Determination or Final Internal Adverse Benefit Determination to the assigned IRO electronically or by
telephone or facsimile or any other available expeditious method.
The assigned IRO, to the extent the information or documents are available and the IRO considers them
appropriate, must consider the information or documents described above under the procedures for standard
review. In reaching a decision the assigned IRO must review the claim de novo and is not bound by any
decisions or conclusions reached during the HMO's internal claims and appeals process.
4.
Notice of final external review decision. The assigned IRO will provide notice of the final external review
decision, in accordance with the requirements set forth in the Standard External Review section above,
as expeditiously as Your medical condition or circumstances require, but in no event more than 72 hours
after the IRO receives the request for an expedited external review. If the notice is not in writing, within
48 hours after the date of providing verbal notice, the assigned IRO must provide written confirmation of
the decision to the HMO and You or Your authorized representative.
Exhaustion
For standard internal review, You have the right to request external review once the internal review process has been
completed and You have received the Final Internal Adverse Benefit Determination. For expedited internal review,
You may request external review simultaneously with the request for expedited internal review. The IRO will
determine whether or not Your request is appropriate for expedited external review or if the expedited internal
review process must be completed before external review may be requested.
NOTICE-ABD-IND-HMO-22
9
NOTICE
Adverse Benefit Determinations
You will be deemed to have exhausted the internal review process and may request external review if the HMO
waives the internal review process or the HMO has failed to comply with the internal claims and appeals process
other than a de minimis failure. In the event You have been deemed to exhaust the internal review process due to
the failure by the HMO to comply with the internal claims and appeals process other than a de minimis failure, You
also have the right to pursue any available remedies under State law.
The internal review process will not be deemed exhausted based on de minimis violations that do not cause, and are
not likely to cause, prejudice or harm to You SO long as the HMO demonstrates that the violation was for good cause
or due to matters beyond the control of the HMO and that the violation occurred in the context of an ongoing, good
faith exchange of information between You and the HMO.
External review may not be requested for an Adverse Benefit Determination involving a claim for benefits for a
health care service that You have already received until the internal review process has been exhausted.
NOTICE-ABD-IND-HMO-22
10
NOTICE
INTER-PLAN ARRANGEMENTS NOTICE
BLUE CROSS AND BLUE SHIELD OF TEXAS, A DIVISION OF HEALTH CARE SERVICE
CORPORATION
Inter-Plan Arrangements
Out-of Area Services
Blue Cross and Blue Shield of Texas has a variety of relationships with other Blue Cross and/or Blue Shield Plans
and their Licensed Controlled Affiliates ("Licensees") referred to generally as "Inter-Plan Arrangements."
Whenever you obtain healthcare services outside of our Service Area, the claims for these services may be processed
through one of these Inter-Plan Arrangements.
Typically, when accessing care outside our Service Area, you will obtain care from healthcare Providers that have
a contractual agreement (i.e., are "Participating Providers") with the local Blue Cross and/or Blue Shield Licensee
in that other geographic area ("Host Blue"). In some instances, you may obtain care from Non-Participating
Providers. Our payment practices in both instances are described below.
We cover only limited healthcare services received outside of our Service Area. As used in this section, "Covered
Services" include Emergency Care, Urgent Care, and follow-up care obtained outside the geographic area we serve.
Any other services will not be covered when processed through any Inter-Plan Arrangements, unless authorized by
your Primary Care Physician/Practitioner ("PCP")/Blue Cross and Blue Shield of Texas.
A. BlueCard@Program
Under the BlueCard Program, when you obtain Covered Services within the geographic area served by a Host
Blue, we will remain responsible for what we agreed to in the contract. However the Host Blue is responsible
for contracting with and generally handling all interactions with its Participating healthcare Providers.
The BlueCard Program enables you to obtain Covered Services, as defined above, from a healthcare Provider
participating with a Host Blue, where available. The Participating healthcare Provider will automatically file a
claim for the Covered Services provided to you, SO there are no claim forms for you to fill out. You will be
responsible for the Member Copayment amount indicated in the Evidence of Coverage/Policy, Schedule of
Copayments and Benefit Limits.
Emergency Care Services: If you experience a Medical Emergency while traveling outside our Service Area,
go to the nearest Emergency or urgent care facility.
Whenever You receive Covered Services and the claim is processed through the BlueCard Program, the amount
you pay for such services, if not a flat dollar Copayment, is calculated based on the lower of:
the billed covered charges for the Covered Services, or
the negotiated price that the Host Blue makes available to us.
Often, this "negotiated price" is a simple discount that reflects the actual price the Host Blue pays to your
healthcare Provider. Sometimes, it is an estimated price that takes into account special arrangements with an
individual Provider or a provider group that may include settlements, incentive payments, and/or other credit
or charges. Occasionally, it may be an average price based on a discount that results in expected average savings
for similar types of healthcare Providers after taking into account the same types of transactions as with an
estimated price.
Estimated pricing and average pricing also take into account adjustments to correct for over- or underestimation
of past pricing of claims, as noted above. However, such adjustments will not affect the price we use for your
claim because they will not be applied after a claim has already been paid.
Notice-2022 TX BlueCard-HMO-Ind
NOTICE
Federal or state laws or regulations may require a surcharge, tax or other fee that applies to insured accounts. If
applicable, Blue Cross and Blue Shield of Texas will include any such surcharge, tax or other fee as part of the
claim charge passed on to you. If federal law or any state laws mandate other liability calculation methods,
including a surcharge, HMO would then calculate your liability for any Covered Services according to the
applicable law in effect when care is received.
B. Non-Participating Healthcare Providers outside our Service Area
Liability Calculation
Except for Emergency Care and Urgent Care, services received from a Non-Participating Provider
outside of our Service Area will not be covered.
For Emergency Care and Urgent Care services received from Non-Participating Providers within
the state of Texas, please refer to the "Emergency Services" section of this benefit booklet.
For Emergency Care and Urgent Care services that are provided outside of the state of Texas by a
Non-Participating Provider, the amount(s) you pay for such services will be calculated using the
methodology described in the "Emergency Services" section for Non-Participating Providers
located inside our Service Area. You may be responsible for the difference between the amount
that the Non-Participating Provider bills and the payment the HMO will make for the Covered
Services as set forth in this paragraph.
Federal or state law, as applicable, will govern payments for out-of-network emergency services.
C. Blue Cross Blue Shield Global Core
If you are outside the United States, the Commonwealth of Puerto Rico and the U.S. Virgin Islands, you
may be able to take advantage of Blue Cross Blue Shield Global Core when accessing Covered Services.
Blue Cross Blue Shield Global Core is unlike the BlueCard Program available in the United States, the
Commonwealth of Puerto Rico and the U.S. Virgin Islands in certain ways. For instance, although Blue
Cross Blue Shield Global Core assists you with accessing a network of inpatient, outpatient and professional
providers, the network is not served by a Host Blue. As such, when you receive care from providers outside
the United States, the Commonwealth of Puerto Rico and the U.S. Virgin Islands, you will typically have
to pay the providers and submit the claims yourself to obtain reimbursement for these services.
If you need medical assistance services (including locating a doctor or hospital) outside the United States,
the Commonwealth of Puerto Rico and the U.S. Virgin Islands, you should call the service center at
1.800.810.BLUE (2583) or call collect at 1.804.673.1177, 24 hours a day, seven days a week. An assistance
coordinator, working with a medical professional, will arrange a physician appointment or hospitalization,
if necessary.
Inpatient Services
In most cases, if you contact the service center for assistance, hospitals will not require you to pay for
covered inpatient services, except for your cost-share amounts/deductibles, coinsurance, etc. In such
cases, the hospital will submit your claims to the service center to begin claims processing. However,
if you paid in full at the time of service, you must submit a claim to receive reimbursement for Covered
Services.
You must contact Blue Cross and Blue Shield of Texas to obtain Prior Authorization for non-
emergency inpatient services.
Outpatient Services
Physicians, urgent care centers and other outpatient providers located outside the United States, the
Commonwealth of Puerto Rico and the U.S. Virgin Islands will typically require you to pay in full at
the time of service. You must submit a claim to obtain reimbursement for Covered Services.
Submitting a Blue Cross Blue Shield Global Core Claim
Notice-2022 TX BlueCard-HMO-Ind
NOTICE
When you pay for Covered Services outside the BlueCard service area, you must submit a claim to obtain
reimbursement. For institutional and professional claims, you should complete a Blue Cross Blue Shield Global
Core International claim form and send the claim form the provider's itemized bill(s) to the service center (the
address is on the form) to initiate claims processing. Following the instructions on the claim form will help ensure
timely processing of your claim. The claim form is available from Blue Cross and Blue Shield of Texas, the
service center or online at www.bcbsglobalcore.com. If you need assistance with your claim submission, you
should call the service center at 1.800.810.BLUE (2583) or call collect at 1.804.673.1177, 24 hours a day, seven
days a week.
Notice-2022 TX BlueCard-HMO-Ind
NOTICE TO BLUE CROSS BLUE SHIELD
OF TEXAS CONTRACT HOLDERS
You are hereby notified that you are a member of Health Care Service Corporation, a Mutual Legal Reserve
Company, and are entitled to vote either in person, by its designated representative or by proxy at all meetings
of members of said company. The annual meeting is held at its principal office at 300 East Randolph Street,
Chicago, Illinois each year on the last Tuesday in October at 12:30 p.m.
NOTICE - Annual Meeting
NOTICE OF CERTAIN MANDATORY BENEFITS
This notice is to advise you of certain coverage and/or benefits provided by your contract with Blue Cross
and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve
Company, an Independent Licensee of the Blue Cross and Blue Shield Association.
Mastectomy or Lymph Node Dissection
Minimum Inpatient Stay: If due to treatment of breast cancer, any person covered by this plan has either a
mastectomy or a lymph node dissection, this plan will provide coverage for inpatient care for a minimum
of:
a.
48 hours following a mastectomy;
b.
24 hours following a lymph node dissection.
The minimum number of inpatient hours is not required if the covered person receiving the treatment and
the attending physician determine that a shorter period of inpatient care is appropriate.
Prohibitions: We may not (a) deny any covered person eligibility or continued eligibility or fail to renew
this plan solely to avoid providing the minimum inpatient hours; (b) provide money payments or rebates
to encourage any covered person to accept less than the minimum inpatient hours; (c) reduce or limit the
amount paid to the attending physician, or otherwise penalize the physician, because the physician
required a covered person to receive the minimum inpatient hours; or (d) provide financial or other
incentives to the attending physician to encourage the physician to provide care that is less than the
minimum hours.
Coverage and/or Benefits for Reconstructive Surgery After Mastectomy -Enrollment
Coverage and/or benefits are provided to each covered person for reconstructive surgery after mastectomy,
including;
a.
all stages of the reconstruction of the breast on which the mastectomy was performed;
b.
surgery and reconstruction of the other breast to achieve a symmetrical appearance; and
C.
prostheses and treatment of physical complications, including lymphedemas, at all stages of the
mastectomy.
The coverage and/or benefits must be provided in a manner determined to be appropriate in consultation
with the covered person and the attending physician.
Deductibles, coinsurance and copayment amounts will be the same as those applied to other similarly
covered medical services as shown on the Schedule of Copayments and Benefit Limits.
Prohibitions: We may not (a) offer the covered person a financial incentive to forego breast reconstruction
or waive the coverage and/or benefits shown above; (b) condition, limit, or deny any covered person's
eligibility or continued eligibility to enroll in the plan or fail to renew this plan solely to avoid providing
the coverage and/or benefits shown above; or (c) reduce or limit the amount paid to the physician or
provider, nor otherwise penalize, or provide a financial incentive to induce the physician or provider to
provide care to a covered person in a manner inconsistent with the coverage and/or benefits shown above.
Examinations for Detection of Prostate Cancer
Benefits are provided for each covered male for an annual medically recognized diagnostic examination
for the detection of prostate cancer. Benefits include:
TX-I-H-NMB-0124
1
NOTICE OF CERTAIN MANDATORY BENEFITS
a physical examination for the detection of prostate cancer; and
a prostate-specific antigen test for each covered male who is
at least 50 years of age; or
at least 40 years of age with a family history of prostate cancer or other prostate cancer risk factor.
Inpatient Stay following Birth of a Child
For each person covered for maternity/childbirth benefits, we will provide inpatient care for the mother
and her newborn child in a health care facility for a minimum of:
(a) 48 hours following an uncomplicated vaginal delivery, and
(b) 96 hours following an uncomplicated delivery by cesarean section.
This benefit does not require a covered female who is eligible for maternity/childbirth benefits to (a) give
birth in a hospital or other health care facility or (b) remain in a hospital or other health care facility for
the minimum number of hours following birth of the child.
If a covered mother or her newborn child is discharged before the 48 or 96 hours has expired, we will
provide coverage for post-delivery care. Post-delivery care includes parent education, assistance and
training in breast-feeding and bottle-feeding and the performance of any necessary and appropriate clinical
tests. Care will be provided by a physician, registered nurse or other appropriate licensed health care
provider, and the mother will have the option of receiving the care at her home, the health care provider's
office or a health care facility.
Since we provide in-home post-delivery care, we are not required to provide the minimum number of
hours outlined above unless (a) the mother's or child's physician determines the inpatient care is medically
necessary, or (b) the mother requests the inpatient stay.
Prohibitions. We may not (a) modify the terms of this coverage based on any covered person requesting
less than the minimum coverage required; (b) offer the mother financial incentives or other compensation
for waiver of the minimum number of hours required; (c) refuse to accept a physician's recommendation
for a specified period of inpatient care made in consultation with the mother if the period recommended
by the physician does not exceed guidelines for prenatal care developed by nationally recognized
professional associations of obstetricians and gynecologists or pediatricians; (d) reduce payments or
reimbursements below the usual and customary rate; or (e) penalize a physician for recommending
inpatient care for the mother and/or the newborn child.
Coverage for Tests for Detection of Colorectal Cancer
Benefits are provided, for each person enrolled in the plan who is 45 years of age or older and at normal
risk for developing colon cancer, for expenses incurred in conducting a medically recognized screening
examination for the detection of colorectal cancer. Benefits include the covered person's choice of:
(a) a fecal occult blood test performed annually and a flexible sigmoidoscopy performed every five
years, or
(b) a colonoscopy performed every 10 years.
TX-I-H-NMB-0124
2
NOTICE OF CERTAIN MANDATORY BENEFITS
Coverage of Tests for Detection of Human Papillomavirus, Ovarian Cancer, and
Cervical Cancer
Coverage is provided for each woman enrolled in the plan who is 18 years of age or older for expenses
incurred for an annual, medically recognized diagnostic examination for the early detection of ovarian and
cervical cancer. Coverage required under this section includes a CA 125 blood test and, at a minimum, a
conventional Pap smear screening or a screening using liquid-based cytology methods, as approved by the
FDA, alone or in combination with a test approved by the FDA for the detection of the human
papillomavirus.
Treatment of Acquired Brain Injury
Your health benefit plan coverage for an acquired brain injury includes the following services:
a.
cognitive rehabilitation therapy;
b. cognitive communication therapy;
C. neurocognitive therapy and rehabilitation;
d.
neurobehavioral, neurophysiological, neuropsychological and psychophysiological
testing and treatment;
e. neurofeedback therapy, remediation;
f.
post-acute transition services and community reintegration services, including
outpatient day treatment services or other post-acute care treatment services; and
g.
reasonable expenses related to periodic reevaluation of the care of an individual
covered under the plan who has incurred an acquired brain injury, has been
unresponsive to treatment, and becomes responsive to treatment at a later date, at
which time the cognitive rehabilitation services would be a covered benefit.
The fact that an acquired brain injury does not result in hospitalization or acute care treatment does not
affect the right of the insured or the enrollee to receive the preceding treatments or services commensurate
with their condition. Post-acute care treatment or services may be obtained in any facility where such
services may legally be provided, including acute or post-acute rehabilitation hospitals and assisted living
facilities regulated under the Health and Safety Code.
If any person covered by this plan has questions concerning the information above, please call Blue Cross
and Blue Shield of Texas at 1-888-697-0683 or write us at P.O. Box 660044, Dallas, Texas 75266-0044.
TX-I-H-NMB-0124
3
PLAN DESCRIPTION
AND
MEMBER HANDBOOK
Blue Cross and Blue Shield of Texas
(herein called "BCBSTX" or "HMO")
This plan is offered by the following organization, which
operates under Chapter 843 of the Texas Insurance Code:
BLUE CROSS AND BLUE SHIELD OF TEXAS,
A DIVISION OF HEALTH CARE SERVICE CORPORATION
1001 E. Lookout Drive
Richardson, TX 75082
Plan Description and Member Handbook
The following is a brief summary of the benefits, rights
and responsibilities under this plan. This document
may be delivered to You electronically. Any notices
included in this document may be sent to you
electronically by HMO. Paper copies are available
upon request. You can find more complete information
about this plan in the Evidence of Coverage
documents (EOC) which you will receive after you
enroll.
We want you to be satisfied with your new health care
program. If you would like more information about the
plan, a Customer Service representative will be happy
to help you. Call Customer Service Monday through
Friday from 7:30 a.m. to 6:00 p.m. CST at 1-888-697-
0683. You may also write HMO at:
HMO Customer Service
P.O. Box 660044
Dallas, Texas 75266-0044
Again, thank you for considering us for your health
care coverage.
If this plan is purchased through the Exchange (also known as health insurance marketplace),
BCBSTX is not the agent for the Exchange and is not responsible for the Exchange. All information
that you provide to the Exchange will be relied upon as accurate and complete.
You must promptly notify the Exchange and BCBSTX of any changes to such information.
TX-I-H-PD-HB-25-B
1
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
TABLE OF CONTENTS
MEDICALLY NECESSARY COVERED SERVICES AND BENEFITS
4
Hospitalization
4
Other Medical Services
4
Preventive Care
4
Behavioral Health Care
5
EMERGENCY CARE, AFTER HOURS CARE AND URGENT CARE
5
Medical Emergencies
5
After Hours Care
6
Urgent Care Services
6
Out-of-Area Services and Benefits
6
OUT-OF-NETWORK FACILITY-BASED PROVIDERS AND DIAGNOSTIC IMAGING AND LAB
PROVIDERS
7
YOUR FINANCIAL RESPONSIBILITIES
7
LIMITATIONS AND EXCLUSIONS
7
PRIOR AUTHORIZATION REQUIREMENTS, REFERRAL PROCEDURES AND OTHER REVIEW
REQUIREMENTS
7
CONTINUITY OF TREATMENT IN THE EVENT OF TERMINATION OF A NETWORK PROVIDER
8
COMPLAINT PROCEDURE FOR ENROLLEES: APPEAL OF ADVERSE DETERMINATION;
INDEPENDENT REVIEW ORGANIZATION PROCESS; AND NON-RETALIATION
9
NETWORK PROVIDERS
13
SERVICE AREA
15
GENERAL INFORMATION
15
Identification (ID) Card
15
RECEIVING CARE
15
Your Primary Care Physician/Practitioner (PCP)
15
Changing PCPs
16
ADDITIONAL INFORMATION
17
Status Changes
17
Duplication of Coverage and Coordination of Benefits
17
New Medical Technology
18
YOUR RIGHTS AND RESPONSIBILITIES
18
Your Rights
18
Your Responsibilities
18
TX-I-H-PD-HB-25-B
2
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
CONFIDENTIALITY AND ACCESS TO RECORDS
19
CUSTOMER SERVICE
20
Questions
20
TX-I-H-PD-HB-25-B
3
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
MEDICALLY NECESSARY COVERED SERVICES AND BENEFITS
The EOC contains specific information regarding health care benefits, Copayments, any other
amounts due, limitations and exclusions. You will receive this document after You enroll. To
obtain the most from Your health care coverage, please take time to review your EOC, Benefit
Highlights and attachments carefully and keep them for reference. A Benefit Highlights also
accompanies this Plan Description and Member Handbook. During enrollment, You will select
a Primary Care Physician/Practitioner (PCP) for Yourself and one for each of Your covered
Dependents. Your PCP can provide most of Your health care needs. A PCP may be a family or
general practitioner, Advanced Practice Nurse, Physician Assistant, internist, pediatrician or
Obstetrician/Gynecologist (OB/GYN). Please see the "Receiving Care" section below for more
information about PCPs.
The Copayment and any other Coinsurance or Deductible amount is determined by Your plan.
Consumer Choice plans do not include all state mandated health insurance benefits which
means these plans may include Deductibles and benefit limits that are not included on other
plans.
Hospitalization
If You need to be hospitalized, Your PCP or Participating OB/GYN can arrange for Your care at
a local Participating hospital. Your PCP or participating OB/GYN will make the necessary
arrangements (including Referrals) and keep You informed. HMO shall review the Referral
request and issue a determination indicating whether proposed services are approved
through Prior Authorization within 24 hours of the request by the PCP or Participating
OB/GYN. You may have to pay a Copayment and any other applicable Coinsurance or
Deductibles for some of these services, depending on Your plan.
When You think You need hospital care, in non-emergency situations, first call Your PCP.
Special rules apply in emergency situations or in cases where You are out of the area (see
"Emergency Care" section).
Other Medical Services
In addition to PCPs, Specialists, and hospitals, the network includes other Health Care
Professionals to meet Your needs. If You need diagnostic testing, laboratory services or other
health care services, Your PCP or Participating OB/GYN will coordinate Your care or refer You
to an appropriate setting. You may have to pay a Copayment and any other applicable
Coinsurance or Deductibles for some of these services, depending on Your plan.
Preventive Care
Preventive care is a key part of Your plan, which emphasizes staying healthy by covering:
Well-child care, including immunizations;
Prenatal and postnatal care;
Hearing loss screenings through 24 months;
Periodic health assessments;
Eye and ear screenings;
Annual well-woman exams, including, but not limited to, a conventional Pap smear;
Annual screening mammograms for females over age 35, or females with other risk
factors
Annual in home health assessment;
Bone mass measurement for osteoporosis;
TX-I-H-PD-HB-25-B
4
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
Colorectal cancer exams, preventive services, and lab tests that have in effect a rating
of "A" or "B" in the current recommendations of the United States Preventive Services
Task Force ("USPSTF") for persons 45 years of age and older;
Any other evidence-based items or services that have in effect a rating of "A" or "B"
in the current recommendations of the United States Preventive Services Task Force
("USPSTF") or as required by state law.
Behavioral Health Care
Your mental health benefits include outpatient and inpatient visits for crisis intervention and
evaluation. Please refer to Your EOC for additional information. To access mental health
services, call the designated behavioral health vendor listed on the back of Your ID card.
Prescription Drugs
To find out which prescription drugs are covered under a plan, You can review the applicable
drug list at www.bcbstx.com/member/prescription-drug-plan-information/drug-lists.) You may also
request a drug list exception. For information on how to request a drug list exception please refer to
Your Evidence of Coverage.
REMEMBER:
Your PCP or Participating OB/GYN will arrange for specialty care or hospitalization.
Preventive care is an important part of Your program to help You stay healthy. These services
can be provided or arranged by Your PCP.
Usually, a Copayment and any applicable Coinsurance or Deductible is all You will be responsible
for when You obtain services provided or arranged by Your PCP.
You won't have to file claims for services received from Participating Providers.
EMERGENCY CARE, AFTER HOURS CARE AND URGENT CARE
Medical Emergencies
Emergency care is defined as health care services provided in a Participating or non-Participating
hospital emergency facility, freestanding emergency medical care facility, or comparable facility to
evaluate and stabilize medical conditions of a recent onset and severity, including but not limited to
severe pain, that would lead a prudent layperson, possessing an average knowledge of medicine and
health, to believe that his or her condition, sickness, or injury is of such a nature that failure to get
immediate medical care could result in placing the patient's health in serious jeopardy, cause serious
impairment to bodily function, cause serious dysfunction of any organ or part of the body, cause
serious disfigurement or, in the case of a pregnant woman, cause serious jeopardy to the health of
the fetus.
In a medical emergency, seek care immediately. Present Your ID card to the hospital emergency room
or comparable facility. You or a family member should call Your PCP within 48 hours or as soon as
possible after receiving Emergency Care. This call is important so that Your PCP can coordinate or
provide any follow-up care required as a result of a medical emergency.
REMEMBER:
In an emergency, seek care immediately.
You or a family member should call Your PCP within 48 hours or as soon as possible after
receiving Emergency Care
TX-I-H-PD-HB-25-B
5
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
If post stabilization care is required after an Emergency Care condition has been treated and
stabilized, the treating Physician or Provider will contact HMO or its designee, who must approve or
deny such treatment within the time appropriate to the circumstances relating to the delivery of the
services and the condition of the patient, but in no case shall approval or denial exceed one hour
from the time of the request.
After Hours Care
HMO Participating Providers have systems in place to respond to Your needs when their business
offices are closed. These systems may include the use of an answering service or a recorded
telephone message informing patients how to access further care.
Urgent Care Services
Urgent Care services are covered when rendered by a Participating Urgent Care center Provider for
the immediate treatment of a medical condition that requires prompt medical attention but where a
brief time lapse before receiving services will not endanger life or permanent health and does not
require Emergency Care services.
Retail Health Clinics
Retail Health Clinics provide diagnosis and treatment of uncomplicated minor conditions in situations
that can be handled without a traditional PCP office visit, Urgent Care visit or Emergency Care visit.
A PCP Referral is not required to obtain Covered Services.
Virtual Visits
Virtual visits provide You with access to Virtual Network Providers that can provide diagnosis and
treatment of non-emergency medical and behavioral health conditions in situations that can be
handled without a traditional PCP office visit, behavioral health office visit, Urgent Care visit or
Emergency Care visit. Covered Services may be provided via a consultation with a licensed medical
professional through interactive audio via telephone or interactive audio-video via online portal or
mobile application. For information on accessing this service, You may access the website at
www.bcbstx.com or contact customer service at the toll-free number on the back of Your identification
card. A PCP Referral is not required to obtain Covered Services.
Note: Not all medical or behavioral health conditions can be appropriately treated through Virtual
Visits. The Virtual Network Provider will identify any condition for which treatment by an in-person
Provider is necessary.
Out-of-Area Services and Benefits
Emergency Services Outside the Service Area
In an emergency, go directly to the nearest Hospital. If You are outside the Service Area and require
medical care, You are covered for emergency services only.
Urgent Care Outside the Service Area
When You are traveling outside of Texas and You need Urgent Care that cannot be postponed until
You return home, the BlueCard® Program gives You the ability to obtain health care services through
a Blue Cross and Blue Shield-affiliated Physician or Hospital outside of Texas.
Follow these easy steps:
1. Locate a Participating Provider by calling BlueCard Access at 1-800-810-BLUE (2583) or visit
the BlueCard Doctor and Hospital Finder website (www.bcbs.com).
2. Call Your PCP for Referrals and for care requiring Prior Authorization.
3. Schedule an appointment directly with the Provider.
4. Present Your ID card.
TX-I-H-PD-HB-25-B
6
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
5. Pay any applicable Copayments, Coinsurance or Deductible.
6. Discuss follow-up care with Your PCP.
OUT-OF-NETWORK FACILITY-BASED PROVIDERS AND DIAGNOSTIC IMAGING AND
LAB PROVIDERS
In some instances where you do not have the ability to choose a network provider, such as when you
receive services from a non-participating facility-based provider in a network facility, or when you
receive services from a non-Participating laboratory or diagnostic imaging facility in connection with
care provided by Your Participating Provider. In these instances, Your services may be covered and
You would not be responsible for any amounts beyond the Copayment/Coinsurance or any
Deductibles. If You receive a bill from an out-of-network Provider in such circumstances please
contact HMO. If You elect to use out-of-network Providers for non-Emergency Care services and
supplies available from Participating Providers, benefits will not be covered.
YOUR FINANCIAL RESPONSIBILITIES
BCBSTX requires a Premium from you as a condition of coverage. A copayment and any applicable
coinsurance or deductible may be due at the time a participating provider renders service. Certain
copayment amounts and any applicable coinsurance or deductible and the corresponding types of
services are listed on your ID card. For a complete list, refer to the Schedule of Copayments and
Benefit Limits in your EOC. The copayment and any other coinsurance or deductible amount is
determined by your plan. Consumer Choice plans do not include all state mandated health insurance
benefits which means these plans may include deductibles and benefit limits that are not included on
other plans. Also, you will have to pay for services that are not covered by HMO.
HMO network physicians and providers have agreed to look only to HMO and not to its members for
payment of Covered Services. Usually, you are expected to pay nothing more than a copayment and
any applicable coinsurance or deductible to participating providers. You should not receive a bill for
services received from participating providers. If this occurs, call Customer Service to help determine
if the service is a covered benefit and/or to correct the problem.
LIMITATIONS AND EXCLUSIONS
Your EOC contains specific information including limitations and exclusions. Your EOC will include
prescription drug benefit exclusions and limitations. The Benefit Highlights also include a summary
of limitations and exclusions.
PRIOR AUTHORIZATION REQUIREMENTS, REFERRAL PROCEDURES AND OTHER
REVIEW REQUIREMENTS
Except for emergency care, your PCP or OB/GYN must authorize all Referrals in advance. When
your PCP refers you for care, this helps ensure that you receive care that is medically necessary and
appropriate. If your PCP or OB/GYN cannot render the services you require, then the PCP or OB/GYN
will refer you to the provider(s) you need. Any Referral services will be subject to all of the terms,
conditions, limitations and exclusions of the HMO plan. Please see the "Receiving Care" section
below for more information about PCPs.
Emergency care services for screening and stabilization do not require prior authorization. Routine
requests for prior authorization for inpatient admissions are requested by registered nurses who
utilize a system of clinical protocols and criteria to determine the following:
Medical necessity of the requested care;
Appropriateness of the location and level of care;
Appropriateness of the length of stay; and/or
TX-I-H-PD-HB-25-B
7
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
Assignment of the next anticipated review point.
Concurrent Review
HMO supports the review of requests for continued services including inpatient hospital admissions.
Concurrent review is conducted both telephonically and via onsite review at selected facilities.
Reviews are conducted by registered nurses and include the following:
Evaluation for appropriateness (medical necessity/level of care/length of stay);
Evaluation and coordination of discharge planning requirements;
Referral to Case Management or Disease Management Programs; and/or
Identification of potential quality of care issues.
Retrospective Review
HMO may conduct reviews after services have been provided to the patient. Retrospective review
includes a medical necessity evaluation of the care/service provided to the member, and of physician
compliance to the Utilization/Case Management Program Requirements.
Case Management Review
The Case Management Department facilitates a collaborative process to access, plan, implement,
coordinate, monitor, and evaluate options and/or service to meet a member's health care needs
through communication and available resources to promote appropriate, cost-effective outcomes.
CONTINUITY OF TREATMENT IN THE EVENT OF TERMINATION OF A
NETWORK PROVIDER
If you are under the care of a participating provider who stops participating in HMO's network (for
reasons other than failure to meet applicable quality standards, including medical incompetence or
professional behavior, or for fraud), HMO will continue coverage for that provider's covered services
if all the following conditions are met:
you are undergoing a course of treatment for a serious and complex condition, you are
undergoing institutional or inpatient care, you are scheduled to undergo nonelective surgery
from the provider (including receipt of postoperative care from such provider with respect to
such surgery), you are pregnant or undergoing a course of treatment for the pregnancy, or
you are determined to be terminally ill. A serious and complex condition is one that (1) for an
acute illness, is serious enough to require specialized medical treatment to avoid the
reasonable possibility of death or permanent harm care (for example, you are currently
receiving chemotherapy, radiation therapy, or post-operative visits for a serious acute disease
or condition), and (2) for a chronic illness or condition, is (i) life-threatening, degenerative,
disabling or potentially disabling, or congenital, and (ii) requires specialized medical care over
a prolonged period of time.
HMO may request provider submits a request to HMO to continue coverage of your care that
identifies the condition for which you are being treated and, where required, indicates that the
provider reasonably believes that discontinuing treatment could cause you harm; and
the provider agrees to continue accepting the same reimbursement that applied when
participating in HMO's network, and not to seek payment from you for any amounts for which
you would not be responsible if the provider were still participating in HMO's network.
Continuity coverage shall continue until the treatment is complete but shall not extend for more than
ninety (90) days (or more than nine (9) months if you have been diagnosed with a terminal illness)
beyond the date the provider's termination takes effect. If you are past the thirteenth (13th) week of
pregnancy when the provider's termination takes effect, coverage may be extended through
TX-I-H-PD-HB-25-B
8
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
delivery, immediate postpartum care and the follow-up check-up within the first six (6) weeks of
delivery.
You have the right to appeal any decision made for a request for benefits under this subsection as
explained in the COMPLAINT PROCEDURE FOR ENROLLEES section of this handbook.
COMPLAINT PROCEDURE FOR ENROLLEES: APPEAL OF ADVERSE
DETERMINATION;
INDEPENDENT REVIEW ORGANIZATION PROCESS; AND NON-RETALIATION
Claim or Benefit Reconsideration
If a claim or request for benefits is partially or completely denied, you will receive a written
explanation of the reason for the denial and be entitled to a full review. If you wish to request a review
or have a question regarding the explanation of benefits, call or write Customer Service at the
telephone number or address on the back of your ID card. If you are still not satisfied, you may
request an appeal of the decision or file a complaint. You may obtain a review of the denial by
following the procedures set forth below and more fully in the Complaint and Appeal Procedures in
the EOC.
Complaints
There may be times when you find that you don't agree with a particular HMO policy or procedure or
benefit decision, or you are not satisfied with some aspect of the treatment by a participating provider.
We encourage you to communicate your dissatisfaction promptly and directly to the source of the
problem.
The goal of Customer Service is to prevent small problems from becoming large issues. To express
a complaint regarding any aspect of the HMO program, call or write Customer Service.
If an inquiry is not resolved promptly to your satisfaction, it will be handled according to the complaint
procedure described below.
Enrollee Complaint Procedure
A complaint is any dissatisfaction expressed orally or in writing, made by an enrollee or by someone
designated to act on behalf of an enrollee, to HMO regarding any aspect of our operation, such as
plan administration; procedures related to review or appeal of an adverse determination; the denial,
reduction, or termination of a service for reasons not related to medical necessity; the way a service
is provided; or disenrollment decisions. A complaint is not a misunderstanding or problem of
misinformation that is resolved promptly by clearing up the misunderstanding or supplying the
appropriate information to your satisfaction.
Also, a complaint does not include your oral or written dissatisfaction or disagreement with an adverse
determination (a denial of care or service based on a lack of medical necessity or appropriateness of
care).
Within five days of receiving your oral or written complaint, HMO will send you a letter acknowledging
the complaint, together with a description of our complaint process and timeframes. If the complaint
was received orally, we send a complaint form that you must fill out and return for prompt resolution.
After receiving your written complaint or the written complaint form, HMO will investigate your
concerns and send you a letter outlining and explaining the resolution. The letter includes a statement
of the specific medical and contractual reasons for the resolution including any benefit exclusion,
limitation or medical circumstance; additional information required to adjudicate a claim, if applicable,
and the specialization of any provider consulted. The total time for acknowledging, investigating and
resolving your written complaint will not exceed thirty calendar days from the date HMO receives your
written complaint or complaint form.
TX-I-H-PD-HB-25-B
9
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
If the complaint is not resolved to your satisfaction, you have the right to dispute the resolution by
following the complaint appeals process. A full description of the complaint appeals process will
accompany the complaint resolution.
Investigation and resolution of complaints concerning emergencies or denials of the continued
hospitalization are concluded in accordance with the medical or dental immediacy of the case, not to
exceed one business day from receipt of the complaint.
HMO is prohibited from retaliating against an individual because the individual has filed a complaint
against or appealed a decision of HMO. Also, we are prohibited from retaliating against a physician
or provider because the physician or provider has on your behalf, reasonably filed a complaint against
or appealed a decision of HMO.
Enrollee Complaint Appeals to HMO
The complaint appeals process allows an enrollee to dispute the complaint resolution before a
complaint appeal panel. Following receipt of your written request for a complaint appeal, you have
the opportunity to dispute the complaint resolution in person, in writing, by telephone, or by other
technological methods. HMO will send you an acknowledgement letter no later than five business
days after the date of receipt of your written request for appeal.
The complaint appeal panel is an advisory committee composed of an equal number of HMO staff,
physicians or other providers, and others covered by HMO. Participants of the complaint appeal panel
will not have been involved in the previously disputed decisions related to the complaint. Experienced
physicians or other providers review the case; the resolution recommended by the panel is
independent of any prior physician or provider determinations. If you are disputing specialty care, the
appeal panel must include a person who is a Specialist in the field of care being disputed. Persons
selected to participate on the complaint appeal panel are not HMO staff. The appeals process will not
exceed thirty calendar days from the date HMO receives the written request for appeal.
No later than the fifth business day before the scheduled meeting of the panel, HMO will supply you
or your designated representative with:
Any documents to be presented to the panel by HMO staff;
The specialization of any physicians or providers consulted during the investigation;
The name and affiliation of each HMO representative on the panel; and
The date and location of the hearing.
You are entitled to:
Appear in person by conference call or other appropriate technology or through a
representative, if the complainant is a minor or disabled, before the complaint appeal panel;
Present written or oral information to the appeal panel;
Present alternative expert testimony; and
Request the presence of and question any person responsible for making the prior
determination that resulted in the appeal.
You will receive a written decision of the complaint appeal. When appropriate, it includes specific
medical determination, clinical basis, contractual criteria used to reach the final decision and the toll-
free telephone number and address of the Texas Department of Insurance.
Upon request and free of charge, you are provided reasonable access to, and copies of all
documents, records and other information relevant to the claim or appeal, including:
Information relied upon in making the benefit determination;
TX-I-H-PD-HB-25-B
10
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
Information submitted, considered or generated in the course of making the benefit
determination, whether or not it was relied upon in making the benefit determination;
Descriptions of the administrative process and safeguards used in making the benefit
determination;
Records of any independent reviews conducted by HMO;
Medical judgments, including determinations about whether a particular service is
experimental, investigational or not medically necessary or appropriate; and
Expert advice and consultation obtained by HMO in connection with the denied claim, whether
or not the advice was relied upon in making the benefit determination.
Filing Complaints with the Texas Department of Insurance
Any person, including those who have attempted to resolve complaints through HMO's
enrollee complaint process, who is dissatisfied with the resolution, may report their
dissatisfaction to the Texas Department of Insurance, Consumer Protection, MC: CO-CP,
Texas Department of Insurance, PO Box 12030, Austin, TX 78711-2030.
There are two methods of filing a TDI complaint:
via mail;
via online at www.TDI.texas.gov.
The Texas Department of Insurance will investigate complaints against HMO within sixty (60) days of
receiving the complaint. The time necessary to complete an investigation may be extended if:
additional information is needed;
an on-site review is necessary;
complainant, HMO, or the physician or provider does not provide all documentation necessary
to complete the investigation; or
other circumstances beyond the control of the Texas Department of Insurance occur.
Appeal of Adverse Determinations
An adverse determination is a determination made by HMO or a utilization review agent physician
that health care services provided or proposed to be provided are experimental, investigational or not
medically necessary. An adverse determination is not a denial of health care services due to the
failure to request prospective or concurrent utilization review. In life-threatening or urgent care
circumstances, if HMO has discontinued coverage of prescription drugs or intravenous infusions for
which you were receiving health benefits under this Evidence of Coverage, or if you do not receive a
timely decision, you are entitled to an immediate appeal to an Independent Review Organization
("IRO") and are not required to comply with HMO's appeal of an Adverse Determination process. An
IRO is an organization independent of the HMO which may perform a final administrative review of
an Adverse Determination made by HMO.
HMO maintains an internal appeal system that provides reasonable procedures for the resolution of
an oral or written appeal concerning dissatisfaction or disagreement with an adverse determination.
The appeal of an adverse determination process is not part of the complaint process. You, your
designated representative or your physician or provider may initiate an appeal of an adverse
determination.
When services provided or proposed to be provided are deemed experimental, investigational or not
medically necessary, HMO or a utilization review agent will regard the expression of dissatisfaction
or disagreement as an appeal of an adverse determination.
Within five working days of your appeal request, HMO will send you a letter acknowledging the date
of receipt of the appeal and a list of documents you must submit. For oral appeals, we will also send
TX-I-H-PD-HB-25-B
11
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
you a one-page appeal form for completion that must be returned to HMO. HMO will provide a review
by a board certified physician or provider who has not already reviewed your case and who is of the
same or similar specialty as typically manages the medical condition, procedure or treatment under
review. We have thirty days from your appeal request to provide you written notice of the appeal
determination.
Note: If HMO is seeking to discontinue coverage of prescription drugs or intravenous infusions for
which you are receiving health benefits under the EOC, you will be notified no later than the 30th day
before the date on which coverage will be discontinued.
You will receive a written decision of the appeal that will include dental, medical and contractual
reasons for the resolution; clinical basis for the decision; specialization of provider consulted; notice
of your right to have an independent review organization review the denial; and TDI's toll free
telephone number and address.
Expedited Appeal of Adverse Determination Procedures
Investigation and resolution of appeals relating to ongoing emergencies or denials of continued
hospital stays, or the discontinuance by HMO of prescription drugs or intravenous infusions for which
you were receiving health benefits under the Evidence of Coverage, are referred directly to an
expedited appeal process and will be concluded in accordance with the medical or dental immediacy
of the case. In no event will the request for an expedited appeal exceed one business day from the
date all information necessary to complete the appeal request is received or three calendar days of
the appeal request, whichever is sooner. HMO will provide a review by a board certified physician or
provider who has not already reviewed your case and who is of the same or similar specialty as
typically manages the medical condition, procedure or treatment under review. That physician or
provider may interview you and will render a decision on the appeal. The initial notice of the decision
may be made orally with written notice of the determination following within three days.
Appeals Process to Independent Review Organization
An independent review organization is an organization independent of HMO that may perform a final
administrative review of an adverse determination made by us.
In a circumstance involving a life-threatening or urgent care circumstances, if HMO has discontinued
coverage of prescription drugs or intravenous infusions for which you were receiving health benefits
under the Evidence of Coverage, or if you do not receive a timely decision, you are entitled to an
immediate appeal to an independent review organization rather than going through HMO's appeal of
an adverse determination process.
The independent review organization process is not part of the complaint process, but is available
only for appeals of adverse determination.
You may request a review of an appeal of an adverse determination by the independent review
organization. HMO will adhere to the following guidelines/criteria:
Provide you, your designated representative, or your provider of record, information on how to
appeal the denial of an adverse determination to an independent review organization;
Provide this information at the initial adverse determination and the denial of the appeal;
Provide the appropriate form to complete;
You, a designated representative, or your provider of record must complete the form and return
it to HMO to begin the independent review process;
In life-threatening or urgent care situations, or if HMO has discontinued coverage of prescription
drugs or intravenous infusions for which you were receiving health benefits under the Evidence
of Coverage, you, your designated representative, or provider of record, may contact HMO by
telephone to request the review;
TX-I-H-PD-HB-25-B
12
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
Submit medical records, names of providers and any documentation pertinent to the adverse
determination to the independent review organization;
Comply with the determination by the independent review organization; and
Pay for the
independent review.
Upon request and free of charge you are provided reasonable access to, and copies of all documents,
records and other information relevant to the claim or appeal, including:
Information relied upon in making the benefit determination;
Information submitted, considered or generated in the course of making the benefit
determination, whether or not it was relied upon in making the benefit determination;
Descriptions of the administrative process and safeguards used in making the benefit
determination;
Records of any independent reviews conducted by HMO;
Medical judgments, including determinations about whether a particular service is
experimental, investigational or not medically necessary or appropriate; and
Expert advice and consultation obtained by HMO in connection with the denied claim, whether
or not the advice was relied upon in making the benefit determination.
The appeal process does not prohibit you from pursuing other appropriate remedies, including
injunctive relief, a declaratory judgment, or relief available under law, if exhausting the procedures of
HMO's process for appeal and review places your health in serious jeopardy.
NETWORK PROVIDERS
To find out more about HMO participating providers, refer to the website at www.bcbstx.com/find-a-
doctor-or-hospital for Provider Finder, an Internet-based provider directory. It has important
information about the locations and availability of providers, restrictions on accessibility and Referrals
to Specialists, and information about limited provider networks. You may also request a hard copy or
electronic copy of the provider directory, which is updated quarterly, by calling or writing Customer
Service. The directories can also be found at www.bcbstx.com. Upon admission to an inpatient facility,
(e.g. hospital or skilled nursing facility), a participating physician other than your PCP may direct and
oversee your care.
Your PCP will be the one you call when you need medical advice, when you are sick and when you
need preventive care such as immunizations.
Your PCP will play a key role in the delivery of your health care. The network to which your PCP
belongs will provide or arrange for all of your care, so make sure that your PCP's network includes
the Specialists and hospitals that you prefer.
If your PCP changes networks, you will be notified and will receive an updated ID card. You and your
covered dependents may select the same or a different provider network, and the same or a different
PCP within the network.
TX-I-H-PD-HB-25-B
13
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
The following demographics describe the network as of August 2023, that your Texas HMO Plan
provides access to for the provision of Covered Services.
Participating
Network
Enrollees
Providers
Specialty
Access
MyBlue Health
133,653
Internal Medicine
3,455
Yes
Network
Family/Gen. Practice
3,519
Yes
Pediatrics
1,585
Yes
Obstetrics and
1,120
Yes
Gynecology
Anesthesiology
2,934
Yes
Psychiatry
24
Yes
General Surgery
667
Yes
Acute Care Hospitals
60
Yes
For additional information regarding network adequacy please call the customer service
telephone number shown on the back of your identification card or visit the website at
www.bcbstx.com.
DIRECT ACCESS FOR OBSTETRICIAN/GYNECOLOGIST (OB/GYN) CARE
ATTENTION FEMALE MEMBERS: Your HMO plan provides direct access to participating
OB/GYNs for gynecologic and obstetric conditions, including annual well-woman exams and
maternity care, without first obtaining a Referral from a PCP or calling HMO. Your PCP or
participating OB/GYN will establish a Referral for you for any required obstetric/gynecologic specialty
care.
Your HMO has opted not to limit your selection of an OB/GYN to your PCP's network. It is not required
that you select an OB/GYN; you may choose to receive your OB/GYN services from your PCP.
If you need help in locating a participating OB/GYN in your area, refer to the online provider directory
(an Internet-based provider directory available on our website at www.bcbstx.com), or to your provider
directory, or call Customer Service at the telephone number on the back of your ID card for assistance.
TX-I-H-PD-HB-25-B
14
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
SERVICE AREA
For a map of the HMO service area, refer to the website at www.bcbstx.com/find-a-doctor-or-hospital
for Provider Finder, an Internet-based provider directory, or request a hard copy or electronic copy of
the provider directory by calling Customer Service.
GENERAL INFORMATION
Identification (ID) Card
Once enrolled, you and each of your covered dependents will receive an ID card. Please take a
moment to check the following information on the card for accuracy, and call Customer Service if
changes are needed.
Identification number;
Coverage effective date;
Your and/or your covered dependents' names;
Primary care physician/practitioner (or "PCP") name;
PCP telephone number.
Your ID card also shows certain copayments and any other amounts due for services that are part of
the plan you selected. The back of your ID card includes the toll-free Customer Service telephone
number.
Be sure to take your ID card with you when you seek health care. It has important information on it
that your PCP or other health care professional will need to know. Always present your ID card to the
medical office staff, so they can verify eligibility and collect the appropriate copayment and any other
amounts due.
If your ID card is lost or stolen, call Customer Service immediately and a new ID card will be sent to
you. Or you may go to the website at www.bcbstx.com, and print a temporary ID card or order a
replacement under the Blue Access for Members section. You will also receive an updated ID card if
you change your PCP, or if your PCP changes to another network.
REMEMBER:
Your EOC contains important details about your health care benefits. Please review them
carefully. Contact Customer Service if you have questions about your plan.
Your provider directory gives you a complete listing of participating providers in your area. Contact
Customer Service if you need assistance in locating a PCP in your area.
Take your ID card with you when you seek care. It has important information your provider needs
to know.
RECEIVING CARE
Your Primary Care Physician/Practitioner (PCP)
We encourage you to make an appointment with your PCP before you need health care so that you
can establish yourself as a patient. One of the advantages of establishing a physician/patient
relationship with your PCP is that your PCP becomes familiar with you and your medical history, which
helps make sure you receive the care that is right for you.
It is very important to visit or contact your PCP first when seeking medical care. Your PCP will either
treat you or refer you for specialty care. Your PCP will also coordinate any required hospital
admissions.
TX-I-H-PD-HB-25-B
15
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
REMEMBER:
Always see your PCP first when you need health care. Services received from any provider without a
Referral from your PCP will not be covered, except in emergency situations or for OB/GYN services
provided by a participating OB/GYN in your network, as described below.
Changing PCPs
Changing your PCP is easy. Simply use the online provider directory at www.bcbstx.com, refer to
your provider directory, or call Customer Service for assistance in selecting a new PCP in your area.
Sometimes a PCP may not be accepting new patients. When selecting a new PCP, you may call
Customer Service or the PCP's office and ask about availability. If the PCP is unavailable, Provider
Finder or Customer Service can help you find another physician in your area.
Once you've made your decision, either call Customer Service or complete a change form and submit
it to the Membership Department, P.O. Box 660819 Dallas, TX 75266-0819. You may also request
the transfer of your medical records from your previous PCP to the newly selected physician.
PCP changes become effective the first day of the month following HMO's receipt and approval of
your request. You will receive an updated ID card that shows your new PCP's name and phone
number. If you need health care but have not received your new ID card with your new PCP's name,
call Customer Service to verify that your request has been processed. You may also go to the website
at www.bcbstx.com, and print a temporary ID card under the Blue Access for Members section.
Making Appointments
You may make appointments for periodic health assessments at a time convenient for you.
If the nature of an illness warrants an urgent appointment, your PCP can generally fit you into his or
her schedule within a reasonable period of time. If your PCP cannot fit you in, he or she may direct
you to a designated back-up physician. If you need assistance, you may call Customer Service at the
telephone number on the back of your ID card.
If you need to change or cancel an appointment, be sure to call your PCP as soon as you can. When
you visit your PCP's office for Covered Services, you will pay only a copayment and any other
applicable coinsurance or deductibles for the office visit. There are no claims to file. If you need the
care of a Specialist, your PCP will refer you and will handle any Prior Authorization requirements for
you.
REMEMBER:
Have your health care provided or arranged by your PCP.
For obstetric or gynecologic conditions, you may directly access a participating OB/GYN (in the
same provider network as your PCP).
Contact Customer Service for assistance in changing your PCP.
It is important to schedule an appointment with your PCP as soon as you can. Contact Customer
Service if your PCP cannot fit you in.
Telehealth and Telemedicine Medical Services
Telehealth and Telemedicine Medical Services are covered as defined below and may require Prior
Authorization.
TX-I-H-PD-HB-25-B
16
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
Telehealth Service means a health service, other than a Telemedicine Medical Service, delivered by
a health professional licensed, certified, or otherwise entitled to practice in Texas and acting within
the scope of the health professional's license, certification, or entitlement to a patient at a different
physical location than the health professional using telecommunications or information technology.
Telemedicine Medical Services means a health care service delivered by a Physician licensed in
Texas, or a health professional acting under the delegation and supervision of Physician licensed in
Texas, and acting within the scope of the Physician's or health professional's license to a patient at a
different physical location than the Physician or health professional using telecommunication or
information technology.
ADDITIONAL INFORMATION
Status Changes
Your records are very important to us. Incorrect records can delay membership verification or medical
care, create problems in continuing coverage for a dependent, and possibly cost you money. To keep
your coverage up to date notify us of changes and notify the Exchange if this plan is purchased
through the Exchange. Completed forms must be received by HMO within 60 days from the date of
any change listed below:
Birth of a child;
Adoption or becoming a party in a suit for adoption, or legal guardianship;
Change of dependency status of a child;
Court-ordered dependents;
Loss of other health coverage;
Marriage;
Divorce;
Death;
Change of address; and
Change of telephone number.
Coverage will be automatic for subscriber or subscriber's spouse's newborn child for the first thirty-
one (31) days following the date of birth. Coverage will continue beyond the thirty-one (31) days only
if the child is an eligible dependent and You notify HMO (verbally or in writing) or submit an enrollment
application/change form to HMO timely and make or agree to make any additional Premium
payments.
Duplication of Coverage and Coordination of Benefits
Injuries and sometimes illnesses may be covered by other types of insurance such as auto,
homeowners or workers' compensation. Please call Customer Service in cases such as these for
information on what steps to take.
REMEMBER:
Notify BCBSTX and the Exchange (if purchased through the Exchange) of changes within 60
days of a change to your coverage.
Be sure to indicate any other health coverage you have, or contact Customer Service with this
information.
TX-I-H-PD-HB-25-B
17
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
It is important that you provide this information to us to allow coordination of payment of your claims
to ensure that claims are not paid twice. This helps keep your health care costs down.
New Medical Technology
HMO keeps abreast of medical breakthroughs, experimental treatments and newly approved
medication. The medical policy department evaluates new technologies, medical procedures, drugs
and devices for potential inclusion in the benefit packages we offer. Clinical literature and accepted
medical practice standards are assessed thoroughly with ongoing reviews and determinations made
by our Medical Policy Group.
YOUR RIGHTS AND RESPONSIBILITIES
You have certain rights and responsibilities when receiving health care services and should expect
the best possible care available. We have provided the following information, so you can be an
informed customer and active participant in your plan.
Your Rights
You have the right to:
Select or change your PCP and know the qualifications, titles and responsibilities of the
professionals responsible for your health care;
Receive prompt and appropriate treatment for physical or emotional disorders and participate
with your providers in decisions regarding your care;
Be treated with dignity, compassion and respect for your privacy;
Have a candid discussion of appropriate or medically necessary treatment options for your
condition, regardless of cost or benefit coverage;
Have all medical and other information held confidential unless disclosure is required by law
or authorized in writing by you;
Be provided with information about:
-
HMO,
-
Health care benefits,
-
Copayments, copayment limitations, and/or other charges,
-
Service access,
-
Changes and/or termination in benefits and participating providers,
-
Limitations and Exclusions;
Express opinions, concerns, and complaints in a constructive manner or appeal regarding any
aspect of the HMO;
Receive timely resolution of complaints or appeals through Customer Service and the
complaint procedure;
Have access to review by an Independent Review Organization;
Refuse treatment and be informed of the medical consequences that may be a result of your
decision; and
Make recommendations regarding your HMO rights and responsibilities policies.
Your Responsibilities
You have the responsibility to:
Meet all eligibility requirements;
TX-I-H-PD-HB-25-B
18
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
Identify yourself by presenting your ID card and pay the copayment and any other applicable
amount due at the time of service for network benefits;
Establish a physician/patient relationship with your PCP and seek your PCP's medical
advice/Referral for network services prior to receiving medical care, unless it is an emergency
situation or services are performed by your HMO participating OB/GYN;
Understand the medications you are taking and receive proper instructions on how to take
them;
Communicate complete and accurate medical information to health care providers;
Call in advance to schedule appointments with network providers and notify them prior to
canceling or rescheduling appointments;
Ask questions and follow instructions and guidelines given by providers to achieve and
maintain good health;
Discuss disagreements and/or misunderstandings regarding treatment from providers;
Notify your PCP or HMO within 48 hours or as soon as reasonably possible after receiving
emergency care services;
Provide, to the extent possible, information that HMO needs in order to administer your benefit
plan, including changes in your family status, address and phone numbers within 60 days of
the change;
Read your EOC for information about HMO benefits, limitations, and exclusions; and
Understand your health conditions, and participate to the degree possible in the development
of treatment goals mutually agreed upon between you and your provider.
CONFIDENTIALITY AND ACCESS TO RECORDS
We are required by federal and state law to maintain the privacy of your protected health information.
"Protected health information" (PHI) is information about you that may identify you and that relates to
your past, present or future physical or mental health or condition and related health care services.
With limited exceptions, your medical records may not be disclosed to others, including your
employer, without your written consent. You, or an individual acting on your behalf, may request
medical records for the purpose of providing care or resolving disputes related to coverage,
reimbursement, or complaints.
Routine consent signed at the time of enrollment permits us to release information for purposes of
quality assessment and measurement, treatment, coordination of care, accreditation, billing and other
uses. Identifiable information is minimized and protected from inappropriate disclosure.
You have a right to specifically approve the release of information beyond the uses identified in the
routine consent that you sign upon enrollment and, at other times, as needed for worker's
compensation claims, auto insurance claims, marketing or data used for research studies.
You may give us written authorization to use your PHI or to disclose it to another person only for the
purpose you designate. PHI may not be disclosed to your spouse or family without written
authorization from you or an authorized representative. Information regarding children under 18 years
of age may be released to a parent or legal guardian. If an adult is incapacitated, a legally appointed
guardian may act on their behalf. Unless you give us written authorization, we cannot use or disclose
your PHI for any reason except those described in the HIPAA Notice.
Participating providers must comply with applicable HIPAA laws, professional standards and policies
regarding the confidential treatment of medical information, including security measures to control
access to confidential information maintained in computer systems. Access to electronic files
containing information is to be protected and restricted to employees who have a business-related
need to know. Oral, written and electronic personal health information across the organization will be
kept confidential in accordance with applicable law.
TX-I-H-PD-HB-25-B
19
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
Blue Cross Blue Shield of Texas understands the importance of confidentiality and respects your right
to privacy. A summary of our privacy practices is available on the BCBSTX website at
www.bcbstx.com/legal-and-privacy/privacy-notice-and-formsor you may call Customer Service at the
telephone number on the back of your ID card to obtain a paper copy.
CUSTOMER SERVICE
Questions
If you have questions about your benefits, Customer Service representatives are available to help
you at the telephone number on the back of your ID card. Customer Service can also help if you want
to change your PCP. They will have an up-to-date list of participating providers in your area.
Customer Service can also assist you with special communications needs. If your first language is
not
English, you can ask to speak to a bilingual staff member (English or Spanish). Some written materials
(including this HMO handbook) are available in Spanish. Members may also ask for access to a
telephone-based translation service to assist with other languages.
BCBSTX provides TDD/TYY services and language assistance for incoming callers for deaf, hard-of-
hearing and speech-disabled members. Members can utilize their Tele Typewriter
(TTY)
or
Telecommunication Device (TDD) to access a teletype operator.
If you are not satisfied with service you have received, HMO has a formal complaint process you can
follow to advise us of issues related to quality of care or service. We monitor the care you receive
and follow through on all complaints and inquiries, because your satisfaction is important to us.
TX-I-H-PD-HB-25-B
20
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association
NOTICE OF RIGHT TO AN ADEQUATE NETWORK
A health maintenance organization (HMO) plan provides no benefits for services you receive from out-of-
network physicians or providers, with specific exceptions as described in your Evidence of Coverage and
below.
You have the right to an adequate network of in-network physicians and providers (known as
network Physicians and Providers).
If you believe that the network is inadequate, you may file a complaint with the Texas Department
of Insurance at: www.tdi.texas.gov/consumer/complfrm.html
If your HMO approves a Referral for out-of-network services because no network physician or
provider is available, or if you have received out-of-network emergency care, the HMO must, in
most cases, resolve the out-of-network physician's or provider's bill SO that you only have to pay
any applicable in-network copayment, coinsurance, and deductible amounts.
You may obtain a current directory of network physicians and providers at the following website:
www.bcbstx.com/find-a-doctor-or-hospital or by calling 1-888-697-0683 for assistance in finding
available network physicians and providers. If you relied on materially inaccurate directory information,
you may be entitled to have a claim by an out-of-network physician or provider paid as if it were from a
network physician or provider, if you present a copy of the inaccurate directory information to the HMO,
dated not more than 30 days before you received the service.
TX-I-H-PD-HB-25-B
21
Blue Cross and Blue Shield of Texas, a Division of Health Care Service Corporation, a Mutual Legal Reserve Company,
an Independent Licensee of the Blue Cross and Blue Shield Association''',
		user_input={
			"premium": 100,
			"budget": 200,
			"health_concerns": "Diabetes",
			"age": 30,
			"zip_code": "14127",
			"city": "OP",
			"state": "New York"
		}
	)

	asyncio.run(plan.ranking_logics())
	print(plan.scores)
	print(plan.pair_keys())
	print(plan.total_scores())


main()
