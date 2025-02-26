from google import genai
from google.genai import types
import pathlib
import httpx
import os
from dotenv import load_dotenv
import base64

load_dotenv()

## OF NOTE, set up a .env file in the same directory as this file with the following:
## GENAI_API = "YOUR_API_KEY"
## This is to keep the API key secure and not in the codebase. Please ask me for the key
## or just create your own through this link. Make sure creativity is set to 0.
## https://aistudio.google.com/prompts/1rPA9590dNh3Z1bsfi6QiLgtwKYInwN3a
key = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=key)

doc_url = "https://www.cms.gov/cciio/resources/files/downloads/sbc-sample.pdf"  # Replace with the actual URL of your PDF

# Retrieve and encode the PDF byte
filepath = pathlib.Path('file.pdf')
filepath.write_bytes(httpx.get(doc_url).content)


def generate(filepath):
    client = genai.Client(api_key=os.environ.get("GENAI_API_KEY"))

    prompt_text = (
        "You are a data scientist tasked with extracting data from a PDF file of "
        "an insurance plan. Your job is to parse the PDF and generate six CSV "
        "data rows—one for each CSV format specified. For each CSV, output only"
        " a single data row that precisely follows the provided column structure, "
        "without including the column headers. Do not include any additional commentary,"
        " explanations, or meta-comments about your process. Simply output the CSV data "
        "rows based solely on the information extracted from the PDF."
        
        'There are six CSVs you must output in total.'
        'CSV1 Columns: ""BUSINESS YEAR","STATE CODE","ISSUER ID","SOURCE NAME",'
        '"VERSION NUMBER","IMPORT DATE","STANDARD COMPONENT ID","PLAN ID",'
        '"BENEFIT NAME","IS EHB","IS STATE MANDATE","IS COVERED","QUANTITY '
        'LIMIT ON SVC","LIMIT QUANTITY","LIMIT UNIT","MINIMUM STAY",'
        'EXCLUSIONS,EXPLANATION,"EHB VAR REASON","IS SUBJECTED TO DED TIER 1",'
        '"IS SUBJECTED TO DED TIER 2","IS EXCLUDED FROM INN MOOP","IS EXCLUDED FROM OON MOOP"'
        
        'CSV1 Example: 2024,CT,76962,SERFF,1,2/12/2024,76962CT0010001,76962CT0010001-01,'
        '"Habilitation Services",Yes,,Yes,Yes,40,"Visit(s) per Year",,,,,,,No,No'

        'CSV2 Columns: "BUSINESS YEAR","STATE CODE","ISSUER ID","SOURCE NAME",'
        '"VERSION NUMBER","IMPORT DATE","PRODUCT ID","STANDARD COMPONENT ID",'
        '"DEPENDENT MAX AGE RULE","AGE DETERMINATION RULE","MINIMUM TOBACCO'
        ' FREE MONTHS RULE","COHABITATION RULE REQUIRED","COHABITATION RULE CODE",'
        '"MARKET COVERAGE","DENTAL ONLY PLAN","MEDICAL OR DENTAL RULE","MAX CHILDREN IN POLICY"'

        'CSV2 Example: 2024,CT,76962,SERFF,1,02-12-2024,,,26,"'
        'Age on effective date","Not Applicable",No,"Stepson or Stepdaughter",,,Medical,3'

        'CSV3 Columns: "BUSINESS YEAR","STATE CODE","ISSUER ID","SOURCE NAME",'
        '"VERSION NUMBER","IMPORT DATE","NETWORK ID","NETWORK NAME","NETWORK URL",'
        '"MARKET COVERAGE","DENTAL PLAN ONLY"'

        'CSV3 Examples: 2024,CT,76962,SERFF,1,02-12-2024,CTN001,"ConnectiCare '
        'Benefits, Inc. Choice",,Individual,No'

        'CSV4 Columns: "BUSINESS YEAR","STATE CODE","ISSUER NAME","ISSUER ID",'
        '"SOURCE NAME","VERSION NUMBER","IMPORT DATE","BENEFIT PACKAGE ID",'
        '"MARKET COVERAGE","DENTAL ONLY PLAN",TIN,"STANDARD COMPONENT ID",'
        '"PLAN MARKETING NAME","HIOS PRODUCT ID",HPID,"NETWORK ID",'
        '"SERVICE AREA ID","FORMULARY ID","IS IT A NEW PLAN","PLAN TYPE",'
        '"METAL LEVEL","UNIQUE PLAN DESIGN","QHP NONQHP TYPE ID","IS NOTICE '
        'REQUIRED FOR PREGNACY","IS REFERRAL REQUIRED FOR SPECIALIST",'
        '"SPECIALIST REQUIRING REFERRAL","PLAN LEVEL EXCLUSIONS",'
        '"IS HSA ELIGIBLE","HSA OR HRA EMPLOYER CONTRIBUTION",'
        '"HSA OR HRA EMPLOYER CONTRIBUTION AMOUNT","CHILD ONLY OFFERING",'
        '"CHILD ONLY PLAN ID","WELLNESS PROGRAM OFFERED","DISEASE MANAGEMENT '
        'PROGRAMS OFFERED","EHB PEDIATRIC DENTAL APPORTIONMENT QUANTITY"'
        ',"IS GUARANTEED RATE?","SPECIALITY DRUG MAXIMUM COINSURANCE",'
        '"INPATIENT COPAYMENT MAXIMUM DAYS","BEGIN PRIMARY CARE COST SHARING '
        'AFTER NUMBER OF VISITS","BEGIN PRIMARY CARE DEDUCTIBLE COINSURANCE '
        'AFTER NUMBER OF COPAYS","PLAN EFFECTIVE DATE","PLAN EXPIRATION DATE",'
        '"OUT OF COUNTRY COVERAGE","OUT OF COUNTRY COVERAGE DESCRIPTION",'
        '"OUT OF SERVICE AREA COVERAGE","OUT OF SERVICE AREA COVERAGE '
        'DESCRIPTION","NATIONAL NETWORK","URL FOR SUMMARY OF BENEFITS '
        'COVERAGE","URL FOR ENROLLMENT PAYMENT","PLAN BROCHURE",'
        '"FORMULARY URL","PLAN ID","CSR VARIATION TYPE","ISSUER ACTUARIAL '
        'VALUE","AV CALCULATOR OUTPUT NUMBER","MEDICAL DRUG DEDUCTIBLES'
        ' INTEGRATED","MEDICAL DRUG MAXIMUM OUT OF POCKET INTEGRATED",'
        '"MULTIPLE NETWORK TIERS","FIRST TIER UTILIZATION",'
        '"SECOND TIER UTILIZATION","MEHB INN TIER 1 INDIVIDUAL MOOP",'
        '"MEHB INN TIER 1 FAMILY MOOP","MEHB INN TIER 2 INDIVIDUAL MOOP",'
        '"MEHB INN TIER 2 FAMILY MOOP","MEHB OUT OF NET INDIVIDUAL MOOP",'
        '"MEHB OUT OF NET FAMILY MOOP","MEHB COMB INN OON INDIVIDUAL MOOP",'
        '"MEHB COMB INN OON FAMILY MOOP","DEHB INN TIER 1 INDIVIDUAL MOOP",'
        '"DEHB INN TIER 2 INDIVIDUAL MOOP","DEHB INN TIER 1 FAMILY MOOP",'
        '"DEHB INN TIER 2 FAMILY MOOP","DEHB OUT OF NET INDIVIDUAL MOOP",'
        '"DEHB OUT OF NET FAMILY MOOP","DEHB COMB INN OON INDIVIDUAL MOOP",'
        '"DEHB COMB INN OON FAMILY MOOP","TEHB INN TIER 1 INDIVIDUAL MOOP",'
        '"TEHB INN TIER 1 FAMILY MOOP","TEHB INN TIER 2 INDIVIDUAL MOOP",'
        '"TEHB INN TIER 2 FAMILY MOOP","TEHB OUT OF NET INDIVIDUAL MOOP",'
        '"TEHB OUT OF NET FAMILY MOOP","TEHB COMB INN OON INDIVIDUAL MOOP",'
        '"TEHB COMB INN OON FAMILY MOOP","MEHB DED INN TIER1 INDIVIDUAL",'
        '"MEHB DED INN TIER1 FAMILY","MEHB DED INN TIER1 COINSURNACE",'
        '"MEHB DED INN TIER2 INDIVIDUAL","MEHB DED INN TIER2 FAMILY",'
        '"MEHB DED INN TIER2 COINSURANCE","MEHB DED OUT OF NET INDIVIDUAL",'
        '"MEHB DED OUT OF NET FAMILY","MEHB DED COMB INN OON INDIVIDUAL",'
        '"MEHB DED COMB INN OON FAMILY","DEHB DED INN TIER1 INDIVIDUAL",'
        '"DEHB DED INN TIER1 FAMILY","DEHB DED INN TIER1 COINSURNACE",'
        '"DEHB DED INN TIER2 INDIVIDUAL","DEHB DED INN TIER2 FAMILY",'
        '"DEHB DED INN TIER2 COINSURANCE","DEHB DED OUT OF NET INDIVIDUAL",'
        '"DEHB DED OUT OF NET FAMILY","DEHB DED COMB INN OON INDIVIDUAL",'
        '"DEHB DED COMB INN OON FAMILY","TEHB DED INN TIER 1 INDIVIDUAL",'
        '"TEHB DED INN TIER 1 FAMILY","TEHB DED INN TIER 1 COINSURANCE",'
        '"TEHB DED INN TIER 2 INDIVIDUAL","TEHB DED INN TIER 2 FAMILY",'
        '"TEHB DED INN TIER 2 COINSURANCE","TEHB DED OUT OF NET INDIVIDUAL",'
        '"TEHB DED OUT OF NET FAMILY","TEHB DED OUT COMB INN OON INDIVIDUAL",'
        '"TEHB DED OUT COMB INN OON FAMILY","SBC HAVING A BABY DEDUCTIBLE",'
        '"SBC HAVING A BABY COPAYMENT","SBC HAVING A BABY COINSURANCE",'
        '"SBC HAVING A BABY LIMIT","SBC HAVING DIABETES DEDUCTIBLE",'
        '"SBC HAVING  DIABETES COPAYMENT","SBC HAVING DIABETES COINSURANCE",'
        '"SBC HAVING DIABETES LIMIT","EHB PERCENT PREMIUM","PLAN DESIGN TYPE",'
        '"INSURANCE PLAN COMPOSITE PREMIUM AVAILABLE INDICATOR","PLAN VARIANT '
        'MARKETING NAME","SBC HAVING SIMPLE FRACTURE DEDUCTIBLE","SBC HAVING '
        'SIMPLE FRACTURE COPAYMENT","SBC HAVING SIMPLE FRACTURE COINSURANCE",'
        '"SBC HAVING SIMPLE FRACTURE LIMIT"'

        'CSV4 Example: 2024,CT,,76962,SERFF,1,2/12/2024,,Individual,No,,76962CT0010001,'
        '"Choice Bronze Standard POS",76962CT001,,CTN001,CTS001,CTF003,Existing,POS,'
        '"Expanded Bronze",Yes,Both,No,No,,,No,,,"Allows Adult and Child-Only",,Yes,'
        '"Diabetes, Heart Disease, Asthma",,,"$500 ",2,,,1/1/2024,12/31/2024,No,,'
        'No,,No,,,,,76962CT0010001-01,"Standard Bronze On Exchange Plan",64.97%,,'
        'Yes,Yes,No,100%,,,,,,,,,,,,,,,,,,"$9,100 ","$9100 per person | '
        '$18200 per group",,,"$18,200 ","$18200 per person | $36400 per group",'
        '"Not Applicable","per person not applicable | per group not applicable"'
        ',,,,,,,,,,,,,,,,,,,,,"$6,550 ","$6550 per person | $13100 per group",'
        '0.00%,,,,"$13,100 ","$13100 per person | $26200 per group",'
        '"Not Applicable","per person not applicable | per group not applicable",'
        '"$6,550 ","$1,300 ","$0 ","$60 ","$1,100 ","$1,000 ","$0 ","$20 ",99%,'
        '"Not Applicable",No,"Choice Bronze Standard POS","$2,800 ","$10 ","$0 ","$0 "'

        'CSV5 Columns: "BUSINESS YEAR","STATE CODE","ISSUER ID","SOURCE NAME",'
        '"VERSION NUMBER","IMPORT DATE","FEDERAL TIN","RATE EXPIRATION",'
        '"RATE EFFECTIVE DATE","PLAN ID","RATING AREA ID",TOBACCO,AGE,'
        'QHP_NON_QHP_TYPE_ID,"INDIVIDUAL RATE","INDIVIDUAL TOBACCO RATE",'
        'COUPLE,"PRIMARY SUBSCRIBER AND ONE DEPENDENT","PRIMARY SUBSCRIBER AND '
        'TWO DEPENDENTS","PRIMARY SUBSCRIBER AND THREE OR MORE DEPENDENTS",'
        '"COUPLE AND ONE DEPENDENT","COUPLE AND TWO DEPENDENTS","COUPLE AND '
        'THREE OR MORE DEPENDENTS"'

        'CSV5 Example: 2024,CT,76962,SERFF,1,02-12-2024,,2024-12-31,2024-01-01,'
        '76962CT0010001,"Rating Area 1","No Preference",0-14,Both,381.93,,,,,,,,'

        'CSV6 Columns: "BUSINESS YEAR","STATE CODE","ISSUER ID","SOURCE NAME",'
        '"VERSION NUMBER","IMPORT DATE","SERVICE AREA ID","SERVICE AREA NAME",'
        '"COVER ENTIRE STATE",COUNTY,"COUNTY NAME","PARTIAL COUNTY","ZIP CODE",'
        '"PARTIAL COUNTY JUSTIFICATION","MARKET COVERAGE","DENTAL PLAN ONLY"'

        'CSV6 Example: 2024,CT,76962,SERFF,1,02-12-2024,CTS001,"Service Area 1",true,,,,,,Individual,No'
    )

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part(text=prompt_text),
                types.Part.from_bytes(
                    data=filepath.read_bytes(),
                    mime_type='application/pdf',
                ),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=0.0,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
            model="gemini-2.0-flash",
            contents=contents,
            config=generate_content_config,
    ):
        print(chunk.text)


generate(filepath)
