## Algoritimos de Aprendizado de Máquina - FastAPI

Esta API fornece endpoints para aplicar algoritmos de aprendizado de máquina, como K-Nearest Neighbors (KNN), Árvore de Decisão e Algoritmo Genético. Os endpoints aceitam arquivos CSV como entrada e retornam várias métricas e resultados da execução do algoritmo.

<div align="center">
   <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
   <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"/>
   <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
</div>
<br>

### Dependências
O projeto usa as seguintes bibliotecas:

- FastAPI
- pandas
- scikit-learn
- matplotlib
- joblib
- pydantic

<br>

## Iniciando o projeto

###### Requisitos de Software

- Python
- VSCode
  
### Instalação

1. Clone o repositório para o seu computador:

```
git clone https://github.com/aasjunior/mlapp-api.git
```

2. Abra o projeto pelo VSCode e execute o comando pelo terminal: 

```
pip install -r requirements.txt
```

3. Navegue até o diretório `app` e execute:

```
python -m uvicorn main:app --reload
```
4. A API estará rodando em `http://127.0.0.1:8000`
<br>

## Endpoints

### 1. K-Nearest Neighbors (KNN)

**POST /knn**

- **Descrição**: Aplica o algoritmo KNN no dataset fornecido.
- **Requisição**:

    - `DataScheme` (Corpo JSON): Contém os cabeçalhos dos atributos e a classe.
    - `file` (UploadFile): Um arquivo CSV contendo o dataset.

- **Resposta**:
    - `number_of_examples`: Número de exemplos no dataset.
    - `number_of_classes`: Número de classes únicas no dataset.
    - `number_of_attributes`: Número de atributos usados para predição.
    - `accuracy`: Precisão do algoritmo KNN.

**Exemplo de Requisição com `multipart/form-data`**

Ao fazer a requisição, você deve enviar o arquivo CSV e o JSON com o esquema de dados. Um exemplo utilizando `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/knn" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@caminho/do/seu/arquivo.csv" \
-F 'data={"attributeHeaders":["sepal_length","sepal_width","petal_length","petal_width"],"classHeader":"class"}'
```

**Exemplo de Resposta:**

```json
{
  "number_of_examples": 150,
  "number_of_classes": 3,
  "number_of_attributes": 4,
  "accuracy": "96.67%"
}
```

<br>

### 2. Testar KNN

**GET /test-knn**

- **Descrição**: Testa o algoritmo KNN usando um dataset pré-definido (dataset Iris).

- **Resposta**:

    - `number_of_examples`: Número de exemplos no dataset.
    - `number_of_classes`: Número de classes únicas no dataset.
    - `number_of_attributes`: Número de atributos usados para predição.
    - `accuracy`: Precisão do algoritmo KNN.

**Exemplo de Resposta:**

```json
{
  "number_of_examples": 150,
  "number_of_classes": 3,
  "number_of_attributes": 4,
  "accuracy": "96.67%"
}
```

<br>

### 3. Árvore de Decisão

**POST /decision-tree**

- **Descrição**: Aplica o algoritmo de Árvore de Decisão no dataset fornecido.
- **Requisição**:
  - `DataScheme` (Corpo JSON): Contém os cabeçalhos dos atributos e a classe.
  - `file` (UploadFile): Um arquivo CSV contendo o dataset.

**Exemplo de Requisição com multipart/form-data**

```bash
curl -X POST "http://seu-dominio/decision-tree" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@caminho/do/seu/arquivo.csv" \
-F 'data={"attributeHeaders":["sepal_length","sepal_width","petal_length","petal_width"],"classHeader":"class"}'
```

**Exemplo de Resposta:**

```json
{
  "result": {
    "number_of_examples": 150,
    "number_of_classes": 3,
    "number_of_attributes": 4,
    "model_info": {
      "accuracy": "96.67%",
      "model_image": "base64_encoded_image"
    }
  }
}
```

<br>

### 4. Testar Árvore de Decisão

**GET /test-decision-tree**

- **Descrição**: Testa o algoritmo de Árvore de Decisão usando um dataset pré-definido (dataset Iris).
- **Resposta**:
  - `number_of_examples`: Número de exemplos no dataset.
  - `number_of_classes`: Número de classes únicas no dataset.
  - `number_of_attributes`: Número de atributos usados para predição.
  - `model_info`: Detalhes do modelo, incluindo precisão e imagem do modelo.

**Exemplo de Resposta:**

```json
{
  "number_of_examples": 150,
  "number_of_classes": 3,
  "number_of_attributes": 4,
  "model_info": {
    "accuracy": "96.67%",
    "model_image": "base64_encoded_image"
  }
}

```

<br>

### 5. Algoritmo Genético

**GET /genetic-algorithm**

- **Descrição**: Aplica o Algoritmo Genético e retorna o resultado.
- **Resposta**:
  - `size`: Tamanho da população.
  - `n_childrens`: Número de filhos em cada geração.
  - `n_generations`: Número de gerações.
  - `fitness`: Função de aptidão usada.
  - `plot_images`: Imagens dos gráficos de aptidão e evolução codificadas em base64.

**Exemplo de Resposta:**

```json
{
  "size": 50,
  "n_childrens": 35,
  "n_generations": 10,
  "fitness": "minimizar z = 20 + x² + y² - 10 * (cos(2πx) + cos(2πy))",
  "plot_images": {
    "plot_fitness": "base64_encoded_image",
    "plot_evolution": "base64_encoded_image"
  }
}
```

<br>

## Tratamento de Erros

Em caso de erros durante a execução dos algoritmos, a API retorna um código de status HTTP 400 juntamente com os detalhes do erro.

**Exemplo de Resposta de Erro:**

```json
{
  "detail": "Mensagem de erro"
}
```

<br>

### Notas

- Os endpoints que requerem uploads de arquivos esperam que o arquivo esteja em formato CSV.

- Os endpoints /test-knn e /test-decision-tree utilizam um dataset pré-definido localizado em assets/db/iris.csv.

- Os gráficos do algoritmo genético são retornados como strings codificadas em base64.

##
###### Aviso
Este é um trabalho acadêmico realizado como tarefa da disciplina de Laboratório Mobile/Computação Natural no 5º Semestre de Desenvolvimento de Software Multiplataforma
