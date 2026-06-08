# Observations & Insights

## 1. Why SQL Agents are better than manual SQL generation

SQL agents automatically:

* Understand natural language
* Inspect schema
* Generate queries
* Execute queries

This reduces manual SQL writing.

---

## 2. Difference Between SQL Agent and RAG

SQL Agent:

* Works on structured data.
* Generates SQL queries.

RAG:

* Works on unstructured documents.
* Retrieves text chunks.

---

## 3. Risks of Unrestricted SQL Access

* Data leakage
* Unauthorized updates
* Table deletion
* Performance issues

Production systems should enforce:

* Read-only access
* Query validation
* Permission controls
