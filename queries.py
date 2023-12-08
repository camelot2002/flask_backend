queries = {
    "Tell me all the reasons for dishonour of a cheque.": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix table:<http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?reason
        WHERE {
        ?cheque table:reasonForChequeDishonour ?reason
        }
    """,
    "What follows notice issuance?": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix table:<http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?name ?desc
        WHERE {
        ?issuanceOfNotice table:name "Issuance Of Notice".
        ?issuanceOfNotice table:nextProceeding ?np.
        ?np table:name ?name.
        ?np table:stageDescription ?desc
        }
    """,
    "Give the names and descriptions of all possible resolutions.": """
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
    "Give me the details of some stages of proceedings.": """
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
    "Fetch the names and descriptions of 5 stages within the legal proceedings concerning cheque dishonor.": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX chequeDishonour: <http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?proceedingName ?description
        WHERE {
        ?legalProceeding chequeDishonour:name ?proceedingName.
        ?legalProceeding chequeDishonour:stageDescription ?description.
        }
        LIMIT 5
    """,
    "Retrieve Different Types of Cheques": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX chequeDishonour: <http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?chequeType
        WHERE {
            ?chequeType rdf:type chequeDishonour:Cheque .
        }
    """,
    "Retrieve Issuers of Dishonored Cheques": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX chequeDishonour: <http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?issuer
        WHERE {
            ?cheque rdf:type chequeDishonour:Cheque .
            ?cheque chequeDishonour:issuedBy ?issuer .
        }
    """,
    "Retrieve Bank Information Associated with Dishonored Cheques": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX chequeDishonour: <http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?bankName ?branch
        WHERE {
            ?cheque rdf:type chequeDishonour:Cheque .
            ?cheque chequeDishonour:bankName ?bankName .
            ?cheque chequeDishonour:branch ?branch .
        }
    """,
    "Retrieve Legal Advisors in the Dishonor Case": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX chequeDishonour: <http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?legalAdvisor
        WHERE {
            ?legalAdvisor rdf:type chequeDishonour:LegalAdvisor .
            ?legalAdvisor chequeDishonour:associatedWith ?case .
        }
    """,
    "Retrieve Different Categories of Dishonor": """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX chequeDishonour: <http://www.semanticweb.org/camelot/ontologies/2023/11/chequeDishonour#>

        SELECT ?dishonorCategory
        WHERE {
            ?dishonor rdf:type chequeDishonour:Dishonor .
            ?dishonor chequeDishonour:category ?dishonorCategory .
        }
    """,
}