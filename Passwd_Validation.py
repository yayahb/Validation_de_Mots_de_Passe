# -----------------------------------------------------
# Projet : Validation de Mots de Passe
# Auteur : Aya HABTI
# Date : 25-09-2024
# Description : Ce script vérifie la validité des mots de passe
# selon des politiques données en utilisant les règles de 
# l'exercice Advent of Code.
# -----------------------------------------------------

def is_valid_password(policy, password):
    """
    Vérifie si un mot de passe est valide selon la politique spécifiée.
    
    Args:
        policy (str): La politique de mot de passe au format 'min-max lettre'.
        password (str): Le mot de passe à vérifier.
    
    Returns:
        bool: True si le mot de passe est valide, False sinon.
    """
    # Séparer la politique en minimum, maximum et lettre
    range_part, letter_part = policy.split(' ')
    min_count, max_count = map(int, range_part.split('-'))
    letter = letter_part[0]

    # Compter le nombre d'occurrences de la lettre dans le mot de passe
    letter_count = password.count(letter)
    
    # Vérifier si le nombre d'occurrences est dans la plage valide
    return min_count <= letter_count <= max_count

def count_valid_passwords(password_list):
    """
    Compte le nombre de mots de passe valides dans une liste.
    
    Args:
        password_list (list): Liste de chaînes contenant la politique et le mot de passe.
    
    Returns:
        int: Nombre total de mots de passe valides.
    """
    valid_count = 0  # Compteur pour les mots de passe valides
    print("Vérification des mots de passe en cours... 🚀")
    
    for entry in password_list:
        # Séparer chaque entrée en politique et mot de passe
        policy, password = entry.split(': ')
        # Vérifier si le mot de passe est valide
        if is_valid_password(policy, password):
            valid_count += 1  # Incrémenter le compteur si valide
    
    print(f"\nVérification terminée! 🌟")
    return valid_count

# Exemple d'entrée
input_data = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

# Compter le nombre de mots de passe valides
valid_password_count = count_valid_passwords(input_data)
print(f"\nNombre total de mots de passe valides : {valid_password_count} 💻✅")
