def porcentagem(total, args):
    
    resultados_porcentagem = []
   
    for valor in args:
        percentual = (valor / total) * 100
        resultados_porcentagem.append(round(percentual))

    
    resultados_porcentagem.append(100 - sum(resultados_porcentagem))
    return resultados_porcentagem


        

categorias = ["qualidade da internet", "cobranca indevida", "cancelamento", "propaganda enganosa", "mau atendimento sac", "problema equipamento", "outros"]
dividendos_tim = [15564, 8557, 3411, 2863, 3818, 4050]
dividendos_oi = [12886, 7341,3079,2838,2428,2068]


percentual_tim = porcentagem(52420, dividendos_tim)
percentual_oi = porcentagem(42138, dividendos_oi)


avaliacao_tim = dict(zip(categorias, percentual_tim))
avaliacao_oi = dict(zip(categorias, percentual_oi))

print(avaliacao_tim)
print(avaliacao_oi)




