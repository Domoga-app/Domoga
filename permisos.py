permisos_por_rol = {
    "admin": {

    },
    "usuario": {
        
    }
}
def tiene_permiso(usuario,permiso):
    return permiso in permisos_por_rol.get(usuario.rol, set())