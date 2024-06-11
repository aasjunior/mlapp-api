## Algoritimos de Aprendizado de Máquina - FastAPI

Esta API fornece endpoints para aplicar algoritmos de aprendizado de máquina, como K-Nearest Neighbors (KNN), Árvore de Decisão e Algoritmo Genético. Os endpoints aceitam arquivos CSV como entrada e retornam várias métricas e resultados da execução do algoritmo.

### Dependências
O projeto usa as seguintes bibliotecas:

- FastAPI
- pandas
- scikit-learn
- matplotlib
- joblib
- pydantic


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
cd app
python -m uvicorn main:app --reload
```
4. A API estará rodando em `http://127.0.0.1:8000`
<br>

## Endpoints

### 1. K-Nearest Neighbors (KNN)

#### POST /knn
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

### 2. Testar KNN

#### GET /test-knn

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

## Notas

- Os endpoints que requerem uploads de arquivos esperam que o arquivo esteja em formato CSV.

- Os endpoints /test-knn e /test-decision-tree utilizam um dataset pré-definido localizado em assets/db/iris.csv.

- Os gráficos do algoritmo genético são retornados como strings codificadas em base64.