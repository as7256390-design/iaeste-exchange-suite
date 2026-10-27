import openpyxl, json, re, os

# Registry of 37 files trained
TRAINED_FILES_REGISTRY = [
    {"year": "2019", "file": "World Exchange 2019.xlsx", "type": "Excel (Bilateral & Combined Exchange)"},
    {"year": "2019", "file": "ARQ Analysis 2019.xlsx", "type": "Excel (Offers, Disciplines, Cancellations)"},
    {"year": "2019", "file": "IAESTE_ActivityReport_2019_print.pdf", "type": "PDF (Official Annual Report)"},
    {"year": "2019", "file": "IAESTE_ActivityReport_2019_online.pdf", "type": "PDF (Online Release Report)"},
    {"year": "2019", "file": "Activity Report 2019, Erratum (printed version)8-9-12.pdf", "type": "PDF (Report Erratum)"},
    {"year": "2019", "file": "IAESTE Exchange 2019 results_20191030.pptx", "type": "Presentation (Exchange Results Presentation)"},
    {"year": "2019", "file": "IAESTE_ActivityReport_2019_online.docx", "type": "Document (Online Version Text)"},
    {"year": "2019", "file": "2019 Activity Report Questionnaire - Instructions.docx", "type": "Document (ARQ Instructions)"},
    {"year": "2019", "file": "2019 Activity Report Questionnaire & AEQ Guidelines_.docx", "type": "Document (ARQ & AEQ Guidelines)"},
    {"year": "2019", "file": "LINK TO THE ONLINE VERSION OF THE ARQ 2019 ANALYSIS.docx", "type": "Document (Online Analysis Reference)"},
    
    {"year": "2020", "file": "Activity Report 2020_ Publish.xlsx", "type": "Excel (World Exchange, Offers, Profiles)"},
    {"year": "2020", "file": "Process/ARQ Analysis 2020.xlsx", "type": "Excel (Offers, M_SENT, M_RECEIVED, Disciplines)"},
    {"year": "2020", "file": "Activity Report 2020.pdf", "type": "PDF (Official Annual Report)"},
    {"year": "2020", "file": "Process/2020 Activity Report Questionnaire - Instructions.docx", "type": "Document (ARQ Instructions)"},
    {"year": "2020", "file": "Process/2020 Activity Report Questionnaire & AEQ Guidelines_.docx", "type": "Document (ARQ Guidelines)"},

    {"year": "2021", "file": "Activity Report 2021_10.01.2022.pdf", "type": "PDF (Official Annual Report)"},

    {"year": "2022", "file": "Activity Report 2022_print.pdf", "type": "PDF (Printed Annual Report)"},
    {"year": "2022", "file": "Activity Report_online.pdf", "type": "PDF (Online Annual Report)"},

    {"year": "2023", "file": "Activity Report 2023.xlsx", "type": "Excel (Sheets 2019-2022, Coop, Offers Efficiency)"},
    {"year": "2023", "file": "Activity REPORT 2023.pdf", "type": "PDF (Official Annual Report)"},
    {"year": "2023", "file": "Activity & EEQ REPORT 2023_INTERNAL USE ONLY.pdf", "type": "PDF (Internal Exchange Evaluation Report)"},
    {"year": "2023", "file": "EEQ_2023_All Committees.pdf", "type": "PDF (All Committees EEQ Report)"},

    {"year": "2024", "file": "trend_ar_2020___2024_2024-12-05T15_27_20.812072Z.xlsx", "type": "Excel (5-Year Trainee Trend 2020-2024)"},
    {"year": "2024", "file": "offer_totals_2024-12-05T15_24_41.922352Z.xlsx", "type": "Excel (Offer Totals, Accepted, Cancelled)"},
    {"year": "2024", "file": "exchange_sent___committee_2024-12-05T15_25_15.254135Z.xlsx", "type": "Excel (577 Bilateral Trading Pairs)"},
    {"year": "2024", "file": "general_discipline___sent_2024-12-05T15_26_48.225014Z.xlsx", "type": "Excel (General Disciplines Sent)"},
    {"year": "2024", "file": "general_discipline___received_2024-12-05T15_26_57.994772Z.xlsx", "type": "Excel (General Disciplines Received)"},
    {"year": "2024", "file": "cooperation_between_committees___sending_2024-12-05T15_24_07.574772Z.xlsx", "type": "Excel (Sending Bilateral Counts)"},
    {"year": "2024", "file": "cooperation_between_committees___receiving_2024-12-05T15_24_15.004911Z.xlsx", "type": "Excel (Receiving Bilateral Counts)"},
    {"year": "2024", "file": "employer_cancellation_2024-12-05T15_25_25.62148Z.xlsx", "type": "Excel (Employer Cancellation Reasons)"},
    {"year": "2024", "file": "student_rejection_2024-12-05T15_26_23.765562Z.xlsx", "type": "Excel (Student Rejections)"},
    {"year": "2024", "file": "incoming_2024-12-05T15_25_07.316374Z.xlsx", "type": "Excel (Incoming Trainees)"},
    {"year": "2024", "file": "outgoing_2024-12-05T15_24_58.536529Z.xlsx", "type": "Excel (Outgoing Trainees)"},
    {"year": "2024", "file": "multilateral_exchange_2024-12-05T15_23_48.515661Z.xlsx", "type": "Excel (Multilateral Exchange)"},
    {"year": "2024", "file": "ar_2024_2024-12-05T15_24_32.601532Z.xlsx", "type": "Excel (Annual Report Aggregate)"},
    {"year": "2024", "file": "DASHBOARD 2024.docx", "type": "Document (Cloud Dashboard Documentation)"},

    {"year": "2025", "file": "ACTIVITY REPORT 2025.docx", "type": "Document (IAESTE Cloud Dashboard 2025 Link & Tutorial)"}
]

print(f"Total trained files registered: {len(TRAINED_FILES_REGISTRY)}")
