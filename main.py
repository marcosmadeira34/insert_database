from database import *
import pandas as pd


host_postgres = 'postgresql://postgres:123456789@localhost:5432/postgres'
app = ConnectPostgresQL(host_postgres)

df_news_orders = pd.read_excel('janeiro2024.xlsx', sheet_name='Planilha1', engine='openpyxl')
df_news_orders = df_news_orders.astype(str)
#app.create_database()

for i in range(len(df_news_orders.astype(str))):
    try:
        data = app.insert_data('pedidosfaturados',
                codigo_cliente = df_news_orders['codigo_cliente'][i],
                loja_cliente = df_news_orders['loja_cliente'][i],
                nome_do_cliente = df_news_orders['nome_do_cliente'][i],
                cnpj_de_faturamento = df_news_orders['cnpj_de_faturamento'][i],
                cnpj_de_remessa = df_news_orders['cnpj_de_remessa'][i],
                equipamento = df_news_orders['equipamento'][i],
                nota_de_remessa = df_news_orders['nota_de_remessa'][i],
                data_de_remessa = df_news_orders['data_de_remessa'][i],
                serie_da_nf_remessa = df_news_orders['serie_da_nf_remessa'][i],
                produto = df_news_orders['produto'][i],
                #descricao_do_produto = df_news_orders['descricao_do_produto'][i],
                quantidade = df_news_orders['quantidade'][i],
                pedido_de_remessa = df_news_orders['pedido_de_remessa'][i],
                projeto = df_news_orders['projeto'][i],
                obra = df_news_orders['obra'][i],
                prazo_do_contrato = df_news_orders['prazo_do_contrato'][i],
                data_de_ativacao_legado = df_news_orders['data_de_ativacao_legado'][i],
                data_de_ativacao = df_news_orders['data_de_ativacao'][i],
                ultimo_faturamento = df_news_orders['ultimo_faturamento'][i],
                data_do_termo = df_news_orders['data_do_termo'][i],
                aniversario = df_news_orders['aniversario'][i],
                desc_ajuste = df_news_orders['desc_ajuste'][i],
                indice_aplicado = df_news_orders['indice_aplicado'][i],
                dias_de_locacao = df_news_orders['dias_de_locacao'][i],
                valor_de_origem = df_news_orders['valor_de_origem'][i],
                valor_unitario = df_news_orders['valor_unitario'][i],
                valor_bruto = df_news_orders['valor_bruto'][i],
                tipo_do_mes = df_news_orders['tipo_do_mes'][i],
                contrato_legado = df_news_orders['contrato_legado'][i],
                acrescimo = df_news_orders['acrescimo'][i],
                franquia = df_news_orders['franquia'][i],
                id_equipamento = df_news_orders['id_equipamento'][i],
                id_equip_substituido = df_news_orders['id_equip_substituido'][i],
                data_da_substituicao = df_news_orders['data_da_substituicao'][i],
                data_proximo_faturamento = df_news_orders['data_proximo_faturamento'][i],
                data_fim_locacao = df_news_orders['data_fim_locacao'][i],
                tipo_de_servico = df_news_orders['tipo_de_servico'][i],
                email = df_news_orders['email'][i],
                calculo_reajuste = df_news_orders['calculo_reajuste'][i],
                nome_da_obra = df_news_orders['nome_da_obra'][i],
                numero_da_as = df_news_orders['numero_da_as'][i],
                pedido_faturamento = df_news_orders['pedido_faturamento'][i],
                nf_de_faturamento = df_news_orders['nf_de_faturamento'][i],
                serie_de_faturamento = df_news_orders['serie_de_faturamento'][i],
                data_de_faturamento = df_news_orders['data_de_faturamento'][i],
                qtde_faturamento = df_news_orders['qtde_faturamento'][i],
                vlr_unitario_faturamento = df_news_orders['vlr_unitario_faturamento'][i],
                vlr_total_faturamento = df_news_orders['vlr_total_faturamento'][i],
                periodo_de_faturamento = df_news_orders['periodo_de_faturamento'][i],
                status_de_cobranca = df_news_orders['status_de_cobranca'][i]
                
                )
        
        print(f'Dados inseridos com sucesso!{data}')        
    except Exception as e:                    
        print(f'Erro ao inserir dados no banco de dados: {e}')