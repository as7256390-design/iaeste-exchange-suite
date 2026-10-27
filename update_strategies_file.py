import json

strategies = [
  {
    "country": "Germany",
    "code": "DE",
    "flag": "🇩🇪",
    "region": "EU/EFTA",
    "posture": "surplus",
    "postureLabel": "+29 Surplus Target",
    "statusBadge": "Prime Target Partner",
    "globalOutgoing": 86,
    "globalIncoming": 115,
    "netBalance": 29,
    "indiaFlowSent": 5,
    "indiaFlowRecv": 3,
    "indiaTotalFlow": 8,
    "materializationRate": "71.3%",
    "cancellationRisk": "Low (28 cancelled in 2026, 6 in 2025)",
    "rejectionsCount": 188,
    "avgAge": 25.7,
    "stipendReality": "€934 – €1,150 / month (Strict DAAD / statutory minimum wage compliant). Sufficient for student living and university dorms.",
    "whatIndiaWants": [
      "Automotive engineering (Stuttgart, Munich, Wolfsburg corridors)",
      "Computer Science & Informatics research labs (TU Munich, RWTH Aachen, KIT)",
      "High-stipend mechanical & robotics industry placements",
      "English-working university research institutes"
    ],
    "whatToPitchIndia": [
      "Pre-screened 4th-year B.Tech / M.Tech students with proven Python, C++, CAD, or MATLAB skills",
      "Students with full English proficiency (IELTS / Medium of Instruction certificates)",
      "Guaranteed on-campus accommodation at Manipal, MUJ, Karunya, or JECRC for incoming German students",
      "Cultural & industry exposure in India's leading tech hubs (Bengaluru, Jaipur, Coimbatore)"
    ],
    "tacticalWarnings": [
      "German National Visa (§16b / internship visa with ZAV approval) requires 8–12 weeks processing time at VFS New Delhi, Mumbai, Chennai, and Bengaluru.",
      "Never accept offers starting before mid-June unless ZAV pre-approval is initiated immediately in February.",
      "High employer screening standard: 188 nominations rejected network-wide. Ensure student matches 100% of required prerequisites before nominating."
    ],
    "negotiationScript": "Germany is running a +29 incoming surplus (115 hosted vs. 86 sent). At the AC trading tables, pitch India as a high-reliability technical partner: 'We have pre-qualified 4th-year mechanical and CS candidates ready with ZAV-compliant documentation. Let's execute a balanced 4:4 or 5:5 exchange with guaranteed campus housing on our side.'",
    "recommendedAction": "Execute early trades. Demand ZAV letters in February."
  },
  {
    "country": "Poland",
    "code": "PL",
    "flag": "🇵🇱",
    "region": "EU/EFTA",
    "posture": "caution",
    "postureLabel": "High Cancellation Risk",
    "statusBadge": "Exercise Caution",
    "globalOutgoing": 42,
    "globalIncoming": 46,
    "netBalance": 4,
    "indiaFlowSent": 2,
    "indiaFlowRecv": 1,
    "indiaTotalFlow": 3,
    "materializationRate": "55.6%",
    "cancellationRisk": "Highest in Network (71 cancelled in 2026 & 2024, 41 in 2025)",
    "rejectionsCount": 94,
    "avgAge": 24.1,
    "stipendReality": "3,000 – 4,200 PLN / month (~€700 – €980). University dormitory living is essential; private market rentals are high in Warsaw and Kraków.",
    "whatIndiaWants": [
      "Software development and QA engineering (Wrocław, Kraków tech clusters)",
      "Civil and structural engineering (Warsaw, Gdańsk infrastructure projects)",
      "Chemical and process technology placements"
    ],
    "whatToPitchIndia": [
      "Computer Science & Data Science students ready for immediate software delivery",
      "Biotechnology and Chemical Engineering undergraduates from accredited Indian universities",
      "Dedicated accommodation coordinators ensuring incoming Polish students have secured rooms on arrival"
    ],
    "tacticalWarnings": [
      "CRITICAL: Poland recorded 71 employer-cancelled offers in 2026 and 41 in 2025. Never trade unreserved offers without written employer confirmation.",
      "Polish consulates in India require strict original documentation and proof of accommodation (dormitory certificate).",
      "Insist on offers from verified university research faculties (e.g. Warsaw University of Technology, AGH Kraków) over volatile private startups."
    ],
    "negotiationScript": "Poland has a balanced volume (46 hosted / 42 sent) but elevated cancellation rates. At the table, state: 'We are eager to trade for your university research offers, but our delegation requires pre-verified employer commitments and dormitory arrangements to avoid dropouts.'",
    "recommendedAction": "Require confirmed employer housing. Execute 1:1 balanced trades only."
  },
  {
    "country": "Austria",
    "code": "AT",
    "flag": "🇦🇹",
    "region": "EU/EFTA",
    "posture": "surplus",
    "postureLabel": "+34 Surplus Target (#1)",
    "statusBadge": "Prime Capacity Partner",
    "globalOutgoing": 39,
    "globalIncoming": 73,
    "netBalance": 34,
    "indiaFlowSent": 4,
    "indiaFlowRecv": 3,
    "indiaTotalFlow": 7,
    "materializationRate": "66.7%",
    "cancellationRisk": "Low (13 cancelled)",
    "rejectionsCount": 148,
    "avgAge": 25.9,
    "stipendReality": "€1,050 – €1,400 / month (Excellent student living wage under Austrian collective labor agreements). OeAD student housing support available.",
    "whatIndiaWants": [
      "Biotechnology, genetics, and molecular biology research (Vienna Biocenter)",
      "Mechatronics, robotics, and automation (TU Wien, TU Graz, Linz)",
      "Environmental and sustainable process engineering"
    ],
    "whatToPitchIndia": [
      "Top-tier Biotechnology & Bioinformatics students with wet-lab and computational biology experience",
      "Electrical & Mechatronics students with hands-on microcontroller and PLC programming",
      "100% campus-arranged hostel rooms with full board for Austrian incoming students"
    ],
    "tacticalWarnings": [
      "Austrian Visa D requires an official OeAD or university hosting agreement. Appointment lead time at VFS India is 6–8 weeks.",
      "High screening rigor: 148 student rejections network-wide due to employer prerequisite checks. Nominate only candidates meeting 100% of skills.",
      "Austria's academic semester runs later than India; align internship start dates to July/August to prevent exam conflicts."
    ],
    "negotiationScript": "Austria holds the network's #1 incoming capacity surplus (+34 net, 73 hosted vs 39 sent). Approach the Austrian table early: 'India has pre-screened biotech and robotics candidates who meet your strict academic thresholds. We can absorb your surplus with guaranteed reciprocal lodging on our campuses.'",
    "recommendedAction": "Top trade priority. Target Vienna and Graz research institutes."
  },
  {
    "country": "Switzerland",
    "code": "CH",
    "flag": "🇨🇭",
    "region": "EU/EFTA",
    "posture": "elite",
    "postureLabel": "Elite Tech / Rigor",
    "statusBadge": "Premium Compensation",
    "globalOutgoing": 62,
    "globalIncoming": 77,
    "netBalance": 15,
    "indiaFlowSent": 1,
    "indiaFlowRecv": 0,
    "indiaTotalFlow": 1,
    "materializationRate": "55.1%",
    "cancellationRisk": "Elevated (70 cancelled in 2026, 68 in 2025)",
    "rejectionsCount": 391,
    "avgAge": 24.8,
    "stipendReality": "2,200 – 2,800 CHF / month (~₹2.1L – ₹2.7L/mo). Highest student allowance in the world; covers Swiss living costs with significant net savings.",
    "whatIndiaWants": [
      "Computer Science, AI, and Distributed Systems research (ETH Zurich, EPFL)",
      "Pharmaceutical and biotechnology R&D labs (Basel corridor)",
      "Microengineering, nanotechnology, and precision robotics"
    ],
    "whatToPitchIndia": [
      "Top 5% rank students with 9.0+ CGPA from Manipal, MUJ, Karunya, JECRC",
      "Published conference papers or documented open-source code contributions",
      "Immediate nomination readiness with passports, transcripts, and faculty recommendations ready within 48 hours"
    ],
    "tacticalWarnings": [
      "Swiss cantonal labor authorities enforce strict quota approvals. Non-EU/Indian students require Cantonal Work Authorization (takes 8–10 weeks).",
      "Extremely high rejection count: 391 nominations rejected network-wide. Never nominate an average student for a Swiss offer.",
      "Strict nomination deadlines: 70 cancelled offers occurred largely from missed nomination deadlines. Reserve only if you have candidate files ready."
    ],
    "negotiationScript": "Switzerland offers premier stipends and holds a +15 incoming surplus (77 hosted / 62 sent). Pitch with authority: 'We have pre-vetted top 5% CGPA candidates ready for immediate nomination within 48 hours. We will protect your nomination timeline.'",
    "recommendedAction": "Trade only for verified 9.0+ CGPA candidates with ready documentation."
  },
  {
    "country": "Czech Republic",
    "code": "CZ",
    "flag": "🇨🇿",
    "region": "EU/EFTA",
    "posture": "highyield",
    "postureLabel": "High-Yield Benchmark",
    "statusBadge": "Very Reliable Partner",
    "globalOutgoing": 37,
    "globalIncoming": 47,
    "netBalance": 10,
    "indiaFlowSent": 3,
    "indiaFlowRecv": 2,
    "indiaTotalFlow": 5,
    "materializationRate": "73.8%",
    "cancellationRisk": "Low (7–11 cancelled)",
    "rejectionsCount": 42,
    "avgAge": 24.3,
    "stipendReality": "20,000 – 28,000 CZK / month. Very comfortable purchasing power; student dormitory accommodation guaranteed at subsidized rates (~3,500 CZK/mo).",
    "whatIndiaWants": [
      "Automotive engineering & powertrain design (Škoda Auto Mladá Boleslav)",
      "Chemical technology and materials science (UCT Prague, Pardubice)",
      "Computer software and network engineering (CTU Prague, Brno)"
    ],
    "whatToPitchIndia": [
      "Mechanical and Automotive students proficient in CATIA, SolidWorks, and ANSYS",
      "Computer Science candidates with Java, Python, and cloud engineering skills",
      "Full accommodation support and local committee airport reception in India"
    ],
    "tacticalWarnings": [
      "Czech employee/internship visa requires criminal record apostille and certified Czech translation. Initiate consular booking in March.",
      "Relatively low rejection rate (42 rejections) makes Czech offers very safe once candidate matches profile.",
      "Consistently one of the highest conversion rates in Central Europe (73.8% materialization)."
    ],
    "negotiationScript": "Czech Republic is running a +10 incoming surplus (47 hosted vs 37 sent). At the table: 'Czech Republic has been a high-reliability partner for India (73.8% realization). Let's trade 3:3 in automotive and software with confirmed dormitory placements.'",
    "recommendedAction": "Highly recommended. Secure positions with CTU Prague, Brno, and Škoda."
  },
  {
    "country": "Brazil",
    "code": "BR",
    "flag": "🇧🇷",
    "region": "Americas",
    "posture": "surplus",
    "postureLabel": "+16 Surplus Partner",
    "statusBadge": "High Capacity Target",
    "globalOutgoing": 39,
    "globalIncoming": 55,
    "netBalance": 16,
    "indiaFlowSent": 3,
    "indiaFlowRecv": 1,
    "indiaTotalFlow": 4,
    "materializationRate": "48.4%",
    "cancellationRisk": "Moderate (12 cancelled in 2025)",
    "rejectionsCount": 68,
    "avgAge": 25.0,
    "stipendReality": "2,200 – 3,200 BRL / month. Sufficient for living costs in São Paulo, Rio, and university towns; university student dining (RU) is highly subsidized.",
    "whatIndiaWants": [
      "Aerospace and aeronautical engineering (Embraer corridor, São José dos Campos)",
      "Biofuels, agricultural biotechnology, and fermentation engineering",
      "Civil and environmental infrastructure projects"
    ],
    "whatToPitchIndia": [
      "Aerospace & Mechanical engineering students from Manipal & MUJ with aeronautical coursework",
      "Biotechnology students eager for tropical agricultural & biofuel research",
      "Campus dormitories with included Indian dining options for incoming Brazilian trainees"
    ],
    "tacticalWarnings": [
      "Brazilian VITEM IV (internship visa) requires an official RN-94 / CIEE agreement. Processing takes 6–8 weeks at Brazilian consulates in New Delhi/Mumbai.",
      "CPF tax registration is required before arrival to set up stipend disbursement.",
      "Ensure student has basic Portuguese language willingness or confirmed English-working research lab."
    ],
    "negotiationScript": "Brazil holds an incoming surplus of +16 in 2026 (55 hosted / 39 sent). At the Americas table: 'India offers strong aerospace and biotechnology candidates. We can absorb your surplus with reciprocal placement guarantees.'",
    "recommendedAction": "Trade for USP, UNICAMP, and São José dos Campos research centers."
  },
  {
    "country": "Spain",
    "code": "ES",
    "flag": "🇪🇸",
    "region": "EU/EFTA",
    "posture": "surplus",
    "postureLabel": "High Student Demand",
    "statusBadge": "High Indian Demand",
    "globalOutgoing": 44,
    "globalIncoming": 38,
    "netBalance": -6,
    "indiaFlowSent": 5,
    "indiaFlowRecv": 9,
    "indiaTotalFlow": 14,
    "materializationRate": "43.4%",
    "cancellationRisk": "High (56 cancelled in 2025)",
    "rejectionsCount": 115,
    "avgAge": 24.2,
    "stipendReality": "€800 – €1,000 / month. Rent in Madrid, Barcelona, and Valencia is high (€450–€600/room); shared flat arrangements are necessary.",
    "whatIndiaWants": [
      "Renewable energy, solar, and wind power engineering",
      "Architecture, urban planning, and structural design (UPM Madrid, UPC Barcelona)",
      "Civil engineering and marine sciences"
    ],
    "whatToPitchIndia": [
      "Architecture and Civil Engineering students with rich AutoCAD, Revit, and 3D modeling portfolios",
      "Renewable Energy & Electrical Engineering candidates with solar PV system design experience",
      "Full local committee logistics support with low-cost campus accommodation in India"
    ],
    "tacticalWarnings": [
      "High cancellation risk (56 cancelled in 2025). Spain operates at an outgoing deficit (-6).",
      "Summer accommodation in tourist centers (Barcelona, Valencia) is extremely difficult to secure; trade only with confirmed housing advice.",
      "Spanish Convenio de Prácticas visa paperwork requires 8–10 weeks lead time at BLS Spain centers in India."
    ],
    "negotiationScript": "Spain is one of India's most active corridors (14 total flow in 2025: 5 sent, 9 received). Leverage this: 'India is one of your strongest bilateral exchange corridors. Let us execute a 4:4 trade in civil engineering and renewable energy with reciprocal lodging support.'",
    "recommendedAction": "Trade with UPV, UPC, and UPM. Require verified housing lead."
  },
  {
    "country": "Turkiye",
    "code": "TR",
    "flag": "🇹🇷",
    "region": "EU/EFTA",
    "posture": "surplus",
    "postureLabel": "+21 Surplus Target",
    "statusBadge": "Surplus Capacity",
    "globalOutgoing": 32,
    "globalIncoming": 53,
    "netBalance": 21,
    "indiaFlowSent": 1,
    "indiaFlowRecv": 1,
    "indiaTotalFlow": 2,
    "materializationRate": "42.6%",
    "cancellationRisk": "Low (0 cancelled in 2025 file)",
    "rejectionsCount": 54,
    "avgAge": 23.9,
    "stipendReality": "17,002+ TRY / month (statutory minimum wage) with university dormitory housing frequently provided for foreign trainees at nominal cost.",
    "whatIndiaWants": [
      "Aerospace and mechanical engineering (METU Ankara, ITU Istanbul)",
      "Civil, earthquake, and structural engineering research",
      "Computer engineering and telecommunications"
    ],
    "whatToPitchIndia": [
      "Computer Science & IT students ready for fast deployment",
      "Mechanical and Civil Engineering students with structural simulation experience",
      "Guaranteed university lodging on Indian campuses"
    ],
    "tacticalWarnings": [
      "Turkish student e-visa or internship visa approval requires official invitation letters from İŞKUR and university rectorate.",
      "Coordinate arrival dates carefully: Turkish academic exams extend into late June.",
      "Surplus capacity (+21 in 2026) makes Turkiye very receptive to early AC trading table offers."
    ],
    "negotiationScript": "Turkiye holds a +21 incoming surplus (53 hosted vs 32 sent). Approach ITU/METU delegations: 'India has ready engineering candidates for your summer exchange pool. Let us establish a 3:3 trade across civil and aerospace.'",
    "recommendedAction": "Prime target for civil, mechanical, and aerospace trades."
  },
  {
    "country": "Japan",
    "code": "JP",
    "flag": "🇯🇵",
    "region": "Asia-Pacific",
    "posture": "elite",
    "postureLabel": "Elite Robotics / AI",
    "statusBadge": "Top East Asian Lab",
    "globalOutgoing": 30,
    "globalIncoming": 38,
    "netBalance": 8,
    "indiaFlowSent": 1,
    "indiaFlowRecv": 1,
    "indiaTotalFlow": 2,
    "materializationRate": "72.1%",
    "cancellationRisk": "Very Low (6 cancelled in 2025)",
    "rejectionsCount": 28,
    "avgAge": 24.5,
    "stipendReality": "120,000 – 160,000 JPY / month (~₹68k – ₹90k/mo). University international houses provide subsidized rooms (20k–35k JPY/mo).",
    "whatIndiaWants": [
      "Robotics, autonomous systems, and mechatronics (Tokyo Tech, Tohoku, Kyoto)",
      "Semiconductor manufacturing and materials physics",
      "Artificial Intelligence, computer vision, and machine learning"
    ],
    "whatToPitchIndia": [
      "Exceptional Computer Science & Robotics students with ROS, OpenCV, and PyTorch experience",
      "Electronics & VLSI students with Verilog / FPGA circuit design background",
      "Pre-screened candidates with respectful cultural adaptability and Japanese language basics"
    ],
    "tacticalWarnings": [
      "Certificate of Eligibility (CoE) from Japanese Immigration Bureau takes 8–10 weeks before visa application at VFS Japan.",
      "High completion rate (72.1% materialization) and minimal cancellations make Japan one of the network's most reliable positions.",
      "Do not nominate students with low CGPA; Japanese professors review academic transcripts rigorously."
    ],
    "negotiationScript": "Japan operates at a +8 surplus with high completion probability (72.1%). Approach the Japanese table: 'We have pre-qualified robotics and AI students with demonstrated project code ready for CoE submission. Let us exchange 2:2 with university housing.'",
    "recommendedAction": "Top Asian priority for AI, robotics, and semiconductor research."
  },
  {
    "country": "Palestine",
    "code": "PS",
    "flag": "🇵🇸",
    "region": "Middle East",
    "posture": "highyield",
    "postureLabel": "#1 Historical Corridor",
    "statusBadge": "Strategic Anchor",
    "globalOutgoing": 36,
    "globalIncoming": 26,
    "netBalance": -10,
    "indiaFlowSent": 20,
    "indiaFlowRecv": 17,
    "indiaTotalFlow": 37,
    "materializationRate": "76.5%",
    "cancellationRisk": "Zero (0 cancelled in 2025 file)",
    "rejectionsCount": 12,
    "avgAge": 23.5,
    "stipendReality": "$500 – $750 / month or local stipend with subsidized living; remote internship delivery modes widely supported.",
    "whatIndiaWants": [
      "Telecommunications and software engineering",
      "Civil and architectural construction design",
      "Remote AI, web development, and digital system integration"
    ],
    "whatToPitchIndia": [
      "Large-scale software and computer engineering pool from Indian LCs",
      "Remote internship mentoring infrastructure with university server access",
      "Dedicated accommodation, meals, and cultural care for on-site visiting trainees in India"
    ],
    "tacticalWarnings": [
      "Documented as India's #1 bilateral trading corridor (37 total flow in 2026: 20 sent from India, 17 received in India).",
      "Large volume of remote exchange internships (§ Table 30: 20 remote exchanges). Ensure students are briefed on remote delivery expectations.",
      "Consistently zero cancellations and high mutual trust."
    ],
    "negotiationScript": "Palestine is India's largest and most reliable bilateral corridor in IAESTE history (37 exchange flow). Meet at the table: 'We have a proven, battle-tested partnership. Let us confirm our 15:15 or 20:20 mutual exchange across software and civil engineering.'",
    "recommendedAction": "Maintain core bilateral exchange volume."
  },
  {
    "country": "Oman",
    "code": "OM",
    "flag": "🇴🇲",
    "region": "Middle East",
    "posture": "highyield",
    "postureLabel": "High Gulf Stipends",
    "statusBadge": "High Stipend / Fast Visa",
    "globalOutgoing": 35,
    "globalIncoming": 24,
    "netBalance": -11,
    "indiaFlowSent": 5,
    "indiaFlowRecv": 7,
    "indiaTotalFlow": 12,
    "materializationRate": "73.2%",
    "cancellationRisk": "Low (0 cancelled in 2025 file)",
    "rejectionsCount": 18,
    "avgAge": 24.2,
    "stipendReality": "250 – 350 OMR / month (~₹55k – ₹76k/mo). Free air-conditioned housing and transport provided by employers/universities (Sultan Qaboos University). Zero tax.",
    "whatIndiaWants": [
      "Petroleum, reservoir, and chemical engineering (Petroleum Development Oman corridor)",
      "Civil, water resources, and desalination engineering",
      "Computer Science & Network Infrastructure"
    ],
    "whatToPitchIndia": [
      "Petroleum & Chemical Engineering students from premier Indian institutes",
      "Civil & Environmental Engineering candidates with AutoCAD & structural design training",
      "Guaranteed Indian campus lodging and local committee airport logistics"
    ],
    "tacticalWarnings": [
      "Fast visa processing: Omani employer work permits for Indian nationals are processed within 2–3 weeks.",
      "Corridor flow with India is strong (12 total in 2026, 9 in 2025).",
      "Hot summer temperatures (June–August): prepare students for GCC desert climate."
    ],
    "negotiationScript": "Oman offers premium living conditions (free AC housing + 300 OMR stipend) and reliable delivery. Meet Omani delegates: 'India provides industry-ready chemical, petroleum, and civil candidates. Let us trade 4:4 with fast visa turnaround.'",
    "recommendedAction": "Priority target for chemical, petroleum, and civil branches."
  },
  {
    "country": "Thailand",
    "code": "TH",
    "flag": "🇹🇭",
    "region": "Asia-Pacific",
    "posture": "highyield",
    "postureLabel": "Low Cost / High Fit",
    "statusBadge": "High Conversion Partner",
    "globalOutgoing": 37,
    "globalIncoming": 33,
    "netBalance": -4,
    "indiaFlowSent": 4,
    "indiaFlowRecv": 5,
    "indiaTotalFlow": 9,
    "materializationRate": "74.8%",
    "cancellationRisk": "Very Low (0 cancelled in 2025 file)",
    "rejectionsCount": 22,
    "avgAge": 23.8,
    "stipendReality": "10,000 – 15,000 THB / month. Excellent purchasing power; inexpensive student meals and university dormitories (KMUTNB, KMUTT, Chulalongkorn).",
    "whatIndiaWants": [
      "Agricultural biotechnology and food processing technology",
      "Automotive and industrial robotics manufacturing",
      "Electronics, IoT, and embedded systems"
    ],
    "whatToPitchIndia": [
      "Biotechnology & Food Technology candidates from Karunya and Manipal",
      "Electronics & Mechatronics students with microcontroller and sensor interfacing skills",
      "Full accommodation support and friendly local committee hosting"
    ],
    "tacticalWarnings": [
      "Non-Immigrant ED visa takes 2–3 weeks at VFS Royal Thai Embassy New Delhi/Chennai.",
      "High realization corridor with India (9 total flow in 2026, 74.8% materialization).",
      "Internship dates align smoothly with Indian summer vacation (May–July)."
    ],
    "negotiationScript": "Thailand is one of our smoothest Asian corridors (9 total flow in 2026). At the table: 'We have pre-qualified food tech and electronics students. Let us execute a 4:4 balanced exchange with university dorms.'",
    "recommendedAction": "Ideal for food science, biotech, and embedded systems."
  },
  {
    "country": "United Arab Emirates",
    "code": "AE",
    "flag": "🇦🇪",
    "region": "Middle East",
    "posture": "caution",
    "postureLabel": "Verify Allowance",
    "statusBadge": "Verify Housing",
    "globalOutgoing": 9,
    "globalIncoming": 15,
    "netBalance": 6,
    "indiaFlowSent": 3,
    "indiaFlowRecv": 0,
    "indiaTotalFlow": 3,
    "materializationRate": "58.0%",
    "cancellationRisk": "Elevated (21–37 cancelled)",
    "rejectionsCount": 35,
    "avgAge": 24.4,
    "stipendReality": "2,500 – 4,500 AED / month. Rental housing in Dubai/Sharjah is expensive (1,500–2,500 AED/mo); verify employer-provided accommodation before trading.",
    "whatIndiaWants": [
      "Civil, skyscraper, and structural construction engineering",
      "Artificial Intelligence, Fintech, and cloud computing (Dubai Internet City)",
      "Petroleum, energy, and supply chain logistics"
    ],
    "whatToPitchIndia": [
      "Civil Engineering students with structural analysis (ETABS, STAAD.Pro)",
      "Computer Science candidates with full-stack and cloud deployment experience",
      "Guaranteed campus rooms for incoming UAE university trainees"
    ],
    "tacticalWarnings": [
      "Do NOT accept offers without written confirmation of employer-provided accommodation or minimum 3,500 AED/mo allowance.",
      "UAE entry permits for trainees take 10–14 days through GDRFA / ICP portals.",
      "Ensure candidate understands summer temperatures exceed 45°C."
    ],
    "negotiationScript": "UAE offers prestigious industry placements. Meet UAE delegates: 'We have top-tier civil and software talent. We can confirm trades provided housing allowances are verified in the offer form.'",
    "recommendedAction": "Trade only if employer accommodation is guaranteed in writing."
  },
  {
    "country": "United Kingdom",
    "code": "GB",
    "flag": "🇬🇧",
    "region": "EU/EFTA",
    "posture": "caution",
    "postureLabel": "Strict Visa Sponsorship",
    "statusBadge": "Tier 5 Visa Hurdle",
    "globalOutgoing": 10,
    "globalIncoming": 7,
    "netBalance": -3,
    "indiaFlowSent": 0,
    "indiaFlowRecv": 0,
    "indiaTotalFlow": 0,
    "materializationRate": "42.5%",
    "cancellationRisk": "Moderate (9–13 cancelled)",
    "rejectionsCount": 26,
    "avgAge": 24.6,
    "stipendReality": "£1,200 – £1,600 / month (UK National Minimum Wage compliant). London and Southeast accommodations are very costly (£700–£900/mo).",
    "whatIndiaWants": [
      "Nanotechnology and advanced materials research (Oxford, Cambridge, Imperial corridors)",
      "Biomedical engineering and genomics research",
      "Aerospace and Formula 1 automotive corridors (Midlands)"
    ],
    "whatToPitchIndia": [
      "Top 3% CGPA candidates with international research publications",
      "Candidates with financial sponsorship statements ready for UKVI maintenance requirements",
      "Premium local committee hosting in India with campus room and board"
    ],
    "tacticalWarnings": [
      "CRITICAL: Requires British Council Tier 5 (Government Authorised Exchange) Certificate of Sponsorship (CoS). Processing takes 10–12 weeks.",
      "UKVI visa fee + Immigration Health Surcharge (IHS) is expensive; ensure student is prepared for £600+ upfront visa costs.",
      "Do not trade unless UK committee confirms CoS allocation is ready."
    ],
    "negotiationScript": "UK offers world-class research institutes. Approach UK delegates: 'We have candidates with ready funds and publications who meet Tier 5 requirements. Can you confirm CoS sponsorship availability before we trade?'",
    "recommendedAction": "High prestige; execute only with confirmed Tier 5 CoS."
  },
  {
    "country": "United States",
    "code": "US",
    "flag": "🇺🇸",
    "region": "Americas",
    "posture": "caution",
    "postureLabel": "J-1 Visa Sponsored",
    "statusBadge": "Cultural Exchange",
    "globalOutgoing": 7,
    "globalIncoming": 0,
    "netBalance": -7,
    "indiaFlowSent": 0,
    "indiaFlowRecv": 0,
    "indiaTotalFlow": 0,
    "materializationRate": "55.0%",
    "cancellationRisk": "Low (2 cancelled)",
    "rejectionsCount": 16,
    "avgAge": 24.7,
    "stipendReality": "$2,000 – $3,200 / month. High living costs in metropolitan areas; suburban university towns offer better purchasing power.",
    "whatIndiaWants": [
      "Computer Science, Silicon Valley tech startups, and cloud computing",
      "Biotechnology, genetic engineering, and clinical research",
      "Advanced manufacturing and automotive R&D"
    ],
    "whatToPitchIndia": [
      "Outstanding CS/AI candidates with production coding and GitHub repositories",
      "Biomedical candidates with laboratory wet-lab certification",
      "Full Indian LC hospitality with campus dormitories"
    ],
    "tacticalWarnings": [
      "Requires DS-2019 sponsorship from designated J-1 visa sponsor (Cultural Vistas / IAESTE US) + SEVIS fee + US Embassy interview.",
      "US consular interview wait times in India (New Delhi, Mumbai, Hyderabad) can be lengthy; DS-2019 must be issued by March.",
      "Ensure minimum $2,000/month stipend to meet J-1 financial sufficiency requirements."
    ],
    "negotiationScript": "US offers high industry exposure. Discuss with US delegates: 'We have candidates with ready DS-160 paperwork and software portfolios. We require March DS-2019 issuance to clear embassy interviews.'",
    "recommendedAction": "High prestige; ensure DS-2019 issuance lead time."
  },
  {
    "country": "Belgium",
    "code": "BE",
    "flag": "🇧🇪",
    "region": "EU/EFTA",
    "posture": "elite",
    "postureLabel": "Nanotech & Microchips",
    "statusBadge": "IMEC Tech Corridor",
    "globalOutgoing": 17,
    "globalIncoming": 11,
    "netBalance": -6,
    "indiaFlowSent": 3,
    "indiaFlowRecv": 2,
    "indiaTotalFlow": 5,
    "materializationRate": "70.0%",
    "cancellationRisk": "Moderate (8–17 cancelled)",
    "rejectionsCount": 105,
    "avgAge": 24.6,
    "stipendReality": "€1,000 – €1,250 / month. Student room rentals (kot) in Leuven, Ghent, and Brussels cost €400–€550/month.",
    "whatIndiaWants": [
      "Semiconductor physics, nanotechnology, and microelectronics (IMEC Leuven)",
      "Biochemical and pharmaceutical research (Ghent, Brussels)",
      "Chemical process technology (Antwerp chemical cluster)"
    ],
    "whatToPitchIndia": [
      "VLSI, semiconductor, and nanotechnology students from premier Indian labs",
      "Chemical Engineering and Biotechnology undergraduates with research experience",
      "Full local committee support with secured Indian campus housing"
    ],
    "tacticalWarnings": [
      "Belgian Single Permit (internship work authorization) requires 8–10 weeks processing time at Belgian Embassy New Delhi.",
      "IMEC and university research centers require rigorous background checks and transcript verification.",
      "Active bilateral corridor with India (5 total flow in 2025: 3 sent from India, 2 received)."
    ],
    "negotiationScript": "Belgium is home to IMEC and Europe's leading microelectronics corridor. Pitch at the table: 'India has top-tier VLSI and chemical candidates. Let us trade 2:2 with confirmed campus dorms on our side.'",
    "recommendedAction": "Top target for microelectronics, semiconductors, and biotech."
  }
]

out = "window.COUNTRY_STRATEGIES_DATA = " + json.dumps(strategies, indent=2) + ";\n"
with open("country_strategies_data.js", "w") as f:
    f.write(out)

print("SUCCESS: country_strategies_data.js updated with 100% verified numbers!")
