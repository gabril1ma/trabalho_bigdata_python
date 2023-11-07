import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

headers =  {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}


titulos = []
conteudo = []



# filtro internet para casa 

for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv/lista-reclamacoes/?pagina={i}&produto=0000000000000478"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fhFBEY > div.sc-1mzw716-1.fBLFOw > div.sc-wydd4i-0.kacUJs > main > section.sc-wydd4i-5.srIBT > div.sc-eXsaLi.bptwiJ.sc-xh9b9g-0.uWmSg > div.sc-1sm4sxr-0.iwOeoe > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)

# filtro internet para casa avaliada

for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv/lista-reclamacoes/?pagina={i}&status=EVALUATED&produto=0000000000000478"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fhFBEY > div.sc-1mzw716-1.fBLFOw > div.sc-wydd4i-0.kacUJs > main > section.sc-wydd4i-5.srIBT > div.sc-eXsaLi.bptwiJ.sc-xh9b9g-0.uWmSg > div.sc-1sm4sxr-0.iwOeoe > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)
    
 # filtro qualidade da internet

for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv/lista-reclamacoes/?pagina={i}&produto=0000000000000478&problema=0000000000000872"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fhFBEY > div.sc-1mzw716-1.fBLFOw > div.sc-wydd4i-0.kacUJs > main > section.sc-wydd4i-5.srIBT > div.sc-eXsaLi.bptwiJ.sc-xh9b9g-0.uWmSg > div.sc-1sm4sxr-0.iwOeoe > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)


# filtro qualidade da internet avaliada

for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv/lista-reclamacoes/?pagina={i}&status=EVALUATED&produto=0000000000000478&problema=0000000000000872"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fhFBEY > div.sc-1mzw716-1.fBLFOw > div.sc-wydd4i-0.kacUJs > main > section.sc-wydd4i-5.srIBT > div.sc-eXsaLi.bptwiJ.sc-xh9b9g-0.uWmSg > div.sc-1sm4sxr-0.iwOeoe > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)

# filtro provedores e serv de internet baixa qualidade 
for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv/lista-reclamacoes/?pagina={i}&categoria=0000000000000069&produto=0000000000000478&problema=0000000000000004"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fhFBEY > div.sc-1mzw716-1.fBLFOw > div.sc-wydd4i-0.kacUJs > main > section.sc-wydd4i-5.srIBT > div.sc-eXsaLi.bptwiJ.sc-xh9b9g-0.uWmSg > div.sc-1sm4sxr-0.iwOeoe > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)


# filtro provedores e servidores de baixa qualidade avaliadas
for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/vivo-celular-fixo-internet-tv/lista-reclamacoes/?pagina={i}&status=EVALUATED&categoria=0000000000000069&produto=0000000000000478&problema=0000000000000004"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fhFBEY > div.sc-1mzw716-1.fBLFOw > div.sc-wydd4i-0.kacUJs > main > section.sc-wydd4i-5.srIBT > div.sc-eXsaLi.bptwiJ.sc-xh9b9g-0.uWmSg > div.sc-1sm4sxr-0.iwOeoe > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)


df = pd.DataFrame({
    "Titulos": [],
    "Conteudo": [],
    
})

for key, value in zip(titulos, conteudo):
    print(key)
    print("------------------------------------------------------")
    df = df._append({'Titulos': key,
                    'Conteudo': value},

                       ignore_index=True)



df.to_csv('vivo.csv', index=False)

print(len(titulos))
print(len(conteudo))



