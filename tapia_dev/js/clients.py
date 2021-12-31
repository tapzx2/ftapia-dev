# this is a list of clients
# script used to generate the html

fat = """Abramson Smith Waldsmith, LLP
AC Transit
Acro Associates, Inc.
Air Liquide Industrial U.S. LP
American Art Collector
Anna Beck Designs
Becherer, Kannett & Schweitzer
Bio-Rad Laboratories
Bogaards & Davis
CA Dept Of Health Services
California Public Utilities Commission
Casper, Meadows, Schwartz & Cook
Clorox Company
Columbus Distributing
Corbett Law Firm
Cotchett, Pitre & McCarthy
Crosslink Capital
CTP Aviation
Cyan Inc
Danko Law Firm
Dolan Law Firm
Eastbaypro Realty
Emison Hullverson LLP
Farrise Firm, P.C.
FDIC
FM Industries
Fuse Architects Inc
Gagen McCoy
GEA Westfalia Separator
Gillin Jacobson Ellis & Larsen
Girard Gibbs LLP
Go Smile
Go West Creative
Golden State Warriors
Goldman, Sachs & Co
Health Plan of San Francisco
Heffernan Finanical Services
Infinity Financial Services
Kaiser Gornick, LLP
Kaiser Permanente
Kappe+Du Architects
Kennet Venture Partners, LLC
Kessenick, Phillips & Gamma, LLP
Law Offices of Sanford M. Cipinko
Lawrence Berkeley National Laboratory
Linde North America Inc
Mary Alexander & Associates, P. C.
Murphy, Pearson, Brandley & Feeney
Nanogram Corporation
Ogletree Deakins
Oona Sera Designs
Pillsbury & Levinson, LLP
Piquarium, Inc.
Principal Financial Group
Providence Creative Group
Rainin Instrument, LLC
RCM Broadcast Communications Inc
Rosen, Bien & Galvan. LLP
Rouda, Feder, Tietjen & Zanobini
Rutherford Bolen Group
Safeway Corporation
Santur Corporation
Scarlett Law Group
Schuering Zimmerman & Doyle
Sideman & Bancroft LLP
Sik Inc
SOHA Engineers
SP Aviation
Spinal Modulation, Inc.
StonePeak Ceramics
Street Fire Sound Lab
Suddath Relocation Systems
Super Lawyers,Thomson Reuters Service
Target Corp
TenCate Advanced Composites USA, Inc
Teraoka & Partners LLP
The Myers Law Firm, P.C.
Therma-Wave Corporation
Timbron International
Trammell Crow Company
Treadwell & Rollo, Inc
Tyson Steele Dental Marketing
Veritas Marketing, LLC
Walker, Hamilton & Koenig LLP
Winer and McKenna
Wolfe & Wyman LLP
XEI Scientific, Inc
Z-Line Designs, Inc
Zacks & Freedman, P.C."""

fatList = fat.split('\n')
fatNoDupes = list(set(fatList))
fatNoDupes.sort()
print(fatNoDupes)
divideme = 0
if (len(fatNoDupes) % 3 == 0):
  print("mod 3 == 0: " + str(len(fatNoDupes)))
  divideme = len(fatNoDupes)
else:
  print(len(fatNoDupes) + 3 - len(fatNoDupes) % 3)
  divideme = len(fatNoDupes) + - len(fatNoDupes) % 3

col_length = int(divideme / 3)

each_div = [
  fatNoDupes[0:col_length],
  fatNoDupes[col_length:col_length*2],
  fatNoDupes[col_length*2:]
]

for div in each_div:
  print('<div class="client-column">')
  for client in div:
    print(f'    <p class="client">{client}</p>')
  print('</div>')