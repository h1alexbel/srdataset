"""
Similarity between repository dimensions.
"""
from steps.similar import similar

print(similar("repo", "samples"))
print(similar("description", "Awesome Docker Compose samples"))
print(similar("description", "Java maven samples"))
