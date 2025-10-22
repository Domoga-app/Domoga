from dao import UsuarioDAO, DispositivoDAO, TipoDispositivoDAO
from views import menu_principal

def main():
    usuario_dao = UsuarioDAO()
    dispositivo_dao = DispositivoDAO()
    tipo_dispositivo_dao = TipoDispositivoDAO()

    menu_principal(usuario_dao, dispositivo_dao, tipo_dispositivo_dao)


if __name__ == "__main__":

    main()