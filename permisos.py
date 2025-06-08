permisos_por_rol = {
    "admin": {
         "Eliminar dispositivos",
         "Eliminar ambiente",
         "Eliminar hogar",
         "Eliminar automatización",
         "Mostrar automatizaciones",
         "Crear automatizaciones",
         "Eliminar automatizaciones",
         "gestionar_ambientes",
         "gestionar_dispositivos",
         "gestionar_roles",
    },
    "usuario": {
        
    }
}
def tiene_permiso(usuario,permiso):
    return permiso in permisos_por_rol.get(usuario.rol, set())