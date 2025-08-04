import requests
from bs4 import BeautifulSoup
import nltk
from indicnlp.tokenize import indic_tokenize

urls = [
    "https://www.mathrubhumi.com/money/news/trump-tariffs-us-car-prices-1.10676621",
    "https://www.mathrubhumi.com/money/commodities/crude-oil-price-israel-iran-conflict-1.10671092",
    "https://www.mathrubhumi.com/money/news/indian-middle-class-debt-crisis-1.10670970",
    "https://www.mathrubhumi.com/money/news/income-tax-bill-2025-refund-changes-1.10668274",
    "https://www.mathrubhumi.com/money/news/geojit-appoints-jayakrishnan-sasidharan-executive-director-1.10653191",
    "https://www.mathrubhumi.com/money/news/vehicle-insurance-premium-hike-1.10646846",
    "https://www.mathrubhumi.com/money/news/gst-slab-reduction-12-percent-removal-1.10641369",
    "https://www.mathrubhumi.com/money/news/reliance-top-global-tech-company-1.10635702",
    "https://www.mathrubhumi.com/money/news/2000-rupee-note-exchange-1.10633087",
    "https://www.mathrubhumi.com/money/news/jsw-acquires-akzo-nobel-india-1.10614634",
    "https://www.mathrubhumi.com/money/news/geojit-financial-results-fy24-25-1.10604942",
    "https://www.mathrubhumi.com/money/news/lic-mutual-fund-new-investment-plans-1.10589862",
    "https://www.mathrubhumi.com/money/news/aster-dm-acquires-5-stake-in-qcil-at-849-13-crore-1.10554857",
    "https://www.mathrubhumi.com/money/news/govt-targets-faster-health-insurance-claims-in-3-hours-cashless-in-1-1.10510859",
    "https://www.mathrubhumi.com/money/news/jiofin-share-backed-loans-get-up-to-1-cr-1.10502336",
    "https://www.mathrubhumi.com/pravasi/uae/lulu-group-s-mega-mall-in-visakhapatnam-1.10459971",
    "https://www.mathrubhumi.com/money/news/stock-market-crash-impacts-consumer-spending-1.10400107",
    "https://www.mathrubhumi.com/money/news/icici-lombard-launches-iar-supreme-a-first-of-its-kind-all-risk-insurance-solution-1.10397035",
    "https://www.mathrubhumi.com/money/news/logistics-warehousing-boom-in-india-s-tier-2-cities-1.10391162",
    "https://www.mathrubhumi.com/money/news/100-crore-indians-have-no-extra-money-to-spend-1.10379805",
    "https://www.mathrubhumi.com/money/news/girish-kumar-nair-appointed-ceo-of-eastern-business-unit-1.10338992",
    "https://www.mathrubhumi.com/money/news/new-income-tax-bill-2025-what-it-means-for-you-1.10335849",
    "https://www.mathrubhumi.com/money/news/artha-bharat-coo-wins-ca-woman-of-the-year-award-from-icai-1.10318652",
    "https://www.mathrubhumi.com/money/personal-finance/get-1-3-lakh-monthly-pension-nps-investment-1.10701311",
    "https://www.mathrubhumi.com/money/personal-finance/itr-1-now-includes-capital-gains-from-shares-1.10551729"
    
    
    
    
    
  

    ]
all_text = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")

    all_text += paragraphs
                               
    
sentences = []
for para in all_text:
    para_text = para.get_text()

    sentences += para_text

with open("webscrap.txt", "w", encoding = "utf-8") as file:
    for sentence in sentences:
        file.write(sentence)                       


import re
from indicnlp.tokenize import indic_tokenize

with open("webscrap.txt", "r", encoding = "utf-8") as file:
    raw_text = file.read()

remove_whitespace = re.sub(r'\s+',' ', raw_text)
cleaned_text = raw_text.replace('\t', ' ')
cleaned_text = re.sub(r'[^\u0D00-\u0D7F\s.]+','', cleaned_text)

tokens = list(indic_tokenize.trivial_tokenize(cleaned_text, lang='ml'))

length_of_tokens = len(tokens)
print(length_of_tokens)

with open("webscrap_clean.txt", "w", encoding= "utf-8") as file:
    for token in tokens:
        file.write(token + "\n")
