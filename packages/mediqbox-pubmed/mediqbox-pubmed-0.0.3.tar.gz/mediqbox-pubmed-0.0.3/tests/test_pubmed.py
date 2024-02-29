from dotenv import load_dotenv

from mediqbox.pubmed.pubmed import (
  Pubmed,
  PubmedConfig,
  PubmedInputData,
)

load_dotenv()

from tests.settings import settings

pubmed = Pubmed(config=PubmedConfig(
  ncbi_email=settings.NCBI_EMAIL,
  ncbi_api_key=settings.NCBI_API_KEY
))

def test_pubmed():
  result = pubmed.process(PubmedInputData(
    term="10.1080/1120009X.2021.1937782[doi]"
  ))
  print(result)
  assert result.count == 1 and result.retmax == 1 and len(result.records) == 1

  result = pubmed.process(PubmedInputData(
    term="10.1200/JCO.22[doi]"
  ))
  print(result)
  assert result.count == 0 and result.retmax == 0 and len(result.records) == 0

if __name__ == '__main__':
  test_pubmed()