import openpyxl, json, re, os, glob

print("Starting training of trade leads model with 55 files...")

# --- 1. 2019 World Exchange ---
wb19 = openpyxl.load_workbook('Activity Report 2019/World Exchange 2019.xlsx', data_only=True)
ws19 = wb19['Combined SentReceived']
data_2019 = {}
for r in list(ws19.iter_rows(values_only=True))[2:]:
    name = r[0]
    if not name or 'total' in str(name).lower():
        continue
    sent = r[5]
    recv = r[6]
    sent_val = float(sent) if sent not in ('-', None, '#N/A') else 0.0
    recv_val = float(recv) if recv not in ('-', None, '#N/A') else 0.0
    data_2019[str(name).strip()] = {'outgoing': sent_val, 'incoming': recv_val}

print(f"2019 data loaded: {len(data_2019)} committees.")

# --- 2. 2020-2026 Trend from 'Activity report all details 2025/trend_ar_2020___2026_...' ---
trend_file = glob.glob('Activity report all details 2025/trend_ar_2020___2026_*.xlsx')[0]
wb_tr = openpyxl.load_workbook(trend_file, data_only=True)
ws_tr = wb_tr.active
rows_tr = list(ws_tr.iter_rows(values_only=True))

# Header row 0: (None, '2020', '2020', '2021', '2021', '2022', '2022', '2023', '2023', '2024', '2024', '2025', '2025', '2026', '2026', 'Row totals', 'Row totals')
years_in_trend = ['2020', '2021', '2022', '2023', '2024', '2025', '2026']
trend_by_year_comm = {y: {} for y in years_in_trend}
cumulative_trend = {}

for r in rows_tr[2:]:
    comm = str(r[0]).strip() if r[0] else ''
    if not comm:
        continue
    
    cum_out = 0.0
    cum_in = 0.0

    # 2019 addition
    if comm in data_2019:
        cum_out += data_2019[comm]['outgoing']
        cum_in += data_2019[comm]['incoming']
    else:
        for k19, v19 in data_2019.items():
            if k19.lower() in comm.lower() or comm.lower() in k19.lower():
                cum_out += v19['outgoing']
                cum_in += v19['incoming']
                break

    for i, y in enumerate(years_in_trend):
        out_col = 1 + (i * 2)
        in_col = 2 + (i * 2)
        out_v = float(r[out_col] or 0.0)
        in_v = float(r[in_col] or 0.0)
        trend_by_year_comm[y][comm] = {'outgoing': out_v, 'incoming': in_v}
        cum_out += out_v
        cum_in += in_v

    cumulative_trend[comm] = {
        'outgoing': cum_out,
        'incoming': cum_in,
        'net': cum_in - cum_out
    }

print(f"2020-2026 trend loaded for {len(cumulative_trend)} committees.")

# --- 3. Offer totals (2025/2026 cycle) ---
ot_file = glob.glob('Activity report all details 2025/offer_totals_2026-10-26*.xlsx')[0]
wb_ot = openpyxl.load_workbook(ot_file, data_only=True)
ws_ot = wb_ot.active
ot_data = {}
for r in list(ws_ot.iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip() if r[0] else ''
    if not comm:
        continue
    pub = float(r[1] or 0)
    nom = float(r[2] or 0)
    acc = float(r[3] or 0)
    unused = float(r[4] or 0)
    canc = float(r[5] or 0)
    tot = acc + canc + unused
    if tot == 0:
        tot = pub if pub > 0 else (acc + canc)
    
    mat = round((acc / tot * 1000) / 10, 1) if tot > 0 else 0.0
    canc_r = round((canc / tot * 1000) / 10, 1) if tot > 0 else 0.0
    
    ot_data[comm] = {
        'published': pub,
        'nominated': nom,
        'accepted': acc,
        'unused': unused,
        'cancelled': canc,
        'totalOffers': tot,
        'materializationRate': mat,
        'cancellationRate': canc_r
    }

print(f"Offer totals loaded for {len(ot_data)} committees.")

# --- 4. Bilateral exchanges with India (2025/2026 file) ---
ex_file = glob.glob('Activity report all details 2025/exchange_sent___committee_2026-10-26*.xlsx')[0]
wb_ex = openpyxl.load_workbook(ex_file, data_only=True)
ws_ex = wb_ex.active
india_sent = {}
india_recv = {}
all_bilateral = []

for r in list(ws_ex.iter_rows(values_only=True))[1:]:
    sender = str(r[0]).strip() if r[0] else ''
    recvr = str(r[1]).strip() if r[1] else ''
    cnt = float(r[2] or 0)
    if not sender or not recvr:
        continue
    all_bilateral.append({'sender': sender, 'receiver': recvr, 'count': cnt})
    if 'india' in sender.lower():
        india_sent[recvr] = cnt
    if 'india' in recvr.lower():
        india_recv[sender] = cnt

print(f"Bilateral matrix loaded: {len(all_bilateral)} pairs. India sent to {len(india_sent)}, received from {len(india_recv)}.")

# --- 5. Cooperation breadth (sending and receiving counts) ---
coop_s_file = glob.glob('Activity report all details 2025/cooperation_between_committees___sending_*.xlsx')[0]
wb_cs = openpyxl.load_workbook(coop_s_file, data_only=True)
coop_sent = {str(r[0]).strip(): float(r[1] or 0) for r in list(wb_cs.active.iter_rows(values_only=True))[1:] if r[0]}

coop_r_file = glob.glob('Activity report all details 2025/cooperation_between_committees___receiving_*.xlsx')[0]
wb_cr = openpyxl.load_workbook(coop_r_file, data_only=True)
coop_recv = {str(r[0]).strip(): float(r[1] or 0) for r in list(wb_cr.active.iter_rows(values_only=True))[1:] if r[0]}

# --- 6. Disciplines Sent and Received ---
disc_s_file = glob.glob('Activity report all details 2025/general_discipline___sent_*.xlsx')[0]
wb_ds = openpyxl.load_workbook(disc_s_file, data_only=True)
ws_ds = wb_ds.active
header_ds = list(ws_ds.iter_rows(values_only=True))[0]
disc_sent = {}
for r in list(ws_ds.iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip() if r[0] else ''
    if not comm:
        continue
    top_d = []
    for col_idx in range(1, len(r)):
        val = float(r[col_idx] or 0)
        if val > 0:
            top_d.append((str(header_ds[col_idx]), val))
    top_d.sort(key=lambda x: x[1], reverse=True)
    disc_sent[comm] = [t[0] for t in top_d[:4]]

disc_r_file = glob.glob('Activity report all details 2025/general_discipline___received_*.xlsx')[0]
wb_dr = openpyxl.load_workbook(disc_r_file, data_only=True)
ws_dr = wb_dr.active
header_dr = list(ws_dr.iter_rows(values_only=True))[0]
disc_recv = {}
for r in list(ws_dr.iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip() if r[0] else ''
    if not comm:
        continue
    top_d = []
    for col_idx in range(1, len(r)):
        val = float(r[col_idx] or 0)
        if val > 0:
            top_d.append((str(header_dr[col_idx]), val))
    top_d.sort(key=lambda x: x[1], reverse=True)
    disc_recv[comm] = [t[0] for t in top_d[:4]]

# --- 7. Employer Cancellation Root Causes ---
emp_canc_file = glob.glob('Activity report all details 2025/employer_cancellation_*.xlsx')[0]
wb_ec = openpyxl.load_workbook(emp_canc_file, data_only=True)
ws_ec = wb_ec.active
header_ec = list(ws_ec.iter_rows(values_only=True))[0]
emp_canc_reasons = {}
for r in list(ws_ec.iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip() if r[0] else ''
    if not comm:
        continue
    top_r = []
    for col_idx in range(1, len(r)-1): # ignore row totals
        val = float(r[col_idx] or 0)
        if val > 0 and header_ec[col_idx]:
            top_r.append((str(header_ec[col_idx]), val))
    top_r.sort(key=lambda x: x[1], reverse=True)
    if top_r:
        emp_canc_reasons[comm] = top_r[0][0]

# --- 8. Student Rejection Root Causes ---
stud_rej_file = glob.glob('Activity report all details 2025/student_rejection_*.xlsx')[0]
wb_sr = openpyxl.load_workbook(stud_rej_file, data_only=True)
ws_sr = wb_sr.active
header_sr = list(ws_sr.iter_rows(values_only=True))[0]
stud_rej_reasons = {}
for r in list(ws_sr.iter_rows(values_only=True))[1:]:
    comm = str(r[0]).strip() if r[0] else ''
    if not comm:
        continue
    top_r = []
    for col_idx in range(1, len(r)-1):
        val = float(r[col_idx] or 0)
        if val > 0 and header_sr[col_idx]:
            top_r.append((str(header_sr[col_idx]), val))
    top_r.sort(key=lambda x: x[1], reverse=True)
    if top_r:
        stud_rej_reasons[comm] = top_r[0][0]

print("All file categories parsed successfully.")
