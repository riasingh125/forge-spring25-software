from backend.RankingLogics import rankings
import asyncio


def main():
	plan = rankings.WeightedPlanRanking(
		weights={
			'coverage_of_all_benefits': 1.0,
			'affordability': 1.0,
			'personalized_coverage': 1.0,
			'emergency_coverage': 1.0,
			'flexibility_of_coverage': 1.0,
			'convenience_of_coverage': 1.0,
			'geographic_coverage': 1.0
		},
		corpus='''BLUE CROSS AND BLUE SHIELD OF TEXAS
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
''',
		user_input={
			"premium": 100,
			"budget": 200,
			"health_concerns": "Type 1 Diabetes",
			"age": 30,
			"zip_code": "14127",
			"city": "Orchard Park",
			"state": "New York"
		}
	)

	asyncio.run(plan.ranking_logics())
	print(plan.scores)
	print(plan.pair_keys())
	print(plan.total_scores())
	print(plan.weighted_scores)


main()
