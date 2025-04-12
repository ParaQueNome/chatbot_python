# 🌌  Astronomy Chatbot
Este é um chatbot interativo que permite aos usuários fazer perguntas sobre Astronomia. O bot busca artigos da Wikipedia sobre um tópico relacionado à Astronomia (como a Teoria da Relatividade) e responde perguntas com base no conteúdo do artigo extraído. O chatbot utiliza técnicas de processamento de linguagem natural (PLN) e aprendizado de máquina para identificar a melhor resposta.

## Funcionalidades
- Busca automática de artigos: O chatbot busca artigos da Wikipedia relacionados à Astronomia.

- Processamento de Linguagem Natural: Usa o spaCy para o processamento de texto e o NLTK para tokenização de frases.

- Respostas inteligentes: O bot utiliza técnicas de similaridade de texto (TF-IDF e similaridade cosseno) para fornecer respostas relevantes com base no artigo carregado.

- Interface gráfica: Desenvolvido com a biblioteca Tkinter, proporcionando uma interface simples para interagir com o chatbot.

## Tecnologias Utilizadas
- spaCy: Biblioteca de PLN para análise linguística.

- NLTK: Biblioteca de processamento de linguagem natural para tokenização de sentenças.

- scikit-learn: Usado para calcular a similaridade de texto usando o TF-IDF e a similaridade cosseno.

- Goose3: Para extrair o conteúdo limpo de páginas da web (artigos).

- Tkinter: Biblioteca para criar a interface gráfica.

## Como Executar
### Pré-requisitos
### Antes de executar o projeto, você precisará instalar algumas dependências:

- bash
- Copiar
- Editar
- pip install spacy
- pip install nltk
- pip install scikit-learn
- pip install goose3

### Além disso, será necessário baixar o modelo do spaCy para processamento de linguagem:

- bash
- Copiar
- Editar
- python -m spacy download en_core_web_lg
- Como Executar o Bot
- Clone o repositório ou baixe os arquivos.

### Execute o script Python:

- bash
- Copiar
- Editar
- python chatbot_astronomy.py


A interface gráfica será aberta. Digite uma pergunta sobre Astronomia e o bot buscará informações para responder.

## Estrutura do Código
- Função update_article_about_astronomy(): Extrai o artigo sobre a Teoria da Relatividade da Wikipedia.

- Função preprocessing(): Realiza o pré-processamento do texto, removendo stopwords, pontuação, números e palavras curtas.

- Função get_question_type(): Determina o tipo da pergunta com base em palavras-chave como "qual", "quem", "como", etc.

- Função answer(): Utiliza a similaridade de cosseno entre a pergunta do usuário e o artigo carregado para encontrar a melhor resposta.

- Interface Gráfica com Tkinter: O bot interage com o usuário através de uma interface simples onde o texto é mostrado e perguntas podem ser feitas.

### Exemplo de Uso
- Pergunte ao bot sobre a Teoria da Relatividade ou qualquer outro tópico relacionado à Astronomia.

- O bot buscará a melhor resposta dentro do artigo da Wikipedia.

### Exemplos de Perguntas:
- "What is general relativity?"

- "How does general relativity explain gravity?"

- "Who proposed the theory of relativity?"

## Contribuição
- Sinta-se à vontade para contribuir com este projeto! Você pode:

- Fazer um fork do repositório.

- Criar uma branch para novas funcionalidades.

- Enviar um pull request com suas alterações.

## Licença
- Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

- Se precisar de ajustes ou mais detalhes no README, é só avisar!
