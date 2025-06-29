# Airflow GDP ELT EU

Un projet data pipeline pour extraire des données brutes économique de l'UE

## 🚀 Fonctionnalités

- Extraction des données brutes à l'aide
- Création d'une base de données SQLITE
- Chargements des données brutes 
- Transformation des données 
- Une visualization des données à l'aide de streamlit

```bash
python3 -m venv airflow_venv
source airflow_venv/bin/activate
pip install apache-airflow==2.7.0 \
  --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.7.0/constraints-3.10.txt
```

## Technolgies utilisées

- Python 3.10.8
- Pandas
- Plotly
- AIRFLOW 2.7
- SQLALCHEMY
- Docker 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
