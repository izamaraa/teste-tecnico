def read_file(filepath:str) -> list[dict]:
    with open(filepath, 'r',encoding="utf-8") as file:
      list_data=[]
      lines= file.readlines()
      for line in lines:
        tipo= line[0]
        date= line[1:9]
        valor= line[9:19]
        cpf= line[19:30]
        cartao= line[30:42]
        hora= line[42:48]
        dono= line[48:62]
        loja= line[62:81]  
        valor_real = int(valor)*100

        final_date= (tipo,date,valor_real,cpf, cartao, hora, dono, loja) 
        list_data.append(final_date)
      return list_data

