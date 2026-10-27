import openpyxl, zipfile, xml.etree.ElementTree as ET, json, os

print("=== BUILDING 100% ACCURATE DATASET DIRECTLY FROM OFFICIAL FILES ===")

# -------------------------------------------------------------
# 1. Parse trend_ar_2020___2026 (Official 2020-2026 Outgoing/Incoming)
# -------------------------------------------------------------
wb_trend = openpyxl.load_workbook("Activity report all details 2025/trend_ar_2020___2026_2026-10-26T15_12_27.858485821Z.xlsx", data_only=True)
ws_trend = wb_trend["Query result"]
trend_rows = list(ws_trend.iter_rows(values_only=True))[2:]

trend_by_year = {
    "2020": {}, "2021": {}, "2022": {}, "2023": {}, "2024": {}, "2025": {}, "2026": {}
}

years_order = ["2020", "2021", "2022", "2023", "2024", "2025", "2026"]
for r in trend_rows:
    comm = str(r[0]).strip()
    if not comm or comm.lower() in ["none", "commitee", "total", "totals", "row totals"]:
        continue
    for i, yr in enumerate(years_order):
        out_v = float(r[1 + i*2] or 0)
        in_v = float(r[2 + i*2] or 0)
        trend_by_year[yr][comm] = {
            "outgoing": int(out_v),
            "incoming": int(in_v),
            "net": int(in_v - out_v)
        }

print("Loaded trend_ar_2020___2026 for", len(trend_rows), "committees.")

# -------------------------------------------------------------
# 2. Parse 2019 World Exchange
# -------------------------------------------------------------
wb_19 = openpyxl.load_workbook("Activity Report 2019/World Exchange 2019.xlsx", data_only=True)
ws_19 = wb_19["Combined SentReceived"]
rows_19 = list(ws_19.iter_rows(values_only=True))[2:]
data_2019 = {}
for r in rows_19:
    comm = str(r[0]).strip()
    if not comm or comm.lower() in ["none", "iaeste name", "total", "combined"]:
        continue
    try:
        out_s = float(r[5] or 0) if r[5] != "-" else 0
        in_s = float(r[6] or 0) if r[6] != "-" else 0
        data_2019[comm] = {
            "outgoing": int(out_s),
            "incoming": int(in_s),
            "net": int(in_s - out_s)
        }
    except:
        pass
print("Loaded 2019 World Exchange for", len(data_2019), "committees.")

# -------------------------------------------------------------
# 3. Parse 2025 Official Offer Totals & Details
# -------------------------------------------------------------
wb_offers25 = openpyxl.load_workbook("Activity report all details 2025/offer_totals_2026-10-26T15_11_21.772877699Z.xlsx", data_only=True)
ws_offers25 = wb_offers25["Query result"]
offers25_map = {}
for r in list(ws_offers25.iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip()
    pub = int(r[1] or 0)
    nom = int(r[2] or 0)
    acc = int(r[3] or 0)
    unused = int(r[4] or 0)
    canc = int(r[5] or 0)
    types_tot = int(r[6] or 0) + int(r[7] or 0) + int(r[8] or 0)
    status_tot = pub + nom + acc + unused + canc
    tot = max(types_tot, status_tot, acc + canc + unused)
    mat_rate = round((acc / tot) * 100, 1) if tot > 0 else 0
    canc_rate = round((canc / tot) * 100, 1) if tot > 0 else 0
    offers25_map[comm] = {
        "published": pub,
        "nominated": nom,
        "accepted": acc,
        "unused": unused,
        "cancelled": canc,
        "totalOffers": tot,
        "materializationRate": mat_rate,
        "cancellationRate": canc_rate
    }

# -------------------------------------------------------------
# 4. Parse 2024 Official Offer Totals & Details
# -------------------------------------------------------------
wb_offers24 = openpyxl.load_workbook("Activity Report 2024/offer_totals_2024-12-05T15_24_41.922352Z.xlsx", data_only=True)
ws_offers24 = wb_offers24["Query result"]
offers24_map = {}
for r in list(ws_offers24.iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip()
    pub = int(r[1] or 0)
    nom = int(r[2] or 0)
    acc = int(r[3] or 0)
    unused = int(r[4] or 0)
    canc = int(r[5] or 0)
    types_tot = int(r[6] or 0) + int(r[7] or 0) + int(r[8] or 0)
    status_tot = pub + nom + acc + unused + canc
    tot = max(types_tot, status_tot, acc + canc + unused)
    mat_rate = round((acc / tot) * 100, 1) if tot > 0 else 0
    canc_rate = round((canc / tot) * 100, 1) if tot > 0 else 0
    offers24_map[comm] = {
        "published": pub,
        "nominated": nom,
        "accepted": acc,
        "unused": unused,
        "cancelled": canc,
        "totalOffers": tot,
        "materializationRate": mat_rate,
        "cancellationRate": canc_rate
    }

# -------------------------------------------------------------
# 5. Parse 2025 Corridors (exchange_sent___committee)
# -------------------------------------------------------------
wb_flows25 = openpyxl.load_workbook("Activity report all details 2025/exchange_sent___committee_2026-10-26T15_10_53.412595664Z.xlsx", data_only=True)
flows25 = []
for r in list(wb_flows25["Query result"].iter_rows(values_only=True))[1:]:
    s, rec, cnt = str(r[0]).strip(), str(r[1]).strip(), float(r[2] or 0)
    if cnt > 0:
        flows25.append({"sender": s, "receiver": rec, "count": int(cnt)})

# -------------------------------------------------------------
# 6. Parse 2024 Corridors (exchange_sent___committee 2024)
# -------------------------------------------------------------
wb_flows24 = openpyxl.load_workbook("Activity Report 2024/exchange_sent___committee_2024-12-05T15_25_15.254135Z.xlsx", data_only=True)
flows24 = []
for r in list(wb_flows24["Query result"].iter_rows(values_only=True))[1:]:
    s, rec, cnt = str(r[0]).strip(), str(r[1]).strip(), float(r[2] or 0)
    if cnt > 0:
        flows24.append({"sender": s, "receiver": rec, "count": int(cnt)})

# -------------------------------------------------------------
# 7. Parse 2026 DOCX Tables (Official 2026 Activity Report)
# -------------------------------------------------------------
with zipfile.ZipFile("IAESTE_Activity_Report_2026.docx") as z:
    xml_content = z.read("word/document.xml")
    tree = ET.fromstring(xml_content)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    tables = tree.findall(".//w:tbl", ns)
    
    # Table 22: Accepted offers
    acc_offers_26 = {}
    for r in tables[21].findall(".//w:tr", ns)[1:]:
        cells = ["".join(c.itertext()).strip().replace("\n", " ") for c in r.findall(".//w:tc", ns)]
        if len(cells) >= 2:
            acc_offers_26[cells[0].strip()] = int(cells[1].replace(",", "").strip() or 0)
            
    # Table 32: Cancelled offers
    canc_offers_26 = {}
    for r in tables[31].findall(".//w:tr", ns)[1:]:
        cells = ["".join(c.itertext()).strip().replace("\n", " ") for c in r.findall(".//w:tc", ns)]
        if len(cells) >= 2:
            canc_offers_26[cells[0].strip()] = int(cells[1].replace(",", "").strip() or 0)

    # Table 13: Corridors 2026
    flows26 = []
    for r in tables[12].findall(".//w:tr", ns)[1:]:
        cells = ["".join(c.itertext()).strip().replace("\n", " ") for c in r.findall(".//w:tc", ns)]
        if len(cells) >= 3:
            s, rec, cnt = cells[0].strip(), cells[1].strip(), int(cells[2].replace(",", "").strip() or 0)
            if cnt > 0:
                flows26.append({"sender": s, "receiver": rec, "count": cnt})

    # Also parse Paragraphs with arrows (e.g. 🇮🇳 India → 🇦🇹 Austria 4)
    paragraphs = tree.findall(".//w:p", ns)
    for idx, p in enumerate(paragraphs):
        txt = "".join(p.itertext()).strip()
        if "→" in txt and len(txt) < 80:
            parts = txt.split("→")
            if len(parts) == 2:
                s_raw = parts[0].replace("🇮🇳", "").replace("🇦🇹", "").replace("🇩🇪", "").replace("🇧🇷", "").replace("🇨🇭", "").replace("🇵🇸", "").replace("🇧🇩", "").replace("🇹🇳", "").replace("🇫🇷", "").replace("🇰🇪", "").replace("🇴🇲", "").replace("🇪🇸", "").replace("🇹🇭", "").replace("🇯🇵", "").replace("🇵🇱", "").replace("🌐", "").replace("🇧🇮", "").strip()
                r_raw = parts[1].replace("🇮🇳", "").replace("🇦🇹", "").replace("🇩🇪", "").replace("🇧🇷", "").replace("🇨🇭", "").replace("🇵🇸", "").replace("🇧🇩", "").replace("🇹🇳", "").replace("🇫🇷", "").replace("🇰🇪", "").replace("🇴🇲", "").replace("🇪🇸", "").replace("🇹🇭", "").replace("🇯🇵", "").replace("🇵🇱", "").replace("🌐", "").replace("🇧🇮", "").strip()
                # next paragraph might be the count
                if idx + 1 < len(paragraphs):
                    next_txt = "".join(paragraphs[idx+1].itertext()).strip()
                    if next_txt.isdigit():
                        cnt = int(next_txt)
                        # Add if not duplicate
                        if not any(f["sender"] == s_raw and f["receiver"] == r_raw for f in flows26):
                            flows26.append({"sender": s_raw, "receiver": r_raw, "count": cnt})

print("Parsed 2026 docx: acc_offers =", len(acc_offers_26), ", canc_offers =", len(canc_offers_26), ", flows26 =", len(flows26))

# -------------------------------------------------------------
# 8. Employer Cancellations & Rejection Reasons (2025 file)
# -------------------------------------------------------------
wb_emp_canc = openpyxl.load_workbook("Activity report all details 2025/employer_cancellation_2026-10-26T15_10_34.567530712Z.xlsx", data_only=True)
emp_canc_map = {}
for r in list(wb_emp_canc["Query result"].iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip()
    hdr = list(wb_emp_canc["Query result"].iter_rows(values_only=True))[0]
    # find top reason
    best_reason = ""
    max_c = 0
    for idx in range(1, len(r)-1):
        v = float(r[idx] or 0)
        if v > max_c:
            max_c = v
            best_reason = str(hdr[idx]).strip()
    if best_reason:
        emp_canc_map[comm] = best_reason

wb_stud_rej = openpyxl.load_workbook("Activity report all details 2025/student_rejection_2026-10-26T15_08_31.436233902Z.xlsx", data_only=True)
stud_rej_map = {}
for r in list(wb_stud_rej["Query result"].iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip()
    hdr = list(wb_stud_rej["Query result"].iter_rows(values_only=True))[0]
    best_reason = ""
    max_c = 0
    for idx in range(1, len(r)-1):
        v = float(r[idx] or 0)
        if v > max_c:
            max_c = v
            best_reason = str(hdr[idx]).strip()
    if best_reason:
        stud_rej_map[comm] = best_reason

# Disciplines
wb_disc_sent = openpyxl.load_workbook("Activity report all details 2025/general_discipline___sent_2026-10-26T15_07_54.49469001Z.xlsx", data_only=True)
disc_sent_map = {}
hdr_sent = list(wb_disc_sent["Query result"].iter_rows(values_only=True))[0]
for r in list(wb_disc_sent["Query result"].iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip()
    pairs = []
    for idx in range(1, len(r)-1):
        v = float(r[idx] or 0)
        if v > 0:
            pairs.append((hdr_sent[idx], v))
    pairs.sort(key=lambda x: -x[1])
    disc_sent_map[comm] = [p[0] for p in pairs[:4]]

wb_disc_recv = openpyxl.load_workbook("Activity report all details 2025/general_discipline___received_2026-10-26T15_07_42.109980585Z.xlsx", data_only=True)
disc_recv_map = {}
hdr_recv = list(wb_disc_recv["Query result"].iter_rows(values_only=True))[0]
for r in list(wb_disc_recv["Query result"].iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip()
    pairs = []
    for idx in range(1, len(r)-1):
        v = float(r[idx] or 0)
        if v > 0:
            pairs.append((hdr_recv[idx], v))
    pairs.sort(key=lambda x: -x[1])
    disc_recv_map[comm] = [p[0] for p in pairs[:4]]

print("Loaded employer cancellation reasons, student rejection reasons, and disciplines.")
