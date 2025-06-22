# OOP Data Consolidator

## pt-BR

Este é um projeto pessoal de estudo sobre orientação a objetos. Simula uma empresa fictícia do ramo de produtos financeiros que armazena arquivos de diferentes formatos e extensões em pastas distintas. O objetivo é ler esses arquivos via programação e consolidá-los em um banco de dados DuckDB.

### Funcionalidades

- Leitura de arquivos em múltiplos formatos (CSV, Excel, Json, etc)
- Organização dos arquivos em pastas por tipo
- Salvamento dos dados consolidados em DuckDB
- Estrutura orientada a objetos
- Contrato de dados para garantir a consistência e integridade das informações
- Estrutura modular, facilitando a manutenção e extensão do projeto
- Implementação de pipelines de dados para automação do fluxo de ingestão, transformação e carga (ETL)
- Validação e tratamento de dados durante o processo de consolidação

#### Palavras-chave

Pipeline de dados, ETL, orientação a objetos, modularidade, contrato de dados, validação, engenharia de dados, automação, DuckDB, ingestão de dados, Polars.

### Como usar

1. Clone o repositório (`git clone https://github.com/matheus-amon/oop_data_consolidator.git`)
2. Entre no diretório (`cd oop_data_consolidator`)
3. Crie um ambiente virtual (`python -m venv .venv`)
4. Ative o ambiente virtual: **Linux** ou **Mac** → (`source .venv/bin/activate`) | **Windows** → (`.venv\Scripts\activate`)
5. Instale as dependências (`pip install -r requirements.txt`)
6. Execute o script principal (`python main.py`)

---

## en-US

This is a personal project to study object-oriented programming. It simulates a fictional financial products company that stores files of different formats and extensions in separate folders. The goal is to read these files programmatically and consolidate them into a DuckDB database.

### Features

- Reads files in multiple formats (CSV, Excel, Json, etc)
- Organizes files into folders by type
- Saves consolidated data into DuckDB
- Object-oriented structure
- Data contract to ensure consistency and integrity of information
- Modular structure for easy maintenance and extension
- Data pipeline implementation for automating ingestion, transformation, and loading (ETL)
- Data validation and cleansing during consolidation

#### Keywords

Data pipeline, ETL, object-oriented, modularity, data contract, validation, data engineering, automation, DuckDB, data ingestion, Polars.

### How to use

1. Clone the repository (`git clone https://github.com/matheus-amon/oop_data_consolidator.git`)
2. Navigate to the project directory (`cd oop_data_consolidator`)
3. Create a virtual environment (`python -m venv .venv`)
4. Activate the virtual environment: **Linux** or **Mac** → (`source .venv/bin/activate`) | **Windows** → (`.venv\Scripts\activate`)
5. Install the dependencies (`pip install -r requirements.txt`)
6. Run the main script (`python main.py`)

