from flask import Flask, jsonify, request, render_template
from rdflib import Graph

app = Flask(__name__)

from flask_cors import CORS

CORS(app)  # Enable CORS for all routes
# Load the ontology
graph = Graph('Memory', identifier='beta_chequeDishonour_ontology.rdf')
graph.parse('beta_chequeDishonour_ontology.rdf', format='xml')

# Define the predefined queries
queries = {
    "query1": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix table:<http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?reason
        WHERE {
        ?cheque table:reasonForChequeDishonour ?reason
        }
    """,
    "query2": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix table:<http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?name
        WHERE {
        ?issuanceOfNotice table:name "Issuance Of Notice".
        ?issuanceOfNotice table:nextProceeding ?np.
        ?np table:name ?name
        }
    """,
    "query3": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix table:<http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?resName ?resDesc ?resolution
        WHERE {
            ?resolution rdf:type table:Resolution .
            ?resolution table:name ?resName .
            ?resolution table:stageDescription ?resDesc
        }
    """,
    "query4": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix table:<http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?pName ?proDesc 
        WHERE {
            ?proceeding rdf:type table:LegalProceedings .
            ?proceeding table:name ?pName.
            ?proceeding table:stageDescription ?proDesc .
        }
    """,
    "query5": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX chequeDishonour: <http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?proceedingName ?description
        WHERE {
        ?legalProceeding chequeDishonour:name ?proceedingName.
        ?legalProceeding chequeDishonour:stageDescription ?description.
        }
    """
}

@app.route("/query", methods=["POST" , "GET"])
def receive_query():
    # Get the JSON data from the POST request
    # Extract the query name from the "query" key in the JSON data
    json_data = request.get_json()
    query_name = json_data.get("query", "").strip()

    if query_name in queries: 
        query = queries[query_name]
        # print(f"Received query: {query}")  # Print the received query

        try:
            result = graph.query(query)
            triples = list(result) 
            final = []
            for i in triples:
                for j in i:
                    final.append(j)
                final.append("\n")
            return final
        except Exception as e:
            # print(f"Query execution error: {e}")  # Print any query execution error
            return jsonify({"error": "Query execution error"})
    else:   
        return jsonify({"error": "Invalid query name"})

if __name__ == "__main__":
    app.run(debug=True)
