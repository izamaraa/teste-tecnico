def read_file(filepath:str) -> list[dict]:
    with open(filepath, 'r') as file:
      list_data=[]
      Linhas= file.readlines()
      for linha in Linhas:
        tipo= linha[0]
        date= linha[1:9]
        valor= linha[9:19]
        cpf= linha[19:30]
        cartao= linha[30:42]
        hora= linha[42:48]
        dono= linha[48:62]
        loja= linha[62:81]  
        valor_real = int(valor)*100

        data_final= (tipo,date,valor_real,cpf, cartao, hora, dono, loja) 
        list_data.append(data_final)
      return list_data

