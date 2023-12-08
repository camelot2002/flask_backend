from rdflib import Graph

# Load the ontology file
g = Graph()
g.parse("beta_chequeDishonour_ontology.rdf", format="xml")

# Count the number of triples
num_triples = len(g)

# Display the number of triples
print("Number of triples:", num_triples)

# Display all the triples
for subj, pred, obj in g:
    print(subj, pred, obj)
