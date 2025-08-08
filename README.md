# 🛡️ Qualidator  
*A modern CLI for managing SQL-based data quality checks — now with connector setup.*

![Qualidator Banner](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)  
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen?style=for-the-badge)  
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge)

---

## 📌 Overview
**Qualidator** is a command-line tool that helps you **define, manage, and store SQL-based data quality validations**.  
It can set up a connector to your data source and organize validation queries in a `.qualidations` folder for easy reuse and version control.

With Qualidator, you can:
- 📂 Initialize a validations project
- 🔌 Configure a connector (Databricks, Snowflake, Postgres, or None)
- ➕ Add a variety of built-in validation checks
- 🗑 Remove one or all validations
- 📊 View project status and existing validations
- 💥 Destroy the project

---

## 🚀 Installation

```bash
pip install qualidator
