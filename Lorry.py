## Treinamento para amostras "lorry"
    def treinar(self):
        # Inserir o valor do limiar na posição "0" para cada amostra da lista "amostras"
        # Ex.: [[0.40, 0.70], ...] vira [[1, 0.40, 0.70], ...]
        for amostra in self.amostras:
            amostra.insert(0, self.limiar)
        # Gerar valores randômicos entre 0 e 1 (pesos) conforme o número de atributos
        for i in range(self.n_atributos):
            self.pesos.append(random.random())
        # Inserir o valor do limiar na posição "0" do vetor de pesos
        self.pesos.insert(0, self.limiar)

        # Inicializar contador de épocas
        n_epocas = 0
        while True:
            # Inicializar variável erro
            # (quando terminar loop e erro continuar False, é pq não tem mais diferença entre valor calculado e desejado)
            erro = False
            # Para cada amostra...
            for i in range(self.n_amostras):
                # Inicializar potencial de ativação
                u = 0
                # Para cada atributo...
                for j in range(self.n_atributos + 1):
                    # Multiplicar amostra e seu peso e também somar com o potencial que já tinha
                    u += self.pesos[j] * self.amostras[i][j]
                # Obter a saída da rede considerando g a função sinal
                y = self.sinal(u)
                # Verificar se a saída da rede é diferente da saída desejada
                if y != self.saidas[i]:
                    # Calcular o erro
                    erro_aux = self.saidas[i] - y
                    # Fazer o ajuste dos pesos para cada elemento da amostra
                    for j in range(self.n_atributos + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
                    # Atualizar variável erro, já que erro é diferente de zero (existe)
                    erro = ;True
            # Atualizar contador de épocas
            n_epocas += 1
            # Critérios de parada do loop: erro inexistente ou o número de épocas ultrapassar limite pré-estabelecido
            if not erro or n_epocas > self.epocas:
                break
