def verificar_role(user, role_esperado):
    """
    Verifica se um utilizador tem uma role específica.
    
    Args:
        user (dict): dados do utilizador
        role_esperado (str): role a verificar
    
    Returns:
        bool: True se o utilizador tiver a role esperada, False caso contrário
    """
    return user.get("role") == role_esperado
